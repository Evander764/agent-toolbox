#!/usr/bin/env bash
set -u

echo "XHS auto-deploy local check"
echo "==========================="

show_cmd() {
  local name="$1"
  local path
  path="$(command -v "$name" 2>/dev/null || true)"
  if [[ -n "$path" ]]; then
    echo "$name: $path"
  else
    echo "$name: missing"
  fi
}

show_cmd xhs
show_cmd agent-reach
show_cmd uv
show_cmd pipx
show_cmd mcporter
show_cmd yt-dlp

echo
if command -v agent-reach >/dev/null 2>&1; then
  agent-reach version 2>&1 | sed -E 's/(token|cookie|secret|key)[^[:space:]]*/[redacted]/Ig'
else
  echo "agent-reach version: unavailable"
fi

echo
if command -v xhs >/dev/null 2>&1; then
  echo "xhs status:"
  if command -v timeout >/dev/null 2>&1; then
    timeout 15 xhs status 2>&1 | sed -E 's/(web_session|a1|webId|gid|token|cookie)[^[:space:]]*/[redacted]/Ig'
  else
    xhs status 2>&1 | sed -E 's/(web_session|a1|webId|gid|token|cookie)[^[:space:]]*/[redacted]/Ig'
  fi
else
  echo "xhs status: unavailable"
fi

echo
config="$HOME/.agent-reach/config.yaml"
if [[ -f "$config" ]]; then
  mode="$(stat -f '%Lp' "$config" 2>/dev/null || stat -c '%a' "$config" 2>/dev/null || echo unknown)"
  echo "Agent-Reach config: $config mode=$mode"
  if grep -q '^xhs_cookie:' "$config"; then
    echo "Agent-Reach xhs_cookie: configured"
  else
    echo "Agent-Reach xhs_cookie: not configured"
  fi
else
  echo "Agent-Reach config: missing"
fi

echo
echo "Key source paths:"
echo "- /Users/evander/Documents/Software/必备工具/Agent-Reach"
echo "- /Users/evander/Documents/Software/Viral Brief Plus"
echo "- /Users/evander/Documents/Great things of AI/25IP开源干货-精华沉淀/skills/xhs-scraping"
echo "- ~/.codex/skills/xhs-auto-deploy/scripts/download-blogger-videos.py"
