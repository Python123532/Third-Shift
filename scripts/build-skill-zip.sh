#!/usr/bin/env bash
# Builds dist/third-shift.zip (the skill only, for Settings > Skills) and
# dist/third-shift-plugin.zip (the full plugin).
# Usage: scripts/build-skill-zip.sh [output path]   (default: dist/third-shift.zip)
set -euo pipefail
root="$(cd "$(dirname "$0")/.." && pwd)"
out="$(realpath -m "${1:-$root/dist/third-shift.zip}")"
mkdir -p "$(dirname "$out")"
tmp="$(mktemp -d)"
cp -r "$root/skills/third-shift" "$tmp/third-shift"
rm -f "$out"
(cd "$tmp" && zip -qr "$out" third-shift)
rm -rf "$tmp"
echo "built $out"

# Also build the full plugin zip next to it (for uploading as a plugin)
pout="$(dirname "$out")/third-shift-plugin.zip"
rm -f "$pout"
(cd "$root" && zip -qr "$pout" .claude-plugin skills commands agents assets/icon.png README.md LICENSE)
echo "built $pout"
