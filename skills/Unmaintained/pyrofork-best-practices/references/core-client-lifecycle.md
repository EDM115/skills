---
name: core-client-lifecycle
description: Client startup/shutdown patterns for invoking Pyrofork methods safely in async and sync contexts.
---

# Client Lifecycle and Method Invocation

Use the client lifecycle pattern to avoid leaked sessions and half-open connections.

## Usage

```python
from pyrogram import Client

app = Client("my_account")


async def main():
    async with app:
        await app.send_message("me", "Hi from Pyrofork")


app.run(main())
```

Alternative with explicit lifecycle calls:

```python
async def main():
    await app.start()
    await app.send_message("me", "Hi")
    await app.stop()
```

## Key Points

- Prefer `async with app` for automatic `start()` / `stop()` and cleaner exception behavior.
- Use `app.run(main())` to schedule your coroutine in the client-managed event loop path.
- For small scripts, sync mode (`with app:`) is possible, but async mode is the primary design path.

<!--
Source references:
- https://github.com/Mayuri-Chan/pyrofork/blob/main/docs/source/start/invoking.rst
- https://github.com/Mayuri-Chan/pyrofork/blob/main/docs/source/topics/synchronous.rst
-->
