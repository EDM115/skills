---
name: api-api-errors
description: Offline API backup extracted from Pyrofork source docstrings.
---

# Pyrofork API Backup: `errors`

Extracted from `sources/pyrofork/pyrogram/**.py` using AST parsing of module, class, function, and method docstrings.

## File: `errors/__init__.py`

### Classes

#### `class BadMsgNotification(Exception)`

_No docstring._

##### Methods

###### `def __init__(self, code)`

_No docstring._

#### `class SecurityError(Exception)`

```text
Generic security error.
```

##### Methods

###### `def check(cls, cond: bool, msg: str)`

```text
Raises this exception if the condition is false
```

#### `class SecurityCheckMismatch(SecurityError)`

```text
Raised when a security check mismatch occurs.
```

##### Methods

###### `def __init__(self, msg: str = None)`

_No docstring._

#### `class CDNFileHashMismatch(SecurityError)`

```text
Raised when a CDN file hash mismatch occurs.
```

##### Methods

###### `def __init__(self, msg: str = None)`

_No docstring._

---

## File: `errors/pyromod/__init__.py`

---

## File: `errors/pyromod/listener_stopped.py`

### Classes

#### `class ListenerStopped(Exception)`

_No docstring._

---

## File: `errors/pyromod/listener_timeout.py`

### Classes

#### `class ListenerTimeout(Exception)`

_No docstring._

---

## File: `errors/rpc_error.py`

### Classes

#### `class RPCError(Exception)`

_No docstring._

##### Methods

###### `def __init__(self, value: Union[int, str, raw.types.RpcError] = None, rpc_name: str = None, is_unknown: bool = False, is_signed: bool = False)`

_No docstring._

###### `def raise_it(rpc_error: 'raw.types.RpcError', rpc_type: Type[TLObject])`

_No docstring._

#### `class UnknownError(RPCError)`

_No docstring._

---
