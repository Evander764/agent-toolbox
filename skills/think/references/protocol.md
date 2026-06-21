# Evolutionary Thinking Protocol

Use this protocol for a complete thinking-room run.

## 1. Input

Convert the user's raw input into a compact problem brief:

- objective: what is being sought;
- decision/action horizon: when this matters;
- success criteria: what would count as better;
- constraints: time, money, tools, authority, energy, risk;
- current state: what is already true;
- explicit preferences: what the user values;
- unknowns: what must be learned or tested.

If the brief is too vague to act on, ask one concise clarifying question. Do not
ask questions that can be answered by local inspection or current-source lookup.

## 2. Blockization

Break the problem into blocks:

- facts: source-backed or directly observed;
- assumptions: plausible but unproven;
- judgments: interpretations or priorities;
- variables: things that can change the outcome;
- incentives: who benefits from each outcome;
- constraints: hard limits;
- decay forces: entropy, friction, maintenance, coordination cost;
- action options: things that can be tried;
- evidence: what would update the belief.

Keep the original user wording visible where it matters. Many bad conclusions
come from silently changing the user's problem.

## 3. Standards

Create `standards.md`, `hard-standards.md`, and `standards-package.md` before
final synthesis. `standards.md` captures the user's bar in prose:

- user standards exactly as stated;
- inferred success criteria;
- evidence gates;
- non-negotiable rejection criteria;
- what counts as `accepted`, `needs-revision`, or `blocked`.

`hard-standards.md` is mandatory for every non-trivial run. Each standard must
have:

- standard id;
- scope;
- hard requirement;
- observable metric;
- pass line;
- hard reject line;
- evidence required;
- owner role;
- dispatch target.

`standards-package.md` is the portable packet a project team can import into
its project instructions, project map, review gates, and next execution packet.

The `Standards Judge` may tighten or clarify standards after the module split,
but must not lower the user's bar for convenience.

## 4. Logic Orchestration / 逻辑编排

Create `logic-orchestration.md` before final synthesis for every non-trivial
run. The Conductor owns this file.

It must contain:

- current phase state;
- dependency graph;
- invariants that must not be violated;
- handoff matrix across roles or project surfaces;
- next-action queue;
- failure and recovery ledger;
- open loops.

When a required artifact, thread route, project dispatch, validator, or judge
gate fails, record:

- failure signal;
- owner;
- recovery action;
- re-check evidence;
- final status.

No final synthesis is `accepted` while a critical open loop lacks a recovery
decision.

## 5. Engineering Governance / 工程治理

Create `engineering-governance.md` before final synthesis for every
non-trivial run that changes files, routes work into a project, or proposes a
durable system update.

It must contain:

- change scope and non-scope;
- owner and reviewer;
- implementation plan;
- validation matrix;
- evidence ledger;
- rollback plan;
- drift and maintenance detector;
- unresolved risks.

Skill self-evolution runs must record the proposal, changed files, validator
result, fresh-session generation check when templates/scripts changed, and
rollback path before completion.

## 6. Project Link And Dispatch

When the thinking run is project-related, locate the project before final
synthesis:

- scan the current workspace;
- scan `/Users/evander/Documents/**/teams/team-*`;
- scan `/Users/evander/.openclaw/**/teams/team-*`;
- inspect directories containing `project-map.md`, `team.md`, `board.md`,
  `status.md`, `ROADMAP.md`, or `LATEST_STATE.md`;
- score candidates by query match, evidence paths, team goal, project map,
  current status, recency, and whether packet/queue execution surfaces exist.

Record the candidate table and selected target in `project-link.md`. If
multiple candidates exist, choose the highest score and record the reason. If
no project is found, do not create one automatically; fill
`project-start-prompt.md` with a copyable launch prompt that points to the run
folder and required standards files.

If a project is selected, fill `project-dispatch.md`. When the project has a
team `message-queue.md`, create one project-side packet with purpose
`plan_feedback` / `standard_update`. Default receiver is `协调师`; if no
coordinator surface exists but planner exists, use `规划师`. The packet must
require the project to update acceptance gates and create the next plan,
execution, or review packet.

## 7. Modular Decomposition

For complex tasks, break the problem into modules:

- module name;
- question it answers;
- dependencies;
- assigned roles;
- acceptance gate;
- recomposition order.

Each module should be small enough for independent red-team, evidence, and
judge review.

## 8. Judgment

Each role must make an independent judgment before reading the other roles'
arguments. The judgment must contain:

- core claim;
- reasoning chain;
- model or principle used;
- confidence level;
- what would change the judgment.

## 9. Falsification

For every serious claim, generate the strongest counter-case:

- What premise could be false?
- What hidden variable could dominate?
- What example would break this?
- What incentive makes this conclusion convenient but wrong?
- What does the entropy lens predict will fail over time?

Do not soften the counter-case to protect the original idea.

## 10. Experiment

Turn uncertainty into the smallest useful experiment:

- hypothesis;
- test action;
- minimum evidence;
- failure signal;
- cost and time box;
- next decision after the result.

Prefer experiments that expose reality quickly over plans that merely feel
complete.

## 11. Judge Verdict

Before final synthesis, `Standards Judge` must write both
`agents/standards-judge.md` and `verdict.md`:

- accepted modules;
- rejected modules;
- missing evidence;
- revision requests;
- logic orchestration audit;
- engineering governance audit;
- final status.

The Conductor cannot call the run complete without `accepted`. `accepted` means
the synthesis, hard standards, evidence gates, rejection lines, next experiment,
logic orchestration, engineering governance, and project dispatch/startup path
all meet the bar.

## 12. Feedback

After an experiment or new evidence, update:

- what changed;
- what did not change;
- what was surprising;
- which model became more or less useful;
- which assumption should be retired.

## 13. Update

Write proposed updates to `evolution-proposal.md`. Updates can target:

- prompt wording;
- role definitions;
- model library;
- quality gates;
- output templates;
- workflow order.

Do not write changes into the skill itself until the user explicitly approves
the proposal. If writeback is approved, track the changed files, validation
evidence, and rollback plan in `engineering-governance.md`. When validator,
generator, quality-gate, role-prompt, or required-artifact contracts changed,
also run `validate_models.py --self-test` and record the negative-fixture
result.

## 14. Next Input Loop

End every run with the next best input for the system:

- a sharper question;
- a concrete experiment result to collect;
- a missing fact to verify;
- or a decision card ready for action.
