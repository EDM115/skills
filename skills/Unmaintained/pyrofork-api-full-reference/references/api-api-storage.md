---
name: api-api-storage
description: Offline API backup extracted from Pyrofork source docstrings.
---

# Pyrofork API Backup: `storage`

Extracted from `sources/pyrofork/pyrogram/**.py` using AST parsing of module, class, function, and method docstrings.

## File: `storage/__init__.py`

---

## File: `storage/dummy_client.py`

### Classes

#### `class DummyMongoClient(Protocol)`

_No docstring._

##### Methods

###### `def __init__(self, *args: Any, **kwargs: Any) -> None`

_No docstring._

###### `def get_database(self, name: Optional[str] = None, *, codec_options: Optional[CodecOptions] = None, read_preference: Optional[ReadPreferences] = None, write_concern: Optional[WriteConcern] = None, read_concern: Optional[ReadConcern] = None)`

_No docstring._

###### `async def start_session(self, *, causal_consistency: Optional[bool] = None, default_transaction_options: Optional[TransactionOptions] = None, snapshot: bool = False)`

_No docstring._

---

## File: `storage/file_storage.py`

### Classes

#### `class FileStorage(SQLiteStorage)`

_No docstring._

##### Methods

###### `def __init__(self, name: str, workdir: Path)`

_No docstring._

###### `def update(self)`

_No docstring._

###### `async def open(self)`

_No docstring._

###### `async def delete(self)`

_No docstring._

---

## File: `storage/memory_storage.py`

### Classes

#### `class MemoryStorage(SQLiteStorage)`

_No docstring._

##### Methods

###### `def __init__(self, name: str, session_string: str = None)`

_No docstring._

###### `async def open(self)`

_No docstring._

###### `async def delete(self)`

_No docstring._

---

## File: `storage/mongo_storage.py`

### Classes

#### `class MongoStorage(Storage)`

```text
Initializes a new session.

Parameters:
    - name (`str`):
        The session name used for database name.

    - connection (`obj`):
        Mongodb connections object.
        ~async_pymongo.AsyncClient or ~motor.motor_asyncio.AsyncIOMotorClient object

    - remove_peers (`bool`, *optional*):
        Flag to remove data in the peers collection. If set to True,
        the data related to peers will be removed everytime client log out.
        If set to False or None, the data will not be removed.

Example:
    import async_pymongo

    conn = async_pymongo.AsyncClient("mongodb://...")
    bot_db = conn["my_bot"]
    session = MongoStorage("my_session", connection=conn, remove_peers=True)
```

##### Methods

###### `def __init__(self, name: str, connection: DummyMongoClient, remove_peers: bool = False)`

_No docstring._

###### `async def open(self)`

```text
dc_id     INTEGER PRIMARY KEY,
api_id    INTEGER,
test_mode INTEGER,
auth_key  BLOB,
date      INTEGER NOT NULL,
user_id   INTEGER,
is_bot    INTEGER
```

###### `async def save(self)`

_No docstring._

###### `async def close(self)`

_No docstring._

###### `async def delete(self)`

_No docstring._

###### `async def update_peers(self, peers: List[Tuple[int, int, str, str, str]])`

```text
(id, access_hash, type, username, phone_number)
```

###### `async def update_usernames(self, usernames: List[Tuple[int, str]])`

_No docstring._

###### `async def update_state(self, value: Tuple[int, int, int, int, int] = object)`

_No docstring._

###### `async def remove_state(self, chat_id)`

_No docstring._

###### `async def get_peer_by_id(self, peer_id: int)`

_No docstring._

###### `async def get_peer_by_username(self, username: str)`

_No docstring._

###### `async def get_peer_by_phone_number(self, phone_number: str)`

_No docstring._

###### `async def _get(self)`

_No docstring._

###### `async def _set(self, value: Any)`

_No docstring._

###### `async def _accessor(self, value: Any = object)`

_No docstring._

###### `async def dc_id(self, value: int = object)`

_No docstring._

###### `async def api_id(self, value: int = object)`

_No docstring._

###### `async def test_mode(self, value: bool = object)`

_No docstring._

###### `async def auth_key(self, value: bytes = object)`

_No docstring._

###### `async def date(self, value: int = object)`

_No docstring._

###### `async def user_id(self, value: int = object)`

_No docstring._

###### `async def is_bot(self, value: bool = object)`

_No docstring._

---

## File: `storage/sqlite_storage.py`

### Top-level Functions

#### `def get_input_peer(peer_id: int, access_hash: int, peer_type: str)`

_No docstring._

### Classes

#### `class SQLiteStorage(Storage)`

_No docstring._

##### Methods

###### `def __init__(self, name: str)`

_No docstring._

###### `def create(self)`

_No docstring._

###### `async def open(self)`

_No docstring._

###### `async def save(self)`

_No docstring._

###### `async def close(self)`

_No docstring._

###### `async def delete(self)`

_No docstring._

###### `async def update_peers(self, peers: List[Tuple[int, int, str, str, str]])`

_No docstring._

###### `async def update_usernames(self, usernames: List[Tuple[int, str]])`

_No docstring._

###### `async def update_state(self, value: Tuple[int, int, int, int, int] = object)`

_No docstring._

###### `async def remove_state(self, chat_id)`

_No docstring._

###### `async def get_peer_by_id(self, peer_id: int)`

_No docstring._

###### `async def get_peer_by_username(self, username: str)`

_No docstring._

###### `async def get_peer_by_phone_number(self, phone_number: str)`

_No docstring._

###### `def _get(self)`

_No docstring._

###### `def _set(self, value: Any)`

_No docstring._

###### `def _accessor(self, value: Any = object)`

_No docstring._

###### `async def dc_id(self, value: int = object)`

_No docstring._

###### `async def api_id(self, value: int = object)`

_No docstring._

###### `async def test_mode(self, value: bool = object)`

_No docstring._

###### `async def auth_key(self, value: bytes = object)`

_No docstring._

###### `async def date(self, value: int = object)`

_No docstring._

###### `async def user_id(self, value: int = object)`

_No docstring._

###### `async def is_bot(self, value: bool = object)`

_No docstring._

###### `def version(self, value: int = object)`

_No docstring._

---

## File: `storage/storage.py`

### Classes

#### `class Storage`

_No docstring._

##### Methods

###### `def __init__(self, name: str)`

_No docstring._

###### `async def open(self)`

_No docstring._

###### `async def save(self)`

_No docstring._

###### `async def close(self)`

_No docstring._

###### `async def delete(self)`

_No docstring._

###### `async def update_peers(self, peers: List[Tuple[int, int, str, str, str]])`

_No docstring._

###### `async def update_usernames(self, usernames: List[Tuple[int, str]])`

_No docstring._

###### `async def update_state(self, update_state: Tuple[int, int, int, int, int] = object)`

```text
Get or set the update state of the current session.

Parameters:
    update_state (``Tuple[int, int, int, int, int]``): A tuple containing the update state to set.
        Tuple must contain the following information:
        - ``int``: The id of the entity.
        - ``int``: The pts.
        - ``int``: The qts.
        - ``int``: The date.
        - ``int``: The seq.
```

###### `async def get_peer_by_id(self, peer_id: int)`

_No docstring._

###### `async def get_peer_by_username(self, username: str)`

_No docstring._

###### `async def get_peer_by_phone_number(self, phone_number: str)`

_No docstring._

###### `async def dc_id(self, value: int = object)`

_No docstring._

###### `async def api_id(self, value: int = object)`

_No docstring._

###### `async def test_mode(self, value: bool = object)`

_No docstring._

###### `async def auth_key(self, value: bytes = object)`

_No docstring._

###### `async def date(self, value: int = object)`

_No docstring._

###### `async def user_id(self, value: int = object)`

_No docstring._

###### `async def is_bot(self, value: bool = object)`

_No docstring._

###### `async def export_session_string(self)`

_No docstring._

---
