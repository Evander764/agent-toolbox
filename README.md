# xhs-auto-deploy

Personal Codex skill for routing Xiaohongshu/XHS automation work on this Mac.

It documents the local split between:

- `xhs-cli` for Xiaohongshu reading, search, interaction, and image-note posting
- Agent-Reach for agent setup and health checks
- Viral Brief Plus for account-pool batch opening and patrol/report workflows
- `xhs-scraping` for crawling, diagnosis, and video-pipeline work

## Files

- `SKILL.md` - skill entrypoint
- `scripts/check-xhs-auto-deploy.sh` - narrow local health check that avoids printing cookie values

## Quick Check

```bash
scripts/check-xhs-auto-deploy.sh
```

## Safety Notes

This repository intentionally contains no cookies, API keys, or local account secrets. Publishing a note to Xiaohongshu should only happen after explicit user intent, and smoke tests should use `xhs post --private`.
