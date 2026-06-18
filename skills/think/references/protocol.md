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

Create `standards.md` before role work begins:

- user standards exactly as stated;
- inferred success criteria;
- evidence gates;
- non-negotiable rejection criteria;
- what counts as `accepted`, `needs-revision`, or `blocked`.

The `Standards Judge` may tighten or clarify standards after the module split,
but must not lower the user's bar for convenience.

## 4. Modular Decomposition

For complex tasks, break the problem into modules:

- module name;
- question it answers;
- dependencies;
- assigned roles;
- acceptance gate;
- recomposition order.

Each module should be small enough for independent red-team, evidence, and
judge review.

## 5. Judgment

Each role must make an independent judgment before reading the other roles'
arguments. The judgment must contain:

- core claim;
- reasoning chain;
- model or principle used;
- confidence level;
- what would change the judgment.

## 6. Falsification

For every serious claim, generate the strongest counter-case:

- What premise could be false?
- What hidden variable could dominate?
- What example would break this?
- What incentive makes this conclusion convenient but wrong?
- What does the entropy lens predict will fail over time?

Do not soften the counter-case to protect the original idea.

## 7. Experiment

Turn uncertainty into the smallest useful experiment:

- hypothesis;
- test action;
- minimum evidence;
- failure signal;
- cost and time box;
- next decision after the result.

Prefer experiments that expose reality quickly over plans that merely feel
complete.

## 8. Judge Verdict

Before final synthesis, `Standards Judge` must write `verdict.md`:

- accepted modules;
- rejected modules;
- missing evidence;
- revision requests;
- final status.

The Conductor cannot call the run complete without `accepted`.

## 9. Feedback

After an experiment or new evidence, update:

- what changed;
- what did not change;
- what was surprising;
- which model became more or less useful;
- which assumption should be retired.

## 10. Update

Write proposed updates to `evolution-proposal.md`. Updates can target:

- prompt wording;
- role definitions;
- model library;
- quality gates;
- output templates;
- workflow order.

Do not write changes into the skill itself until the user explicitly approves
the proposal.

## 11. Next Input Loop

End every run with the next best input for the system:

- a sharper question;
- a concrete experiment result to collect;
- a missing fact to verify;
- or a decision card ready for action.
