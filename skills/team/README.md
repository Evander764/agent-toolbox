# Team Skill

Minimal self-organizing AI team workflow for Codex-style agents.

## What It Does

- Creates a durable shared team folder for multi-agent work.
- Routes work through planner, coordinator, executor, and reviewer roles.
- Uses packets, queues, thread routing, handoff logs, and inbox files so agents do not depend on hidden chat history.
- Keeps one team-root `project-map.md` that tracks the end-first project map, current stage, progress table, task map, defects, highlights, future metrics, blockers, and next coordination actions.

## Install

Copy or symlink this folder into a Codex skills directory:

```bash
~/.codex/skills/team
```

Then invoke it with:

```text
/team 项目：<目标>
```

or join a role:

```text
/team 协调师
团队：<team_id>
```

## Core Files

- `SKILL.md`: skill instructions.
- `README.md`: repository overview.

## Notes

The coordinator is responsible for maintaining `project-map.md` and directly showing the current progress tracking table plus project map summary in chat after routing, review closeout, blocker handling, or status replies.
