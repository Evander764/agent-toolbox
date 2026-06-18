---
name: think
description: >
  Short "$think" second-brain skill for automatic Codex multi-window thinking
  rooms, adversarial multi-agent reasoning, first principles, entropy/system
  failure analysis, Munger-style mental models, falsification, strict standards
  judging, modular decomposition, experiments, and self-evolution proposals. Use
  when the user invokes "$think" or asks for "第二大脑", "多 Agent 探讨",
  "第一性原理反证", "自进化思考", deeply challenging a goal/problem, creating
  2-4 Codex agent windows, generating decision cards, or improving this thinking
  system without automatically writing unreviewed changes.
---

# Think

## Overview

Use this skill to turn a vague goal, decision, or question into an automatic
Codex multi-window thinking room. The main thread is the Conductor: it creates
role windows, routes packets, reads results, enforces a strict judge verdict,
and synthesizes only after the standards gate accepts the work.

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
- `references/quality-gates.md`: hard gates that prevent shallow agreement.
- `references/outputs.md`: run folder and output templates.

Read `references/mental-models.md` for any non-trivial judgment, strategy,
business, product, learning, investment, or life decision.

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

4. Use automatic Codex thread windows by default. If thread tools are not
   already available, search for `create_thread`, `read_thread`,
   `send_message_to_thread`, `set_thread_title`, and `set_thread_archived`.
   Create one local project thread per active role, normally four:
   `Standards Judge`, `Systems Decomposer`, `Red Team Devil's Advocate`, and
   `Evidence & Mental Models Strategist`. Do not set a model override unless
   the user explicitly asks; new windows should inherit the current Codex model.

5. Record all thread IDs in `thread-routing.md`. Send each window a
   self-contained role prompt containing the run folder, its exact output file,
   the module or packet it owns, and the rule that it must not edit other role
   files. Use `set_thread_title` so the user can recognize each window.

6. Run modular discussion:
   - `Systems Decomposer` splits the problem into modules and recomposition
     order.
   - Each module gets independent analysis, red-team critique, evidence/model
     review, and standards judgment.
   - If `Standards Judge` returns `needs-revision`, create a revision packet
     and route it before final synthesis.

7. Query current information when the answer depends on recent, unstable, or
   external facts such as model capabilities, markets, prices, law, policy,
   public company facts, product specs, current events, or live technical
   behavior. Separate source-backed facts from inference and assumptions.

8. Synthesize the result only after the judge accepts, into:
   - disruptive conclusion;
   - conservative conclusion;
   - strongest counterargument;
   - entropy/system decay cost;
   - Munger model hits;
   - smallest next experiment;
   - observation metrics;
   - decision card;
   - judge verdict;
   - update proposal.

9. Write or update the run artifacts in the session folder. Do not modify this
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
- Let roles adapt to the task, but never remove standards judging or red-team
  pressure. For complex domain tasks, one role slot may become a domain
  specialist, premortem officer, or synthesis agent.
- Always include entropy: what decays, what gets harder, what needs maintenance,
  and what happens if nobody acts.
- Treat mental models as lenses, not decorations. Choose only models that
  change the conclusion or the next experiment.
- Never present unverified current facts as confirmed. Cite sources when
  browsing or external lookup is used.
- Keep self-evolution reviewable: proposal first, writeback only after explicit
  user approval.
- If thread tools are unavailable, mark `mode: simulated` in `session.md` and
  explain the fallback in the final answer.

## Updating This Skill

When the user approves an update proposal:

1. Patch the smallest relevant file under this skill.
2. Preserve the "proposal before writeback" rule unless the user explicitly
   changes it.
3. Run the skill validator after edits.
4. Record the changed file paths in the final response.
