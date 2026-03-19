# Typography Reference

Font recommendations, type scale, line heights, and setup instructions for Next.js projects.

---

## Recommended Fonts

### Primary Font: Plus Jakarta Sans

A modern, geometric sans-serif with excellent readability. Warm and SaaS-friendly.

```typescript
import { Plus_Jakarta_Sans } from 'next/font/google'

const plusJakartaSans = Plus_Jakarta_Sans({
  subsets: ['latin'],
  display: 'swap',
  variable: '--font-sans',
})
```

### Alternative Primary Fonts

If Plus Jakarta Sans is unavailable:

**DM Sans** - Clean, slightly rounder, professional:
```typescript
import { DM_Sans } from 'next/font/google'
const dmSans = DM_Sans({ subsets: ['latin'], display: 'swap', variable: '--font-sans' })
```

**Outfit** - Contemporary with variable weight support:
```typescript
import { Outfit } from 'next/font/google'
const outfit = Outfit({ subsets: ['latin'], display: 'swap', variable: '--font-sans' })
```

**Inter** - Universal SaaS standard, ultra-clean:
```typescript
import { Inter } from 'next/font/google'
const inter = Inter({ subsets: ['latin'], display: 'swap', variable: '--font-sans' })
```

### Monospace Font: JetBrains Mono or Geist Mono

For prices, numeric data, IDs, and code:

```jsx
<p className="font-mono text-lg font-bold">$125.50</p>
<p className="font-mono text-sm text-slate-600">ID: PRJ-2024-001</p>
```

### Arabic/RTL Support: IBM Plex Sans Arabic

For plusJakartaSansnational deployments with Arabic language:

```typescript
import { IBM_Plex_Sans_Arabic } from 'next/font/google'

const arabicFont = IBM_Plex_Sans_Arabic({
  subsets: ['arabic'],
  display: 'swap',
  variable: '--font-arabic',
  weight: ['400', '500', '600', '700'],
})

export default function RootLayout({ children }) {
  return (
    <html lang="ar" dir="rtl" className={arabicFont.variable}>
      <body className="font-arabic">{children}</body>
    </html>
  )
}
```

---

## Font Setup in Next.js

### Step 1: Configure in `app/layout.tsx`

```typescript
import { Plus_Jakarta_Sans } from 'next/font/google'

const plusJakartaSans = Plus_Jakarta_Sans({
  subsets: ['latin'],
  display: 'swap',
  variable: '--font-sans',
})

export default function RootLayout({ children }) {
  return (
    <html lang="en" className={plusJakartaSans.variable}>
      <body className="font-sans">{children}</body>
    </html>
  )
}
```

### Step 2: Configure in `tailwind.config.ts`

```typescript
import type { Config } from 'tailwindcss'

const config: Config = {
  theme: {
    extend: {
      fontFamily: {
        sans: ['var(--font-sans)', 'system-ui', 'sans-serif'],
        mono: ['JetBrains Mono', 'Courier New', 'monospace'],
      },
    },
  },
}

export default config
```

### Step 3: Use Throughout Application

```jsx
// Font is applied globally via font-sans on body
<h1 className="text-3xl font-bold">Dashboard</h1>

// Monospace for numeric data
<p className="font-mono text-lg">$125.50</p>
```

---

## Modular Type Scale (1.25 Ratio)

```
Tailwind Class    Size     Use Case
text-xs           12px     Helper text, metadata, captions
text-sm           14px     Labels, secondary information
text-base         16px     Body text, default reading size
text-lg           18px     Subsection headings
text-xl           20px     Section headings
text-2xl          24px     Page subtitles
text-3xl          30px     Page titles
text-4xl          36px     Hero headlines
```

### Type Scale with Tailwind Config

```typescript
theme: {
  extend: {
    fontSize: {
      xs:   ['12px', { lineHeight: '16px' }],
      sm:   ['14px', { lineHeight: '20px' }],
      base: ['16px', { lineHeight: '24px' }],
      lg:   ['18px', { lineHeight: '28px' }],
      xl:   ['20px', { lineHeight: '28px' }],
      '2xl': ['24px', { lineHeight: '32px' }],
      '3xl': ['30px', { lineHeight: '36px' }],
    },
  },
}
```

---

## Typography Hierarchy

```jsx
// Page Title
<h1 className="text-3xl md:text-4xl font-bold text-slate-900 mb-2">Page Title</h1>

// Subtitle
<p className="text-base text-slate-600 mb-8">Supporting description text</p>

// Section Title
<h2 className="text-xl font-semibold text-slate-800 mt-8 mb-4">Section Title</h2>

// Subsection Title
<h3 className="text-lg font-semibold text-slate-700 mb-4">Subsection</h3>

// Body text
<p className="text-base text-slate-600">Default body content</p>

// Label
<label className="text-sm font-medium text-slate-700">Field Label</label>

// Helper / metadata
<p className="text-xs text-slate-500">Last updated 2 minutes ago</p>
```

### Weight for Emphasis Within Same Size

```jsx
<p className="text-base">
  <span className="font-semibold text-slate-900">Status:</span>
  <span className="text-slate-600"> Active</span>
</p>

<p className="text-lg">
  <span className="text-slate-600">Total: </span>
  <span className="font-bold text-slate-900">$125.50</span>
</p>
```

---

## Font Weights

```
font-normal    400   Body text
font-medium    500   Labels, emphasis
font-semibold  600   Section headings, table headers
font-bold      700   Page titles, strong emphasis
```

---

## Line Height

```
leading-tight     1.25    Headings (compact)
leading-snug      1.375   Subheadings
leading-normal    1.5     Default body text
leading-relaxed   1.625   Long-form content (better readability)
```

### Usage

```jsx
// Headings: tight line height, negative tracking
<h1 className="text-3xl font-bold leading-tight tracking-tight text-slate-900">
  Make Great Decisions
</h1>

// Body: relaxed for readability
<p className="text-base text-slate-600 leading-relaxed max-w-3xl">
  Detailed description text that benefits from generous line spacing
  for comfortable reading across longer paragraphs.
</p>
```

---

## Letter Spacing

```
tracking-tight    -0.02em   Headings (tighter feel)
tracking-normal   0em       Default
tracking-wide     0.025em   All-caps labels, small text
```

---

## Max Line Width

Optimal reading width is 65-75 characters per line:

```jsx
<article className="max-w-3xl mx-auto">
  <p className="text-base text-slate-600 leading-relaxed">
    {/* Stays within readable width on wide screens */}
  </p>
</article>
```

---

## Font Loading Performance

The Next.js font configuration optimizes loading automatically:

- **`display: 'swap'`** - Shows system font immediately, swaps when loaded
- **CSS variable** - Avoids duplicate font declarations
- **`subsets: ['latin']`** - Reduces file size to needed characters only
- **Variable fonts** - Single file supports all weights

### Troubleshooting

1. Verify correct subsets: `subsets: ['latin']` (or `['latin-ext']`, `['cyrillic']`)
2. Always use `display: 'swap'` for best UX
3. Load fonts in root layout (`app/layout.tsx`), not page layouts
4. Use CSS variable approach (`variable: '--font-sans'`) for reliability
5. Declare in tailwind.config with system fallbacks

---

## Font Test Page

Use this to verify fonts are working correctly:

```jsx
export default function FontTestPage() {
  return (
    <div className="max-w-4xl mx-auto p-8 space-y-8">
      <section>
        <h1 className="text-4xl font-bold mb-4">Heading Font Test</h1>
        <p className="text-lg text-slate-600">
          Body text for visual comparison.
        </p>
      </section>

      <section>
        <h2 className="text-2xl font-semibold mb-4">Type Scale</h2>
        <div className="space-y-2">
          <p className="text-xs text-slate-500">Extra small - 12px</p>
          <p className="text-sm text-slate-600">Small - 14px</p>
          <p className="text-base text-slate-700">Base - 16px</p>
          <p className="text-lg text-slate-800">Large - 18px</p>
          <p className="text-xl text-slate-900">Extra Large - 20px</p>
        </div>
      </section>

      <section>
        <h2 className="text-2xl font-semibold mb-4">Monospace (Numeric Data)</h2>
        <p className="font-mono text-xl">$125.50</p>
        <p className="font-mono text-sm">ID: PRJ-2024-001</p>
      </section>

      <section>
        <h2 className="text-2xl font-semibold mb-4">Font Weights</h2>
        <p className="font-normal">Normal weight (400)</p>
        <p className="font-medium">Medium weight (500)</p>
        <p className="font-semibold">Semibold weight (600)</p>
        <p className="font-bold">Bold weight (700)</p>
      </section>
    </div>
  )
}
```
