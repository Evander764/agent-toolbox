---
name: xhs-auto-deploy
description: Use when the user asks to set up, verify, repair, or run Xiaohongshu/XHS automated publishing, Agent-Reach XHS access, xhs-cli posting, or Viral Brief Plus Xiaohongshu batch patrol on this Mac
---

# XHS Auto Deploy

## Overview

This Mac already has a Xiaohongshu automation stack. Route the request before acting: `xhs-cli` is for reading/searching/interacting/posting, Agent-Reach is for agent install and health checks, Viral Brief Plus is for batch account opening and patrol, and `xhs-scraping` is for analysis/crawling.

## Local Sources

| Need | Source |
|---|---|
| Agent install and XHS setup | `/Users/evander/Documents/Software/必备工具/Agent-Reach` |
| XHS setup guide | `agent_reach/guides/setup-xiaohongshu.md` |
| XHS channel check | `agent_reach/channels/xiaohongshu.py` |
| Installed `xhs` source | `/Users/evander/.local/share/uv/tools/xiaohongshu-cli/.../xhs_cli` |
| Batch account opening/patrol | `/Users/evander/Documents/Software/Viral Brief Plus` |
| Crawling, diagnosis, video pipeline | `/Users/evander/Documents/Great things of AI/25IP开源干货-精华沉淀/skills/xhs-scraping` |

## Intent Routing

| User asks for | Use |
|---|---|
| "帮我装/部署小红书能力", "让 agent 能读搜发小红书" | Agent-Reach + `xhs-cli` |
| "发一篇/自动发布小红书笔记" | `xhs post` |
| "批量打开小红书主页", "巡检账号池", "生成日报" | Viral Brief Plus API |
| "抓竞品/分析账号/提取笔记/生成小红书视频" | `xhs-scraping` skill |

## First Checks

Run the bundled check first:

```bash
~/.codex/skills/xhs-auto-deploy/scripts/check-xhs-auto-deploy.sh
```

Narrow checks are safer than full `agent-reach doctor`; full doctor can hang while probing unrelated channels.

If missing:

```bash
uv tool install xiaohongshu-cli || pipx install xiaohongshu-cli
```

## Login And Cookies

1. Prefer a dedicated/secondary Xiaohongshu account.
2. Try `xhs --cookie-source chrome login`, then verify with `xhs status`.
3. For Agent-Reach cookies, prefer `agent-reach configure --from-browser chrome`.
4. If browser extraction fails, use Cookie-Editor export. Do not echo full cookies in chat or logs. `agent-reach configure xhs-cookies "..."` stores a 0600 local file, but command-line arguments may still be briefly visible to the OS.

Important: Agent-Reach `xhs_cookie` and `xhs-cli` login state are not the same thing. Verify both when both surfaces matter.

## Publishing

Public publishing needs explicit user intent. For smoke tests, only use `--private` after the user accepts that it still creates a private note.

Use absolute image paths. Multiple images require repeated `--images` flags:

```bash
xhs post \
  --title "标题" \
  --body "$(cat /tmp/xhs-body.txt)" \
  --images /abs/path/cover.png \
  --images /abs/path/detail.png \
  --topic "AI工具" \
  --private \
  --json
```

Verify after posting:

```bash
xhs my-notes --page 0 --json
```

## Viral Brief Plus

For account-pool opening, use `POST /api/accounts/open-platform` with:

```json
{ "platform": "xiaohongshu" }
```

It only accepts valid homepages shaped like `https://www.xiaohongshu.com/user/profile/<id>`, dedupes them, and opens them together in Chrome tabs. For patrol/report work, keep Xiaohongshu and Douyin stages separate; Xiaohongshu runs before Douyin.

## Common Mistakes

- Do not comma-join images; repeat `--images`.
- Do not treat full `agent-reach doctor` as the only health check.
- Do not publish publicly unless the user clearly asked for it.
- Do not rely on QR login as the first route; Cookie-Editor or browser extraction is more reliable.
- Do not use crawling/signature scripts for posting. Use `xhs post` for posting.
- Stop aggressive scraping on 461, 300012, 403, or empty-result rate-limit patterns.
