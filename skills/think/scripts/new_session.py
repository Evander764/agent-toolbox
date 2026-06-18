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
DEFAULT_PROJECT_ID = "/Users/evander/Documents/Agent thinking"

ROLE_FILES = {
    "Standards Judge": "agents/standards-judge.md",
    "Systems Decomposer": "agents/systems-decomposer.md",
    "Red Team Devil's Advocate": "agents/red-team.md",
    "Evidence & Mental Models Strategist": "agents/evidence-models.md",
}


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
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(dedent(content).lstrip(), encoding="utf-8")


def table_rows_for_threads() -> str:
    rows = []
    for role, output_file in ROLE_FILES.items():
        rows.append(f"| {role} |  |  | {output_file} | queued |  |  |")
    return "\n".join(rows)


def role_output(role: str, topic: str) -> str:
    return f"""
        # {role}: {topic}

        - status: queued
        - thread_id:
        - assigned_packets:

        ## Role Output

        ## Blockers

        ## Revision Requests

        ## Summary For Conductor
    """


def build_files(
    run_dir: Path,
    topic: str,
    now: datetime,
    agent_count: int,
    project_id: str,
) -> dict[str, str]:
    created_at = now.astimezone().isoformat(timespec="seconds")
    files = {
        "session.md": f"""
            # Thinking Session: {topic}

            - created_at: {created_at}
            - mode: pending
            - agent_count: {agent_count}
            - status: draft
            - project_id: {project_id}
            - conductor_thread:

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

            ## Standards Snapshot

            See `standards.md`.

            ## Module Map

            See `modules.md`.

            ## Thread Routing

            See `thread-routing.md`.

            ## Round 1: Independent Judgments

            ## Round 2: Cross-examination

            ## Synthesis

            - Judge verdict:
            - Disruptive conclusion:
            - Conservative conclusion:
            - Strongest counterargument:
            - Entropy cost:
            - Mental models that changed the decision:
            - Smallest next experiment:
            - Next input loop:
        """,
        "thread-routing.md": f"""# Thread Routing: {topic}

| role | thread_title | thread_id | output_file | status | last_prompt | last_read_at |
| --- | --- | --- | --- | --- | --- | --- |
{table_rows_for_threads()}

## Notes

- Real multi-window mode requires thread ids in this table.
- If thread tools are unavailable, set session mode to `simulated`.
""",
        "message-queue.md": f"""
            # Message Queue: {topic}

            | packet | from | to | purpose | status | thread_id | source_refs | next |
            | --- | --- | --- | --- | --- | --- | --- | --- |
        """,
        "standards.md": f"""
            # Standards: {topic}

            - status: draft

            ## User Standards

            ## Inferred Acceptance Gates

            ## Rejection Criteria

            ## Evidence Required
        """,
        "modules.md": f"""
            # Modules: {topic}

            | id | module | question | dependencies | assigned_roles | acceptance_gate | status |
            | --- | --- | --- | --- | --- | --- | --- |
            | M1 |  |  |  |  |  | draft |

            ## Recomposition Order
        """,
        "verdict.md": f"""
            # Verdict: {topic}

            - judge: Standards Judge
            - status: draft

            ## Accepted

            ## Needs Revision

            ## Blocked

            ## Required Next Packet
        """,
        "decision-card.md": f"""
            # Decision Card: {topic}

            - decision_needed:
            - recommended_action:
            - confidence:
            - time_horizon:
            - judge_verdict:

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
        "packets/README.md": f"""
            # Packets: {topic}

            Use one packet per role assignment, revision request, blocker, or
            judge verdict routed between threads.
        """,
    }
    for role, output_file in ROLE_FILES.items():
        files[output_file] = role_output(role, topic)
    return {str(run_dir / name): content for name, content in files.items()}


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a thinking-room session folder.")
    parser.add_argument("--topic", required=True, help="Short topic for this thinking session")
    parser.add_argument("--root", default=str(DEFAULT_ROOT), help="Second-brain root directory")
    parser.add_argument("--agent-count", type=int, default=4, help="Planned agent count, usually 2-4")
    parser.add_argument("--project-id", default=DEFAULT_PROJECT_ID, help="Codex project id for thread creation")
    parser.add_argument("--dry-run", action="store_true", help="Print planned paths without writing files")
    parser.add_argument("--json", action="store_true", help="Print machine-readable output")
    args = parser.parse_args()

    if args.agent_count < 1:
        raise SystemExit("--agent-count must be at least 1")

    root = Path(args.root).expanduser()
    now = datetime.now().astimezone()
    run_dir = unique_run_dir(root, args.topic, now)
    files = build_files(run_dir, args.topic, now, args.agent_count, args.project_id)

    result = {
        "root": str(root),
        "run_dir": str(run_dir),
        "topic": args.topic,
        "agent_count": args.agent_count,
        "project_id": args.project_id,
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
