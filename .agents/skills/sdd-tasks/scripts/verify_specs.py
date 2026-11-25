#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml"]
# ///
"""Verify a specs/ tree: which PRDs and tasks are finished, and whether the graph is sound.

Reads specs/prd/*.md (YAML frontmatter) and specs/tasks/*.yml (YAML sequences),
resolves dependsOn across every task file, and reports finished against unfinished.

Exit codes: 0 everything finished and the graph is clean; 1 unfinished work remains;
2 schema or graph errors.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from dataclasses import dataclass, field
from pathlib import Path

import yaml

TASK_KEYS = [
    "name",
    "description",
    "content",
    "status",
    "dependsOn",
    "goals",
    "authored",
    "createdAt",
    "updatedAt",
]
PRD_KEYS = [
    "name",
    "description",
    "status",
    "tasks",
    "authored",
    "createdAt",
    "updatedAt",
]
STATUSES = ("draft", "pending", "in-review", "complete", "canceled")
FINISHED = "complete"


@dataclass
class Issue:
    level: str
    scope: str
    where: str
    message: str


@dataclass
class Task:
    file: str
    index: int
    name: str
    status: str
    goals: list[str] = field(default_factory=list)
    depends: list[str] = field(default_factory=list)
    content: str = ""

    @property
    def where(self) -> str:
        return f"{self.file} #{self.index}"

    @property
    def finished(self) -> bool:
        return self.status == FINISHED


@dataclass
class Prd:
    path: str
    front: dict
    name: str = ""
    status: str = ""
    task_paths: list[str] = field(default_factory=list)

    @property
    def finished(self) -> bool:
        return self.status == FINISHED


def valid_timestamp(value: object) -> bool:
    # YAML resolves an unquoted ISO timestamp to datetime/date before we see it, so both types are valid.
    if isinstance(value, (dt.datetime, dt.date)):
        return True
    if not isinstance(value, str):
        return False
    try:
        dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return False
    return True


def split_frontmatter(text: str) -> tuple[dict | None, str | None]:
    if not text.startswith("---"):
        return None, "no frontmatter block"
    parts = text.split("\n---", 1)
    if len(parts) != 2:
        return None, "frontmatter block is not closed"
    raw = parts[0].removeprefix("---").strip()
    try:
        data = yaml.safe_load(raw)
    except yaml.YAMLError as exc:
        return None, f"unparseable frontmatter: {exc}"
    if not isinstance(data, dict):
        return None, f"frontmatter is {type(data).__name__}, expected a mapping"
    return data, None


def check_key_order(keys: list[str], expected: list[str], where: str, scope: str, issues: list[Issue]) -> None:
    if set(keys) != set(expected):
        missing = [k for k in expected if k not in keys]
        extra = [k for k in keys if k not in expected]
        detail = []
        if missing:
            detail.append(f"missing {missing}")
        if extra:
            detail.append(f"unexpected {extra}")
        level = "error" if missing else "warning"
        issues.append(Issue(level, scope, where, "wrong keys: " + ", ".join(detail)))
    elif keys != expected:
        issues.append(Issue("warning", scope, where, "keys are present but out of declared order"))


def load_tasks(specs: Path, issues: list[Issue]) -> list[Task]:
    tasks_dir = specs / "tasks"
    tasks: list[Task] = []
    if not tasks_dir.is_dir():
        issues.append(Issue("warning", "task", str(tasks_dir), "no specs/tasks directory"))
        return tasks

    files = sorted(tasks_dir.glob("*.yml")) + sorted(tasks_dir.glob("*.yaml"))
    if not files:
        issues.append(Issue("warning", "task", str(tasks_dir), "no task files"))
        return tasks

    for path in files:
        rel = path.as_posix()
        try:
            doc = yaml.safe_load(path.read_text())
        except yaml.YAMLError as exc:
            issues.append(Issue("error", "task", rel, f"unparseable YAML: {exc}"))
            continue
        if doc is None:
            issues.append(Issue("warning", "task", rel, "file is empty"))
            continue
        if not isinstance(doc, list):
            issues.append(
                Issue("error", "task", rel, f"root is {type(doc).__name__}, expected a YAML sequence")
            )
            continue

        for index, entry in enumerate(doc, 1):
            where = f"{rel} #{index}"
            if not isinstance(entry, dict):
                issues.append(Issue("error", "task", where, f"entry is {type(entry).__name__}, expected a mapping"))
                continue

            check_key_order(list(entry.keys()), TASK_KEYS, where, "task", issues)

            name = entry.get("name")
            if not isinstance(name, str) or not name.strip():
                issues.append(Issue("error", "task", where, "name is missing or empty"))
                continue

            status = entry.get("status")
            if status not in STATUSES:
                issues.append(Issue("error", "task", where, f"status {status!r} is not one of {list(STATUSES)}"))

            depends_raw = entry.get("dependsOn", [])
            depends: list[str] = []
            if not isinstance(depends_raw, list) or not all(isinstance(d, str) for d in depends_raw):
                issues.append(Issue("error", "task", where, "dependsOn must be a list of strings"))
            else:
                depends = depends_raw

            goals_raw = entry.get("goals")
            goals: list[str] = []
            if not isinstance(goals_raw, list) or not all(isinstance(g, str) for g in goals_raw):
                issues.append(Issue("error", "task", where, "goals must be a list of strings"))
            else:
                goals = goals_raw
                if not goals:
                    issues.append(
                        Issue("error", "task", where, "goals is empty, so this task can never be finished")
                    )

            content = entry.get("content") or ""
            if not isinstance(content, str):
                content = ""
            if "Satisfies:" not in content:
                issues.append(
                    Issue("warning", "task", where, "content has no `Satisfies:` line, so traceability is broken")
                )

            for stamp in ("createdAt", "updatedAt"):
                if not valid_timestamp(entry.get(stamp)):
                    issues.append(Issue("warning", "task", where, f"{stamp} is not an ISO-8601 timestamp"))

            authored = entry.get("authored")
            if not isinstance(authored, list) or not authored:
                issues.append(Issue("warning", "task", where, "authored is empty"))

            tasks.append(
                Task(
                    file=rel,
                    index=index,
                    name=name,
                    status=status if isinstance(status, str) else "",
                    goals=goals,
                    depends=depends,
                    content=content,
                )
            )

    seen: dict[str, str] = {}
    for task in tasks:
        if task.name in seen:
            issues.append(
                Issue(
                    "error",
                    "graph",
                    task.where,
                    f'duplicate task name "{task.name}", already defined at {seen[task.name]}; '
                    "dependsOn resolves by name, so this merges two nodes",
                )
            )
        else:
            seen[task.name] = task.where

    return tasks


def load_prds(specs: Path, issues: list[Issue]) -> list[Prd]:
    prd_dir = specs / "prd"
    prds: list[Prd] = []
    if not prd_dir.is_dir():
        issues.append(Issue("warning", "prd", str(prd_dir), "no specs/prd directory"))
        return prds

    files = sorted(prd_dir.glob("*.md"))
    if not files:
        issues.append(Issue("warning", "prd", str(prd_dir), "no PRD files"))
        return prds

    for path in files:
        rel = path.as_posix()
        front, err = split_frontmatter(path.read_text())
        if err:
            issues.append(Issue("error", "prd", rel, err))
            continue
        assert front is not None

        check_key_order(list(front.keys()), PRD_KEYS, rel, "prd", issues)

        status = front.get("status")
        if status not in STATUSES:
            issues.append(Issue("error", "prd", rel, f"status {status!r} is not one of {list(STATUSES)}"))

        task_paths = front.get("tasks")
        if not isinstance(task_paths, list) or not all(isinstance(t, str) for t in task_paths):
            issues.append(Issue("error", "prd", rel, "tasks must be a list of task file paths"))
            task_paths = []

        for stamp in ("createdAt", "updatedAt"):
            if not valid_timestamp(front.get(stamp)):
                issues.append(Issue("warning", "prd", rel, f"{stamp} is not an ISO-8601 timestamp"))

        prds.append(
            Prd(
                path=rel,
                front=front,
                name=front.get("name") or "",
                status=status if isinstance(status, str) else "",
                task_paths=task_paths,
            )
        )

    return prds


def resolve_graph(tasks: list[Task], issues: list[Issue]) -> dict[str, list[str]]:
    by_name = {t.name: t for t in tasks}
    edges: dict[str, list[str]] = {t.name: [] for t in tasks}

    for task in tasks:
        for dep in task.depends:
            if dep in by_name:
                edges[task.name].append(dep)
                continue
            if dep.endswith((".yml", ".yaml")):
                members = [
                    t.name for t in tasks if t.file == dep or Path(t.file).name == Path(dep).name
                ]
                if members:
                    edges[task.name].extend(members)
                    continue
            issues.append(
                Issue("error", "graph", task.where, f'dependsOn "{dep}" is a dangling reference: no such task or task file')
            )

    color: dict[str, int] = {}
    stack: list[str] = []
    reported: set[frozenset[str]] = set()

    def walk(node: str) -> None:
        color[node] = 1
        stack.append(node)
        for nxt in edges.get(node, []):
            if color.get(nxt, 0) == 1:
                cycle = stack[stack.index(nxt) :] + [nxt]
                key = frozenset(cycle)
                if key not in reported:
                    reported.add(key)
                    where = by_name[node].where if node in by_name else node
                    issues.append(Issue("error", "graph", where, "cycle: " + " -> ".join(cycle)))
            elif color.get(nxt, 0) == 0:
                walk(nxt)
        stack.pop()
        color[node] = 2

    for task in tasks:
        if color.get(task.name, 0) == 0:
            walk(task.name)

    for task in tasks:
        if not task.finished:
            continue
        for dep in edges.get(task.name, []):
            target = by_name.get(dep)
            if target and not target.finished:
                issues.append(
                    Issue(
                        "error",
                        "graph",
                        task.where,
                        f'marked complete but depends on "{dep}" which is {target.status} at {target.where}',
                    )
                )

    return edges


def reconcile(prds: list[Prd], tasks: list[Task], issues: list[Issue]) -> dict[str, dict]:
    by_path: dict[str, list[Task]] = {}
    by_base: dict[str, list[Task]] = {}
    for task in tasks:
        by_path.setdefault(task.file, []).append(task)
        by_base.setdefault(Path(task.file).name, []).append(task)

    def lookup(ref: str) -> list[Task] | None:
        return by_path.get(ref) or by_base.get(Path(ref).name)

    claimed: set[str] = set()
    summary: dict[str, dict] = {}

    for prd in prds:
        members: list[Task] = []
        for ref in prd.task_paths:
            matched = lookup(ref)
            if not matched:
                issues.append(Issue("error", "prd", prd.path, f'tasks lists "{ref}" but no such task file exists'))
                continue
            claimed.add(matched[0].file)
            members.extend(matched)

        done = sum(1 for t in members if t.finished)
        total = len(members)
        summary[prd.path] = {"finished": prd.finished, "complete_tasks": done, "total_tasks": total}

        if prd.finished and done != total:
            issues.append(
                Issue("error", "prd", prd.path, f"marked complete but {total - done} of {total} tasks are not complete")
            )
        if not prd.finished and total and done == total:
            issues.append(
                Issue("warning", "prd", prd.path, f"all {total} tasks are complete but the PRD status is {prd.status}")
            )

    for task in tasks:
        if task.file not in claimed:
            issues.append(
                Issue("warning", "prd", task.where, f"{task.file} is not listed in any PRD's tasks")
            )

    return summary


def collect(specs: Path) -> tuple[list[Prd], list[Task], list[Issue], dict]:
    issues: list[Issue] = []
    prds = load_prds(specs, issues)
    tasks = load_tasks(specs, issues)
    edges = resolve_graph(tasks, issues)
    prd_summary = reconcile(prds, tasks, issues)
    return prds, tasks, issues, {"edges": edges, "prd": prd_summary}


def render(specs: Path, prds: list[Prd], tasks: list[Task], issues: list[Issue], extra: dict) -> str:
    out: list[str] = [f"specs/  →  {specs.resolve()}", ""]

    out.append("PRD")
    if not prds:
        out.append("  (none)")
    for prd in prds:
        info = extra["prd"][prd.path]
        label = "finished  " if prd.finished else "unfinished"
        counts = f"{info['complete_tasks']}/{info['total_tasks']} tasks complete"
        out.append(f"  {label}  {Path(prd.path).name:<28} {prd.status:<10} {counts}")
    out.append("")

    finished = [t for t in tasks if t.finished]
    unfinished = [t for t in tasks if not t.finished]

    out.append("TASKS")
    if not tasks:
        out.append("  (none)")
    if finished:
        out.append(f"  finished ({len(finished)})")
        for task in finished:
            out.append(f"    {task.name:<34} {task.status:<10} {task.where}")
    if unfinished:
        if finished:
            out.append("")
        out.append(f"  unfinished ({len(unfinished)})")
        blocking = {
            i.where: i.message
            for i in issues
            if i.scope == "graph" and i.level == "error" and i.message.startswith("dependsOn")
        }
        for task in unfinished:
            out.append(f"    {task.name:<34} {task.status:<10} {task.where}")
            note = blocking.get(task.where)
            if note:
                out.append(f"         {note}")
    out.append("")

    graph_issues = [i for i in issues if i.level == "error"]
    if graph_issues:
        out.append("ERRORS")
        for issue in graph_issues:
            out.append(f"  {issue.where}: {issue.message}")
        out.append("")

    warnings = [i for i in issues if i.level == "warning"]
    if warnings:
        out.append("NOTES")
        for issue in warnings:
            out.append(f"  {issue.where}: {issue.message}")
        out.append("")

    errors = [i for i in issues if i.level == "error"]
    parts = []
    if errors:
        parts.append(f"{len(errors)} error{'s' if len(errors) != 1 else ''}")
    parts.append(f"{len(unfinished)} unfinished task{'s' if len(unfinished) != 1 else ''}")
    unfinished_prds = sum(1 for p in prds if not p.finished)
    if unfinished_prds:
        parts.append(f"{unfinished_prds} unfinished PRD{'s' if unfinished_prds != 1 else ''}")
    out.append(", ".join(parts))

    return "\n".join(out)


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify specs/prd and specs/tasks finished state.")
    parser.add_argument("specs", nargs="?", default="specs", help="specs directory (default: specs)")
    parser.add_argument("--json", action="store_true", help="emit machine-readable output")
    args = parser.parse_args()

    specs = Path(args.specs)
    if not specs.is_dir():
        print(f"error: {specs} is not a directory", file=sys.stderr)
        return 2

    prds, tasks, issues, extra = collect(specs)
    errors = [i for i in issues if i.level == "error"]
    unfinished = [t for t in tasks if not t.finished]
    unfinished_prds = [p for p in prds if not p.finished]

    if args.json:
        print(
            json.dumps(
                {
                    "specs": str(specs.resolve()),
                    "prd": [
                        {
                            "path": p.path,
                            "name": p.name,
                            "status": p.status,
                            "finished": p.finished,
                            **extra["prd"].get(p.path, {}),
                        }
                        for p in prds
                    ],
                    "tasks": [
                        {
                            "name": t.name,
                            "file": t.file,
                            "index": t.index,
                            "status": t.status,
                            "finished": t.finished,
                            "goals": t.goals,
                            "dependsOn": t.depends,
                        }
                        for t in tasks
                    ],
                    "finished": [t.name for t in tasks if t.finished],
                    "unfinished": [t.name for t in tasks if not t.finished],
                    "issues": [vars(i) for i in issues],
                    "summary": {
                        "errors": len(errors),
                        "warnings": len(issues) - len(errors),
                        "finished_tasks": len(tasks) - len(unfinished),
                        "unfinished_tasks": len(unfinished),
                        "finished_prds": len(prds) - len(unfinished_prds),
                        "unfinished_prds": len(unfinished_prds),
                    },
                },
                indent=2,
            )
        )
    else:
        print(render(specs, prds, tasks, issues, extra))

    if errors:
        return 2
    if unfinished or unfinished_prds:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())