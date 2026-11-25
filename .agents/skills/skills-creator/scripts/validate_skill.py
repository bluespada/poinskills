#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["tiktoken>=0.7", "pyyaml>=6"]
# ///
"""Validate a skill directory against the Agent Skills spec and local house rules.

Usage: validate_skill.py <skill-dir> [--desc-tokens 80:120] [--body-tokens 350:600] [--strict]

Exit codes: 0 clean, 1 errors, 2 warnings only, 3 usage error.
"""

import argparse
import re
import sys
from pathlib import Path

import tiktoken
import yaml

SPEC_KEYS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
CLIENT_EXTRA_KEYS = {"disable-model-invocation"}
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
MANDATE_RE = re.compile(r"^you must use this skill\b", re.IGNORECASE)
CONDITIONAL_RE = re.compile(r"\b(?:when|whenever|unless|if)\b", re.IGNORECASE)
QUOTED_RE = re.compile(r"'[^']*'|\"[^\"]*\"")
FENCE_RE = re.compile(r"^\s{0,3}(```+|~~~+)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*\S)\s*$")
BULLET_RE = re.compile(r"^\s*[-*+]\s+")
ORDERED_RE = re.compile(r"^\s*(\d+[.)]|[a-zA-Z][.)])\s+")
DOTS = 34


class Report:
    def __init__(self, labels):
        self.width = max(len(label) for label in labels)
        self.errors = 0
        self.warnings = 0

    def add(self, label, level, detail=""):
        if level == "error":
            self.errors += 1
            status = "FAIL"
        elif level == "warn":
            self.warnings += 1
            status = "WARN"
        else:
            status = "ok"
        pad = " " * (self.width - len(label))
        rule = "." * max(3, DOTS - self.width - 1)
        print(f"  {label}{pad} {rule} {status}" + (f" ({detail})" if detail else ""))


def split_frontmatter(text):
    if not text.startswith("---"):
        return None, None
    match = re.match(r"^---\r?\n(.*?)\r?\n---[ \t]*(?:\r?\n|$)", text, re.DOTALL)
    if not match:
        return None, None
    return match.group(1), text[match.end():]


def scan_body(body):
    headings, bullets, ordered, prose, fences = [], 0, [], [], 0
    in_fence = False
    for number, line in enumerate(body.splitlines(), start=1):
        if FENCE_RE.match(line):
            in_fence = not in_fence
            fences += 1
            continue
        if in_fence:
            continue
        heading = HEADING_RE.match(line)
        if heading:
            headings.append((len(heading.group(1)), heading.group(2), number))
        elif BULLET_RE.match(line):
            bullets += 1
        elif ORDERED_RE.match(line):
            ordered.append(number)
        elif line.strip():
            prose.append(number)
    return headings, bullets, ordered, prose, fences


def token_count(encoder, text):
    return len(encoder.encode(text)) if text.strip() else 0


def parse_band(value, flag):
    match = re.fullmatch(r"(\d+):(\d+)", value)
    if not match:
        raise argparse.ArgumentTypeError(f"{flag} expects MIN:MAX, got {value!r}")
    low, high = int(match.group(1)), int(match.group(2))
    if low > high:
        raise argparse.ArgumentTypeError(f"{flag}: MIN {low} exceeds MAX {high}")
    return low, high


def main():
    parser = argparse.ArgumentParser(add_help=True, description=__doc__.splitlines()[0])
    parser.add_argument("path", help="skill directory, or the SKILL.md inside it")
    parser.add_argument("--desc-tokens", default="80:120", metavar="MIN:MAX")
    parser.add_argument("--body-tokens", default="350:600", metavar="MIN:MAX")
    parser.add_argument("--strict", action="store_true", help="treat warnings as errors")
    args = parser.parse_args()

    try:
        desc_band = parse_band(args.desc_tokens, "--desc-tokens")
        body_band = parse_band(args.body_tokens, "--body-tokens")
    except argparse.ArgumentTypeError as error:
        print(f"error: {error}", file=sys.stderr)
        return 3

    target = Path(args.path).expanduser().resolve()
    skill_dir = target.parent if target.is_file() else target
    skill_md = skill_dir / "SKILL.md"

    labels = [
        "name", "frontmatter", "description prefix", "description conditional",
        "description tokens", "description chars", "description wording",
        "body tokens", "headings", "sections", "lists", "prose lines", "fenced code",
    ]
    report = Report(labels)

    if not skill_md.is_file():
        report.add("name", "error", f"no SKILL.md in {skill_dir}")
        print(f"{report.errors} error(s), {report.warnings} warning(s)")
        return 1

    text = skill_md.read_text(encoding="utf-8")
    frontmatter, body = split_frontmatter(text)
    if frontmatter is None:
        report.add("frontmatter", "error", "missing or unterminated --- block")
        report.add("name", "error", "unavailable")
        for label in labels[2:]:
            report.add(label, "error", "unavailable")
        print(f"{report.errors} error(s), {report.warnings} warning(s)")
        return 1

    try:
        meta = yaml.safe_load(frontmatter)
    except yaml.YAMLError as error:
        meta = None
        report.add("frontmatter", "error", f"invalid YAML: {str(error).splitlines()[0]}")
    else:
        if not isinstance(meta, dict):
            report.add("frontmatter", "error", "not a YAML mapping")
            meta = None
        else:
            unknown = sorted(set(meta) - SPEC_KEYS - CLIENT_EXTRA_KEYS)
            extra = sorted(set(meta) & CLIENT_EXTRA_KEYS)
            detail = f"keys ok ({len(meta)})"
            level = "pass"
            if unknown:
                detail, level = f"non-spec key(s): {', '.join(unknown)}", "warn"
            report.add("frontmatter", level, detail + (f", extension key(s): {', '.join(extra)}" if extra else ""))

    if meta is None:
        report.add("name", "error", "unavailable")
        for label in labels[2:]:
            report.add(label, "error", "unavailable")
        print(f"{report.errors} error(s), {report.warnings} warning(s)")
        return 1

    name = meta.get("name")
    if not isinstance(name, str) or not name.strip():
        report.add("name", "error", "missing or not a string")
    else:
        problems = []
        if not NAME_RE.fullmatch(name):
            problems.append("not kebab-case")
        if len(name) > 64:
            problems.append(f"{len(name)} chars, max 64")
        if skill_dir.name != name:
            problems.append(f"dir is {skill_dir.name!r}")
        report.add("name", "error" if problems else "pass",
                   "; ".join(problems) if problems else f"{name}")

    description = meta.get("description")
    if not isinstance(description, str) or not description.strip():
        report.add("description prefix", "error", "missing or not a string")
        for label in labels[3:]:
            report.add(label, "error", "unavailable")
        print(f"{report.errors} error(s), {report.warnings} warning(s)")
        return 1

    description = " ".join(description.split())
    encoder = tiktoken.get_encoding("o200k_base")

    match = MANDATE_RE.match(description)
    report.add("description prefix", "pass" if match else "error",
               '"You must use this skill"' if match else 'must start with "You must use this skill"')

    conditional = CONDITIONAL_RE.search(description)
    report.add("description conditional", "pass" if conditional else "error",
               f"{conditional.group(0)!r}" if conditional else "no when/if/unless clause")

    desc_tokens = token_count(encoder, description)
    low, high = desc_band
    report.add("description tokens", "pass" if low <= desc_tokens <= high else "error",
               f"{desc_tokens}, need {low}-{high}")

    desc_chars = len(description)
    angle = "<" in description or ">" in description
    report.add("description chars", "error" if angle or desc_chars > 1024 else "pass",
               f"{desc_chars} / 1024" + (", angle brackets break markup-based renderers" if angle else ""))

    segments = [s for s in QUOTED_RE.sub("", description).split(",") if s.strip()]
    report.add("description wording", "warn" if len(segments) >= 8 else "pass",
               f"{len(segments)} comma segments, flag at 8")

    headings, bullets, ordered, prose, fences = scan_body(body)
    body_tokens = token_count(encoder, body)
    low, high = body_band
    report.add("body tokens", "pass" if low <= body_tokens <= high else "error",
               f"{body_tokens}, need {low}-{high}")

    h1s = [h for h in headings if h[0] == 1]
    deeper = [h for h in headings if h[0] > 3]
    heading_problems = []
    if len(h1s) != 1:
        heading_problems.append(f"{len(h1s)} H1, want exactly 1")
    if h1s and any(h[2] < h1s[0][2] for h in headings):
        heading_problems.append("section heading before the H1 title")
    if deeper:
        heading_problems.append(f"H4+ at line {deeper[0][2]}")
    report.add("headings", "error" if heading_problems else "pass",
               "; ".join(heading_problems) if heading_problems else f"{len(h1s)} H1, {len(headings) - len(h1s)} H2/H3")

    sections = [h for h in headings if h[0] == 2]
    report.add("sections", "pass" if sections else "error",
               f"{len(sections)} H2 section(s)" if sections else "no H2 sections under the H1 title")

    if ordered:
        report.add("lists", "error", f"ordered list at line {ordered[0]}; bullets only")
    else:
        report.add("lists", "pass", f"0 ordered, {bullets} bullets")

    if prose:
        report.add("prose lines", "error", f"non-bullet line {prose[0]} ({len(prose)} total)")
    else:
        report.add("prose lines", "pass", "0")

    if fences % 2:
        report.add("fenced code", "error", f"{fences} fence markers, unbalanced")
    else:
        report.add("fenced code", "pass", f"{fences // 2} closed")

    compatibility = meta.get("compatibility")
    if isinstance(compatibility, str) and len(compatibility) > 500:
        report.add("frontmatter", "warn", f"compatibility {len(compatibility)} chars, max 500")

    errors, warnings = report.errors, report.warnings
    if args.strict:
        errors += warnings
    print(f"{errors} error(s), {warnings} warning(s)")
    return 1 if errors else (2 if warnings else 0)


if __name__ == "__main__":
    sys.exit(main())
