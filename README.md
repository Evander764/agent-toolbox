# Agent Toolbox

Personal public toolbox for useful AI-agent skills, workflows, scripts, and
small reusable code.

This repository is meant to be a stable place to collect things that are useful
outside one local project.

## Contents

### Skills

- `skills/team`: a low-typing multi-agent coordination skill. It lets multiple
  AI chat windows work as a small team with Chinese role names:
  `规划师`, `协调师`, `执行人`, and `审核官`.

### Tools

- `tools/`: reusable scripts or small utilities.

### Snippets

- `snippets/`: small reusable prompts, templates, and code fragments.

## Current Skill: team

Use:

```text
/team 项目：<目标>
```

Then open a new chat and send:

```text
/team
```

Without an explicit role, `/team` defaults to `规划师`. The planner creates the
first project plan and gives copyable prompts for the remaining roles:

```text
/team 协调师
/team 执行人
/team 审核官
```

The workflow keeps durable state in a shared team folder and uses packet-based
handoffs so agents do not depend on hidden chat history.

## Repository Policy

- Keep assets reusable.
- Do not commit secrets, local runtime state, generated team folders, or private
  project data.
- Prefer short names and copyable commands.
- Add a short README for each new skill or tool.

