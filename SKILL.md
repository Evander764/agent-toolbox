---
name: xhs-auto-deploy
description: Use when the user asks to set up, verify, repair, or run Xiaohongshu/XHS automated publishing, video downloading, account exports, Agent-Reach XHS access, xhs-cli posting, or Viral Brief Plus Xiaohongshu batch patrol on this Mac
---

# XHS Auto Deploy

## Overview

This Mac already has a Xiaohongshu automation stack. Route the request before acting: `xhs-cli` is for reading/searching/interacting/posting, `yt-dlp` downloads video URLs, Agent-Reach is for agent install and health checks, Viral Brief Plus is for batch account opening and patrol, and `xhs-scraping` is for analysis/crawling.

## Local Sources

| Need | Source |
|---|---|
| Agent install and XHS setup | `/Users/evander/Documents/Software/必备工具/Agent-Reach` |
| XHS setup guide | `agent_reach/guides/setup-xiaohongshu.md` |
| XHS channel check | `agent_reach/channels/xiaohongshu.py` |
| Installed `xhs` source | `/Users/evander/.local/share/uv/tools/xiaohongshu-cli/.../xhs_cli` |
| Blogger video downloader | `scripts/download-blogger-videos.py` |
| Batch account opening/patrol | `/Users/evander/Documents/Software/Viral Brief Plus` |
| Crawling, diagnosis, video pipeline | `/Users/evander/Documents/Great things of AI/25IP开源干货-精华沉淀/skills/xhs-scraping` |

## Capability Matrix

| Capability | Use |
|---|---|
| Install/repair XHS agent access | Agent-Reach + `xhs-cli` |
| Check login and local readiness | `scripts/check-xhs-auto-deploy.sh` |
| Search/read notes and comments | `xhs search`, `xhs read`, `xhs comments` |
| Export one blogger's posts | `xhs user-posts USER_ID --json` |
| Download one blogger's video notes | `scripts/download-blogger-videos.py USER_ID` |
| Like/favorite/comment/reply/follow | `xhs like`, `xhs favorite`, `xhs comment`, `xhs reply`, `xhs follow` |
| Publish image notes | `xhs post` |
| Batch-open account pool and patrol | Viral Brief Plus API |
| Competitor/account/title analysis | `xhs-scraping` skill |
| Generate vertical XHS video assets | `xhs-scraping` video pipeline |

## First Checks

Run the bundled check first:

```bash
~/.codex/skills/xhs-auto-deploy/scripts/check-xhs-auto-deploy.sh
```

Narrow checks are safer than full `agent-reach doctor`; full doctor can hang while probing unrelated channels. The check also verifies `yt-dlp` for video downloading.

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

## Blogger Video Download

Use this when the user asks "下载某个博主所有视频". It paginates `xhs user-posts`, writes `notes.jsonl` and `videos.jsonl`, then sends video note URLs to `yt-dlp` with a `download-archive.txt` for resume/skip behavior.

```bash
python3 ~/.codex/skills/xhs-auto-deploy/scripts/download-blogger-videos.py \
  "https://www.xiaohongshu.com/user/profile/USER_ID" \
  --out ~/Downloads/xhs-USER_ID \
  --max-pages 50 \
  --delay 2 \
  --cookies-from-browser chrome
```

Safe preview:

```bash
python3 ~/.codex/skills/xhs-auto-deploy/scripts/download-blogger-videos.py USER_ID --dry-run
```

If `xhs status` is expired, stop and restore login first. If the account has hundreds of notes, keep `--delay` and use a reasonable `--max-pages`; do not aggressively scrape through 461, 300012, 403, or repeated empty results.

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

## Export And Interaction Commands

```bash
xhs search "关键词" --json
xhs read NOTE_ID_OR_URL --json
xhs comments NOTE_ID_OR_URL --json
xhs search-user "昵称" --json
xhs user USER_ID --json
xhs user-posts USER_ID --json
xhs like NOTE_ID_OR_URL
xhs favorite NOTE_ID_OR_URL
xhs comment NOTE_ID_OR_URL --content "评论内容"
xhs follow USER_ID
```

## Viral Brief Plus

For account-pool opening, use `POST /api/accounts/open-platform` with:

```json
{ "platform": "xiaohongshu" }
```

It only accepts valid homepages shaped like `https://www.xiaohongshu.com/user/profile/<id>`, dedupes them, and opens them together in Chrome tabs. For patrol/report work, keep Xiaohongshu and Douyin stages separate; Xiaohongshu runs before Douyin.

## Common Mistakes

- Do not comma-join images; repeat `--images`.
- Do not claim full video download is verified unless a real logged-in run has completed.
- Do not treat full `agent-reach doctor` as the only health check.
- Do not publish publicly unless the user clearly asked for it.
- Do not rely on QR login as the first route; Cookie-Editor or browser extraction is more reliable.
- Do not use crawling/signature scripts for posting. Use `xhs post` for posting.
- Stop aggressive scraping on 461, 300012, 403, or empty-result rate-limit patterns.
