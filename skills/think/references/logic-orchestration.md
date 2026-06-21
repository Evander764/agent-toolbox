# Logic Orchestration / 逻辑编排

Use this reference to keep a `$think` run ordered, observable, and recoverable.
`逻辑编排` means the Conductor owns the run as a state machine, not as a loose
conversation.

## Required Artifact

Every non-trivial run must create `logic-orchestration.md` before final
synthesis.

Required sections:

- phase state;
- dependency graph;
- invariants;
- handoff matrix;
- next-action queue;
- failure and recovery ledger;
- open loops.

## Phase State

Allowed phase states:

- `briefing`;
- `standards-drafting`;
- `project-linking`;
- `thread-routing`;
- `module-analysis`;
- `evidence-check`;
- `judge-review`;
- `revision`;
- `synthesis`;
- `dispatch`;
- `complete`;
- `blocked`.

Each state entry must name:

- current owner;
- entry condition;
- exit condition;
- evidence required to leave the state;
- fallback when the exit condition fails.

The Conductor must not skip directly from `briefing` to `synthesis` on a
non-trivial run.

## Dependency Graph

Record dependencies in a compact table:

| item | depends_on | owner | ready_signal | blocked_signal | recovery |
| --- | --- | --- | --- | --- | --- |

Use this graph to decide execution order. If a later artifact depends on a
missing earlier artifact, the run is `needs-revision` or `blocked`, not
accepted.

## Invariants

These invariants must stay true throughout the run:

- user standards remain visible and are not softened for convenience;
- `Standards Judge` keeps veto power;
- facts, assumptions, and judgments remain separated;
- current or external facts are verified or marked as assumptions;
- every handoff names the receiver, output file, and acceptance gate;
- every serious failure has a detection signal, owner, recovery action, and
  re-check evidence;
- no final synthesis is accepted while a required artifact is missing.

## Handoff Matrix

For each role handoff, record:

- sender;
- receiver;
- packet or file;
- acceptance gate;
- due condition;
- recovery path if the receiver is unavailable or output is incomplete.

If Codex thread tools fail, mark the affected role as `simulated` or
`unconfirmed`; do not claim real multi-window collaboration for that role.

## Next-Action Queue

The queue contains only actionable next steps:

| id | action | owner | prerequisite | success signal | fail signal | status |
| --- | --- | --- | --- | --- | --- | --- |

Do not use the queue as a dumping ground for ideas. Each row must either move
the run toward acceptance or resolve a blocker.

## Failure And Recovery Ledger

Record every meaningful failure or anomaly:

| time | failure | detected_by | owner | recovery_action | recheck | status |
| --- | --- | --- | --- | --- | --- | --- |

Examples:

- thread creation returned an id, but title assignment initially failed;
- validator failed;
- project dispatch target was not found;
- judge verdict was `needs-revision`;
- required current fact could not be verified.

The recovery is not complete until the `recheck` evidence passes or the run is
explicitly marked `blocked`.

## Open Loops

Before final synthesis, list all unresolved loops. A non-trivial run can be
`accepted` only when all critical loops are closed, downgraded with evidence, or
declared blocked with the reason and owner.
