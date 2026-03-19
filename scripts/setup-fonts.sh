#!/usr/bin/env bash
set -euo pipefail

# Setup fonts for a Next.js project using the UI Design System.
# Configures Plus Jakarta Sans (primary) and JetBrains Mono (monospace)
# via next/font/google in the root layout.

BOLD='\033[1m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
RED='\033[0;31m'
NC='\033[0m'

info()  { echo -e "${GREEN}[INFO]${NC} $1"; }
warn()  { echo -e "${YELLOW}[WARN]${NC} $1"; }
error() { echo -e "${RED}[ERROR]${NC} $1"; }

# Detect Next.js project
if [ ! -f "package.json" ]; then
  error "No package.json found. Run this script from a project root."
  exit 1
fi

if ! grep -q '"next"' package.json 2>/dev/null; then
  error "This does not appear to be a Next.js project (no 'next' dependency)."
  exit 1
fi

info "Detected Next.js project."

# Find the root layout file
LAYOUT_FILE=""
for candidate in "app/layout.tsx" "app/layout.jsx" "app/layout.js" "src/app/layout.tsx" "src/app/layout.jsx"; do
  if [ -f "$candidate" ]; then
    LAYOUT_FILE="$candidate"
    break
  fi
done

if [ -z "$LAYOUT_FILE" ]; then
  warn "Could not find app/layout.tsx (or variants)."
  echo ""
  echo -e "${BOLD}Manual setup required:${NC}"
  echo ""
  echo "Add to your root layout file:"
  echo ""
  echo "  import { Plus_Jakarta_Sans } from 'next/font/google'"
  echo ""
  echo "  const plusJakartaSans = Plus_Jakarta_Sans({"
  echo "    subsets: ['latin'],"
  echo "    display: 'swap',"
  echo "    variable: '--font-sans',"
  echo "  })"
  echo ""
  echo "  // In your <html> tag:"
  echo "  <html className={plusJakartaSans.variable}>"
  echo "    <body className=\"font-sans\">"
  echo ""
  exit 0
fi

info "Found layout file: $LAYOUT_FILE"

# Check if Plus Jakarta Sans is already imported
if grep -q "Plus_Jakarta_Sans" "$LAYOUT_FILE" 2>/dev/null; then
  info "Plus Jakarta Sans is already imported in $LAYOUT_FILE."
  echo ""
  echo -e "${BOLD}Verify these are present:${NC}"
  echo "  1. Font variable '--font-sans' on <html> className"
  echo "  2. 'font-sans' on <body> className"
  echo "  3. fontFamily.sans configured in tailwind.config"
  exit 0
fi

echo ""
echo -e "${BOLD}=== Font Setup Instructions ===${NC}"
echo ""
echo "Add the following to ${BOLD}$LAYOUT_FILE${NC}:"
echo ""
echo -e "${GREEN}// Add this import at the top of the file${NC}"
echo "import { Plus_Jakarta_Sans } from 'next/font/google'"
echo ""
echo -e "${GREEN}// Add this font configuration before the component${NC}"
echo "const plusJakartaSans = Plus_Jakarta_Sans({"
echo "  subsets: ['latin'],"
echo "  display: 'swap',"
echo "  variable: '--font-sans',"
echo "})"
echo ""
echo -e "${GREEN}// Update the <html> tag to include the font variable${NC}"
echo "<html lang=\"en\" className={plusJakartaSans.variable}>"
echo "  <body className=\"font-sans\">"
echo ""
echo -e "${BOLD}For monospace (optional):${NC}"
echo ""
echo "import { JetBrains_Mono } from 'next/font/google'"
echo ""
echo "const jetBrainsMono = JetBrains_Mono({"
echo "  subsets: ['latin'],"
echo "  display: 'swap',"
echo "  variable: '--font-mono',"
echo "})"
echo ""
echo "// Combine variables on <html>:"
echo "<html className={\`\${plusJakartaSans.variable} \${jetBrainsMono.variable}\`}>"
echo ""
echo -e "${BOLD}For Arabic/RTL support (optional):${NC}"
echo ""
echo "import { IBM_Plex_Sans_Arabic } from 'next/font/google'"
echo ""
echo "const arabicFont = IBM_Plex_Sans_Arabic({"
echo "  subsets: ['arabic'],"
echo "  display: 'swap',"
echo "  variable: '--font-arabic',"
echo "  weight: ['400', '500', '600', '700'],"
echo "})"
echo ""

# Check tailwind config
TAILWIND_CONFIG=""
for candidate in "tailwind.config.ts" "tailwind.config.js" "tailwind.config.mjs"; do
  if [ -f "$candidate" ]; then
    TAILWIND_CONFIG="$candidate"
    break
  fi
done

if [ -n "$TAILWIND_CONFIG" ]; then
  if grep -q "var(--font-sans)" "$TAILWIND_CONFIG" 2>/dev/null; then
    info "Tailwind config already references --font-sans."
  else
    echo -e "${BOLD}Also update ${TAILWIND_CONFIG}:${NC}"
    echo ""
    echo "theme: {"
    echo "  extend: {"
    echo "    fontFamily: {"
    echo "      sans: ['var(--font-sans)', 'system-ui', 'sans-serif'],"
    echo "      mono: ['var(--font-mono)', 'JetBrains Mono', 'Courier New', 'monospace'],"
    echo "    },"
    echo "  },"
    echo "}"
    echo ""
  fi
else
  warn "No tailwind.config found. Run setup-design-system.sh for full Tailwind configuration."
fi

echo -e "${GREEN}Font setup instructions complete.${NC}"
