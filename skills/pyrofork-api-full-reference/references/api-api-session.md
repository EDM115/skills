---
name: api-api-session
description: Offline API backup extracted from Pyrofork source docstrings.
---

# Pyrofork API Backup: `session`

Extracted from `sources/pyrofork/pyrogram/**.py` using AST parsing of module, class, function, and method docstrings.

## File: `session/__init__.py`

---

## File: `session/auth.py`

### Classes

#### `class Auth`

_No docstring._

##### Methods

###### `def __init__(self, client: 'pyrogram.Client', dc_id: int, test_mode: bool)`

_No docstring._

###### `def pack(data: TLObject) -> bytes`

_No docstring._

###### `def unpack(b: BytesIO)`

_No docstring._

###### `async def invoke(self, data: TLObject)`

_No docstring._

###### `async def create(self)`

```text
https://core.telegram.org/mtproto/auth_key
https://core.telegram.org/mtproto/samples-auth_key
```

---

## File: `session/internals/__init__.py`

---

## File: `session/internals/data_center.py`

### Classes

#### `class DataCenter`

_No docstring._

##### Methods

###### `def __new__(cls, dc_id: int, test_mode: bool, ipv6: bool, alt_port: bool, media: bool) -> Tuple[str, int]`

_No docstring._

---

## File: `session/internals/msg_factory.py`

### Classes

#### `class MsgFactory`

_No docstring._

##### Methods

###### `def __init__(self)`

_No docstring._

###### `def __call__(self, body: TLObject) -> Message`

_No docstring._

---

## File: `session/internals/msg_id.py`

### Classes

#### `class MsgId`

_No docstring._

##### Methods

###### `def __new__(cls) -> int`

_No docstring._

---

## File: `session/internals/seq_no.py`

### Classes

#### `class SeqNo`

_No docstring._

##### Methods

###### `def __init__(self)`

_No docstring._

###### `def __call__(self, is_content_related: bool) -> int`

_No docstring._

---

## File: `session/session.py`

### Classes

#### `class Result`

_No docstring._

##### Methods

###### `def __init__(self)`

_No docstring._

#### `class Session`

_No docstring._

##### Methods

###### `def __init__(self, client: 'pyrogram.Client', dc_id: int, auth_key: bytes, test_mode: bool, is_media: bool = False, is_cdn: bool = False)`

_No docstring._

###### `async def start(self)`

_No docstring._

###### `async def stop(self)`

_No docstring._

###### `async def restart(self)`

_No docstring._

###### `async def handle_packet(self, packet)`

_No docstring._

###### `async def ping_worker(self)`

_No docstring._

###### `async def recv_worker(self)`

_No docstring._

###### `async def send(self, data: TLObject, wait_response: bool = True, timeout: float = WAIT_TIMEOUT, retry: int = 0)`

_No docstring._

###### `def _handle_bad_notification(self)`

_No docstring._

###### `async def invoke(self, query: TLObject, retries: int = MAX_RETRIES, timeout: float = WAIT_TIMEOUT, sleep_threshold: float = SLEEP_THRESHOLD)`

_No docstring._

---
