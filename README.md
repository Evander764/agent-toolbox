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
- `skills/think`: a short `$think` second-brain skill that can launch automatic
  Codex agent windows for adversarial reasoning, modular decomposition, strict
  standards judging, first principles, entropy analysis, Munger-style mental
  models, falsification, experiments, and reviewable self-evolution proposals.
- `skills/huawei-watch-app-builder`: complete development, UI/UX architecture,
  dual-layer signing, and automated wireless sideloading workflow for Huawei
  Lite Wearables (HUAWEI WATCH FIT 5, FIT 3/4, WATCH GT series).

### Tools

- `tools/`: reusable scripts or small utilities.

### Snippets

- `snippets/`: small reusable prompts, templates, and code fragments.

## Skills Overview

### `team`
Use:
```text
/team 项目：<目标>
```

### `think`
Use:
```text
$think <goal or question>
```

### `huawei-watch-app-builder`
Use:
Follow `skills/huawei-watch-app-builder/SKILL.md` to build, dual-layer sign, and sideload Lite Wearable apps on Huawei Watches.

## Repository Policy

- Keep assets reusable.
- Do not commit secrets, local runtime state, generated team folders, or private
  project data.
- Prefer short names and copyable commands.
- Add a short README for each new skill or tool.
