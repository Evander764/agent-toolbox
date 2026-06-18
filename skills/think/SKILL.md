---
name: think
description: >
  Multi-agent second-brain thinking room for adversarial reasoning, first
  principles, entropy/system-failure analysis, Munger-style mental models,
  falsification, experiments, and self-evolution proposals. Use when the user
  invokes "$think" or asks for "第二大脑", "多 Agent 探讨", "第一性原理反证",
  "自进化思考", deeply challenging a goal/problem, running a debate between
  2-4 agents, generating decision cards, or improving this thinking system
  without automatically writing unreviewed changes.
---

# Think

## Overview

Use this skill to turn a vague goal, decision, or question into a disciplined
multi-agent thinking loop. The loop must challenge assumptions, search for
missing facts when needed, produce falsifiable experiments, and leave a
reviewable update proposal instead of silently rewriting itself.

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

4. Use real sub-agents by default. If multi-agent tools are not already
   available, search for them. Spawn 2-4 independent agents, default 4, without
   hardcoding a model override so agents inherit the current Codex/GPT model.
   If sub-agent tools are unavailable, simulate the roles in one window and
   explicitly label the run as simulated.

5. Run two rounds:
   - Round 1: independent role judgments, with no consensus-seeking.
   - Round 2: cross-examination, where each role attacks another role's
     strongest assumption or weakest evidence.

6. Query current information when the answer depends on recent, unstable, or
   external facts such as model capabilities, markets, prices, law, policy,
   public company facts, product specs, current events, or live technical
   behavior. Separate source-backed facts from inference and assumptions.

7. Synthesize the result into:
   - disruptive conclusion;
   - conservative conclusion;
   - strongest counterargument;
   - entropy/system decay cost;
   - Munger model hits;
   - smallest next experiment;
   - observation metrics;
   - decision card;
   - update proposal.

8. Write or update the run artifacts in the session folder. Do not modify this
   skill or its model library automatically. Put proposed improvements in
   `evolution-proposal.md` for user review.

## Operating Rules

- Do not let agents merely agree. At least one role must argue that the current
  framing may be wrong.
- Do not use "first principles" as a slogan. Reduce the problem to physical,
  economic, psychological, or system constraints that would remain true even if
  labels changed.
- Always include entropy: what decays, what gets harder, what needs maintenance,
  and what happens if nobody acts.
- Treat mental models as lenses, not decorations. Choose only models that
  change the conclusion or the next experiment.
- Never present unverified current facts as confirmed. Cite sources when
  browsing or external lookup is used.
- Keep self-evolution reviewable: proposal first, writeback only after explicit
  user approval.

## Updating This Skill

When the user approves an update proposal:

1. Patch the smallest relevant file under this skill.
2. Preserve the "proposal before writeback" rule unless the user explicitly
   changes it.
3. Run the skill validator after edits.
4. Record the changed file paths in the final response.
