#!/usr/bin/env python3
"""Create a stable run folder for Think sessions."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import datetime
from pathlib import Path
from textwrap import dedent


DEFAULT_ROOT = Path("/Users/evander/Documents/Agent thinking/second-brain")


def slugify(topic: str) -> str:
    ascii_topic = topic.encode("ascii", "ignore").decode("ascii").lower()
    slug = re.sub(r"[^a-z0-9]+", "-", ascii_topic).strip("-")
    if not slug:
        digest = hashlib.sha1(topic.encode("utf-8")).hexdigest()[:8]
        slug = f"topic-{digest}"
    return slug[:64].strip("-") or "topic"


def unique_run_dir(root: Path, topic: str, now: datetime) -> Path:
    base = root / "runs" / f"{now:%Y-%m-%d}--{slugify(topic)}"
    if not base.exists():
        return base
    for index in range(2, 100):
        candidate = root / "runs" / f"{now:%Y-%m-%d}--{slugify(topic)}-{index:02d}"
        if not candidate.exists():
            return candidate
    raise RuntimeError("Could not find an available run directory name")


def write_file(path: Path, content: str) -> None:
    path.write_text(dedent(content).lstrip(), encoding="utf-8")


def build_files(run_dir: Path, topic: str, now: datetime, agent_count: int) -> dict[str, str]:
    created_at = now.astimezone().isoformat(timespec="seconds")
    files = {
        "session.md": f"""
            # Thinking Session: {topic}

            - created_at: {created_at}
            - mode: pending
            - agent_count: {agent_count}
            - status: draft

            ## Raw Input

            ## Problem Brief

            - Objective:
            - Success criteria:
            - Constraints:
            - Current state:
            - Assumptions:
            - Unknowns:

            ## Blockization

            | block | content | evidence/status |
            | --- | --- | --- |
            | facts |  |  |
            | assumptions |  |  |
            | judgments |  |  |
            | variables |  |  |
            | risks |  |  |
            | actions |  |  |

            ## Round 1: Independent Judgments

            ## Round 2: Cross-examination

            ## Synthesis

            - Disruptive conclusion:
            - Conservative conclusion:
            - Strongest counterargument:
            - Entropy cost:
            - Mental models that changed the decision:
            - Smallest next experiment:
            - Next input loop:
        """,
        "decision-card.md": f"""
            # Decision Card: {topic}

            - decision_needed:
            - recommended_action:
            - confidence:
            - time_horizon:

            ## Why This Is The Current Best Move

            ## Strongest Case Against It

            ## What Would Change The Decision

            ## Entropy And Maintenance Cost

            ## Minimum Experiment

            - hypothesis:
            - action:
            - metric:
            - pass_signal:
            - fail_signal:
            - time_box:
            - next_decision:
        """,
        "experiments.md": f"""
            # Experiments: {topic}

            | id | hypothesis | action | metric | pass | fail | time_box | status |
            | --- | --- | --- | --- | --- | --- | --- | --- |
            | E1 |  |  |  |  |  |  | proposed |
        """,
        "evolution-proposal.md": f"""
            # Evolution Proposal: {topic}

            - status: pending-user-review
            - target: none

            ## Trigger

            What happened in this run that suggests the system should evolve?

            ## Proposed Change

            ## Why It Improves The System

            ## Risk Of This Change

            ## Writeback Instructions After Approval

            No writeback should happen until the user explicitly approves this proposal.
        """,
    }
    return {str(run_dir / name): content for name, content in files.items()}


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a thinking-room session folder.")
    parser.add_argument("--topic", required=True, help="Short topic for this thinking session")
    parser.add_argument("--root", default=str(DEFAULT_ROOT), help="Second-brain root directory")
    parser.add_argument("--agent-count", type=int, default=4, help="Planned agent count, usually 2-4")
    parser.add_argument("--dry-run", action="store_true", help="Print planned paths without writing files")
    parser.add_argument("--json", action="store_true", help="Print machine-readable output")
    args = parser.parse_args()

    if args.agent_count < 1:
        raise SystemExit("--agent-count must be at least 1")

    root = Path(args.root).expanduser()
    now = datetime.now().astimezone()
    run_dir = unique_run_dir(root, args.topic, now)
    files = build_files(run_dir, args.topic, now, args.agent_count)

    result = {
        "root": str(root),
        "run_dir": str(run_dir),
        "topic": args.topic,
        "agent_count": args.agent_count,
        "files": list(files.keys()),
        "dry_run": args.dry_run,
    }

    if not args.dry_run:
        run_dir.mkdir(parents=True, exist_ok=False)
        for file_path, content in files.items():
            write_file(Path(file_path), content)

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"run_dir: {run_dir}")
        for file_path in files:
            print(f"file: {file_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
