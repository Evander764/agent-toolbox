# Output Templates

Use these templates for run artifacts under:

```text
/Users/evander/Documents/Agent thinking/second-brain/runs/YYYY-MM-DD--topic/
```

## session.md

```markdown
# Thinking Session: <topic>

- created_at:
- mode: real-subagents | simulated
- agent_count:
- status: draft | complete
- project_id:
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
```

## thread-routing.md

```markdown
# Thread Routing: <topic>

| role | thread_title | thread_id | output_file | status | last_prompt | last_read_at |
| --- | --- | --- | --- | --- | --- | --- |
| Standards Judge |  |  | agents/standards-judge.md | queued |  |  |
| Systems Decomposer |  |  | agents/systems-decomposer.md | queued |  |  |
| Red Team Devil's Advocate |  |  | agents/red-team.md | queued |  |  |
| Evidence & Mental Models Strategist |  |  | agents/evidence-models.md | queued |  |  |
```

For `Standards Judge`, the output file cell may be
`agents/standards-judge.md + verdict.md` because the judge owns the detailed
gate file and the canonical verdict.

## message-queue.md

```markdown
# Message Queue: <topic>

| packet | from | to | purpose | status | thread_id | source_refs | next |
| --- | --- | --- | --- | --- | --- | --- | --- |
```

## standards.md

```markdown
# Standards: <topic>

- status: draft | accepted | needs-revision | blocked

## User Standards

## Inferred Acceptance Gates

## Rejection Criteria

## Evidence Required
```

## hard-standards.md

```markdown
# Hard Standards: <topic>

- status: draft | accepted | needs-revision | blocked
- owner: Conductor + Standards Judge

| id | scope | hard requirement | observable metric | pass line | hard reject line | evidence required | owner role | dispatch target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| HS-001 |  |  |  |  |  |  |  |  |

## Notes

- Each row must be judgeable without hidden context.
- Every non-trivial `$think` run needs pass lines, hard reject lines, and
  evidence requirements.
```

## mental-models-selected.md

```markdown
# Mental Models Selected: <topic>

- status: draft | accepted | needs-revision | blocked
- source_library: references/mental-models-100.md
- candidate_pool: 100
- selected_count:
- problem_domain:

## Selection Method

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
```

## logic-orchestration.md

```markdown
# Logic Orchestration: <topic>

- status: draft | accepted | needs-revision | blocked
- owner: Conductor
- current_phase:

## Phase State

| phase | owner | entry_condition | exit_condition | evidence_required | fallback |
| --- | --- | --- | --- | --- | --- |
| briefing | Conductor | raw input exists | problem brief complete | session.md brief | ask one concise question or inspect local context |

## Dependency Graph

| item | depends_on | owner | ready_signal | blocked_signal | recovery |
| --- | --- | --- | --- | --- | --- |

## Invariants

- User standards stay visible.
- Standards Judge keeps veto power.
- Facts, assumptions, and judgments stay separated.
- Required artifacts cannot be skipped.
- Failures need detection, owner, recovery action, and re-check evidence.

## Handoff Matrix

| from | to | packet_or_file | acceptance_gate | fallback |
| --- | --- | --- | --- | --- |

## Next-Action Queue

| id | action | owner | prerequisite | success_signal | fail_signal | status |
| --- | --- | --- | --- | --- | --- | --- |

## Failure And Recovery Ledger

| time | failure | detected_by | owner | recovery_action | recheck | status |
| --- | --- | --- | --- | --- | --- | --- |

## Open Loops
```

## engineering-governance.md

```markdown
# Engineering Governance: <topic>

- status: draft | accepted | needs-revision | blocked
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

## Evidence Ledger

| time | evidence | result | caveat |
| --- | --- | --- | --- |

## Rollback Plan

## Drift And Maintenance

| drift_risk | detector | refresh_trigger | owner |
| --- | --- | --- | --- |

## Unresolved Risks
```

## standards-package.md

```markdown
# Standards Package: <topic>

- status: draft | dispatched | blocked
- source_run:
- linked_project:
- dispatch_status:

## Purpose

## Included Standards

## Required Project-Side Handling

- Update project instructions or equivalent.
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
```

## project-link.md

```markdown
# Project Link: <topic>

- status: unresolved | selected | not-found
- selected_project:
- selected_team_id:
- selected_score:
- selection_policy: choose-highest-score
- locator_command:

## Candidate Projects

| rank | score | project_path | team_id | evidence | reason |
| ---: | ---: | --- | --- | --- | --- |

## Decision Notes
```

## project-dispatch.md

```markdown
# Project Dispatch: <topic>

- status: not-dispatched | dispatched | blocked | not-applicable
- target_project:
- target_team_id:
- target_role:
- packet_id:
- packet_path:
- direct_thread_status:
- direct_thread_id:
- fallback_prompt:

## Dispatch Rule

## Required Packet Meaning

## Dispatch Evidence

| item | value |
| --- | --- |
| queue_row_added |  |
| inbox_written |  |
| direct_message_sent |  |
| blocked_reason |  |
```

## project-start-prompt.md

````markdown
# Project Start Prompt: <topic>

Use this only when no existing project can be selected.

```text
/team 项目：<project goal>

请先读取这个 `$think` run folder：
<run folder>

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
````

## modules.md

```markdown
# Modules: <topic>

| id | module | question | dependencies | assigned_roles | acceptance_gate | status |
| --- | --- | --- | --- | --- | --- | --- |
| M1 |  |  |  |  |  | draft |

## Recomposition Order
```

## verdict.md

```markdown
# Verdict: <topic>

- judge: Standards Judge
- status: draft | accepted | needs-revision | blocked

## Accepted

## Needs Revision

## Blocked

## Required Next Packet
```

## role output files

Default role outputs live under `agents/`:

- `agents/standards-judge.md`;
- `agents/systems-decomposer.md`;
- `agents/red-team.md`;
- `agents/evidence-models.md`.

`Standards Judge` is the exception: it also writes `verdict.md` as the
canonical accepted / needs-revision / blocked gate.

`Evidence & Mental Models Strategist` also writes `mental-models-selected.md`
as the canonical record of model selection from the 100-card library.

## decision-card.md

```markdown
# Decision Card: <topic>

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
```

## experiments.md

```markdown
# Experiments: <topic>

| id | hypothesis | action | metric | pass | fail | time_box | status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 |  |  |  |  |  |  | proposed |
```

## evolution-proposal.md

```markdown
# Evolution Proposal: <topic>

- status: pending-user-review
- target: SKILL.md | protocol | roles | mental-models | quality-gates | outputs | none

## Trigger

What happened in this run that suggests the system should evolve?

## Proposed Change

## Why It Improves The System

## Risk Of This Change

## Writeback Instructions After Approval

No writeback should happen until the user explicitly approves this proposal.
```
