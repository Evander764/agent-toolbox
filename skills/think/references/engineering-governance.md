# Engineering Governance / 工程治理

Use this reference when a `$think` run changes files, routes work into a
project, or proposes a durable system update. `工程治理` means changes are
scoped, validated, reversible, and owned after the first successful run.

## Required Artifact

Every non-trivial run must create `engineering-governance.md` before final
synthesis. Skill self-evolution runs must fill it before claiming completion.

Required sections:

- change scope;
- ownership;
- implementation plan;
- validation matrix;
- evidence ledger;
- rollback plan;
- drift and maintenance;
- unresolved risks.

## Change Scope

Record:

- files or project surfaces that may change;
- files or surfaces that must not change;
- reason each changed file is necessary;
- whether the change is reversible;
- whether secrets, credentials, user data, or external accounts are involved.

If scope expands during implementation, update the artifact before editing the
new area.

## Ownership

For each change, name:

- owner role;
- reviewer or judge;
- acceptance evidence;
- recovery owner if validation fails.

Ownership without authority or evidence is not enough.

## Validation Matrix

Use a table:

| gate | command_or_check | pass_line | fail_line | evidence_path | owner |
| --- | --- | --- | --- | --- | --- |

For skill-package changes, the default gates are:

- run the skill validator;
- run `validate_models.py --self-test` when validator, generator, quality-gate,
  role-prompt, or required-artifact contracts changed;
- generate a fresh session folder;
- inspect that required artifacts exist;
- check that quality gates and role prompts mention new responsibilities;
- record changed files and rollback path.

## Evidence Ledger

Record evidence as concrete paths, command summaries, or thread ids. Do not
write secrets or hidden chain-of-thought.

Evidence should show:

- what was checked;
- when it was checked;
- result;
- remaining caveats.

## Rollback Plan

Every durable change needs a rollback note:

- changed files;
- how to undo each file if needed;
- what validation should be rerun after rollback;
- whether any generated run folders are evidence-only and can be left in place.

Do not use destructive commands as the default rollback plan. Prefer targeted
patches or restoring from version control when available and explicitly safe.

## Drift And Maintenance

Record what may decay:

- reference files drifting away from `SKILL.md`;
- templates no longer matching quality gates;
- validator checks becoming stale;
- project packet conventions changing;
- thread tool behavior changing.

Each drift item needs a detector and refresh trigger.

## Failure Handling

When validation or dispatch fails:

1. Record the failure in `logic-orchestration.md`.
2. Record the failed gate in `engineering-governance.md`.
3. Apply the smallest recovery action.
4. Rerun the relevant check.
5. If the check still fails, mark the run `needs-revision` or `blocked`; do not
   present the work as accepted.

## Acceptance Rule

A self-evolution run is not complete until:

- `evolution-proposal.md` exists;
- changed files are listed;
- validator result is recorded;
- validator self-test result is recorded when structural contracts changed;
- fresh-session generation is checked when templates/scripts changed;
- rollback path is recorded;
- Standards Judge verdict is `accepted`, or any missing role verdict is
  explicitly handled with local validation evidence.
