---
name: api-api-raw
description: Offline API backup extracted from Pyrofork source docstrings.
---

# Pyrofork API Backup: `raw`

Extracted from `sources/pyrofork/pyrogram/**.py` using AST parsing of module, class, function, and method docstrings.

## File: `raw/__init__.py`

---

## File: `raw/core/__init__.py`

---

## File: `raw/core/future_salt.py`

### Classes

#### `class FutureSalt(TLObject)`

_No docstring._

##### Methods

###### `def __init__(self, valid_since: int, valid_until: int, salt: int)`

_No docstring._

###### `def read(data: BytesIO, *args: Any) -> 'FutureSalt'`

_No docstring._

###### `def write(self, *args: Any) -> bytes`

_No docstring._

---

## File: `raw/core/future_salts.py`

### Classes

#### `class FutureSalts(TLObject)`

_No docstring._

##### Methods

###### `def __init__(self, req_msg_id: int, now: int, salts: List[FutureSalt])`

_No docstring._

###### `def read(data: BytesIO, *args: Any) -> 'FutureSalts'`

_No docstring._

###### `def write(self, *args: Any) -> bytes`

_No docstring._

---

## File: `raw/core/gzip_packed.py`

### Classes

#### `class GzipPacked(TLObject)`

_No docstring._

##### Methods

###### `def __init__(self, packed_data: TLObject)`

_No docstring._

###### `def read(data: BytesIO, *args: Any) -> 'GzipPacked'`

_No docstring._

###### `def write(self, *args: Any) -> bytes`

_No docstring._

---

## File: `raw/core/list.py`

### Classes

#### `class List(TList[Any], TLObject)`

_No docstring._

##### Methods

###### `def __repr__(self) -> str`

_No docstring._

---

## File: `raw/core/message.py`

### Classes

#### `class Message(TLObject)`

_No docstring._

##### Methods

###### `def __init__(self, body: TLObject, msg_id: int, seq_no: int, length: int)`

_No docstring._

###### `def read(data: BytesIO, *args: Any) -> 'Message'`

_No docstring._

###### `def write(self, *args: Any) -> bytes`

_No docstring._

---

## File: `raw/core/msg_container.py`

### Classes

#### `class MsgContainer(TLObject)`

_No docstring._

##### Methods

###### `def __init__(self, messages: List[Message])`

_No docstring._

###### `def read(data: BytesIO, *args: Any) -> 'MsgContainer'`

_No docstring._

###### `def write(self, *args: Any) -> bytes`

_No docstring._

---

## File: `raw/core/primitives/__init__.py`

---

## File: `raw/core/primitives/bool.py`

### Classes

#### `class BoolFalse(bytes, TLObject)`

_No docstring._

##### Methods

###### `def read(cls, *args: Any) -> bool`

_No docstring._

###### `def __new__(cls) -> bytes`

_No docstring._

#### `class BoolTrue(BoolFalse)`

_No docstring._

#### `class Bool(bytes, TLObject)`

_No docstring._

##### Methods

###### `def read(cls, data: BytesIO, *args: Any) -> bool`

_No docstring._

###### `def __new__(cls, value: bool) -> bytes`

_No docstring._

---

## File: `raw/core/primitives/bytes.py`

### Classes

#### `class Bytes(bytes, TLObject)`

_No docstring._

##### Methods

###### `def read(cls, data: BytesIO, *args: Any) -> bytes`

_No docstring._

###### `def __new__(cls, value: bytes) -> bytes`

_No docstring._

---

## File: `raw/core/primitives/double.py`

### Classes

#### `class Double(bytes, TLObject)`

_No docstring._

##### Methods

###### `def read(cls, data: BytesIO, *args: Any) -> float`

_No docstring._

###### `def __new__(cls, value: float) -> bytes`

_No docstring._

---

## File: `raw/core/primitives/int.py`

### Classes

#### `class Int(bytes, TLObject)`

_No docstring._

##### Methods

###### `def read(cls, data: BytesIO, signed: bool = True, *args: Any) -> int`

_No docstring._

###### `def __new__(cls, value: int, signed: bool = True) -> bytes`

_No docstring._

#### `class Long(Int)`

_No docstring._

#### `class Int128(Int)`

_No docstring._

#### `class Int256(Int)`

_No docstring._

---

## File: `raw/core/primitives/string.py`

### Classes

#### `class String(Bytes)`

_No docstring._

##### Methods

###### `def read(cls, data: BytesIO, *args) -> str`

_No docstring._

###### `def __new__(cls, value: str) -> bytes`

_No docstring._

---

## File: `raw/core/primitives/vector.py`

### Classes

#### `class Vector(bytes, TLObject)`

_No docstring._

##### Methods

###### `def read_bare(b: BytesIO, size: int) -> Union[int, Any]`

_No docstring._

###### `def read(cls, data: BytesIO, t: Any = None, *args: Any) -> List`

_No docstring._

###### `def __new__(cls, value: list, t: Any = None) -> bytes`

_No docstring._

---

## File: `raw/core/tl_object.py`

### Classes

#### `class TLObject`

_No docstring._

##### Methods

###### `def read(cls, b: BytesIO, *args: Any) -> Any`

_No docstring._

###### `def write(self, *args: Any) -> bytes`

_No docstring._

###### `def default(obj: 'TLObject') -> Union[str, Dict[str, str]]`

_No docstring._

###### `def __str__(self) -> str`

_No docstring._

###### `def __repr__(self) -> str`

_No docstring._

###### `def __eq__(self, other: Any) -> bool`

_No docstring._

###### `def __len__(self) -> int`

_No docstring._

###### `def __call__(self, *args: Any, **kwargs: Any) -> Any`

_No docstring._

---
