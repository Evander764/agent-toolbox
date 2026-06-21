# Quality Gates

Use these gates before presenting a final thinking-room result.

## Hard Gates

A run is not acceptable unless it contains:

- a compressed problem brief;
- a `standards.md` file with user-aligned pass/fail gates;
- a `hard-standards.md` file with standard id, scope, hard requirement,
  observable metric, pass line, hard reject line, evidence required, owner role,
  and dispatch target for every non-trivial run;
- a `standards-package.md` file that can be handed to a project team;
- a `logic-orchestration.md` file with phase state, dependency graph,
  invariants, handoff matrix, next-action queue, failure/recovery ledger, and
  open loops for every non-trivial run;
- an `engineering-governance.md` file with change scope, ownership, validation
  matrix, evidence ledger, rollback plan, drift/maintenance checks, and
  unresolved risks for every non-trivial run that changes files, routes project
  work, or proposes durable system updates;
- a `mental-models-selected.md` file for every non-trivial run;
- `project-link.md` and `project-dispatch.md` when the run is project-related,
  or a filled `project-start-prompt.md` when no existing project is found;
- `thread-routing.md` showing real thread IDs, or `mode: simulated` with a
  clear fallback explanation;
- blockization into facts, assumptions, judgments, variables, risks, and action
  options;
- module decomposition for complex tasks;
- first-principles reduction;
- entropy/system-decay analysis;
- at least three and at most nine relevant mental models selected from the
  100-card library, unless the task is trivial or an exception is recorded;
- a strongest counterargument;
- explicit falsification criteria;
- at least one information gap;
- a smallest useful experiment;
- feedback/update path;
- a `verdict.md` result from `Standards Judge`;
- an `evolution-proposal.md` entry, even if the proposal is "no update".

## Standards Judge Gate

`Standards Judge` is mandatory. Final status can be:

- `accepted`: every hard gate is met, including hard standards and the
  project dispatch/startup path when applicable;
- `needs-revision`: at least one required gate fails;
- `blocked`: required evidence, permission, or context is missing.

The Conductor must not present `needs-revision` or `blocked` work as complete.
If the judge rejects a module, create a revision packet and route it before
final synthesis.

`Standards Judge` must be assigned both `agents/standards-judge.md` and
`verdict.md`. It must reject runs whose standards are advice-like, subjective,
or missing pass/reject/evidence lines. It must also reject mental-model output
that names models without changing a conclusion, hard standard, evidence
requirement, or experiment. It must reject runs that lack required
`logic-orchestration.md` or `engineering-governance.md` content, or that leave
serious failures without owner, recovery action, and re-check evidence.

## Hard Standard Gates

Each hard standard must be:

- observable: another agent can inspect evidence and judge it;
- binary or thresholded: the pass line and hard reject line are clear;
- evidence-bound: required proof is named;
- owned: a role or project surface is responsible;
- dispatchable: the target project or role is named when relevant.

Reject standards that use vague words such as "better", "high quality",
"more complete", or "good enough" without a metric, threshold, or hard reject
line.

## Anti-consensus Gates

At least one role must challenge:

- the user's framing;
- the most attractive option;
- the easiest consensus;
- or the assumption that the problem should be solved now.

If all roles agree, run a dissent pass:

```text
Assume the consensus is wrong. What would have to be true?
```

## Evidence Gates

When a claim depends on current or external reality:

- verify it with current lookup or local inspection;
- cite the source or evidence path;
- mark unverified items as assumptions;
- state what remains unknown.

Do not let confident language hide missing evidence.

## Logic Orchestration Gates

For every non-trivial run, `logic-orchestration.md` must show:

- the current phase state and allowed next states;
- dependency graph with owner, ready signal, blocked signal, and recovery;
- invariants that protect user standards and judge veto;
- handoff matrix with receiver, output file, acceptance gate, and fallback;
- next-action queue with actionable rows only;
- failure/recovery ledger with detection, owner, recovery action, re-check, and
  status;
- critical open loops closed, downgraded with evidence, or marked blocked.

Reject runs that skip state, hide dependencies, claim recovery without re-check
evidence, or leave a serious open loop unowned.

## Engineering Governance Gates

For every non-trivial run that changes files, routes project work, or proposes
durable updates, `engineering-governance.md` must show:

- change scope and non-scope;
- owner and reviewer;
- validation matrix with pass and fail lines;
- evidence ledger with concrete paths or command summaries;
- rollback plan for changed files;
- drift and maintenance detector;
- unresolved risks.

For skill-package updates, reject completion unless the default validator ran,
`validate_models.py --self-test` ran when structural contracts changed, a fresh
session was generated when templates/scripts changed, changed files are listed,
and rollback guidance is recorded.

## Mental Model Gates

Every non-trivial run must:

- treat all 100 cards in `references/mental-models-100.md` as the candidate
  pool;
- write `mental-models-selected.md`;
- classify the problem domain;
- select 3-9 models that change the decision, hard standard, evidence
  requirement, or experiment;
- record 2-5 tempting-but-rejected models;
- use the format
  `Model -> what it changes -> implication -> evidence/experiment`.

Reject runs that list model names as decoration, select only familiar models
without scanning the library, or fail to translate models into action.

## Thread Gates

Real multi-window mode requires:

- one recorded thread id per active role;
- one assigned output file per role;
- role prompts that forbid editing other role files;
- at least one `read_thread` check or explicit thread-result collection before
  final synthesis.

If these are missing, mark the run as simulated or incomplete.

If thread creation returns an id but readback or title assignment initially
fails, record the anomaly in `logic-orchestration.md` and mark the thread
`recovered` only after readback succeeds.

## Experiment Gates

Every recommended experiment needs:

- hypothesis;
- action;
- time/cost box;
- metric;
- pass signal;
- fail signal;
- next decision.

Avoid experiments that only produce more opinions.

## Project Link And Dispatch Gates

Project-related runs must:

- scan candidate projects from the current workspace, Documents teams,
  OpenClaw teams, and project marker files;
- record ranked candidates in `project-link.md`;
- choose the highest score when multiple candidates exist;
- write `project-dispatch.md` with target, receiver, packet id, queue/inbox
  status, and direct-thread status;
- create a project-side packet when the selected project has `message-queue.md`;
- avoid claiming delivery if no confirmed direct thread was messaged;
- produce `project-start-prompt.md` instead of creating a new project when no
  project is found.

If the selected project receives a standards package, the package must require
updating project instructions, project map acceptance indicators, and the next
execution/review packet. Archival-only dispatch is not accepted.

## Red Flags

Reject or revise outputs that:

- use "first principles" without reducing the problem;
- mention mental models as a list without implications;
- omit `mental-models-selected.md` for a non-trivial run;
- claim the 100-model library was used without candidate-pool evidence;
- ignore entropy, maintenance, or coordination cost;
- provide advice without falsification;
- provide advice without hard standards;
- call a standards package dispatched when only a local run file was written;
- create a new project automatically when no project was found;
- ask for broad research when a cheap test would work;
- collapse all disagreement into a bland middle ground;
- treat `逻辑编排` or `工程治理` as labels without required artifacts, owners,
  validation, and recovery checks;
- claim a failure was corrected without re-running the relevant check;
- write permanent Skill updates without user approval.
