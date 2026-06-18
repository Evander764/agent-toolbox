# Quality Gates

Use these gates before presenting a final thinking-room result.

## Hard Gates

A run is not acceptable unless it contains:

- a compressed problem brief;
- a `standards.md` file with user-aligned pass/fail gates;
- `thread-routing.md` showing real thread IDs, or `mode: simulated` with a
  clear fallback explanation;
- blockization into facts, assumptions, judgments, variables, risks, and action
  options;
- module decomposition for complex tasks;
- first-principles reduction;
- entropy/system-decay analysis;
- at least three relevant mental models, unless the task is trivial;
- a strongest counterargument;
- explicit falsification criteria;
- at least one information gap;
- a smallest useful experiment;
- feedback/update path;
- a `verdict.md` result from `Standards Judge`;
- an `evolution-proposal.md` entry, even if the proposal is "no update".

## Standards Judge Gate

`Standards Judge` is mandatory. Final status can be:

- `accepted`: every hard gate is met;
- `needs-revision`: at least one required gate fails;
- `blocked`: required evidence, permission, or context is missing.

The Conductor must not present `needs-revision` or `blocked` work as complete.
If the judge rejects a module, create a revision packet and route it before
final synthesis.

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

## Thread Gates

Real multi-window mode requires:

- one recorded thread id per active role;
- one assigned output file per role;
- role prompts that forbid editing other role files;
- at least one `read_thread` check or explicit thread-result collection before
  final synthesis.

If these are missing, mark the run as simulated or incomplete.

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

## Red Flags

Reject or revise outputs that:

- use "first principles" without reducing the problem;
- mention mental models as a list without implications;
- ignore entropy, maintenance, or coordination cost;
- provide advice without falsification;
- ask for broad research when a cheap test would work;
- collapse all disagreement into a bland middle ground;
- write permanent Skill updates without user approval.
