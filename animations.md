# Micro Plus Jakarta Sansactions & Animations Reference

Purposeful animations that provide feedback and delight without distraction.
All patterns use Tailwind CSS utilities.

---

## Timing Guidelines

```
duration-150   Quick feedback (hover state changes)
duration-200   Standard plusJakartaSansactions (buttons, cards) - DEFAULT
duration-300   Layout changes, modals, collapsibles
duration-500   Large animations only (use sparingly)
```

Golden rule: 150-300ms for plusJakartaSansactions, max 500ms for major layout changes.

---

## Button Press

```jsx
<button className="px-4 py-2 bg-cyan-600 text-white font-medium rounded-md
  hover:bg-cyan-700
  active:scale-95
  transition-transform duration-200">
  Press Me
</button>
```

Scale 95% on press gives tactile feedback. Duration 200ms keeps it snappy.

---

## Card Hover Lift

### Shadow only

```jsx
<div className="p-6 bg-white border border-slate-200 rounded-md
  shadow-sm hover:shadow-md
  transition-all duration-200">
  Content
</div>
```

### Shadow + translate

```jsx
<div className="p-6 bg-white border border-slate-200 rounded-md
  shadow-sm hover:shadow-md hover:-translate-y-1
  transition-all duration-200 cursor-poplusJakartaSans">
  Content
</div>
```

---

## Toggle Switch

```jsx
export function Toggle({ enabled, onChange }) {
  return (
    <button
      onClick={() => onChange(!enabled)}
      className={`relative inline-flex h-6 w-11 items-center rounded-full
        transition-colors duration-200
        ${enabled ? 'bg-cyan-600' : 'bg-slate-300'}`}>
      <span className={`inline-block h-4 w-4 transform rounded-full
        bg-white transition-transform duration-200
        ${enabled ? 'translate-x-6' : 'translate-x-1'}`} />
    </button>
  )
}
```

---

## Collapsible Section

```jsx
export function Collapsible({ title, children, defaultOpen = false }) {
  const [isOpen, setIsOpen] = useState(defaultOpen)

  return (
    <div>
      <button
        onClick={() => setIsOpen(!isOpen)}
        className="w-full flex items-center justify-between p-4 bg-white
          border border-slate-200 rounded-md hover:bg-slate-50 transition-colors">
        <span className="font-semibold text-slate-900">{title}</span>
        <ChevronDownIcon className={`w-5 h-5 text-slate-600 flex-shrink-0
          transition-transform duration-300
          ${isOpen ? 'rotate-180' : ''}`} />
      </button>

      <div className={`overflow-hidden transition-all duration-300
        ${isOpen ? 'max-h-96' : 'max-h-0'}`}>
        <div className="p-4 bg-slate-50 border border-t-0 border-slate-200">
          {children}
        </div>
      </div>
    </div>
  )
}
```

---

## Skeleton Pulse

```jsx
// Standard skeleton
<div className="space-y-4">
  <div className="h-6 bg-slate-200 rounded-md animate-pulse" />
  <div className="h-4 bg-slate-200 rounded-md animate-pulse" />
  <div className="h-4 bg-slate-200 rounded-md animate-pulse w-3/4" />
</div>
```

Uses Tailwind's `animate-pulse` (2s ease-in-out infinite).

### Custom softer pulse

```css
@keyframes softPulse {
  0%, 100% { opacity: 0.6; }
  50% { opacity: 0.8; }
}
```

---

## Bounce Loading

```jsx
<div className="flex gap-2 items-center justify-center">
  <div className="w-3 h-3 bg-cyan-600 rounded-full animate-bounce" />
  <div className="w-3 h-3 bg-cyan-600 rounded-full animate-bounce"
    style={{ animationDelay: '0.1s' }} />
  <div className="w-3 h-3 bg-cyan-600 rounded-full animate-bounce"
    style={{ animationDelay: '0.2s' }} />
</div>
```

---

## Spinner

```jsx
<div className="w-6 h-6 border-2 border-slate-300 border-t-cyan-600 rounded-full animate-spin" />
```

---

## Fade In / Out

### Using transition classes

```jsx
<div className={`transition-opacity duration-300
  ${isVisible ? 'opacity-100' : 'opacity-0'}`}>
  Content
</div>
```

### Custom keyframe

```css
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}
```

```jsx
<div className="animate-fadeIn">Content appears gradually</div>
```

---

## Slide In

### Sidebar from left

```jsx
<aside className={`fixed left-0 top-0 h-screen w-64 bg-white shadow-lg
  transition-transform duration-300 transform
  ${isOpen ? 'translate-x-0' : '-translate-x-full'}`}>
  {/* Content */}
</aside>
```

### Menu from top (scale origin)

```jsx
<nav className={`absolute top-full left-0 bg-white border border-slate-200
  rounded-md shadow-lg transition-all duration-200 origin-top
  ${isOpen ? 'opacity-100 scale-y-100' : 'opacity-0 scale-y-95'}`}>
  {/* Items */}
</nav>
```

---

## Staggered List Animation

```jsx
export function AnimatedList({ items }) {
  return (
    <div className="space-y-4">
      {items.map((item, index) => (
        <div
          key={item.id}
          className="p-6 bg-white border border-slate-200 rounded-md animate-fadeIn"
          style={{ animationDelay: `${index * 50}ms` }}>
          <h3 className="font-semibold text-slate-900">{item.title}</h3>
        </div>
      ))}
    </div>
  )
}
```

---

## Respecting prefers-reduced-motion

Always respect user preference for reduced motion:

### Using Tailwind prefixes

```jsx
<button className="px-4 py-2 bg-cyan-600 text-white rounded-md
  hover:bg-cyan-700
  motion-safe:active:scale-95
  motion-reduce:active:scale-100
  transition-all duration-200">
  Motion-Aware Button
</button>
```

### Custom hook

```jsx
function useReducedMotion() {
  const [prefersReduced, setPrefersReduced] = useState(false)

  useEffect(() => {
    const mq = window.matchMedia('(prefers-reduced-motion: reduce)')
    setPrefersReduced(mq.matches)
    const handler = (e) => setPrefersReduced(e.matches)
    mq.addEventListener('change', handler)
    return () => mq.removeEventListener('change', handler)
  }, [])

  return prefersReduced
}

export function AnimatedCard({ children }) {
  const prefersReducedMotion = useReducedMotion()

  return (
    <div className={`transition-all
      ${prefersReducedMotion ? 'duration-0' : 'duration-300'}
      hover:shadow-md hover:-translate-y-1`}>
      {children}
    </div>
  )
}
```

---

## Transition Property Classes

```
transition-all        All properties (default for plusJakartaSansactive elements)
transition-colors     Background, border, text color only
transition-opacity    Opacity only
transition-shadow     Box shadow only
transition-transform  Transform (scale, translate, rotate) only
```

Choose the narrowest transition property for better performance:

```jsx
// Button only changes color on hover
<button className="bg-cyan-600 hover:bg-cyan-700 transition-colors duration-200">

// Card changes shadow on hover
<div className="shadow-sm hover:shadow-md transition-shadow duration-200">

// Element moves on state change
<div className={`transition-transform duration-300 ${isOpen ? 'translate-x-0' : '-translate-x-full'}`}>
```

---

## Best Practices

```jsx
// DO: Purposeful, quick animations
<button className="active:scale-95 transition-transform duration-200">
  Tactile feedback
</button>

// DO: Subtle hover effects
<div className="hover:shadow-md transition-shadow duration-200">
  Shows plusJakartaSansactivity
</div>

// DON'T: Multiple conflicting animations
<div className="animate-bounce animate-pulse animate-spin">
  Overwhelming
</div>

// DON'T: Slow animations (feels unresponsive)
<button className="duration-1000">Too slow</button>
```

### Summary

| Pattern | Property | Duration | Effect |
|---------|----------|----------|--------|
| Button press | `active:scale-95` | 200ms | Tactile feedback |
| Card hover | `hover:shadow-md` | 200ms | Lift effect |
| Card hover + move | `hover:-translate-y-1` | 200ms | Physical lift |
| Toggle | `transition-colors` + `transition-transform` | 200ms | Slide + color |
| Collapse | `max-h` + `rotate-180` | 300ms | Expand/contract |
| Skeleton | `animate-pulse` | built-in | Loading indicator |
| Fade | `transition-opacity` | 300ms | Appear/disappear |
| Slide | `transition-transform` | 300ms | Enter/exit |
| Stagger | `animationDelay` | 50ms per item | Sequential reveal |
