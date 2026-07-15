# xhs-auto-deploy

Personal Codex skill for routing Xiaohongshu/XHS automation work on this Mac.

It documents the local split between:

- `xhs-cli` for Xiaohongshu reading, search, interaction, and image-note posting
- `yt-dlp` for downloading video note URLs
- Agent-Reach for agent setup and health checks
- Viral Brief Plus for account-pool batch opening and patrol/report workflows
- `xhs-scraping` for crawling, diagnosis, and video-pipeline work

## Files

- `SKILL.md` - skill entrypoint
- `scripts/check-xhs-auto-deploy.sh` - narrow local health check that avoids printing cookie values
- `scripts/download-blogger-videos.py` - paginates a blogger's notes, filters video notes, writes manifests, and downloads via `yt-dlp`

## Quick Check

```bash
scripts/check-xhs-auto-deploy.sh
```

## Download A Blogger's Videos

```bash
python3 scripts/download-blogger-videos.py "https://www.xiaohongshu.com/user/profile/USER_ID" \
  --out ~/Downloads/xhs-USER_ID \
  --max-pages 50 \
  --delay 2 \
  --cookies-from-browser chrome
```

Preview only:

```bash
python3 scripts/download-blogger-videos.py USER_ID --dry-run
```

## Safety Notes

This repository intentionally contains no cookies, API keys, or local account secrets. Publishing a note to Xiaohongshu should only happen after explicit user intent, and smoke tests should use `xhs post --private`.
