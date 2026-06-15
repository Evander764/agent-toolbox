#!/usr/bin/env python3
"""Download video notes from a Xiaohongshu user with xhs-cli + yt-dlp.

The script keeps a JSONL manifest so interrupted runs can be audited and
resumed. It never prints cookies.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import time
from pathlib import Path
from typing import Any


def run_json(cmd: list[str]) -> dict[str, Any]:
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    if result.returncode != 0:
        msg = (result.stderr or result.stdout or "").strip()
        raise RuntimeError(msg or f"command failed: {' '.join(cmd)}")
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"command did not return JSON: {' '.join(cmd)}") from exc


def unwrap(payload: dict[str, Any]) -> dict[str, Any]:
    if isinstance(payload, dict) and payload.get("ok") is True and isinstance(payload.get("data"), dict):
        return payload["data"]
    return payload


def page_from_payload(payload: dict[str, Any]) -> tuple[list[dict[str, Any]], str, bool]:
    data = unwrap(payload)
    notes = data.get("notes") or data.get("items") or []
    if not isinstance(notes, list):
        notes = []
    cursor = str(data.get("cursor") or "")
    has_more = bool(data.get("has_more"))
    return [n for n in notes if isinstance(n, dict)], cursor, has_more


def nested(note: dict[str, Any]) -> dict[str, Any]:
    inner = note.get("note_card") or note.get("note") or note
    return inner if isinstance(inner, dict) else note


def first_value(note: dict[str, Any], keys: list[str]) -> str:
    candidates = [note, nested(note)]
    for obj in candidates:
        for key in keys:
            val = obj.get(key)
            if val not in (None, ""):
                return str(val)
    return ""


def note_id(note: dict[str, Any]) -> str:
    return first_value(note, ["note_id", "id"])


def note_title(note: dict[str, Any]) -> str:
    return first_value(note, ["display_title", "title", "desc"])[:120]


def note_type(note: dict[str, Any]) -> str:
    return first_value(note, ["type", "note_type"]).lower()


def xsec_token(note: dict[str, Any]) -> str:
    return first_value(note, ["xsec_token"])


def note_url(note: dict[str, Any]) -> str:
    url = first_value(note, ["url", "share_url"])
    if url:
        return url
    nid = note_id(note)
    if not nid:
        return ""
    return f"https://www.xiaohongshu.com/explore/{nid}"


def is_video(note: dict[str, Any]) -> bool:
    if note_type(note) == "video":
        return True
    inner = nested(note)
    return bool(inner.get("video_info") or inner.get("video"))


def normalize_user_id(raw: str) -> str:
    match = re.search(r"/user/profile/([^/?#]+)", raw)
    return match.group(1) if match else raw


def write_jsonl(path: Path, row: dict[str, Any]) -> None:
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def check_status(skip: bool) -> None:
    if skip:
        return
    payload = run_json(["xhs", "status", "--json"])
    if payload.get("ok") is not True:
        err = payload.get("error") or {}
        code = err.get("code", "unknown")
        msg = err.get("message", "xhs status is not ok")
        raise RuntimeError(f"xhs login required: {code}: {msg}")


def fetch_notes(user_id: str, out_dir: Path, max_pages: int, delay: float) -> list[dict[str, Any]]:
    notes_path = out_dir / "notes.jsonl"
    videos_path = out_dir / "videos.jsonl"
    notes_path.write_text("", encoding="utf-8")
    videos_path.write_text("", encoding="utf-8")

    notes: list[dict[str, Any]] = []
    cursor = ""
    for page in range(1, max_pages + 1):
        cmd = ["xhs", "user-posts", user_id, "--json"]
        if cursor:
            cmd.extend(["--cursor", cursor])
        payload = run_json(cmd)
        page_notes, next_cursor, has_more = page_from_payload(payload)
        if not page_notes:
            break

        for note in page_notes:
            row = {
                "note_id": note_id(note),
                "title": note_title(note),
                "type": note_type(note) or ("video" if is_video(note) else "image"),
                "url": note_url(note),
                "xsec_token_present": bool(xsec_token(note)),
            }
            write_jsonl(notes_path, row)
            if is_video(note) and row["url"]:
                write_jsonl(videos_path, row)
                notes.append(row)

        if not has_more or not next_cursor or next_cursor == cursor:
            break
        cursor = next_cursor
        if delay > 0:
            time.sleep(delay)
    return notes


def download_videos(
    videos: list[dict[str, Any]],
    out_dir: Path,
    cookies_from_browser: str,
    rate_limit: str,
    dry_run: bool,
    delay: float,
) -> None:
    archive = out_dir / "download-archive.txt"
    media_dir = out_dir / "media"
    media_dir.mkdir(parents=True, exist_ok=True)

    template = str(media_dir / "%(title).80B_%(id)s.%(ext)s")
    for row in videos:
        url = row["url"]
        cmd = [
            "yt-dlp",
            "--ignore-errors",
            "--continue",
            "--no-overwrites",
            "--download-archive",
            str(archive),
            "-o",
            template,
        ]
        if cookies_from_browser:
            cmd.extend(["--cookies-from-browser", cookies_from_browser])
        if rate_limit:
            cmd.extend(["--limit-rate", rate_limit])
        cmd.append(url)

        if dry_run:
            print("DRY-RUN", " ".join(cmd))
        else:
            subprocess.run(cmd, check=False)
            if delay > 0:
                time.sleep(delay)


def self_test() -> None:
    sample = {
        "ok": True,
        "data": {
            "notes": [
                {"note_id": "v1", "display_title": "video", "type": "video", "xsec_token": "tok"},
                {"note_id": "i1", "display_title": "image", "type": "normal"},
            ],
            "has_more": False,
            "cursor": "",
        },
    }
    notes, cursor, has_more = page_from_payload(sample)
    videos = [n for n in notes if is_video(n)]
    assert len(notes) == 2
    assert len(videos) == 1
    assert note_url(videos[0]) == "https://www.xiaohongshu.com/explore/v1"
    assert cursor == ""
    assert has_more is False
    print("self-test ok")


def main() -> int:
    parser = argparse.ArgumentParser(description="Download video notes from a Xiaohongshu user.")
    parser.add_argument("user", nargs="?", help="XHS user_id or https://www.xiaohongshu.com/user/profile/<id>")
    parser.add_argument("--out", default="xhs-downloads", help="Output directory")
    parser.add_argument("--max-pages", type=int, default=50, help="Maximum user-posts pages to fetch")
    parser.add_argument("--delay", type=float, default=2.0, help="Delay between page fetches/downloads")
    parser.add_argument("--cookies-from-browser", default="chrome", help="Pass browser cookies to yt-dlp; empty string disables")
    parser.add_argument("--rate-limit", default="", help="yt-dlp rate limit, e.g. 1M")
    parser.add_argument("--dry-run", action="store_true", help="Build manifests and print yt-dlp commands without downloading")
    parser.add_argument("--skip-status-check", action="store_true", help="Skip xhs status check")
    parser.add_argument("--self-test", action="store_true", help="Run parser self-test and exit")
    args = parser.parse_args()

    if args.self_test:
        self_test()
        return 0
    if not args.user:
        parser.error("user is required unless --self-test is used")

    out_dir = Path(args.out).expanduser().resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    user_id = normalize_user_id(args.user)

    try:
        check_status(args.skip_status_check)
        videos = fetch_notes(user_id, out_dir, args.max_pages, args.delay)
        print(f"video notes: {len(videos)}")
        print(f"manifest: {out_dir / 'videos.jsonl'}")
        download_videos(videos, out_dir, args.cookies_from_browser, args.rate_limit, args.dry_run, args.delay)
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
