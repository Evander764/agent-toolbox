#!/usr/bin/env python3
"""Locate the project a Think run should serve.

This helper is intentionally read-only. It scores candidate project/team
directories and prints a ranked table or JSON payload. Dispatch remains the
Conductor's job because project packet state requires human-visible judgment.
"""

from __future__ import annotations

import argparse
import json
import os
import re
from dataclasses import dataclass, field
from pathlib import Path
from time import time
from typing import Iterable


DEFAULT_ROOTS = [
    Path("/Users/evander/Documents"),
    Path("/Users/evander/.openclaw"),
]

MARKER_FILES = {
    "project-map.md",
    "team.md",
    "board.md",
    "status.md",
    "ROADMAP.md",
    "LATEST_STATE.md",
    "message-queue.md",
}

PRUNE_DIRS = {
    ".git",
    ".hg",
    ".svn",
    ".cache",
    ".next",
    ".venv",
    "__pycache__",
    "node_modules",
    "Library",
    "Applications",
    "dist",
    "build",
    "DerivedData",
}


@dataclass
class Candidate:
    path: Path
    markers: set[str] = field(default_factory=set)
    score: int = 0
    reasons: list[str] = field(default_factory=list)
    team_id: str = ""
    mtime: float = 0.0


def normalize(text: str) -> str:
    return text.lower()


def query_terms(text: str) -> list[str]:
    terms: set[str] = set()
    for token in re.findall(r"[a-zA-Z0-9_+-]+", text.lower()):
        if len(token) >= 2 and token not in {"the", "and", "for", "with"}:
            terms.add(token)
    for cjk in re.findall(r"[\u4e00-\u9fff]+", text):
        if len(cjk) <= 4:
            terms.add(cjk)
        for size in (2, 3, 4):
            for idx in range(0, max(0, len(cjk) - size + 1)):
                terms.add(cjk[idx : idx + size])
    return sorted(terms, key=lambda item: (-len(item), item))


def safe_read(path: Path, max_chars: int = 12000) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="ignore")[:max_chars]
    except OSError:
        return ""


def iter_candidate_dirs(roots: Iterable[Path]) -> dict[Path, Candidate]:
    candidates: dict[Path, Candidate] = {}
    for root in roots:
        root = root.expanduser()
        if not root.exists():
            continue
        for current, dirs, files in os.walk(root):
            current_path = Path(current)
            dirs[:] = [
                d
                for d in dirs
                if d not in PRUNE_DIRS
                and not d.endswith(".app")
                and not d.startswith(".")
            ]

            markers = set(files).intersection(MARKER_FILES)
            is_team = current_path.name.startswith("team-") and current_path.parent.name == "teams"
            if is_team or markers:
                candidate = candidates.setdefault(current_path, Candidate(path=current_path))
                candidate.markers.update(markers)
                if is_team:
                    candidate.markers.add("team-dir")
                continue

            # A project root may not have team files itself, but a direct child
            # can be a teams folder; keep the actual team directories as
            # candidates to avoid dispatching to an ambiguous parent.
    return candidates


def extract_team_id(candidate: Candidate) -> str:
    if candidate.path.name.startswith("team-"):
        return candidate.path.name
    team_md = candidate.path / "team.md"
    text = safe_read(team_md, max_chars=4000)
    match = re.search(r"team[_ -]?id:\s*([^\n]+)", text, flags=re.I)
    if match:
        return match.group(1).strip().strip("`")
    return ""


def candidate_text(candidate: Candidate) -> str:
    parts = [str(candidate.path)]
    for marker in sorted(candidate.markers.intersection(MARKER_FILES)):
        parts.append(f"\n--- {marker} ---\n")
        parts.append(safe_read(candidate.path / marker))
    return "\n".join(parts)


def score_candidate(candidate: Candidate, terms: list[str], evidence_paths: list[Path]) -> None:
    text = normalize(candidate_text(candidate))
    path_text = normalize(str(candidate.path))

    for term in terms:
        term_l = normalize(term)
        if term_l in path_text:
            candidate.score += 10
        if term_l in text:
            candidate.score += 6

    for evidence in evidence_paths:
        evidence_l = normalize(str(evidence))
        if evidence_l and (path_text in evidence_l or evidence_l in path_text):
            candidate.score += 25
            candidate.reasons.append(f"evidence path overlaps {evidence}")
        else:
            for part in evidence.parts[-4:]:
                if len(part) > 2 and normalize(part) in text:
                    candidate.score += 4

    marker_score = {
        "project-map.md": 18,
        "message-queue.md": 14,
        "board.md": 10,
        "status.md": 10,
        "team.md": 12,
        "ROADMAP.md": 14,
        "LATEST_STATE.md": 14,
        "team-dir": 8,
    }
    for marker in candidate.markers:
        candidate.score += marker_score.get(marker, 0)

    if (candidate.path / "packets").is_dir():
        candidate.score += 8
        candidate.reasons.append("has packets/")
    if (candidate.path / "inbox").is_dir():
        candidate.score += 4
        candidate.reasons.append("has inbox/")

    try:
        mtimes = [p.stat().st_mtime for p in candidate.path.iterdir() if p.is_file()]
        candidate.mtime = max(mtimes) if mtimes else candidate.path.stat().st_mtime
    except OSError:
        candidate.mtime = 0
    age_days = max(0.0, (time() - candidate.mtime) / 86400) if candidate.mtime else 999
    recency = max(0, 12 - int(age_days))
    candidate.score += recency
    if recency:
        candidate.reasons.append(f"recent:{recency}")

    candidate.team_id = extract_team_id(candidate)
    if "project-map.md" in candidate.markers:
        candidate.reasons.append("has project-map")
    if "message-queue.md" in candidate.markers:
        candidate.reasons.append("has queue")
    if candidate.path.name.startswith("team-"):
        candidate.reasons.append("team directory")


def to_row(rank: int, candidate: Candidate) -> dict[str, object]:
    return {
        "rank": rank,
        "score": candidate.score,
        "project_path": str(candidate.path),
        "team_id": candidate.team_id,
        "markers": sorted(candidate.markers),
        "reason": "; ".join(candidate.reasons[:6]),
    }


def print_markdown(rows: list[dict[str, object]]) -> None:
    print("| rank | score | project_path | team_id | evidence | reason |")
    print("| ---: | ---: | --- | --- | --- | --- |")
    for row in rows:
        evidence = ", ".join(row["markers"])  # type: ignore[arg-type]
        print(
            f"| {row['rank']} | {row['score']} | {row['project_path']} | "
            f"{row['team_id']} | {evidence} | {row['reason']} |"
        )


def main() -> int:
    parser = argparse.ArgumentParser(description="Read-only Think project locator")
    parser.add_argument("--query", required=True, help="Thinking topic or user request")
    parser.add_argument(
        "--root",
        action="append",
        default=[],
        help="Root to scan. Defaults to Documents and .openclaw.",
    )
    parser.add_argument(
        "--evidence",
        action="append",
        default=[],
        help="Evidence path associated with the thinking run.",
    )
    parser.add_argument("--limit", type=int, default=8)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    roots = [Path(item).expanduser() for item in args.root] if args.root else DEFAULT_ROOTS
    evidence_paths = [Path(item).expanduser() for item in args.evidence]
    terms = query_terms(args.query)
    candidates = list(iter_candidate_dirs(roots).values())
    for candidate in candidates:
        score_candidate(candidate, terms, evidence_paths)
    ranked = sorted(candidates, key=lambda item: (-item.score, str(item.path)))[: args.limit]
    rows = [to_row(index + 1, candidate) for index, candidate in enumerate(ranked)]

    if args.json:
        print(json.dumps({"query": args.query, "terms": terms, "candidates": rows}, ensure_ascii=False, indent=2))
    else:
        print_markdown(rows)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
