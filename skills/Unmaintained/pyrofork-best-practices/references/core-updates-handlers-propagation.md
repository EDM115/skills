---
name: core-updates-handlers-propagation
description: Registering handlers and controlling update flow with groups, stop propagation, and continue propagation.
---

# Updates, Handlers, and Propagation

Handlers process Telegram updates (messages, callbacks, member changes, raw updates, and more).

## Usage

Decorator registration:

```python
@app.on_message()
async def my_handler(client, message):
    await message.forward("me")
```

Programmatic registration:

```python
from pyrogram.handlers import MessageHandler

async def my_handler(client, message):
    await message.forward("me")

app.add_handler(MessageHandler(my_handler))
```

Group priority + propagation control:

```python
@app.on_message(filters.private)
async def first(_, message):
    print("A")
    message.continue_propagation()

@app.on_message(filters.private)
async def second(_, message):
    print("B")
```

## Key Points

- Lower group number means higher priority (e.g. `-1` runs before `0`).
- Conflicting handlers in the same group: first match wins unless you continue propagation.
- Use `message.stop_propagation()` to halt downstream handlers.
- Unhandled exceptions in one group do not stop dispatching to later groups.

<!--
Source references:
- https://github.com/Mayuri-Chan/pyrofork/blob/main/docs/source/start/updates.rst
- https://github.com/Mayuri-Chan/pyrofork/blob/main/docs/source/api/handlers.rst
- https://github.com/Mayuri-Chan/pyrofork/blob/main/docs/source/api/decorators.rst
- https://github.com/Mayuri-Chan/pyrofork/blob/main/docs/source/topics/more-on-updates.rst
-->
