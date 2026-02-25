# Updates, Handlers, Filters, Plugins

## Update handling model

- Telegram events are dispatched through handlers.
- Register handlers via:
  - decorators (`@app.on_message(...)`) for static, clean code
  - `add_handler(...)` for dynamic/runtime registration

## Common handler/decorator families

- Message / edited / deleted
- Callback query / inline query / chosen inline result
- Shipping / pre-checkout
- Chat member and join request
- User status, story, poll
- Raw update and error handlers
- Business-related handlers

## Filters

### Built-in usage

- Single filters: `filters.private`, `filters.text`, `filters.photo`, etc.
- Composed filters:
  - invert: `~flt`
  - and: `flt1 & flt2`
  - or: `flt1 | flt2`
- Parametric filters:
  - `filters.command(["start", "help"])`
  - `filters.regex("pattern")`

### Custom filters

- Build with `filters.create(func, **kwargs)`
- Callback signature receives `(filter_obj, client, update)`
- Dynamic filters pass custom data via kwargs and read it from `filter_obj`

## Propagation and groups

### Group priority

- Lower numeric group executes first.
- Default group is `0`.
- Use groups to process same update through multiple handlers.

### Stop propagation

- Preferred: `update.stop_propagation()`
- Alternative: `raise StopPropagation`

### Continue propagation within same group

- Preferred: `update.continue_propagation()`
- Alternative: `raise ContinuePropagation`

## Runtime handler mutation caveat

Calling `.stop()`, `.restart()`, `.add_handler()`, or `.remove_handler()` from inside a running handler can deadlock.
Use non-blocking mode where supported (`block=False`) so call returns immediately.

## Smart Plugins system

### Why use it

- Auto-discovers decorated handlers from plugin modules.
- Scales better for larger projects than manual imports/registrations.

### Base config

- Pass `plugins=dict(root="plugins")` to `Client(...)`.
- Decorate plugin functions with `@Client.on_message(...)` (class-level decorators).

### Include/exclude controls

- `include=["subfolder.module", ...]` loads only listed modules in listed order.
- `exclude=["subfolder.module", ...]` drops selected modules.
- Handler function order can be overridden inside include spec (`"module fn2 fn1"`).

### Runtime plugin load/unload

- Decorated functions expose `.handlers` list of `(handler, group)` tuples.
- Unload with `remove_handler(*entry)`.
- Reload with `add_handler(*entry)`.
