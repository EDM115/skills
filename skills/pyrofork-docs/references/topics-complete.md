# Complete Topic Guides (Self-Contained)

This file embeds complete practical guidance from every file under `docs/source/topics`.
It is written so an agent can work without accessing `.rst` documentation files.

---

## use-filters

Filters control which updates are passed to a handler.

### Single filter usage

- Decorator style:
  - `@app.on_message(filters.sticker)`
- Handler class style:
  - `app.add_handler(MessageHandler(callback, filters.sticker))`

### Combining filters

- Invert: `~filters.xxx`
- AND: `filters.a & filters.b`
- OR: `filters.a | filters.b`

Examples:

- Text OR photo:
  - `filters.text | filters.photo`
- Sticker AND (channel OR private):
  - `filters.sticker & (filters.channel | filters.private)`

### Parameterized filters

- Command filter:
  - `filters.command(["start", "help"])`
- Regex filter:
  - `filters.regex("pyrogram")`

Multiple handlers with different filters can coexist.

---

## create-filters

Custom filters are created with `filters.create(...)`.

### Basic custom filter

- Callback signature: `(self_filter, client, update)`
- Return `True` to allow update, `False` to block.

Example pattern:

- For callback query data matching `"pyrogram"`, return `query.data == "pyrogram"`.

### Dynamic filter with arguments

- Use closure + kwargs on `filters.create`.
- Read passed values from `flt.<kwarg>` inside callback.

Example pattern:

- `dynamic_data_filter("pyrogram")` that checks `flt.data == query.data`.

### Method calls inside filters

- `client` is available in filter callback.
- You can run API calls before deciding whether to pass update.

---

## more-on-updates

Advanced dispatcher behavior: groups, propagation, conflicts.

### Handler groups

- Group `0` is default.
- Lower group number has higher priority.
- If filters conflict in same group, first matching handler wins.
- To handle same update multiple times, place handlers in different groups.

### Update propagation behavior

- Updates are processed group-by-group.
- Unhandled exception in one handler does not stop all other groups.

### Stop propagation

Preferred:

- `update.stop_propagation()`

Alternative (especially for raw updates):

- `raise StopPropagation`

Important:

- Code after `stop_propagation()` does not run because it signals via exception.

### Continue propagation in same group

Preferred:

- `update.continue_propagation()`

Alternative:

- `raise ContinuePropagation`

This allows multiple conflicting handlers in the same group to run sequentially.

---

## client-settings

Customize session appearance in Telegram active sessions list.

Configurable constructor args:

- `app_version`
- `device_model`
- `system_version`
- `lang_code` (ISO 639-1, default `en`)

Example:

- `Client("my_account", app_version="1.2.3", device_model="PC", system_version="Linux", lang_code="it")`

---

## speedups

Performance tooling:

### TgCrypto-pyrofork

- Install: `pip3 install -U tgcrypto-pyrofork`
- Used automatically if installed.

### uvloop

- Install: `pip3 install -U uvloop`
- Improves asyncio event-loop performance.
- Call `uvloop.install()` before `asyncio.run(...)` or `app.run(...)`.
- In practice, set it before creating/using active client runtime path.

---

## text-formatting

Pyrofork supports a custom Markdown + HTML entity parser.

### Basic style features

- bold, italic, underline, strike, spoiler
- URL and inline mention
- custom emoji
- inline code and pre block
- quote and expandable quote

### HTML mode

- Use `parse_mode=enums.ParseMode.HTML`
- Supports tags like: `<b>`, `<i>`, `<u>`, `<s>`, `<spoiler>`, `<a>`, `<emoji>`, `<code>`, `<pre>`, `<blockquote>`

Escaping rule:

- Non-tag `<`, `>`, `&` must be escaped (`html.escape`).

### Markdown mode

- Use `parse_mode=enums.ParseMode.MARKDOWN`
- Simpler syntax but less reliable for complex nested/overlapping entities.

### Mixed mode (default)

- If `parse_mode` omitted, both styles are parsed.

### Disable parsing

- `parse_mode=enums.ParseMode.DISABLED`

### Nested and overlapping entities

- Complex styling is better done with HTML mode.

---

## synchronous

Pyrofork is async-first; sync mode is convenience-only.

### Async canonical usage

- `async with Client(...) as app:`
- `await app.send_message(...)`

### Sync convenience usage

- `with Client(...) as app:`
- `app.send_message(...)`

Warnings:

- Avoid long blocking operations in sync handlers.
- Event loop starvation causes erratic behavior.

### uvloop in sync mode

- Install uvloop before importing or starting Pyrofork execution path.

---

## smart-plugins

Optional plugin system for modular handler loading.

### Project setup

- Create plugin root folder (e.g. `plugins/`).
- Place modules/submodules with decorated handlers.
- Enable in client: `Client("name", plugins=dict(root="plugins"))`.

### Static class-level decorators

- Use `@Client.on_message(...)` in plugin modules (no app instance needed there).

### Loading policy

- Default: load all plugin modules discovered under root.
- `include=[...]`: load only listed modules, in listed order.
- `exclude=[...]`: skip listed modules.
- Include entries can specify handler order: `"module fn2 fn1"`.

### Runtime unload/reload

- Decorated function has `.handlers` with tuples `(handler, group)`.
- Unload: `app.remove_handler(*h)` for each tuple.
- Reload: `app.add_handler(*h)` for each tuple.

Constraint:

- Within a module, decorated function names must be unique.

---

## storage-engines

Session data persistence options.

### File storage (default)

- Uses SQLite file: `<session_name>.session`.
- Reused automatically across restarts.

### Memory storage

- `in_memory=True`
- Session disappears on process exit.

### MongoDB storage

- `mongodb={"connection": <async client>, "remove_peers": False}`
- Supports async drivers:
  - `async_pymongo` (recommended for newer Python)
  - official async Mongo client
  - `motor` (deprecated but still supported in docs)

### Session strings

- Export with `await app.export_session_string()`.
- Reuse with `Client("name", session_string=session_string)`.
- Useful for ephemeral platforms where file persistence is unreliable.

---

## serializing

Object serialization patterns.

### For humans

- `str(obj)` gives pretty JSON-like representation.

### For machines

- `repr(obj)` gives compact reconstructable representation.
- `eval(repr(obj)) == obj` can restore under same Pyrofork version context.

Version caveat:

- Type definitions can change; store/load with same library version for safety.

---

## proxy

Proxy support for MTProto transport.

Supported schemes:

- `socks4`
- `socks5`
- `http` (CONNECT)

Config structure:

- `proxy={"scheme": ..., "hostname": ..., "port": ..., "username": ..., "password": ...}`

Auth keys are optional if proxy does not require authentication.

---

## scheduling

Task scheduling integration via APScheduler.

### Async usage

- Use `AsyncIOScheduler`.
- Schedule async jobs that call awaited client methods.

### Sync usage

- Use `BackgroundScheduler`.
- Schedule sync jobs calling sync-style client methods.

---

## mtproto-vs-botapi

Core conceptual distinction.

- MTProto API is Telegram’s main API and supports user and bot identities.
- Bot API is an HTTP interface backed by an intermediate server that itself uses MTProto.

MTProto/Pyrofork advantages highlighted by docs:

- user + bot authorization support
- broader methods and richer entity details
- direct connection path (less middle-layer overhead)
- multiple sessions support behavior
- larger file capabilities than Bot API limits
- faster access to newer platform capabilities

---

## debugging

Practical debugging style emphasized by docs:

- Use careful reasoning + strategic `print(...)` statements.
- Printing Pyrofork objects yields readable JSON-like structures.

Important type-access rules:

- Pyrofork entities are objects, not dictionaries.
- Access fields with dot notation (`obj.attr`).
- Use `type(obj)` and `isinstance(obj, SomeType)` for robust checks.

---

## test-servers

Use Telegram test environment.

### App-level test mode

- Start client with `test_mode=True` and separate session name.

### Official client test logins

- Telegram Web test URL: `https://web.telegram.org/?test=1`
- Telegram Desktop: modifier-key flow to open test server option.

### Reserved test numbers

- Pattern: `99966XYYYY` where `X` is DC id (1..3).
- Confirmation code pattern tied to repeated DC number.

---

## advanced-usage

Raw API path when high-level methods are insufficient.

### Raw invocation

- Import from `pyrogram.raw.functions` / `pyrogram.raw.types`.
- Instantiate raw function class with named args.
- Execute with `await app.invoke(raw_function_instance)`.

### InputPeer and IDs

- Raw API often needs `InputPeer` structures (`id + access_hash`).
- Use `app.resolve_peer(...)` helper whenever possible.

High-level ID representation reminder:

- user: positive id
- basic group: negative id
- channel/supergroup: `-100...` prefixed range

When mapping raw IDs to high-level calls, ensure type-correct translation.

---

## voice-calls

Voice call support is provided by external ecosystems, not core Pyrofork primitives.

Primary libraries listed:

- `pytgcalls`
- `tgcalls`

Legacy implementation note:

- older `pylibtgvoip` line exists but is considered outdated in docs context.
