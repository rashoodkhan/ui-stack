# ui-stack

**A configuration-driven design system skill for Claude Code that makes AI-generated UI remarkably consistent.**

ui-stack gives Claude Code a comprehensive set of UI/UX design principles — spacing grids, color theory, typography scales, dark mode, animations, accessibility — so every component it builds follows the same visual language. No more inconsistent padding, mismatched colors, or forgotten hover states.

## What It Does

ui-stack is a **Claude Code skill** that activates automatically when you're working on frontend code. It enforces:

- **8px spacing grid** — consistent gaps, padding, and margins across every component
- **Color system** — primary, accent, neutral, and semantic colors with the 60-30-10 rule
- **Type scale** — 1.25 ratio scale with proper weights, line heights, and hierarchy
- **Dark mode** — complete light/dark mappings, never pure black
- **5-state interactions** — every interactive element gets default, hover, active, focus, and disabled states
- **Accessibility** — 4.5:1 contrast, 44px touch targets, semantic HTML, keyboard navigation
- **Micro-interactions** — subtle animations that feel polished (150-300ms, respects `prefers-reduced-motion`)
- **Overlay system** — modals, slide-overs, tooltips, dropdowns with proper z-index layering

## Stack

Built for **Next.js + Tailwind CSS + Shadcn UI** projects. The design tokens and patterns map directly to Tailwind utility classes.

## Installation

**Requirements:** Claude Code, Python 3, jq, curl or wget

### One-line install

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/rashoodkhan/ui-stack/refs/heads/main/install.sh)"
```

### Manual install

```bash
git clone https://github.com/rashoodkhan/ui-stack.git ~/.claude/skills/ui-design
```

The installer downloads the skill files, then launches a **configuration dashboard** in your browser where you can customize colors, fonts, and border radius before the skill activates.

## How It Works

ui-stack is a set of structured reference files that Claude Code reads when building UI:

| File | What it covers |
|------|---------------|
| `SKILL.md` | Core principles, quick-reference for spacing, color, type, buttons, forms |
| `patterns.md` | Full component patterns — cards, tables, empty states, toasts |
| `colors.md` | Complete color palette, semantic colors, dark mode implementation |
| `typography.md` | Font setup, type scale, line heights, RTL support |
| `animations.md` | Micro-interactions, transitions, motion preferences |
| `overlays.md` | Modals, slide-overs, tooltips, dropdowns, alert dialogs |

### Configuration scripts

| Script | Purpose |
|--------|---------|
| `scripts/configure.sh` | Launches the visual configuration dashboard |
| `scripts/generate.py` | Regenerates skill files from your config |
| `scripts/setup-fonts.sh` | Installs and configures project fonts |
| `scripts/setup-design-system.sh` | Scaffolds design tokens into your project |
| `scripts/server.py` | Local server for the configuration dashboard |
| `scripts/config.json` | Your saved design system configuration |

## Configuration

Run the configuration dashboard at any time to customize your design system:

```bash
bash ~/.claude/skills/ui-design/scripts/configure.sh /path/to/your/project
```

This opens a browser-based UI where you can adjust:

- **Primary & accent colors** — pick your brand palette
- **Font families** — choose from system fonts or Google Fonts
- **Border radius** — from sharp to fully rounded
- **Spacing scale** — adjust the base grid

Changes regenerate the skill files so Claude Code immediately uses your updated design language.

## Usage

Once installed, the skill activates automatically in Claude Code whenever you're doing frontend work. Just ask Claude to build UI:

```
> Build a settings page with a sidebar navigation and a form for user profile
> Add a data table with sorting, filtering, and pagination
> Create a modal for confirming destructive actions
```

Claude will follow the design system for every component — consistent spacing, proper color usage, dark mode support, accessible markup, and polished interactions.

## Why This Exists

AI code generation is powerful, but without design constraints it produces inconsistent UI. Every generation picks different spacing, colors, and patterns. ui-stack solves this by giving the AI a complete design system as context, so the output is coherent from the first component to the hundredth.

## License

MIT
