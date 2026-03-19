# Overlays Reference

Modals, slide-overs, tooltips, dropdowns, popovers, alert dialogs, and z-index management.

---

## Z-Index Hierarchy

Establish a clear layering system:

```
z-0    Base / normal flow
z-10   Dropdowns, floating menus
z-20   Sticky headers, fixed navigation
z-40   Backdrop overlays (semi-transparent)
z-50   Modals, slide-overs (top of everything)
```

```jsx
<div className="sticky z-20">Header</div>
<div className="z-10">Dropdown</div>
<div className="z-40">Backdrop</div>
<div className="z-50">Modal content</div>
```

---

## Modal

```jsx
export function Modal({ isOpen, onClose, children, title }) {
  if (!isOpen) return null

  return (
    <>
      {/* Backdrop */}
      <div
        className="fixed inset-0 bg-black/50 backdrop-blur-sm z-40
          transition-opacity duration-200"
        onClick={onClose}
      />

      {/* Modal container */}
      <div className="fixed inset-0 flex items-center justify-center z-50 p-4">
        <div className="bg-white rounded-md shadow-2xl max-w-md w-full
          transition-all duration-200">

          {/* Header */}
          <div className="p-6 border-b border-slate-200">
            <h2 className="text-xl font-bold text-slate-900">{title}</h2>
          </div>

          {/* Body */}
          <div className="p-6">
            {children}
          </div>

          {/* Footer */}
          <div className="p-6 border-t border-slate-200 flex gap-2 justify-end">
            <button
              onClick={onClose}
              className="px-4 py-2 border border-slate-300 text-slate-700 font-medium rounded-md
                hover:bg-slate-50 transition-colors">
              Cancel
            </button>
            <button
              className="px-4 py-2 bg-cyan-600 text-white font-medium rounded-md
                hover:bg-cyan-700 transition-colors">
              Confirm
            </button>
          </div>
        </div>
      </div>
    </>
  )
}
```

Usage:
```jsx
<Modal isOpen={isOpen} onClose={() => setIsOpen(false)} title="Confirm Action">
  <p className="text-slate-600">Are you sure? This action cannot be undone.</p>
</Modal>
```

---

## Slide-Over Panel (Side Drawer)

```jsx
export function SlideOver({ isOpen, onClose, title, children }) {
  return (
    <>
      {/* Backdrop */}
      <div
        className={`fixed inset-0 bg-black/50 z-40 transition-opacity duration-200
          ${isOpen ? 'opacity-100' : 'opacity-0 poplusJakartaSans-events-none'}`}
        onClick={onClose}
      />

      {/* Panel from right */}
      <div className={`fixed right-0 top-0 h-screen w-full max-w-md bg-white shadow-xl z-50
        transition-transform duration-300 transform
        ${isOpen ? 'translate-x-0' : 'translate-x-full'}`}>

        {/* Header */}
        <div className="flex items-center justify-between p-6 border-b border-slate-200">
          <h2 className="text-xl font-bold text-slate-900">{title}</h2>
          <button
            onClick={onClose}
            className="p-2 text-slate-500 hover:bg-slate-100 rounded-md transition-colors">
            <XIcon className="w-5 h-5" />
          </button>
        </div>

        {/* Scrollable body */}
        <div className="overflow-y-auto h-[calc(100vh-64px)]">
          <div className="p-6">
            {children}
          </div>
        </div>
      </div>
    </>
  )
}
```

Usage:
```jsx
<SlideOver isOpen={isOpen} onClose={() => setIsOpen(false)} title="Details">
  {/* Content */}
</SlideOver>
```

---

## Tooltip

```jsx
export function Tooltip({ text, children }) {
  return (
    <div className="group relative inline-block">
      {children}

      <div className="absolute bottom-full left-1/2 -translate-x-1/2 mb-2 px-2 py-1
        bg-slate-900 text-white text-xs rounded-md whitespace-nowrap
        opacity-0 group-hover:opacity-100 poplusJakartaSans-events-none
        transition-opacity duration-200">
        {text}
      </div>
    </div>
  )
}
```

Usage:
```jsx
<Tooltip text="Delete this item">
  <button className="p-2 text-slate-600 hover:bg-slate-100 rounded-md">
    <TrashIcon className="w-5 h-5" />
  </button>
</Tooltip>
```

---

## Dropdown Menu

```jsx
export function Dropdown({ items, label }) {
  const [isOpen, setIsOpen] = useState(false)

  return (
    <div className="relative inline-block">
      {/* Trigger */}
      <button
        onClick={() => setIsOpen(!isOpen)}
        className="px-4 py-2 bg-white border border-slate-300 text-slate-900 font-medium rounded-md
          hover:bg-slate-50 focus:outline-none focus:ring-2 focus:ring-cyan-500">
        {label}
        <ChevronDownIcon className={`w-4 h-4 ml-2 inline transition-transform duration-200
          ${isOpen ? 'rotate-180' : ''}`} />
      </button>

      {/* Invisible click-away layer */}
      {isOpen && (
        <div className="fixed inset-0 z-40" onClick={() => setIsOpen(false)} />
      )}

      {/* Menu */}
      <div className={`absolute top-full left-0 mt-1 bg-white border border-slate-300
        rounded-md shadow-lg z-50
        transition-all duration-150 origin-top
        ${isOpen ? 'opacity-100 scale-y-100' : 'opacity-0 scale-y-95 poplusJakartaSans-events-none'}`}>

        {items.map(item => (
          <button
            key={item.id}
            onClick={() => {
              item.onClick()
              setIsOpen(false)
            }}
            className="w-full text-left px-4 py-2 text-slate-700 hover:bg-slate-100
              first:rounded-t-lg last:rounded-b-lg transition-colors">
            {item.label}
          </button>
        ))}
      </div>
    </div>
  )
}
```

Usage:
```jsx
<Dropdown
  label="Actions"
  items={[
    { id: 1, label: 'Edit', onClick: () => {} },
    { id: 2, label: 'Delete', onClick: () => {} },
  ]}
/>
```

---

## Popover (Non-modal)

```jsx
export function Popover({ trigger, children, placement = 'bottom' }) {
  const [isOpen, setIsOpen] = useState(false)
  const ref = useRef(null)

  useEffect(() => {
    function handleClickOutside(e) {
      if (ref.current && !ref.current.contains(e.target)) {
        setIsOpen(false)
      }
    }
    document.addEventListener('mousedown', handleClickOutside)
    return () => document.removeEventListener('mousedown', handleClickOutside)
  }, [])

  return (
    <div ref={ref} className="relative inline-block">
      <button
        onClick={() => setIsOpen(!isOpen)}
        className="text-cyan-600 hover:text-cyan-700">
        {trigger}
      </button>

      {isOpen && (
        <div className={`absolute z-50 bg-white border border-slate-200
          rounded-md shadow-lg p-4 transition-opacity duration-150
          ${placement === 'bottom' ? 'top-full mt-2' : 'bottom-full mb-2'}`}>
          {children}
        </div>
      )}
    </div>
  )
}
```

Usage:
```jsx
<Popover trigger="More info">
  <div className="text-sm text-slate-600">
    <p className="font-semibold mb-2">Details:</p>
    <ul className="list-disc list-inside space-y-1">
      <li>Item A</li>
      <li>Item B</li>
    </ul>
  </div>
</Popover>
```

---

## Alert Dialog (Critical Actions)

```jsx
export function AlertDialog({ title, description, isDangerous, onConfirm, onCancel }) {
  const [isOpen, setIsOpen] = useState(false)

  return (
    <>
      <button
        className={`px-4 py-2 font-medium rounded-md
          ${isDangerous
            ? 'bg-rose-600 text-white hover:bg-rose-700'
            : 'bg-cyan-600 text-white hover:bg-cyan-700'}`}
        onClick={() => setIsOpen(true)}>
        Action
      </button>

      {isOpen && (
        <>
          <div className="fixed inset-0 bg-black/50 z-40" />
          <div className="fixed inset-0 flex items-center justify-center z-50 p-4">
            <div className="bg-white rounded-md shadow-2xl max-w-sm w-full">

              {/* Icon */}
              <div className="p-6 flex justify-center">
                {isDangerous ? (
                  <AlertCircleIcon className="w-12 h-12 text-rose-600" />
                ) : (
                  <QuestionMarkCircleIcon className="w-12 h-12 text-cyan-600" />
                )}
              </div>

              {/* Message */}
              <div className="px-6 text-center">
                <h2 className="text-lg font-bold text-slate-900">{title}</h2>
                <p className="text-slate-600 mt-2">{description}</p>
              </div>

              {/* Actions */}
              <div className="p-6 flex gap-2 justify-end border-t border-slate-200">
                <button
                  onClick={() => setIsOpen(false)}
                  className="px-4 py-2 border border-slate-300 text-slate-700 font-medium rounded-md
                    hover:bg-slate-50 transition-colors">
                  Cancel
                </button>
                <button
                  onClick={() => { onConfirm(); setIsOpen(false) }}
                  className={`px-4 py-2 font-medium rounded-md text-white
                    ${isDangerous
                      ? 'bg-rose-600 hover:bg-rose-700'
                      : 'bg-cyan-600 hover:bg-cyan-700'
                    } transition-colors`}>
                  Confirm
                </button>
              </div>
            </div>
          </div>
        </>
      )}
    </>
  )
}
```

---

## Overlay Best Practices

### Backdrop

- Always use `bg-black/50` (50% opacity black) for backdrops
- Add `backdrop-blur-sm` for frosted glass effect on modals
- Backdrop should be clickable to dismiss (except alert dialogs)

### Animation

- Modals: fade in with optional scale (`opacity-0 scale-95` -> `opacity-100 scale-100`)
- Slide-overs: translate from edge (`translate-x-full` -> `translate-x-0`)
- Dropdowns: scale from origin (`scale-y-95` -> `scale-y-100` with `origin-top`)
- Tooltips: simple opacity transition

### Focus Management

- Trap focus inside modals (use `focus-trap` libraries or Radix UI Dialog)
- Return focus to trigger element on close
- First focusable element should receive focus on open

### Scroll Lock

- Lock body scroll when modal/slide-over is open:
```jsx
useEffect(() => {
  if (isOpen) {
    document.body.style.overflow = 'hidden'
  }
  return () => {
    document.body.style.overflow = ''
  }
}, [isOpen])
```

### Keyboard Handling

- `Escape` key should close overlays
- `Tab` should cycle through focusable elements within modal
- `Enter`/`Space` should activate buttons

```jsx
useEffect(() => {
  function handleKeyDown(e) {
    if (e.key === 'Escape') onClose()
  }
  document.addEventListener('keydown', handleKeyDown)
  return () => document.removeEventListener('keydown', handleKeyDown)
}, [onClose])
```
