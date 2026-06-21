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
        if role == "Standards Judge":
            output_file = f"{output_file} + verdict.md"
        rows.append(f"| {role} |  |  | {output_file} | queued |  |  |")
    return "\n".join(rows)


def role_output(role: str, topic: str) -> str:
    verdict_note = ""
    if role == "Standards Judge":
        verdict_note = "        - also_owns: verdict.md\n"
    return f"""
        # {role}: {topic}

        - status: queued
        - thread_id:
        - assigned_packets:
{verdict_note}

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

            See `standards.md`, `hard-standards.md`, and `standards-package.md`.

            ## Logic Orchestration

            See `logic-orchestration.md`.

            ## Engineering Governance

            See `engineering-governance.md`.

            ## Mental Models

            See `mental-models-selected.md`.

            ## Project Link

            See `project-link.md` and `project-dispatch.md`.

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
            - Mental model selection file:
            - Smallest next experiment:
            - Hard standards package:
            - Logic orchestration status:
            - Engineering governance evidence:
            - Project link and dispatch:
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
        "hard-standards.md": f"""
            # Hard Standards: {topic}

            - status: draft
            - owner: Conductor + Standards Judge

            Every non-trivial `$think` run must turn the user's quality bar into
            hard, observable, enforceable standards. Advice is not accepted until
            these standards are concrete enough for another agent to judge.

            | id | scope | hard requirement | observable metric | pass line | hard reject line | evidence required | owner role | dispatch target |
            | --- | --- | --- | --- | --- | --- | --- | --- | --- |
            | HS-001 |  |  |  |  |  |  |  |  |

            ## Notes

            - Each row must be judgeable without hidden context.
            - `hard reject line` means the output must be returned for revision
              even if other parts look useful.
            - If a standard depends on current facts, cite the local path or
              external source used to verify it.
        """,
        "mental-models-selected.md": f"""
            # Mental Models Selected: {topic}

            - status: draft
            - source_library: references/mental-models-100.md
            - candidate_pool: 100
            - selected_count:
            - problem_domain:

            ## Selection Method

            Classify the problem domain, scan all 100 model cards, shortlist
            candidate models, and select only models that materially change the
            conclusion, hard standard, evidence requirement, or experiment.

            ## Selected Models

            | id | model | family | what it changes | implication | evidence or experiment |
            | --- | --- | --- | --- | --- | --- |
            | M001 |  |  |  |  |  |

            ## Tempting Rejected Models

            | id | model | why rejected |
            | --- | --- | --- |

            ## Standards And Experiment Changes

            - Hard standards changed:
            - Experiments changed:
            - Decision card changes:
        """,
        "logic-orchestration.md": f"""
            # Logic Orchestration: {topic}

            - status: draft
            - owner: Conductor
            - current_phase: briefing

            ## Phase State

            | phase | owner | entry_condition | exit_condition | evidence_required | fallback |
            | --- | --- | --- | --- | --- | --- |
            | briefing | Conductor | raw input exists | problem brief complete | session.md brief | ask one concise question or inspect local context |
            | standards-drafting | Conductor + Standards Judge | problem brief complete | standards and hard standards drafted | standards.md, hard-standards.md | mark needs-revision and tighten gates |
            | thread-routing | Conductor | initial artifacts drafted | role threads confirmed or simulated mode recorded | thread-routing.md | record failure and run simulated roles |
            | module-analysis | Systems Decomposer | routing ready | modules reviewed | modules.md and role output | create revision packet |
            | evidence-check | Evidence & Mental Models Strategist | modules ready | evidence gaps and models recorded | mental-models-selected.md | mark assumptions or run lookup |
            | judge-review | Standards Judge | artifacts complete | verdict accepted | verdict.md | route revision packet |
            | synthesis | Conductor | verdict accepted | final synthesis written | final-synthesis.md or session synthesis | stay needs-revision |

            ## Dependency Graph

            | item | depends_on | owner | ready_signal | blocked_signal | recovery |
            | --- | --- | --- | --- | --- | --- |
            | problem brief | raw input | Conductor | session.md brief filled | missing objective or standards | ask one concise question |
            | hard standards | problem brief | Standards Judge | hard-standards.md has pass/reject/evidence lines | vague or unowned standards | revise standards |
            | role routing | initial artifacts | Conductor | thread ids or simulated fallback recorded | missing or unconfirmed thread | retry readback or mark simulated |
            | final synthesis | accepted verdict | Conductor | verdict.md accepted | needs-revision or blocked | route revision or report blocker |

            ## Invariants

            - User standards stay visible.
            - Standards Judge keeps veto power.
            - Facts, assumptions, and judgments stay separated.
            - Required artifacts cannot be skipped.
            - Failures need detection, owner, recovery action, and re-check evidence.

            ## Handoff Matrix

            | from | to | packet_or_file | acceptance_gate | fallback |
            | --- | --- | --- | --- | --- |
            | Conductor | Standards Judge | hard-standards.md | pass/reject/evidence lines are judgeable | revise standards |
            | Conductor | Systems Decomposer | modules.md | dependencies and recomposition order are explicit | split modules smaller |
            | Conductor | Red Team Devil's Advocate | standards + modules | strongest failure paths identified | run dissent pass |
            | Conductor | Evidence & Mental Models Strategist | evidence/model packet | facts and models change standards or experiments | mark assumptions and request lookup |

            ## Next-Action Queue

            | id | action | owner | prerequisite | success_signal | fail_signal | status |
            | --- | --- | --- | --- | --- | --- | --- |
            | A1 | fill problem brief and hard standards | Conductor | run folder exists | standards files populated | missing user standard | draft |
            | A2 | route or simulate roles | Conductor | initial artifacts ready | thread-routing.md updated | thread tools unavailable | draft |
            | A3 | collect verdict and validate | Conductor | role outputs ready | verdict accepted and checks pass | needs-revision | draft |

            ## Failure And Recovery Ledger

            | time | failure | detected_by | owner | recovery_action | recheck | status |
            | --- | --- | --- | --- | --- | --- | --- |

            ## Open Loops
        """,
        "engineering-governance.md": f"""
            # Engineering Governance: {topic}

            - status: draft
            - owner: Conductor

            ## Change Scope

            | file_or_surface | action | reason | reversible | in_scope |
            | --- | --- | --- | --- | --- |

            ## Ownership

            | change | owner | reviewer | acceptance_evidence | recovery_owner |
            | --- | --- | --- | --- | --- |

            ## Implementation Plan

            ## Validation Matrix

            | gate | command_or_check | pass_line | fail_line | evidence_path | owner |
            | --- | --- | --- | --- | --- | --- |
            | skill validator | python3 /Users/evander/.codex/skills/think/scripts/validate_models.py | exits 0 | non-zero exit | command output | Conductor |
            | fresh session generation | new_session.py --topic <test> --dry-run --json | includes required artifacts | missing artifact | command output | Conductor |

            ## Evidence Ledger

            | time | evidence | result | caveat |
            | --- | --- | --- | --- |

            ## Rollback Plan

            ## Drift And Maintenance

            | drift_risk | detector | refresh_trigger | owner |
            | --- | --- | --- | --- |
            | references drift from templates | validator structure checks | validator fails or new required artifact added | Conductor |
            | thread tool behavior changes | recorded routing anomalies | readback/title recovery needed | Conductor |

            ## Unresolved Risks
        """,
        "standards-package.md": f"""
            # Standards Package: {topic}

            - status: draft
            - source_run:
            - linked_project:
            - dispatch_status: not-dispatched

            ## Purpose

            This file packages the run's hard standards so a project team can
            import them into its project instructions, project map, review gates,
            and next execution packet.

            ## Included Standards

            - See `hard-standards.md`.

            ## Required Project-Side Handling

            - Update `artifacts/project-instructions.md` or equivalent.
            - Update `project-map.md` acceptance indicators when present.
            - Create the next plan, execution, or review packet.
            - Do not treat this package as archival-only.

            ## Source Artifacts

            - `standards.md`
            - `hard-standards.md`
            - `logic-orchestration.md`
            - `engineering-governance.md`
            - `mental-models-selected.md`
            - `verdict.md`
            - `final-synthesis.md` when present
        """,
        "project-link.md": f"""
            # Project Link: {topic}

            - status: unresolved
            - selected_project:
            - selected_team_id:
            - selected_score:
            - selection_policy: choose-highest-score
            - locator_command:

            ## Candidate Projects

            | rank | score | project_path | team_id | evidence | reason |
            | ---: | ---: | --- | --- | --- | --- |

            ## Decision Notes

            - `$think` should locate the project this thinking run is meant to
              serve before final synthesis when project linkage is relevant.
            - If multiple candidates exist, choose the highest score and record
              the candidate table here.
            - If no project is found, keep this file unresolved and produce
              `project-start-prompt.md`.
        """,
        "project-dispatch.md": f"""
            # Project Dispatch: {topic}

            - status: not-dispatched
            - target_project:
            - target_team_id:
            - target_role:
            - packet_id:
            - packet_path:
            - direct_thread_status:
            - direct_thread_id:
            - fallback_prompt:

            ## Dispatch Rule

            If the selected project has a team `message-queue.md`, create one
            project-side packet named `packets/P-<timestamp>-think-hard-standards.md`.
            Default receiver is `协调师`; if no coordinator profile or inbox exists
            but a planner exists, use `规划师`.

            ## Required Packet Meaning

            Purpose: `plan_feedback` / `standard_update`.

            The project must update its acceptance gates and create the next
            plan, execution, or review packet. The project must not only archive
            the standards package.

            ## Dispatch Evidence

            | item | value |
            | --- | --- |
            | queue_row_added |  |
            | inbox_written |  |
            | direct_message_sent |  |
            | blocked_reason |  |
        """,
        "project-start-prompt.md": f"""
            # Project Start Prompt: {topic}

            Use this only when no existing project can be selected.

            ```text
            /team 项目：<paste the project goal here>

            请先读取这个 `$think` run folder：
            {run_dir}

            必读文件：
            - hard-standards.md
            - logic-orchestration.md
            - engineering-governance.md
            - standards-package.md
            - verdict.md
            - final-synthesis.md（如果存在）

            你的任务：
            1. 把 hard-standards.md 写入项目指示和验收标准。
            2. 建立 project-map.md，并把这些标准转成可观察评估指标。
            3. 创建下一步 packet，让项目直接进入执行或审核链路。
            4. 不要只保存标准；必须让项目开跑。
            ```
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
