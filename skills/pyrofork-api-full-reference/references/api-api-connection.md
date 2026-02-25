---
name: api-api-connection
description: Offline API backup extracted from Pyrofork source docstrings.
---

# Pyrofork API Backup: `connection`

Extracted from `sources/pyrofork/pyrogram/**.py` using AST parsing of module, class, function, and method docstrings.

## File: `connection/__init__.py`

---

## File: `connection/connection.py`

### Classes

#### `class Connection`

_No docstring._

##### Methods

###### `def __init__(self, dc_id: int, test_mode: bool, ipv6: bool, alt_port: bool, proxy: dict, media: bool = False, protocol_factory: Type[TCP] = TCPAbridged) -> None`

_No docstring._

###### `async def connect(self) -> None`

_No docstring._

###### `async def close(self) -> None`

_No docstring._

###### `async def send(self, data: bytes) -> None`

_No docstring._

###### `async def recv(self) -> Optional[bytes]`

_No docstring._

---

## File: `connection/transport/__init__.py`

---

## File: `connection/transport/tcp/__init__.py`

---

## File: `connection/transport/tcp/tcp.py`

### Classes

#### `class Proxy(TypedDict)`

_No docstring._

#### `class TCP`

_No docstring._

##### Methods

###### `def __init__(self, ipv6: bool, proxy: Proxy) -> None`

_No docstring._

###### `async def _connect_via_proxy(self, destination: Tuple[str, int]) -> None`

_No docstring._

###### `async def _connect_via_direct(self, destination: Tuple[str, int]) -> None`

_No docstring._

###### `async def _connect(self, destination: Tuple[str, int]) -> None`

_No docstring._

###### `async def connect(self, address: Tuple[str, int]) -> None`

_No docstring._

###### `async def close(self) -> None`

_No docstring._

###### `async def send(self, data: bytes) -> None`

_No docstring._

###### `async def recv(self, length: int = 0) -> Optional[bytes]`

_No docstring._

---

## File: `connection/transport/tcp/tcp_abridged.py`

### Classes

#### `class TCPAbridged(TCP)`

_No docstring._

##### Methods

###### `def __init__(self, ipv6: bool, proxy: Proxy) -> None`

_No docstring._

###### `async def connect(self, address: Tuple[str, int]) -> None`

_No docstring._

###### `async def send(self, data: bytes, *args) -> None`

_No docstring._

###### `async def recv(self, length: int = 0) -> Optional[bytes]`

_No docstring._

---

## File: `connection/transport/tcp/tcp_abridged_o.py`

### Classes

#### `class TCPAbridgedO(TCP)`

_No docstring._

##### Methods

###### `def __init__(self, ipv6: bool, proxy: Proxy) -> None`

_No docstring._

###### `async def connect(self, address: Tuple[str, int]) -> None`

_No docstring._

###### `async def send(self, data: bytes, *args) -> None`

_No docstring._

###### `async def recv(self, length: int = 0) -> Optional[bytes]`

_No docstring._

---

## File: `connection/transport/tcp/tcp_full.py`

### Classes

#### `class TCPFull(TCP)`

_No docstring._

##### Methods

###### `def __init__(self, ipv6: bool, proxy: Proxy) -> None`

_No docstring._

###### `async def connect(self, address: Tuple[str, int]) -> None`

_No docstring._

###### `async def send(self, data: bytes, *args) -> None`

_No docstring._

###### `async def recv(self, length: int = 0) -> Optional[bytes]`

_No docstring._

---

## File: `connection/transport/tcp/tcp_intermediate.py`

### Classes

#### `class TCPIntermediate(TCP)`

_No docstring._

##### Methods

###### `def __init__(self, ipv6: bool, proxy: Proxy) -> None`

_No docstring._

###### `async def connect(self, address: Tuple[str, int]) -> None`

_No docstring._

###### `async def send(self, data: bytes, *args) -> None`

_No docstring._

###### `async def recv(self, length: int = 0) -> Optional[bytes]`

_No docstring._

---

## File: `connection/transport/tcp/tcp_intermediate_o.py`

### Classes

#### `class TCPIntermediateO(TCP)`

_No docstring._

##### Methods

###### `def __init__(self, ipv6: bool, proxy: Proxy) -> None`

_No docstring._

###### `async def connect(self, address: Tuple[str, int]) -> None`

_No docstring._

###### `async def send(self, data: bytes, *args) -> None`

_No docstring._

###### `async def recv(self, length: int = 0) -> Optional[bytes]`

_No docstring._

---
