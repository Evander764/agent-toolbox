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
```

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
