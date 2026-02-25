# Internals runtime API map

This file documents public symbols and responsibilities for root/internal Pyrofork runtime modules.

## Root module symbols

### `pyrogram/__init__.py`

- Classes/exceptions:
  - `StopTransmission`
  - `StopPropagation`
  - `ContinuePropagation`

### `pyrogram/dispatcher.py`

- Classes:
  - `Dispatcher`

### `pyrogram/file_id.py`

- Classes:
  - `FileType`
  - `ThumbnailSource`
  - `FileId`
  - `FileUniqueType`
  - `FileUniqueId`
- Functions:
  - `b64_encode`, `b64_decode`
  - `rle_encode`, `rle_decode`

### `pyrogram/sync.py`

- Functions:
  - `async_to_sync`
  - `wrap`

### `pyrogram/utils.py`

- Utility functions:
  - `ainput`
  - `get_input_media_from_file_id`
  - `parse_messages`, `parse_deleted_messages`
  - `pack_inline_message_id`, `unpack_inline_message_id`
  - `get_raw_peer_id`, `get_peer_id`, `get_peer_type`, `get_channel_id`
  - `btoi`, `itob`, `sha256`, `xor`
  - `compute_password_hash`, `compute_password_check`
  - `parse_text_entities`, `parse_text_with_entities`
  - `zero_datetime`, `timestamp_to_datetime`, `datetime_to_timestamp`
  - `run_sync`, `get_reply_to`, `get_first_url`

### `pyrogram/emoji.py`

- data/constants module (no public class/function declarations found by AST scan)

### `pyrogram/mime_types.py`

- MIME mapping data module (no public class/function declarations found by AST scan)

---

## `pyrogram/connection` runtime transport stack

- `Connection` (`connection.py`)
- Transport classes (`transport/tcp/*`):
  - `Proxy`, `TCP`
  - `TCPAbridged`
  - `TCPAbridgedO`
  - `TCPFull`
  - `TCPIntermediate`
  - `TCPIntermediateO`

Role: wire-level session connectivity and transport framing.

---

## `pyrogram/crypto`

- `mtproto.py`:
  - `kdf`, `pack`, `unpack`
- `prime.py`:
  - `gcd`, `decompose`
- `rsa.py`:
  - `encrypt`
- `aes.py`:
  - AES primitives module (implementation functions imported/used by session/client code)

Role: MTProto cryptographic primitives used in auth/session/media flows.

---

## `pyrogram/helpers`

- `helpers.py` functions:
  - `ikb`, `btn`, `bki`, `ntb`, `kb`, `force_reply`, `array_chunk`

Role: convenience helpers (especially keyboard construction utilities).

---

## `pyrogram/nav`

- `Pagination` (`pagination.py`)

Role: navigation/pagination helper utilities.

---

## `pyrogram/parser`

- `html.py`:
  - `Parser`, `HTML`
- `markdown.py`:
  - `Markdown`
- `parser.py`:
  - `Parser`
- `utils.py`:
  - `add_surrogates`, `remove_surrogates`, `replace_once`, `within_surrogate`

Role: message entity parsing/unparsing across Markdown+HTML modes.

---

## `pyrogram/session`

- `auth.py`:
  - `Auth`
- `session.py`:
  - `Result`, `Session`
- `internals/data_center.py`:
  - `DataCenter`
- `internals/msg_factory.py`:
  - `MsgFactory`
- `internals/msg_id.py`:
  - `MsgId`
- `internals/seq_no.py`:
  - `SeqNo`

Role: authorization, session lifecycle, message id/seq generation, DC state.

---

## `pyrogram/storage`

- `Storage` base (`storage.py`)
- `SQLiteStorage` (`sqlite_storage.py`)
  - helper: `get_input_peer`
- `FileStorage` (`file_storage.py`)
- `MemoryStorage` (`memory_storage.py`)
- `MongoStorage` (`mongo_storage.py`)
- `DummyMongoClient` (`dummy_client.py`)

Role: persistent and ephemeral session backends.
