# Client API (`pyrogram.Client`)

Source: `pyrogram/client.py`.

## Class

- `class Client(Methods)`
- Purpose: main entrypoint for interacting with Telegram through Pyrofork.

## Constructor signature (exact parameter names)

`Client(name, api_id=None, api_hash=None, app_version=APP_VERSION, device_model=DEVICE_MODEL, system_version=SYSTEM_VERSION, system_lang_code=SYSTEM_LANG_CODE, lang_code=LANG_CODE, lang_pack=LANG_PACK, ipv6=False, alt_port=False, proxy=None, test_mode=False, bot_token=None, session_string=None, use_qrcode=False, in_memory=None, mongodb=None, storage=None, phone_number=None, phone_code=None, password=None, workers=WORKERS, workdir=WORKDIR, plugins=None, parse_mode=enums.ParseMode.DEFAULT, no_updates=None, skip_updates=True, takeout=None, sleep_threshold=Session.SLEEP_THRESHOLD, hide_password=True, max_concurrent_transmissions=MAX_CONCURRENT_TRANSMISSIONS, client_platform=enums.ClientPlatform.OTHER, max_message_cache_size=MAX_CACHE_SIZE, max_business_user_connection_cache_size=MAX_CACHE_SIZE)`

## Constructor parameters (documented semantics)

- `name: str` — session name.
- `api_id: int | str | None` — Telegram API ID.
- `api_hash: str | None` — Telegram API hash.
- `app_version: str` — visible app version.
- `device_model: str` — visible device model.
- `system_version: str` — visible OS/version.
- `system_lang_code: str` — system language code (defaults `en-US`).
- `lang_code: str` — ISO 639-1 client language.
- `lang_pack: str` — language pack hint.
- `ipv6: bool` — use IPv6 transport.
- `alt_port: bool` — use alternative Telegram port.
- `proxy: dict | None` — proxy settings (`scheme`, `hostname`, `port`, optional auth).
- `test_mode: bool` — use Telegram test servers for new sessions.
- `bot_token: str | None` — bot authorization token.
- `session_string: str | None` — in-memory session import.
- `use_qrcode: bool` — QR login flow.
- `in_memory: bool | None` — memory storage mode.
- `mongodb: dict | None` — MongoDB-backed storage config.
- `storage: Storage | None` — custom storage backend.
- `phone_number: str | None` — prefilled phone.
- `phone_code: str | None` — prefilled code (test-number cases included).
- `password: str | None` — 2FA password.
- `workers: int` — update handler worker count.
- `workdir: str | Path` — location for file session storage.
- `plugins: dict | None` — smart-plugin config.
- `parse_mode: enums.ParseMode` — default text parsing mode.
- `no_updates: bool | None` — disable incoming updates.
- `skip_updates: bool` — drop pending offline updates on startup.
- `takeout: bool | None` — takeout session mode.
- `sleep_threshold: int` — flood-wait auto-sleep threshold.
- `hide_password: bool | None` — hide password input in prompt.
- `max_concurrent_transmissions: int` — upload/download concurrency cap.
- `client_platform: enums.ClientPlatform` — platform identity enum.
- `max_message_cache_size: int` — message cache capacity.
- `max_business_user_connection_cache_size: int` — business connection cache capacity.

## Lifecycle and context manager behavior

- Sync context manager delegates to `start()` / `stop()`.
- Async context manager delegates to `await start()` / `await stop()`.
- Disconnection during teardown is handled safely.

## API-documented client methods in class source

- `set_parse_mode(parse_mode)`
  - Sets global parse mode used by methods that support parsing.

### Internal/public operational methods present on class

- `updates_watchdog()`
- `authorize()`
- `fetch_peers(peers)`
- `handle_updates(updates)`
- `recover_gaps()`
- `load_session()`
- `is_excluded(exclude, module)`
- `load_plugins()`
- `handle_download(packet)`
- `get_file(file_id, file_size=0, limit=0, offset=0, progress=None, progress_args=())`
- `guess_mime_type(filename)`
- `guess_extension(mime_type)`

## Storage selection logic

Selection order:

1. custom `storage`
2. `session_string` -> `MemoryStorage`
3. `in_memory` -> `MemoryStorage`
4. `mongodb` -> `MongoStorage` (if pymongo available)
5. fallback `FileStorage`

## Important implementation notes

- API key is required for new authorizations.
- `listeners` initialized by listener type enum.
- transmission semaphores enforce upload/download concurrency limits.
- plugin loader supports include/exclude and per-handler ordered inclusion.
