---
name: think
description: >
  Short "$think" second-brain skill for automatic Codex multi-window thinking
  rooms, adversarial multi-agent reasoning, first principles, entropy/system
  failure analysis, Munger-style mental models, falsification, strict standards
  judging, hard acceptance-standard extraction, project linking, project packet
  dispatch, modular decomposition, logic orchestration / 逻辑编排,
  engineering governance / 工程治理, experiments, and self-evolution proposals.
  Use when the user invokes "$think" or asks for "第二大脑", "多 Agent 探讨",
  "第一性原理反证", "自进化思考", deeply challenging a goal/problem, creating
  2-4 Codex agent windows, generating decision cards, extracting hard standards,
  linking standards to a project, routing thinking results into a team workflow,
  adding explicit failure recovery, engineering governance, or improving this
  thinking system without automatically writing unreviewed changes.
---

# Think

## Overview

Use this skill to turn a vague goal, decision, or question into an automatic
Codex multi-window thinking room. The main thread is the Conductor: it creates
role windows, routes packets, reads results, enforces a strict judge verdict,
extracts hard standards, owns the logic orchestration / 逻辑编排 state machine,
records engineering governance / 工程治理 evidence for durable changes, links
the run to the relevant project when applicable, and synthesizes only after the
standards gate accepts the work.

Default workspace:

```text
/Users/evander/Documents/Agent thinking/second-brain
```

## Required References

Read these files before a full thinking-room run:

- `references/protocol.md`: the input -> blockization -> judgment ->
  falsification -> experiment -> feedback -> update loop.
- `references/agent-roles.md`: default roles, sub-agent prompts, and fallback
  behavior.
- `references/thread-orchestration.md`: automatic Codex thread creation,
  routing, result collection, and fallback behavior.
- `references/logic-orchestration.md`: state machine, dependency graph,
  invariants, handoffs, next-action queue, and recovery ledger.
- `references/engineering-governance.md`: change scope, ownership, validation,
  evidence, rollback, drift, and maintenance rules.
- `references/quality-gates.md`: hard gates that prevent shallow agreement.
- `references/outputs.md`: run folder and output templates.
- `references/mental-models.md`: router for selecting high-impact models from
  the full library.
- `references/mental-models-100.md`: the full original Munger-style operating
  library of 100 compact model cards.

Read `references/mental-models.md` for any non-trivial judgment, strategy,
business, product, learning, investment, or life decision. It must treat all
100 models in `references/mental-models-100.md` as the candidate pool while
surfacing only the models that change the judgment, standard, or experiment.

## Workflow

1. Create or identify a run folder with:

   ```bash
   python3 /Users/evander/.codex/skills/think/scripts/new_session.py --topic "<short topic>"
   ```

2. Compress the user's input into:
   - objective;
   - success criteria;
   - constraints;
   - key assumptions;
   - unknowns;
   - decision deadline or action horizon.

3. Blockize the problem into facts, judgments, variables, constraints, risks,
   incentives, available actions, and possible experiments.

4. Create `standards.md`, `hard-standards.md`, `standards-package.md`, and
   `mental-models-selected.md` before final synthesis. Also create
   `logic-orchestration.md` and `engineering-governance.md` for every
   non-trivial run before final synthesis. For every non-trivial `$think` run,
   `hard-standards.md` must include standards with:
   - standard id;
   - scope;
   - hard requirement;
   - observable metric;
   - pass line;
   - hard reject line;
   - evidence required;
   - owner role;
   - dispatch target.

5. Maintain logic orchestration / 逻辑编排 throughout the run. Record phase
   state, dependency graph, invariants, handoff matrix, next-action queue,
   failure and recovery ledger, and open loops in `logic-orchestration.md`.
   If a required artifact, thread, project dispatch, validator, or judge gate
   fails, record detection, owner, recovery action, and re-check evidence before
   final synthesis.

6. Maintain engineering governance / 工程治理 whenever the run changes files,
   routes standards into a project, or proposes durable updates. Record change
   scope, ownership, implementation plan, validation matrix, evidence ledger,
   rollback plan, drift/maintenance checks, and unresolved risks in
   `engineering-governance.md`.

7. Link the thinking run to a project when the question is project-related.
   Use `scripts/project_locator.py` or equivalent inspection to scan current
   workspace projects, `/Users/evander/Documents/**/teams/team-*`,
   `/Users/evander/.openclaw/**/teams/team-*`, and project directories with
   `project-map.md`, `team.md`, `board.md`, `status.md`, `ROADMAP.md`, or
   `LATEST_STATE.md`. Record ranked candidates in `project-link.md`. If
   multiple candidates exist, choose the highest score and record why.

8. If a selected project exists, prepare `project-dispatch.md` and route the
   standards package through the project team's packet protocol. Default the
   packet purpose to `plan_feedback` / `standard_update`, and default the
   receiver to `协调师`; if no coordinator surface exists but a planner exists,
   use `规划师`. The project-side packet must require updating project
   instructions, project map acceptance indicators, and the next plan,
   execution, or review packet. If no project exists, do not create one
   automatically; fill `project-start-prompt.md` with a copyable startup prompt.

9. Use automatic Codex thread windows by default. If thread tools are not
   already available, search for `create_thread`, `read_thread`,
   `send_message_to_thread`, `set_thread_title`, and `set_thread_archived`.
   Create one local project thread per active role, normally four:
   `Standards Judge`, `Systems Decomposer`, `Red Team Devil's Advocate`, and
   `Evidence & Mental Models Strategist`. Do not set a model override unless
   the user explicitly asks; new windows should inherit the current Codex model.

10. Record all thread IDs in `thread-routing.md`. Send each window a
   self-contained role prompt containing the run folder, its exact output file,
   the module or packet it owns, and the rule that it must not edit other role
   files. `Standards Judge` must be authorized to write both
   `agents/standards-judge.md` and `verdict.md`. Use `set_thread_title` so the
   user can recognize each window.

11. Run modular discussion:
   - `Systems Decomposer` splits the problem into modules and recomposition
     order.
   - Each module gets independent analysis, red-team critique, evidence/model
     review, and standards judgment.
   - `Evidence & Mental Models Strategist` scans the 100-model library as the
     candidate pool, selects 3-9 models that materially change the decision,
     and writes `mental-models-selected.md`.
   - If `Standards Judge` returns `needs-revision`, create a revision packet
     and route it before final synthesis.

12. Query current information when the answer depends on recent, unstable, or
   external facts such as model capabilities, markets, prices, law, policy,
   public company facts, product specs, current events, or live technical
   behavior. Separate source-backed facts from inference and assumptions.

13. Synthesize the result only after the judge accepts, into:
   - disruptive conclusion;
   - conservative conclusion;
   - strongest counterargument;
   - entropy/system decay cost;
   - Munger model hits;
   - `mental-models-selected.md` summary;
   - smallest next experiment;
   - observation metrics;
   - decision card;
   - judge verdict;
   - hard standards package;
   - logic orchestration status;
   - engineering governance evidence;
   - project link and dispatch status;
   - update proposal.

14. Write or update the run artifacts in the session folder. Do not modify this
   skill or its model library automatically. Put proposed improvements in
   `evolution-proposal.md` for user review.

## Operating Rules

- Do not let agents merely agree. At least one role must argue that the current
  framing may be wrong.
- Do not claim real multi-window collaboration unless Codex thread IDs are
  recorded in `thread-routing.md` and results are read back from those threads.
- Do not use "first principles" as a slogan. Reduce the problem to physical,
  economic, psychological, or system constraints that would remain true even if
  labels changed.
- Keep `Standards Judge` mandatory. It has veto power; any non-compliant module
  or final synthesis is `needs-revision`, not complete.
- For non-trivial runs, do not accept advice-only output. The run must produce
  hard standards that another agent can judge without hidden context.
- For non-trivial runs, do not accept un-orchestrated output. The run must
  expose phase state, dependencies, handoffs, recovery actions, and open loops
  in `logic-orchestration.md`.
- For non-trivial runs that change files, create project packets, or evolve a
  workflow, do not accept ungoverned output. The run must expose scope,
  validation, evidence, rollback, and drift/maintenance checks in
  `engineering-governance.md`.
- `accepted` means the answer, hard standards, evidence gates, rejection lines,
  logic orchestration state, engineering governance evidence, next experiment,
  and project dispatch/startup path all satisfy the user's bar. It does not
  merely mean the synthesis is plausible.
- When a run is tied to an existing project, route the standards package into
  that project. A project receiving the package must update its acceptance
  gates and start the next packet; saving the file is not enough.
- If no existing project can be identified, output a copyable startup prompt in
  `project-start-prompt.md`; do not create a new project automatically.
- Let roles adapt to the task, but never remove standards judging or red-team
  pressure. For complex domain tasks, one role slot may become a domain
  specialist, premortem officer, or synthesis agent.
- Always include entropy: what decays, what gets harder, what needs maintenance,
  and what happens if nobody acts.
- Treat mental models as lenses, not decorations. Choose only models that
  change the conclusion, standard, or next experiment. For non-trivial runs,
  scan the full 100-card library as the candidate pool, surface only 3-9
  high-impact models, and record tempting rejected models in
  `mental-models-selected.md`.
- Never present unverified current facts as confirmed. Cite sources when
  browsing or external lookup is used.
- Keep self-evolution reviewable: proposal first, writeback only after explicit
  user approval.
- When validation, thread routing, project dispatch, or judge review fails,
  record the failure in `logic-orchestration.md`, record the failed gate in
  `engineering-governance.md`, apply the smallest recovery action, and rerun the
  relevant check before claiming acceptance.
- If thread tools are unavailable, mark `mode: simulated` in `session.md` and
  explain the fallback in the final answer.

## Updating This Skill

When the user approves an update proposal:

1. Patch the smallest relevant file under this skill.
2. Preserve the "proposal before writeback" rule unless the user explicitly
   changes it.
3. Run the skill validator after edits.
4. For validator, generator, quality-gate, or role-prompt changes, also run the
   validator with `--self-test`.
5. Record the changed file paths in the final response.

Default validator:

```bash
python3 /Users/evander/.codex/skills/think/scripts/validate_models.py
```

Structural self-test:

```bash
python3 /Users/evander/.codex/skills/think/scripts/validate_models.py --self-test
```
