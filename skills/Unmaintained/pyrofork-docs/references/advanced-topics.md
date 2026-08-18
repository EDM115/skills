# Advanced Topics

## Raw Telegram API (`pyrogram.raw`)

Use raw API when high-level methods are missing or you need complete control.

## Invocation pattern

- Import raw classes from `pyrogram.raw.functions` and `pyrogram.raw.types`
- Instantiate function class with named args
- Call `await app.invoke(function_instance)`

## Peer and ID semantics

- Raw API often needs `InputPeer*` with `id + access_hash`
- Use `app.resolve_peer(...)` to resolve high-level IDs/usernames into input peers
- High-level ID conventions:
  - user: `+id`
  - basic group: `-id`
  - channel/supergroup: `-100id`

## Text formatting

Supported styles include bold/italic/underline/strike/spoiler/URL/mentions/emoji/code/pre/blockquote.

### Parse mode guidance

- Complex formatting: prefer `ParseMode.HTML`
- Markdown exists but is less reliable for complex nested/overlapping entities
- Mixed mode is default if parse mode omitted
- Disable parsing via `ParseMode.DISABLED`
- Escape raw HTML special chars (`<`, `>`, `&`) when using HTML mode

## Storage engines

- File storage (default): SQLite session file (`name.session`)
- Memory storage: `in_memory=True`
- MongoDB storage: pass `mongodb=dict(connection=..., remove_peers=...)`
- Session strings: use `export_session_string()` for portable auth state

## Client settings and identity metadata

Configurable `Client(...)` presentation values:

- `app_version`
- `device_model`
- `system_version`
- `lang_code` (ISO 639-1)

## Proxy support

Pass `proxy={"scheme": "socks5|socks4|http", "hostname": ..., "port": ..., "username": ..., "password": ...}`

## Scheduling jobs

Typical integration with `apscheduler`:

- Async app: `AsyncIOScheduler`
- Sync app: `BackgroundScheduler`

## Performance speedups

- `tgcrypto-pyrofork`: C crypto acceleration
- `uvloop`: faster event loop; install before creating/importing active runtime usage

## Test environment

- Use `test_mode=True` with a dedicated session name
- Useful for isolated dev/testing against Telegram test servers

## Serialization and introspection

- `str(obj)`: human-readable JSON-like structure
- `repr(obj)`: machine-oriented representation, restorable with `eval(...)` under matching Pyrofork version

## Voice calls ecosystem

Voice calls are provided by external integrations (`pytgcalls`, `tgcalls`), not built-in core APIs.
