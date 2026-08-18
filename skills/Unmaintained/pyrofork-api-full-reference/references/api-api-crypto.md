---
name: api-api-crypto
description: Offline API backup extracted from Pyrofork source docstrings.
---

# Pyrofork API Backup: `crypto`

Extracted from `sources/pyrofork/pyrogram/**.py` using AST parsing of module, class, function, and method docstrings.

## File: `crypto/__init__.py`

---

## File: `crypto/aes.py`

---

## File: `crypto/mtproto.py`

### Top-level Functions

#### `def kdf(auth_key: bytes, msg_key: bytes, outgoing: bool) -> tuple`

_No docstring._

#### `def pack(message: Message, salt: int, session_id: bytes, auth_key: bytes, auth_key_id: bytes) -> bytes`

_No docstring._

#### `def unpack(b: BytesIO, session_id: bytes, auth_key: bytes, auth_key_id: bytes) -> Message`

_No docstring._

---

## File: `crypto/prime.py`

### Top-level Functions

#### `def gcd(a: int, b: int) -> int`

_No docstring._

#### `def decompose(pq: int) -> int`

_No docstring._

---

## File: `crypto/rsa.py`

### Top-level Functions

#### `def encrypt(data: bytes, fingerprint: int) -> bytes`

_No docstring._

---
