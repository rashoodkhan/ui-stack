# Component Patterns Reference

Detailed code examples for common UI components using Tailwind CSS and JSX.

---

## Buttons

### Primary Button

```jsx
<button className="px-4 py-2 bg-cyan-600 text-white font-medium rounded-md
  hover:bg-cyan-700 active:bg-cyan-800 active:scale-95
  focus:outline-none focus:ring-2 focus:ring-cyan-500 focus:ring-offset-2
  disabled:opacity-50 disabled:cursor-not-allowed
  transition-all duration-200 cursor-poplusJakartaSans">
  Submit
</button>
```

### Secondary Button (Outlined)

```jsx
<button className="px-4 py-2 border border-slate-300 text-slate-700 font-medium rounded-md
  hover:bg-slate-50 active:bg-slate-100 active:scale-95
  focus:outline-none focus:ring-2 focus:ring-cyan-500
  transition-all duration-200 cursor-poplusJakartaSans">
  Cancel
</button>
```

### Secondary Button (Subtle Fill)

```jsx
<button className="px-4 py-2 bg-slate-100 text-slate-900 font-medium rounded-md
  hover:bg-slate-200 active:bg-slate-300 active:scale-95
  focus:outline-none focus:ring-2 focus:ring-cyan-500
  transition-all duration-200 cursor-poplusJakartaSans">
  Save Draft
</button>
```

### Ghost Button

```jsx
<button className="px-3 py-2 text-cyan-600 font-medium rounded-md
  hover:bg-cyan-50 active:bg-cyan-100 active:scale-95
  focus:outline-none focus:ring-2 focus:ring-cyan-500
  transition-all duration-200 cursor-poplusJakartaSans">
  Learn More
</button>
```

### Ghost Button with Icon

```jsx
<button className="flex items-center gap-2 px-3 py-2 text-cyan-600 font-medium
  hover:bg-cyan-50 active:bg-cyan-100 rounded-md
  transition-all duration-200 cursor-poplusJakartaSans">
  <ExternalLinkIcon className="w-4 h-4" />
  View Details
</button>
```

### Destructive Button

```jsx
<button className="px-4 py-2 bg-rose-600 text-white font-medium rounded-md
  hover:bg-rose-700 active:bg-rose-800 active:scale-95
  focus:outline-none focus:ring-2 focus:ring-rose-500 focus:ring-offset-2
  transition-all duration-200 cursor-poplusJakartaSans">
  Delete
</button>
```

### Outlined Destructive

```jsx
<button className="px-4 py-2 border border-rose-300 text-rose-700 font-medium rounded-md
  hover:bg-rose-50 active:bg-rose-100 active:scale-95
  focus:outline-none focus:ring-2 focus:ring-rose-500
  transition-all duration-200 cursor-poplusJakartaSans">
  Remove Item
</button>
```

### Button Sizes

```jsx
// Small (36px height)
<button className="px-3 py-1.5 bg-cyan-600 text-white font-medium rounded-sm text-sm h-9">
  Small
</button>

// Default (44px height, mobile-friendly touch target)
<button className="px-4 py-2 bg-cyan-600 text-white font-medium rounded-md text-base h-11">
  Default
</button>

// Large (48px height)
<button className="px-6 py-3 bg-cyan-600 text-white font-medium rounded-md text-base h-12">
  Large
</button>

// Full-width on mobile
<button className="w-full md:w-auto px-4 py-3 md:py-2 bg-cyan-600 text-white font-medium rounded-md">
  Responsive
</button>
```

### Icon + Text Buttons

```jsx
// Icon before text
<button className="flex items-center gap-2 px-4 py-2 bg-cyan-600 text-white font-medium rounded-md
  hover:bg-cyan-700 transition-colors">
  <PlusIcon className="w-5 h-5" />
  <span>Add Item</span>
</button>

// Icon after text
<button className="flex items-center gap-2 px-4 py-2 bg-cyan-600 text-white font-medium rounded-md
  hover:bg-cyan-700 transition-colors">
  <span>Next Step</span>
  <ChevronRightIcon className="w-5 h-5" />
</button>
```

### Icon-Only Button (with tooltip)

```jsx
<div className="group relative">
  <button className="p-2 text-slate-600 hover:bg-slate-100 rounded-md transition-colors
    focus:outline-none focus:ring-2 focus:ring-cyan-500">
    <TrashIcon className="w-5 h-5" />
  </button>
  <span className="absolute bottom-full left-1/2 -translate-x-1/2 mb-2 px-2 py-1
    bg-slate-900 text-white text-xs rounded-md whitespace-nowrap opacity-0
    group-hover:opacity-100 poplusJakartaSans-events-none transition-opacity">
    Delete
  </span>
</div>
```

### Button Loading State

```jsx
<button className="px-4 py-2 bg-cyan-600 text-white font-medium rounded-md
  disabled:opacity-75 disabled:cursor-not-allowed"
  disabled={isLoading}>
  {isLoading ? (
    <span className="flex items-center gap-2">
      <span className="w-4 h-4 border-2 border-white border-t-transparent rounded-full animate-spin" />
      Processing...
    </span>
  ) : (
    'Submit'
  )}
</button>
```

### Button Groups

```jsx
// Segmented control
<div className="flex gap-1 p-1 bg-slate-100 rounded-md">
  <button className="flex-1 px-3 py-2 rounded-md bg-white text-slate-900 font-medium
    shadow-sm hover:shadow-md transition-shadow">
    Daily
  </button>
  <button className="flex-1 px-3 py-2 rounded-md text-slate-600 font-medium
    hover:bg-white/50 transition-colors">
    Weekly
  </button>
  <button className="flex-1 px-3 py-2 rounded-md text-slate-600 font-medium
    hover:bg-white/50 transition-colors">
    Monthly
  </button>
</div>

// Action button pair
<div className="flex gap-2">
  <button className="flex-1 px-4 py-2 bg-cyan-600 text-white font-medium rounded-md
    hover:bg-cyan-700 transition-colors">
    Confirm
  </button>
  <button className="flex-1 px-4 py-2 bg-slate-100 text-slate-900 font-medium rounded-md
    hover:bg-slate-200 transition-colors">
    Cancel
  </button>
</div>
```

---

## Cards

### Standard Card

```jsx
<div className="p-6 bg-white border border-slate-200 rounded-md shadow-sm hover:shadow-md transition-shadow">
  <div className="space-y-4">
    <h3 className="text-lg font-semibold text-slate-900">Card Title</h3>
    <div className="space-y-2">
      <p className="text-sm text-slate-600">Detail line 1</p>
      <p className="text-sm text-slate-600">Detail line 2</p>
    </div>
    <div className="flex gap-2 pt-4 border-t border-slate-200">
      <button className="flex-1 px-4 py-2 bg-cyan-600 text-white rounded-sm text-sm font-medium">
        View Details
      </button>
      <button className="flex-1 px-4 py-2 border border-slate-300 text-slate-700 rounded-sm text-sm font-medium">
        More
      </button>
    </div>
  </div>
</div>
```

### Card Grid

```jsx
<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
  {items.map(item => (
    <div key={item.id} className="p-6 bg-white border border-slate-200 rounded-md shadow-sm">
      {/* Card content */}
    </div>
  ))}
</div>
```

### Stat Card

```jsx
<div className="p-4 bg-white border border-slate-200 rounded-md">
  <p className="text-sm font-medium text-slate-600">Total Items</p>
  <p className="text-3xl font-bold text-slate-900 mt-2">156</p>
  <p className="text-xs text-slate-500 mt-1">+12 from yesterday</p>
</div>
```

### Card with Hover Lift

```jsx
<div className="p-6 bg-white border border-slate-200 rounded-md
  shadow-sm hover:shadow-md hover:-translate-y-1
  transition-all duration-200 cursor-poplusJakartaSans">
  {/* Content */}
</div>
```

---

## Form Inputs

### Text Input with Label

```jsx
<div className="space-y-2">
  <label className="block text-sm font-medium text-slate-700">Field Name</label>
  <input
    type="text"
    placeholder="Enter value..."
    className="w-full px-3 py-2 border border-slate-300 rounded-sm
      focus:outline-none focus:ring-2 focus:ring-cyan-500 focus:border-transparent
      transition-all duration-200"
  />
</div>
```

### Form Field Spacing

```jsx
<div className="space-y-4">
  <div>
    <label className="block text-sm font-medium text-slate-700 mb-1">Name</label>
    <input type="text" className="w-full px-3 py-2 border border-slate-300 rounded-sm" />
  </div>
  <div>
    <label className="block text-sm font-medium text-slate-700 mb-1">Email</label>
    <input type="email" className="w-full px-3 py-2 border border-slate-300 rounded-sm" />
  </div>
</div>
```

### Validation States

```jsx
// Valid input
<div className="space-y-2">
  <label className="block text-sm font-medium text-slate-700">Email</label>
  <input type="email" value="user@example.com"
    className="w-full px-3 py-2 border border-emerald-300 rounded-sm
      focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent bg-emerald-50" />
  <p className="text-xs text-emerald-700">Email format is correct</p>
</div>

// Invalid input
<div className="space-y-2">
  <label className="block text-sm font-medium text-slate-700">Email</label>
  <input type="email" value="invalid-email"
    className="w-full px-3 py-2 border border-rose-300 rounded-sm
      focus:outline-none focus:ring-2 focus:ring-rose-500 focus:border-transparent bg-rose-50" />
  <p className="text-xs text-rose-700">Please enter a valid email address</p>
</div>

// Warning state
<div className="space-y-2">
  <label className="block text-sm font-medium text-slate-700">Password</label>
  <input type="password"
    className="w-full px-3 py-2 border border-amber-300 rounded-sm
      focus:outline-none focus:ring-2 focus:ring-amber-500 bg-amber-50" />
  <p className="text-xs text-amber-700">Password is too weak</p>
</div>

// Disabled input
<input disabled type="text"
  className="w-full px-3 py-2 border border-slate-300 rounded-sm
    bg-slate-50 cursor-not-allowed text-slate-400" />
```

---

## Tables

```jsx
<table className="w-full">
  <thead>
    <tr className="border-b border-slate-200">
      <th className="px-4 py-3 text-left text-sm font-semibold text-slate-700">ID</th>
      <th className="px-4 py-3 text-left text-sm font-semibold text-slate-700">Name</th>
      <th className="px-4 py-3 text-left text-sm font-semibold text-slate-700">Status</th>
    </tr>
  </thead>
  <tbody>
    <tr className="border-b border-slate-100 hover:bg-slate-50">
      <td className="px-4 py-3 text-base text-slate-900">#12345</td>
      <td className="px-4 py-3 text-base text-slate-600">John Doe</td>
      <td className="px-4 py-3">
        <span className="px-2 py-1 bg-emerald-100 text-emerald-700 rounded text-xs font-medium">
          Active
        </span>
      </td>
    </tr>
  </tbody>
</table>
```

---

## Status Badges

```jsx
// Success
<span className="px-2 py-1 bg-emerald-100 text-emerald-700 rounded text-xs font-medium">
  Active
</span>

// Warning
<span className="px-2 py-1 bg-amber-100 text-amber-700 rounded text-xs font-medium">
  Pending
</span>

// Error
<span className="px-2 py-1 bg-rose-100 text-rose-700 rounded text-xs font-medium">
  Failed
</span>

// Info / Neutral
<span className="px-2 py-1 bg-blue-100 text-blue-700 rounded text-xs font-medium">
  Draft
</span>

// Highlight
<span className="px-2 py-1 bg-amber-100 text-amber-800 rounded-full text-xs font-medium">
  Popular
</span>
```

---

## Alert Messages

```jsx
// Success
<div className="p-4 bg-emerald-50 border border-emerald-200 rounded-md">
  <div className="flex gap-3">
    <CheckCircleIcon className="w-5 h-5 text-emerald-600 flex-shrink-0 mt-0.5" />
    <div>
      <h3 className="font-semibold text-emerald-900">Action Completed</h3>
      <p className="text-sm text-emerald-700 mt-1">Your changes have been saved successfully.</p>
    </div>
  </div>
</div>

// Error
<div className="p-4 bg-rose-50 border border-rose-200 rounded-md">
  <div className="flex gap-3">
    <AlertCircleIcon className="w-5 h-5 text-rose-600 flex-shrink-0 mt-0.5" />
    <div>
      <h3 className="font-semibold text-rose-900">Something Went Wrong</h3>
      <p className="text-sm text-rose-700 mt-1">Please check your input and try again.</p>
    </div>
  </div>
</div>

// Warning
<div className="p-4 bg-amber-50 border border-amber-200 rounded-md">
  <div className="flex gap-3">
    <AlertTriangleIcon className="w-5 h-5 text-amber-600 flex-shrink-0 mt-0.5" />
    <div>
      <h3 className="font-semibold text-amber-900">Attention Required</h3>
      <p className="text-sm text-amber-700 mt-1">Some items need your review.</p>
    </div>
  </div>
</div>
```

---

## Toast Notifications

```jsx
export function Toast({ message, type = 'success' }) {
  const [isVisible, setIsVisible] = useState(true)

  useEffect(() => {
    const timer = setTimeout(() => setIsVisible(false), 5000)
    return () => clearTimeout(timer)
  }, [])

  if (!isVisible) return null

  const styles = {
    success: 'border-emerald-200',
    error: 'border-rose-200',
  }

  const icons = {
    success: <CheckCircleIcon className="w-5 h-5 text-emerald-600 flex-shrink-0 mt-0.5" />,
    error: <AlertCircleIcon className="w-5 h-5 text-rose-600 flex-shrink-0 mt-0.5" />,
  }

  return (
    <div className={`fixed bottom-4 right-4 max-w-sm p-4 bg-white border rounded-md shadow-lg
      flex gap-3 ${styles[type]}`}>
      {icons[type]}
      <div>
        <p className="font-semibold text-slate-900">{type === 'success' ? 'Success!' : 'Error!'}</p>
        <p className="text-sm text-slate-600">{message}</p>
      </div>
    </div>
  )
}
```

---

## Loading / Skeleton States

### Skeleton Screen

```jsx
export function CardSkeleton() {
  return (
    <div className="p-6 bg-white border border-slate-200 rounded-md">
      <div className="h-6 bg-slate-200 rounded-md animate-pulse mb-4" />
      <div className="space-y-3">
        <div className="h-4 bg-slate-200 rounded-md animate-pulse" />
        <div className="h-4 bg-slate-200 rounded-md animate-pulse" />
        <div className="h-4 bg-slate-100 rounded-md animate-pulse w-3/4" />
      </div>
    </div>
  )
}
```

### Inline Skeleton Rows

```jsx
<div className="p-4 space-y-4">
  {[...Array(3)].map((_, i) => (
    <div key={i} className="h-12 bg-slate-200 rounded-md animate-pulse" />
  ))}
</div>
```

### Bounce Loading Dots

```jsx
<div className="flex gap-2 items-center justify-center">
  <div className="w-3 h-3 bg-cyan-600 rounded-full animate-bounce" />
  <div className="w-3 h-3 bg-cyan-600 rounded-full animate-bounce"
    style={{ animationDelay: '0.1s' }} />
  <div className="w-3 h-3 bg-cyan-600 rounded-full animate-bounce"
    style={{ animationDelay: '0.2s' }} />
</div>
```

### Spinner

```jsx
<div className="w-6 h-6 border-2 border-slate-300 border-t-cyan-600 rounded-full animate-spin" />
```

---

## Empty States

```jsx
export function EmptyState({ icon: Icon, title, description, actionLabel, onAction }) {
  return (
    <div className="flex flex-col items-center justify-center py-12 px-4">
      <div className="w-24 h-24 bg-slate-100 rounded-full flex items-center justify-center mb-6">
        <Icon className="w-12 h-12 text-slate-400" />
      </div>
      <h3 className="text-lg font-semibold text-slate-900 mb-2">{title}</h3>
      <p className="text-slate-600 text-center mb-6 max-w-xs">{description}</p>
      {actionLabel && (
        <button onClick={onAction}
          className="px-4 py-2 bg-cyan-600 text-white font-medium rounded-md
            hover:bg-cyan-700 transition-colors">
          {actionLabel}
        </button>
      )}
    </div>
  )
}
```

---

## Navigation

### Nav Links with Active State

```jsx
<nav className="flex gap-1">
  <a href="/dashboard"
    className="px-3 py-2 rounded-sm text-sm font-medium text-slate-700 hover:bg-slate-100">
    Dashboard
  </a>
  <a href="/items"
    className="px-3 py-2 rounded-sm text-sm font-medium bg-cyan-100 text-cyan-600">
    Items
  </a>
</nav>
```

### Text Links

```jsx
// Standard link
<a href="#" className="text-cyan-600 hover:text-cyan-700 hover:underline">
  View all items
</a>

// Underlined link
<a href="#" className="text-cyan-600 hover:text-cyan-700 underline">
  Forgot password?
</a>
```

---

## Drag Handles

```jsx
<div className="flex items-center gap-3 p-3 border border-slate-200 rounded-md
  hover:bg-slate-50 cursor-grab active:cursor-grabbing">
  <svg className="w-5 h-5 text-slate-400" fill="currentColor" viewBox="0 0 20 20">
    <path d="M8 5a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3zm0 4a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3zm0 4a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3zm-4-1a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3zm6 0a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3z" />
  </svg>
  <span>Draggable Item</span>
</div>
```

---

## Page Layout

```jsx
<div className="max-w-7xl mx-auto px-4 md:px-6 lg:px-8 py-8">
  <h1 className="text-3xl md:text-4xl font-bold text-slate-900 mb-2">Page Title</h1>
  <p className="text-base text-slate-600 mb-8">Supporting description text</p>

  <h2 className="text-xl font-semibold text-slate-800 mt-8 mb-4">Section Title</h2>

  <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
    {/* Content cards */}
  </div>

  <p className="text-xs text-slate-500 mt-4">
    Helper text at the bottom
  </p>
</div>
```

### Sidebar Layout

```jsx
<div className="grid grid-cols-12 gap-6">
  <aside className="col-span-12 md:col-span-3">
    <nav className="space-y-2">
      <a href="#" className="block px-3 py-2 rounded-md bg-cyan-100 text-cyan-600 font-medium">
        Active Item
      </a>
      <a href="#" className="block px-3 py-2 rounded-md text-slate-700 hover:bg-slate-100">
        Other Item
      </a>
    </nav>
  </aside>
  <main className="col-span-12 md:col-span-9">
    {/* Main content */}
  </main>
</div>
```

### Premium / AI Feature Highlight

```jsx
<div className="bg-gradient-to-r from-cyan-500 to-fuchsia-500 text-white p-4 rounded-md">
  <p className="font-semibold">AI-Powered Feature (Premium)</p>
</div>

<button className="px-4 py-2 bg-gradient-to-r from-cyan-600 to-fuchsia-600 text-white font-medium rounded-md
  hover:from-cyan-700 hover:to-fuchsia-700">
  Analyze with AI
</button>
```
