---
name: best-practices-errors-sessions-performance
description: Reliable operation patterns for RPC errors, FloodWait retries, session storage choices, and runtime performance tuning.
---

# Reliability: Errors, Sessions, and Performance

Production bots need predictable retry behavior, stable storage, and efficient runtime settings.

## Usage

Flood wait handling:

```python
import asyncio
from pyrogram.errors import FloodWait

try:
    await app.send_message("me", "burst")
except FloodWait as e:
    await asyncio.sleep(e.value)
```

Session strategy:

```python
# Durable local storage (default)
Client("my_account")

# Ephemeral runtime session
Client("my_account", in_memory=True)

# External persistence
Client("my_account", mongodb={"connection": conn, "remove_peers": False})
```

## Key Points

- Catch specific RPC errors (like `FloodWait`) and apply targeted retry logic.
- Use separate session names for parallel clients to avoid SQLite lock collisions.
- For high throughput, install `tgcrypto-pyrofork`; optionally pair with `uvloop`.
- In sync mode, avoid blocking operations inside handlers.

<!--
Source references:
- https://github.com/Mayuri-Chan/pyrofork/blob/main/docs/source/start/errors.rst
- https://github.com/Mayuri-Chan/pyrofork/blob/main/docs/source/faq/how-to-avoid-flood-waits.rst
- https://github.com/Mayuri-Chan/pyrofork/blob/main/docs/source/topics/storage-engines.rst
- https://github.com/Mayuri-Chan/pyrofork/blob/main/docs/source/topics/speedups.rst
- https://github.com/Mayuri-Chan/pyrofork/blob/main/docs/source/topics/synchronous.rst
- https://github.com/Mayuri-Chan/pyrofork/blob/main/docs/source/faq/sqlite3-operationalerror-database-is-locked.rst
-->
