#!/usr/bin/env bash
set -euo pipefail

# Setup Tailwind CSS design system tokens for the UI Design System.
# Configures font families, custom shadows, dark mode, and font sizes.

BOLD='\033[1m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
RED='\033[0;31m'
CYAN='\033[0;36m'
NC='\033[0m'

info()  { echo -e "${GREEN}[INFO]${NC} $1"; }
warn()  { echo -e "${YELLOW}[WARN]${NC} $1"; }
error() { echo -e "${RED}[ERROR]${NC} $1"; }

if [ ! -f "package.json" ]; then
  error "No package.json found. Run this script from a project root."
  exit 1
fi

echo ""
echo -e "${BOLD}=== UI Design System - Tailwind Configuration ===${NC}"
echo ""

# Detect existing Tailwind config
TAILWIND_CONFIG=""
for candidate in "tailwind.config.ts" "tailwind.config.js" "tailwind.config.mjs"; do
  if [ -f "$candidate" ]; then
    TAILWIND_CONFIG="$candidate"
    break
  fi
done

if [ -n "$TAILWIND_CONFIG" ]; then
  info "Found Tailwind config: $TAILWIND_CONFIG"
  echo ""
  echo -e "${BOLD}Merge the following into your existing ${TAILWIND_CONFIG}:${NC}"
else
  warn "No tailwind.config found."
  echo ""
  echo -e "${BOLD}Create a tailwind.config.ts with the following content:${NC}"
fi

echo ""
echo -e "${CYAN}// tailwind.config.ts${NC}"
cat << 'TAILWIND_EOF'
import type { Config } from 'tailwindcss'

const config: Config = {
  darkMode: 'class',
  content: [
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './app/**/*.{js,ts,jsx,tsx,mdx}',
    './src/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ['var(--font-sans)', 'system-ui', 'sans-serif'],
        mono: ['var(--font-mono)', 'JetBrains Mono', 'Courier New', 'monospace'],
      },
      fontSize: {
        xs:   ['12px', { lineHeight: '16px' }],
        sm:   ['14px', { lineHeight: '20px' }],
        base: ['16px', { lineHeight: '24px' }],
        lg:   ['18px', { lineHeight: '28px' }],
        xl:   ['20px', { lineHeight: '28px' }],
        '2xl': ['24px', { lineHeight: '32px' }],
        '3xl': ['30px', { lineHeight: '36px' }],
        '4xl': ['36px', { lineHeight: '40px' }],
      },
      boxShadow: {
        'card-resting': '0 1px 3px rgba(0,0,0,0.04), 0 1px 2px rgba(0,0,0,0.06)',
        'card-hover': '0 4px 6px rgba(0,0,0,0.04), 0 2px 4px rgba(0,0,0,0.06)',
        'elevated': '0 10px 15px rgba(0,0,0,0.04), 0 4px 6px rgba(0,0,0,0.02)',
        'popup': '0 20px 25px rgba(0,0,0,0.1), 0 8px 10px rgba(0,0,0,0.06)',
      },
    },
  },
  plugins: [],
}

export default config
TAILWIND_EOF

echo ""
echo -e "${BOLD}--- Design Token Summary ---${NC}"
echo ""
echo "  Dark Mode:    class-based (add 'dark' class to <html>)"
echo "  Font Sans:    var(--font-sans) -> Plus Jakarta Sans"
echo "  Font Mono:    var(--font-mono) -> JetBrains Mono"
echo ""
echo "  Custom Shadows:"
echo "    shadow-card-resting  Subtle card shadow (resting state)"
echo "    shadow-card-hover    Card shadow on hover"
echo "    shadow-elevated      Elevated elements (popovers)"
echo "    shadow-popup         Maximum elevation (modals)"
echo ""
echo "  Type Scale (1.25 ratio):"
echo "    text-xs    12px/16px   Helper text, metadata"
echo "    text-sm    14px/20px   Labels, secondary info"
echo "    text-base  16px/24px   Body text (default)"
echo "    text-lg    18px/28px   Subsection headings"
echo "    text-xl    20px/28px   Section headings"
echo "    text-2xl   24px/32px   Page subtitles"
echo "    text-3xl   30px/36px   Page titles"
echo "    text-4xl   36px/40px   Hero headlines"
echo ""

# Check for globals.css
GLOBALS_CSS=""
for candidate in "app/globals.css" "src/app/globals.css" "styles/globals.css"; do
  if [ -f "$candidate" ]; then
    GLOBALS_CSS="$candidate"
    break
  fi
done

if [ -n "$GLOBALS_CSS" ]; then
  info "Found global CSS: $GLOBALS_CSS"

  if grep -q "fadeIn" "$GLOBALS_CSS" 2>/dev/null; then
    info "Custom animations already defined in $GLOBALS_CSS."
  else
    echo ""
    echo -e "${BOLD}Add these custom animations to ${GLOBALS_CSS}:${NC}"
    echo ""
    cat << 'CSS_EOF'
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

@keyframes scaleIn {
  from { opacity: 0; transform: scale(0.95); }
  to { opacity: 1; transform: scale(1); }
}

.animate-fadeIn {
  animation: fadeIn 0.2s ease-out;
}

.animate-scaleIn {
  animation: scaleIn 0.2s ease-out;
}
CSS_EOF
  fi
else
  warn "No globals.css found. Custom animations can be added to your global stylesheet."
fi

echo ""
echo -e "${GREEN}Design system configuration complete.${NC}"
echo ""
echo -e "Next steps:"
echo "  1. Run ${BOLD}setup-fonts.sh${NC} to configure font imports in your layout"
echo "  2. Merge the Tailwind config above into your existing config"
echo "  3. Add custom animations to your global CSS if needed"
echo ""
