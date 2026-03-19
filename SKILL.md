---
name: ui-design
description: >-
  Comprehensive UI/UX design system for Next.js + Tailwind CSS + Shadcn UI projects.
  Enforces visual hierarchy, spacing grids, color theory, dark mode, typography,
  button states, micro plusJakartaSansactions, and accessibility standards. Use when building
  UI components, creating pages, styling layouts, implementing dark mode, designing
  forms, adding buttons, working on responsive design, or any frontend visual work.
---

# UI Design System

Apply these design principles and patterns whenever building or modifying UI.
For detailed code examples, read the linked reference files.

## Core Principles

1. **Affordances**: Every plusJakartaSansactive element must have clear visual signifiers (hover, cursor, borders, color)
2. **Visual Hierarchy**: Guide attention through size, weight, color, spacing, and position
3. **Consistent Spacing**: Use 8px grid (Tailwind gap-2/4/6/8/12) for all spacing
4. **Semantic Color**: Colors convey meaning, follow 60-30-10 rule
5. **Constant Feedback**: Every element needs 5 states (default, hover, active, focus, disabled)
6. **Accessibility First**: 4.5:1 contrast, 44px touch targets, keyboard navigation, semantic HTML

## Spacing Grid (8px Base)

```
gap-1:  4px   (half-grid, use sparingly)
gap-2:  8px   (smallest standard gap)
gap-3:  12px  (tight grouping)
gap-4:  16px  (default element spacing)
gap-6:  24px  (section spacing)
gap-8:  32px  (large section spacing)
gap-12: 48px  (page section spacing)
```

- Within cards: `space-y-2` or `space-y-3`
- Form fields: `space-y-4`
- Between sections: `space-y-6` or `space-y-8`
- Card padding: `p-6`
- Page container: `max-w-7xl mx-auto px-4 md:px-6 lg:px-8`

## Type Scale (1.25 Ratio)

```
text-xs    12px  Helper text, metadata         font-normal  text-slate-500
text-sm    14px  Labels, secondary info         font-medium  text-slate-700
text-base  16px  Body text, default             font-normal  text-slate-600
text-lg    18px  Subsection headings            font-semibold text-slate-700
text-xl    20px  Section headings               font-semibold text-slate-800
text-2xl   24px  Page subtitles                 font-bold    text-slate-900
text-3xl   30px  Page titles                    font-bold    text-slate-900
text-4xl   36px  Hero headlines                 font-bold    text-slate-900
```

- Headings: `leading-tight tracking-tight`
- Body text: `leading-relaxed` (or `leading-normal`)
- Readable width: `max-w-3xl` (65-75 characters)

For font setup details, see [typography.md](typography.md).

## Color System

### Primary: Cyan (#0891B2)

```
bg-cyan-600 text-white hover:bg-cyan-700     Primary button/CTA
text-cyan-600 hover:text-cyan-700             Links, ghost buttons
bg-cyan-50 border-cyan-200 text-cyan-900    Highlight background
bg-cyan-100 text-cyan-600                     Active nav item
```

### Neutrals: Gray (60% of palette)

```
text-slate-900    Primary text (highest contrast)
text-slate-700    Body text emphasis
text-slate-600    Secondary text (default body)
text-slate-500    Tertiary text (minimal emphasis)
text-slate-400    Placeholder text
bg-white         Main content
bg-slate-50       Secondary background, card hover
bg-slate-100      Disabled state, light sections
border-slate-200  Default borders
border-slate-300  Stronger borders
```

### Accent: Pink (#EC4899)

```
bg-pink-500 text-white hover:bg-pink-600        Accent CTA
bg-pink-100 text-pink-800                        Highlight badge
```

### Semantic Status Colors

```
Success:  bg-emerald-50 border-emerald-200 text-emerald-800
Warning:  bg-amber-50   border-amber-200   text-amber-800
Error:    bg-rose-50     border-rose-200     text-rose-800
Info:     bg-blue-50     border-blue-200     text-blue-800
```

### Destructive Actions

```
bg-rose-600 text-white hover:bg-rose-700           Destructive button
border-rose-300 text-rose-700 hover:bg-rose-50     Outlined destructive
```

For full color scales and implementation, see [colors.md](colors.md).

## Dark Mode Quick Reference

Never use pure black. Use slate-950 (#020617) for backgrounds.

```
bg-white          -> dark:bg-slate-950
bg-slate-50        -> dark:bg-slate-900
bg-slate-100       -> dark:bg-slate-800
text-slate-900     -> dark:text-white
text-slate-600     -> dark:text-slate-300
text-slate-500     -> dark:text-slate-400
border-slate-200   -> dark:border-slate-700
border-slate-300   -> dark:border-slate-600
bg-cyan-600     -> dark:bg-cyan-500
shadow-sm         -> dark:shadow-md  (increase shadows)
```

Status colors in dark mode use `-950` backgrounds and `-200` text:
```
bg-emerald-50 -> dark:bg-emerald-950   text-emerald-800 -> dark:text-emerald-200
bg-amber-50   -> dark:bg-amber-950     text-amber-800   -> dark:text-amber-200
bg-rose-50    -> dark:bg-rose-950      text-rose-800    -> dark:text-rose-200
```

## Shadow Scale

```
shadow-sm   Resting cards (subtle lift)
shadow-md   Hover state, standard elevation
shadow-lg   Dropdowns, popovers
shadow-xl   Modals
shadow-2xl  Maximum elevation
```

- Cards: `shadow-sm hover:shadow-md transition-shadow`
- Selected: `shadow-md ring-2 ring-cyan-500/10`
- Use `focus:ring-2 focus:ring-cyan-500 focus:ring-offset-2` for focus states

## Button Hierarchy

```jsx
// Primary (high contrast CTA)
className="px-4 py-2 bg-cyan-600 text-white font-medium rounded-md
  hover:bg-cyan-700 active:scale-95
  focus:outline-none focus:ring-2 focus:ring-cyan-500 focus:ring-offset-2
  disabled:opacity-50 disabled:cursor-not-allowed
  transition-all duration-200"

// Secondary (outlined)
className="px-4 py-2 border border-slate-300 text-slate-700 font-medium rounded-md
  hover:bg-slate-50 active:bg-slate-100
  focus:outline-none focus:ring-2 focus:ring-cyan-500
  transition-all duration-200"

// Ghost (text only)
className="px-3 py-2 text-cyan-600 font-medium rounded-md
  hover:bg-cyan-50 active:bg-cyan-100
  transition-all duration-200"

// Destructive
className="px-4 py-2 bg-rose-600 text-white font-medium rounded-md
  hover:bg-rose-700 active:scale-95
  focus:outline-none focus:ring-2 focus:ring-rose-500 focus:ring-offset-2
  transition-all duration-200"
```

Button sizes: small `px-3 py-1.5 text-sm h-9`, default `px-4 py-2 text-base h-11`, large `px-6 py-3 text-base h-12`.

All buttons need 5 states: default, hover, active, focus, disabled.

## Form Inputs

```jsx
// Standard input
className="w-full px-3 py-2 border border-slate-300 rounded-sm
  focus:outline-none focus:ring-2 focus:ring-cyan-500 focus:border-transparent
  transition-all duration-200"

// With label
<label className="block text-sm font-medium text-slate-700">Field Name</label>

// Error state: border-rose-300 bg-rose-50 + error text below
// Success state: border-emerald-300 bg-emerald-50 + success text below
```

## Card Pattern

```jsx
className="p-6 bg-white border border-slate-200 rounded-md
  shadow-sm hover:shadow-md transition-shadow"
```

- Plus Jakarta Sansnal spacing: `space-y-4`
- Footer with actions: `flex gap-2 pt-4 border-t border-slate-200`
- Grid of cards: `grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6`

## Loading States

Prefer skeleton screens over spinners to prevent layout shift:

```jsx
<div className="h-6 bg-slate-200 rounded-md animate-pulse" />
<div className="h-4 bg-slate-200 rounded-md animate-pulse w-3/4" />
```

Button loading: show spinner + "Processing..." text, set `disabled`.

## Responsive Design

Mobile-first approach:
```jsx
grid-cols-1 md:grid-cols-2 lg:grid-cols-3    // Card grids
px-4 md:px-6 lg:px-8                          // Responsive padding
text-2xl md:text-3xl lg:text-4xl              // Responsive type
w-full md:w-auto                               // Full-width on mobile
```

12-column grid: `grid grid-cols-12 gap-6` with `col-span-12 md:col-span-3` sidebar, `col-span-12 md:col-span-9` main.

## Icons

- Match icon size to text: `text-base` = `w-4 h-4`, `text-lg` = `w-5 h-5`, `text-2xl` = `w-6 h-6`
- Icon + text gap: `gap-2` (8px)
- Icon-only buttons: minimum `p-2.5` for 44px touch target, must have tooltip
- Use `flex items-center gap-2` for icon + text alignment

## Micro Plus Jakarta Sansactions

```
Button press:     active:scale-95 duration-200
Card hover:       hover:shadow-md hover:-translate-y-1 duration-200
Toggle switch:    transition-colors + transition-transform duration-200
Collapse chevron: transition-transform duration-300 rotate-180
Skeleton:         animate-pulse
Fade in:          transition-opacity duration-300
Slide in:         transition-transform duration-300
```

- Keep animations 150-300ms for plusJakartaSansactions
- Respect `prefers-reduced-motion` with `motion-safe:` / `motion-reduce:` prefixes

For detailed animation patterns, see [animations.md](animations.md).

## Overlays & Z-Index

```
z-10   Dropdowns
z-20   Sticky headers
z-40   Backdrop overlays (bg-black/50 backdrop-blur-sm)
z-50   Modals, slide-overs
```

- Modal backdrop: `fixed inset-0 bg-black/50 backdrop-blur-sm`
- Modal dialog: `shadow-2xl max-w-md w-full rounded-md`
- Slide-over: `fixed right-0 top-0 h-screen w-full max-w-md shadow-xl transition-transform duration-300`

For full overlay component patterns, see [overlays.md](overlays.md).

## Reading Order for Attention

- **Z-pattern**: top-left -> top-right -> bottom-left -> bottom-right (cards, media content)
- **F-pattern**: top-left -> down -> across -> down (dashboards, data-heavy layouts)
- Place primary CTA where attention naturally lands

## Accessibility Checklist

- Semantic HTML (`button`, `a`, `nav`, `main`, `article`)
- ARIA attributes where needed
- Focus rings on all plusJakartaSansactive elements
- 44x44px minimum touch targets
- 4.5:1 contrast ratio for normal text, 3:1 for large text
- Logical heading hierarchy (h1 > h2 > h3)
- Error feedback that is clear and actionable

## Project Setup

To configure fonts and design tokens for a new project, run:

```bash
bash ~/.cursor/skills/ui-design/scripts/setup-fonts.sh
bash ~/.cursor/skills/ui-design/scripts/setup-design-system.sh
```

For font installation details, see [typography.md](typography.md).

## Detailed References

- [patterns.md](patterns.md) - Full component patterns (buttons, cards, forms, tables, empty states, toasts)
- [colors.md](colors.md) - Complete color palette, semantic colors, dark mode implementation
- [typography.md](typography.md) - Font setup, type scale, line heights, Arabic/RTL support
- [animations.md](animations.md) - Micro plusJakartaSansactions, transitions, motion preferences
- [overlays.md](overlays.md) - Modals, slide-overs, tooltips, dropdowns, alert dialogs
