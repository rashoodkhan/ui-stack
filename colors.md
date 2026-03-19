# Color System Reference

Complete color palette, semantic usage, dark mode mappings, and accessibility guidelines.

---

## The 60-30-10 Rule

- **60%** Neutral/Background colors (establishes calm)
- **30%** Secondary colors (supporting content)
- **10%** Accent colors (calls to action, emphasis)

---

## Primary Color: Cyan (#0891B2)

Trustworthy, professional. Used for primary actions, navigation, and key UI elements.

```
cyan-50:   #ECFEFF  Very light background
cyan-100:  #CFFAFE  Light background, active nav items
cyan-200:  #A5F3FC  Light border
cyan-300:  #67E8F9  Medium highlight
cyan-400:  #22D3EE  Medium
cyan-500:  #06B6D4  Light primary
cyan-600:  #0891B2  PRIMARY (default)
cyan-700:  #0E7490  Dark primary (hover)
cyan-800:  #155E75  Very dark (active)
cyan-900:  #164E63  Darkest (text on light bg)
```

### Usage

```jsx
// Primary button
<button className="bg-cyan-600 text-white hover:bg-cyan-700">Action</button>

// Primary link
<a className="text-cyan-600 hover:text-cyan-700">Link</a>

// Highlight background
<div className="bg-cyan-50 border border-cyan-200 text-cyan-900">Highlighted</div>

// Active nav item
<a className="bg-cyan-100 text-cyan-600">Active</a>
```

---

## Secondary Colors: Grays (60% of palette)

For text, backgrounds, borders, and secondary information.

```
slate-50:   #F8FAFC  Backgrounds, light sections
slate-100:  #F1F5F9  Hover states, disabled buttons
slate-200:  #E2E8F0  Borders, dividers
slate-300:  #CBD5E1  Stronger borders
slate-400:  #94A3B8  Placeholder text
slate-500:  #64748B  Tertiary text
slate-600:  #475569  Secondary text (body)
slate-700:  #334155  Body text emphasis
slate-800:  #1E293B  Headlines
slate-900:  #0F172A  Primary text
slate-950:  #020617  Dark mode background
```

### Text Hierarchy

```jsx
<p className="text-slate-900">Primary text (highest contrast)</p>
<p className="text-slate-700">Body text (emphasis)</p>
<p className="text-slate-600">Secondary text (default body)</p>
<p className="text-slate-500">Tertiary text (minimal emphasis)</p>
<p className="text-slate-400">Muted / placeholder text</p>
```

### Background Hierarchy

```jsx
<div className="bg-white">Main content area</div>
<div className="bg-slate-50">Secondary background, card hover</div>
<div className="bg-slate-100">Disabled state, light section background</div>
```

### Border Hierarchy

```jsx
<div className="border border-slate-200">Default border (subtle)</div>
<div className="border border-slate-300">Stronger border (emphasis)</div>
```

---

## Accent Color: Pink (#EC4899)

Warm accent for highlights and secondary CTAs.

```
pink-50:   #FDF2F8
pink-100:  #FCE7F3
pink-200:  #FBCFE8
pink-400:  #F472B6
pink-500:  #EC4899  PRIMARY ACCENT
pink-600:  #DB2777  Dark accent (hover)
pink-700:  #BE185D
pink-800:  #9D174D
```

### Usage

```jsx
// Accent CTA
<button className="bg-pink-500 text-white hover:bg-pink-600">Highlight Action</button>

// Highlight badge
<span className="px-2 py-1 bg-pink-100 text-pink-800 rounded-full text-xs font-medium">
  Featured
</span>

// Accent background
<div className="bg-pink-50 border border-pink-200 text-pink-900">Featured section</div>
```

---

## Semantic Status Colors

### Success: Emerald

```jsx
// Alert
<div className="bg-emerald-50 border border-emerald-200 rounded-md p-4">
  <p className="text-emerald-800">Action completed successfully</p>
</div>

// Badge
<span className="px-2 py-1 bg-emerald-100 text-emerald-700 rounded text-xs font-medium">
  Active
</span>
```

### Warning: Amber

```jsx
// Alert
<div className="bg-amber-50 border border-amber-200 rounded-md p-4">
  <p className="text-amber-800">Attention required</p>
</div>

// Badge
<span className="px-2 py-1 bg-amber-100 text-amber-700 rounded text-xs font-medium">
  Pending
</span>
```

### Error / Destructive: Rose

```jsx
// Alert
<div className="bg-rose-50 border border-rose-200 rounded-md p-4">
  <p className="text-rose-800">Something went wrong</p>
</div>

// Destructive button
<button className="bg-rose-600 text-white hover:bg-rose-700">Delete</button>

// Rose scale
rose-50:   #FFF5F7
rose-100:  #FFE4E8
rose-200:  #FECDD3
rose-500:  #F43F5E  Primary destructive
rose-600:  #E11D48  Dark destructive (hover)
```

### Info: Blue

```jsx
<div className="bg-blue-50 border border-blue-200 rounded-md p-4">
  <p className="text-blue-800">New report available</p>
</div>
```

### Premium / AI: Purple Gradient

```jsx
<div className="bg-gradient-to-r from-cyan-500 to-fuchsia-500 text-white p-4 rounded-md">
  <p className="font-semibold">AI-Powered Feature (Premium)</p>
</div>
```

---

## Color Implementation Object

Reusable semantic color mappings:

```jsx
export const colors = {
  bg: {
    primary: 'bg-white',
    secondary: 'bg-slate-50',
    tertiary: 'bg-slate-100',
    overlay: 'bg-black/50',
  },
  text: {
    primary: 'text-slate-900',
    secondary: 'text-slate-600',
    tertiary: 'text-slate-500',
    muted: 'text-slate-400',
  },
  button: {
    primary: 'bg-cyan-600 text-white hover:bg-cyan-700',
    secondary: 'bg-slate-100 text-slate-900 hover:bg-slate-200',
    ghost: 'text-cyan-600 hover:bg-cyan-50',
  },
  status: {
    success: 'text-emerald-700 bg-emerald-50 border-emerald-200',
    warning: 'text-amber-700 bg-amber-50 border-amber-200',
    error: 'text-rose-700 bg-rose-50 border-rose-200',
    info: 'text-blue-700 bg-blue-50 border-blue-200',
  },
}
```

---

## Dark Mode Color Palette

### Backgrounds

Never use pure black (`#000000`). Use slate-950 for warmth.

```jsx
<div className="bg-white dark:bg-slate-950">Primary background</div>
<div className="bg-slate-50 dark:bg-slate-900">Secondary background</div>
<div className="bg-slate-100 dark:bg-slate-800">Tertiary background</div>
```

### Text

```jsx
<p className="text-slate-900 dark:text-white">Primary text</p>
<p className="text-slate-600 dark:text-slate-300">Secondary text</p>
<p className="text-slate-500 dark:text-slate-400">Tertiary text</p>
<p className="text-slate-400 dark:text-slate-600">Muted text</p>
```

### Borders

```jsx
<div className="border border-slate-200 dark:border-slate-700">Default border</div>
<div className="border border-slate-300 dark:border-slate-600">Strong border</div>
```

### Plus Jakarta Sansactive Colors

Slightly lighter primary in dark mode for eye comfort:

```jsx
<button className="bg-cyan-600 dark:bg-cyan-500 text-white
  hover:bg-cyan-700 dark:hover:bg-cyan-600">
  Submit
</button>
```

### Status Colors in Dark Mode

Use `-950` backgrounds and `-200` text on dark:

```jsx
<div className="bg-emerald-50 dark:bg-emerald-950 border border-emerald-200 dark:border-emerald-800">
  <p className="text-emerald-800 dark:text-emerald-200">Success</p>
</div>

<div className="bg-amber-50 dark:bg-amber-950 border border-amber-200 dark:border-amber-800">
  <p className="text-amber-800 dark:text-amber-200">Warning</p>
</div>

<div className="bg-rose-50 dark:bg-rose-950 border border-rose-200 dark:border-rose-800">
  <p className="text-rose-800 dark:text-rose-200">Error</p>
</div>
```

### Shadows in Dark Mode

Increase shadow depth (dark backgrounds need stronger shadows):

```jsx
<div className="shadow-sm dark:shadow-md hover:shadow-md dark:hover:shadow-lg transition-shadow">
  Card
</div>
```

### Complete Dark Mode Card

```jsx
<div className="p-6 bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-700
  rounded-md shadow-sm dark:shadow-lg hover:shadow-md dark:hover:shadow-xl transition-shadow">

  <div className="flex items-center justify-between mb-4">
    <h3 className="text-lg font-semibold text-slate-900 dark:text-white">Title</h3>
    <span className="px-2 py-1 bg-cyan-100 dark:bg-cyan-900/30
      text-cyan-700 dark:text-cyan-300 rounded text-xs font-medium">
      Badge
    </span>
  </div>

  <div className="space-y-3 mb-4 pb-4 border-b border-slate-200 dark:border-slate-700">
    <div className="flex justify-between">
      <span className="text-sm text-slate-600 dark:text-slate-400">Label</span>
      <span className="text-sm font-medium text-slate-900 dark:text-slate-100">Value</span>
    </div>
  </div>

  <div className="flex gap-2">
    <button className="flex-1 px-4 py-2 bg-cyan-600 dark:bg-cyan-500 text-white
      font-medium rounded-sm hover:bg-cyan-700 dark:hover:bg-cyan-600 transition-colors">
      Primary
    </button>
    <button className="flex-1 px-4 py-2 border border-slate-300 dark:border-slate-600
      text-slate-700 dark:text-slate-300 font-medium rounded-sm
      hover:bg-slate-50 dark:hover:bg-slate-800 transition-colors">
      Secondary
    </button>
  </div>
</div>
```

### Dark Mode Setup

```jsx
// tailwind.config.js
module.exports = {
  darkMode: 'class',
}

// Toggle implementation
export function DarkModeProvider({ children }) {
  const [isDark, setIsDark] = useState(false)

  useEffect(() => {
    const saved = localStorage.getItem('theme')
    if (saved) {
      setIsDark(saved === 'dark')
    } else {
      setIsDark(window.matchMedia('(prefers-color-scheme: dark)').matches)
    }
  }, [])

  useEffect(() => {
    const root = document.documentElement
    root.classList.toggle('dark', isDark)
    localStorage.setItem('theme', isDark ? 'dark' : 'light')
  }, [isDark])

  return (
    <div>
      <button onClick={() => setIsDark(!isDark)}>
        {isDark ? 'Light Mode' : 'Dark Mode'}
      </button>
      {children}
    </div>
  )
}
```

---

## Contrast & Accessibility

WCAG AA compliance:
- **Normal text** (14px+): 4.5:1 contrast ratio
- **Large text** (18px+ or 14px bold): 3:1 contrast ratio

```jsx
// Good contrast
<p className="text-slate-700 bg-white">Content</p>   // 8.2:1 ratio

// Poor contrast (fails accessibility)
<p className="text-slate-400 bg-white">Content</p>    // 2.0:1 ratio

// White on indigo
<div className="bg-cyan-600 text-white">Content</div>  // 9.5:1 ratio
```

### Rules

- Body text on white: use `text-slate-600` or darker
- Labels: use `text-slate-700` with `font-medium`
- Placeholder text (`text-slate-400`) is acceptable since it disappears on input
- Always test contrast when using colored backgrounds
