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
- Smallest next experiment:
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

Each role writes exactly one file under `agents/`:

- `agents/standards-judge.md`;
- `agents/systems-decomposer.md`;
- `agents/red-team.md`;
- `agents/evidence-models.md`.

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
