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
STATUSES = ("draft", "pending", "complete", "canceled")
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