---
name: advanced-raw-api-peer-resolution
description: Using raw Telegram functions/types with Client.invoke and resolving peers safely for low-level operations.
---

# Raw API and Peer Resolution

Use the raw Telegram API when high-level convenience methods are missing or not expressive enough.

## Usage

Invoke a raw function:

```python
from pyrogram import Client
from pyrogram.raw import functions

async with Client("my_account") as app:
    await app.invoke(
        functions.account.UpdateProfile(
            first_name="First",
            last_name="Last",
            about="Updated via raw API"
        )
    )
```

Resolve peers for raw methods that require `InputPeer*`:

```python
from pyrogram import Client
from pyrogram.raw import functions

async with Client("my_account") as app:
    peer = await app.resolve_peer("username")
    result = await app.invoke(functions.channels.GetFullChannel(channel=peer))
    print(result)
```

## Key Points

- `Client.invoke()` is the gateway for raw function calls.
- Raw methods usually require explicit function/type class construction.
- For peer-dependent calls, resolve entities with `await client.resolve_peer(...)`.
- High-level signed IDs (`-100...`, `-...`, `+...`) and raw IDs are not interchangeable.

<!--
Source references:
- https://github.com/Mayuri-Chan/pyrofork/blob/main/docs/source/topics/advanced-usage.rst
- https://github.com/Mayuri-Chan/pyrofork/blob/main/docs/source/telegram/functions/index.rst
- https://github.com/Mayuri-Chan/pyrofork/blob/main/docs/source/telegram/types/index.rst
-->
