#!/usr/bin/env bash
set -euo pipefail

# Interactive configuration dashboard for the UI Design System.
# Opens a browser-based UI to customize colors, fonts, and styling.

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PORT=8432

BOLD='\033[1m'
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

info()  { echo -e "${GREEN}[INFO]${NC} $1"; }
error() { echo -e "${RED}[ERROR]${NC} $1"; }

if [ $# -lt 1 ]; then
  error "Usage: $0 <project-directory>"
  echo "  Example: $0 /path/to/my-app"
  exit 1
fi

PROJECT_DIR="$(cd "$1" && pwd)"

if [ ! -d "$PROJECT_DIR" ]; then
  error "Project directory does not exist: $1"
  exit 1
fi

# Check for python3
if ! command -v python3 &>/dev/null; then
  error "python3 is required but not found."
  echo "  Install Python 3: https://www.python.org/downloads/"
  exit 1
fi

# Check for jq
if ! command -v jq &>/dev/null; then
  error "jq is required but not found."
  echo "  Install jq: https://jqlang.github.io/jq/download/"
  exit 1
fi

# Check if port is already in use
if lsof -i :"$PORT" &>/dev/null 2>&1; then
  error "Port $PORT is already in use. Kill the existing process or wait for it to finish."
  exit 1
fi

info "Starting configuration dashboard on http://localhost:$PORT"

# Open browser after a short delay
(sleep 1 && open "http://localhost:$PORT" 2>/dev/null || xdg-open "http://localhost:$PORT" 2>/dev/null || true) &

# Start the server (blocks until apply is done)
python3 "$SCRIPT_DIR/server.py" "$SCRIPT_DIR" "$PORT"

echo ""
echo -e "${GREEN}${BOLD}Configuration applied successfully!${NC}"
echo ""

# --- Add permission to .claude/settings.local.json in the target project ---

SETTINGS_FILE="$PROJECT_DIR/.claude/settings.local.json"
PERMISSION="Bash(jq -e '.hooks.UserPromptSubmit[] | .hooks[] | select\\(.type == \"\"prompt\"\"\\) | .prompt' ${SETTINGS_FILE})"

mkdir -p "$PROJECT_DIR/.claude"

if [ -f "$SETTINGS_FILE" ]; then
  if jq -e '.permissions.allow' "$SETTINGS_FILE" &>/dev/null; then
    if jq -e --arg perm "$PERMISSION" '.permissions.allow | index($perm)' "$SETTINGS_FILE" &>/dev/null; then
      info "Permission already present in $SETTINGS_FILE"
    else
      jq --arg perm "$PERMISSION" '.permissions.allow += [$perm]' "$SETTINGS_FILE" > "${SETTINGS_FILE}.tmp" \
        && mv "${SETTINGS_FILE}.tmp" "$SETTINGS_FILE"
      info "Added permission to $SETTINGS_FILE"
    fi
  else
    jq --arg perm "$PERMISSION" '. + {permissions: {allow: [$perm]}}' "$SETTINGS_FILE" > "${SETTINGS_FILE}.tmp" \
      && mv "${SETTINGS_FILE}.tmp" "$SETTINGS_FILE"
    info "Created permissions block in $SETTINGS_FILE"
  fi
else
  jq -n --arg perm "$PERMISSION" '{permissions: {allow: [$perm]}}' > "$SETTINGS_FILE"
  info "Created $SETTINGS_FILE with permission"
fi
