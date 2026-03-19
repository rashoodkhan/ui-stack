#!/usr/bin/env bash
set -euo pipefail

# ─────────────────────────────────────────────────────────────
# UI Design System — One-line Installer
#
# Usage (from your project root):
#   /bin/bash -c "$(curl -fsSL <RAW_URL>/install.sh)"
# ─────────────────────────────────────────────────────────────

SKILL_NAME="ui-design"
REPO_URL="https://raw.githubusercontent.com/rashoodkhan/ui-stack/refs/heads/main"

BOLD='\033[1m'
DIM='\033[2m'
GREEN='\033[0;32m'
CYAN='\033[0;36m'
YELLOW='\033[0;33m'
RED='\033[0;31m'
NC='\033[0m'

info()  { echo -e "  ${GREEN}✓${NC} $1"; }
warn()  { echo -e "  ${YELLOW}!${NC} $1"; }
error() { echo -e "  ${RED}✗${NC} $1"; }
step()  { echo -e "\n${CYAN}${BOLD}▸${NC} ${BOLD}$1${NC}"; }

PROJECT_DIR="$(pwd)"

if [ -d "$PROJECT_DIR/.claude" ]; then
  INSTALL_DIR="$PROJECT_DIR/.claude/skills/$SKILL_NAME"
else
  INSTALL_DIR="$HOME/.claude/skills/$SKILL_NAME"
fi

# ── Banner ──────────────────────────────────────────────────

echo ""
echo -e "${BOLD}  ┌───────────────────────────────────────┐${NC}"
echo -e "${BOLD}  │   UI Design System — Installer        │${NC}"
echo -e "${BOLD}  │   Claude Code Skill for UI Design     │${NC}"
echo -e "${BOLD}  └───────────────────────────────────────┘${NC}"
echo ""
echo -e "  ${DIM}Project:  ${PROJECT_DIR}${NC}"
echo -e "  ${DIM}Install:  ${INSTALL_DIR}${NC}"
echo ""

# ── Preflight checks ───────────────────────────────────────

step "Checking prerequisites"

HAS_CURL=false
HAS_WGET=false
command -v curl  &>/dev/null && HAS_CURL=true
command -v wget  &>/dev/null && HAS_WGET=true

if ! $HAS_CURL && ! $HAS_WGET; then
  error "curl or wget is required but neither was found."
  exit 1
fi
info "curl/wget available"

if ! command -v python3 &>/dev/null; then
  error "python3 is required but not found."
  echo -e "  Install Python 3: ${CYAN}https://www.python.org/downloads/${NC}"
  exit 1
fi
info "python3 $(python3 --version 2>&1 | awk '{print $2}')"

if ! command -v jq &>/dev/null; then
  error "jq is required but not found."
  echo -e "  Install jq:       ${CYAN}https://jqlang.github.io/jq/download/${NC}"
  echo -e "  macOS:            ${DIM}brew install jq${NC}"
  exit 1
fi
info "jq $(jq --version 2>&1)"

# ── Download skill ──────────────────────────────────────────

step "Installing skill to ${DIM}${INSTALL_DIR}${NC}"

fetch() {
  local url="$1" dest="$2"
  if $HAS_CURL; then
    curl -fsSL "$url" -o "$dest"
  else
    wget -qO "$dest" "$url"
  fi
}

mkdir -p "$INSTALL_DIR/scripts"

SKILL_FILES=(
  "SKILL.md"
  "colors.md"
  "typography.md"
  "patterns.md"
  "animations.md"
  "overlays.md"
)

SCRIPT_FILES=(
  "scripts/config.json"
  "scripts/configure.sh"
  "scripts/dashboard.html"
  "scripts/generate.py"
  "scripts/server.py"
  "scripts/setup-design-system.sh"
  "scripts/setup-fonts.sh"
)

download_count=0
total=$(( ${#SKILL_FILES[@]} + ${#SCRIPT_FILES[@]} ))

for file in "${SKILL_FILES[@]}" "${SCRIPT_FILES[@]}"; do
  download_count=$((download_count + 1))
  printf "\r  ${DIM}[%d/%d] %s${NC}                    " "$download_count" "$total" "$file"
  fetch "${REPO_URL}/${file}" "${INSTALL_DIR}/${file}"
done
echo ""

chmod +x "$INSTALL_DIR/scripts/configure.sh"
chmod +x "$INSTALL_DIR/scripts/setup-design-system.sh"
chmod +x "$INSTALL_DIR/scripts/setup-fonts.sh"

info "Downloaded ${total} files"

# ── Launch configuration dashboard ──────────────────────────

step "Launching configuration dashboard"
echo -e "  ${DIM}Customize colors, fonts, and radius in your browser.${NC}"
echo -e "  ${DIM}Close the browser tab or press Ctrl+C when done.${NC}"
echo ""

bash "$INSTALL_DIR/scripts/configure.sh" "$PROJECT_DIR"

# ── Done ────────────────────────────────────────────────────

echo ""
echo -e "${GREEN}${BOLD}  ┌──────────────────────────────────────┐${NC}"
echo -e "${GREEN}${BOLD}  │   Installation complete!              │${NC}"
echo -e "${GREEN}${BOLD}  └──────────────────────────────────────┘${NC}"
echo ""
echo -e "  ${BOLD}What was installed:${NC}"
echo -e "    ${DIM}Skill files  → ${INSTALL_DIR}/${NC}"
echo -e "    ${DIM}Permissions  → ${PROJECT_DIR}/.claude/settings.local.json${NC}"
echo ""
echo -e "  ${BOLD}Next steps:${NC}"
echo -e "    1. Open your project in Claude Code"
echo -e "    2. Start building UI — the skill activates automatically"
echo -e "    3. To reconfigure later, run:"
echo -e "       ${CYAN}bash ${INSTALL_DIR}/scripts/configure.sh ${PROJECT_DIR}${NC}"
echo ""
