# Internals filetree coverage (final pass)

This file explicitly covers source files/folders that were previously under-documented:

- root `pyrogram/*.py` modules
- `connection`
- `crypto`
- `helpers`
- `nav`
- `parser`
- `session`
- `storage`

## Root modules (`pyrogram/*.py`)

- `pyrogram/__init__.py`
- `pyrogram/client.py`
- `pyrogram/dispatcher.py`
- `pyrogram/emoji.py`
- `pyrogram/file_id.py`
- `pyrogram/filters.py`
- `pyrogram/mime_types.py`
- `pyrogram/sync.py`
- `pyrogram/utils.py`

## `pyrogram/connection`

- `pyrogram/connection/__init__.py`
- `pyrogram/connection/connection.py`
- `pyrogram/connection/transport/__init__.py`
- `pyrogram/connection/transport/tcp/__init__.py`
- `pyrogram/connection/transport/tcp/tcp.py`
- `pyrogram/connection/transport/tcp/tcp_abridged.py`
- `pyrogram/connection/transport/tcp/tcp_abridged_o.py`
- `pyrogram/connection/transport/tcp/tcp_full.py`
- `pyrogram/connection/transport/tcp/tcp_intermediate.py`
- `pyrogram/connection/transport/tcp/tcp_intermediate_o.py`

## `pyrogram/crypto`

- `pyrogram/crypto/__init__.py`
- `pyrogram/crypto/aes.py`
- `pyrogram/crypto/mtproto.py`
- `pyrogram/crypto/prime.py`
- `pyrogram/crypto/rsa.py`

## `pyrogram/helpers`

- `pyrogram/helpers/__init__.py`
- `pyrogram/helpers/helpers.py`

## `pyrogram/nav`

- `pyrogram/nav/__init__.py`
- `pyrogram/nav/pagination.py`

## `pyrogram/parser`

- `pyrogram/parser/__init__.py`
- `pyrogram/parser/html.py`
- `pyrogram/parser/markdown.py`
- `pyrogram/parser/parser.py`
- `pyrogram/parser/utils.py`

## `pyrogram/session`

- `pyrogram/session/__init__.py`
- `pyrogram/session/auth.py`
- `pyrogram/session/internals/__init__.py`
- `pyrogram/session/internals/data_center.py`
- `pyrogram/session/internals/msg_factory.py`
- `pyrogram/session/internals/msg_id.py`
- `pyrogram/session/internals/seq_no.py`
- `pyrogram/session/session.py`

## `pyrogram/storage`

- `pyrogram/storage/__init__.py`
- `pyrogram/storage/dummy_client.py`
- `pyrogram/storage/file_storage.py`
- `pyrogram/storage/memory_storage.py`
- `pyrogram/storage/mongo_storage.py`
- `pyrogram/storage/sqlite_storage.py`
- `pyrogram/storage/storage.py`

## Coverage status note

Other major domains are covered in dedicated references:

- methods -> `methods-api.md`
- types -> `types-api.md`
- bound methods -> `bound-methods-api.md`
- handlers/decorators/filters/enums/errors/raw -> corresponding `*-api.md` files
