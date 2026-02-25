# Getting Started (Pyrofork)

## Installation

- Base:
  - `pip3 install -U pyrofork`
- Recommended speedups:
  - `pip3 install -U tgcrypto-pyrofork`
  - optional event loop speedup: `pip3 install -U uvloop`

## Credentials and first setup

1. Create Telegram app credentials at `https://my.telegram.org/apps`
2. Use `api_id` + `api_hash` in first login run
3. For bots, also pass `bot_token` (API key is still required for initial auth)

## Session model

- `Client("name")` creates/uses `name.session` (SQLite-backed, file storage)
- `in_memory=True` avoids file persistence; session is lost when process exits
- `export_session_string()` lets you persist in-memory sessions externally
- Optional MongoDB-backed storage is supported via `mongodb={...}` in `Client(...)`

## Canonical auth examples

### User

- Create `Client("my_account", api_id=..., api_hash=...)`
- Call `app.run()` and complete phone + code prompts

### Bot

- Create `Client("my_bot", api_id=..., api_hash=..., bot_token=...)`
- Call `app.run()` once to initialize the session

After successful authorization, API key values are typically not needed for subsequent runs if session is reused.

## Invocation patterns

### Preferred async pattern

- Use `async with app:` and `await app.some_method(...)`
- Execute via `app.run(main())` or `asyncio.run(main())` (if `Client` is instantiated in `main`)

### Convenience sync pattern

- `with app: app.send_message(...)`
- Use with care; Pyrofork is async-first

## Embedded starter patterns (from official examples)

The following are condensed, reusable patterns so agents can generate code without relying on the original `.rst` files.

### `hello_world` pattern

- Goal: prove credentials/session and first outbound message flow.
- Shape:
  - create client
  - enter client context
  - send message to `"me"`

### `echo_bot` pattern

- Goal: minimal bot update loop.
- Shape:
  - register `on_message(filters.private & filters.text)`
  - reply with incoming text
  - run client continuously

### `welcome_bot` pattern

- Goal: react to new members in groups/channels.
- Shape:
  - listen for member-related updates/service messages
  - craft welcome text with mention/name fallback
  - send welcome in same chat

### `get_chat_history` pattern

- Goal: iterate over message history efficiently.
- Shape:
  - call history iterator (`get_chat_history`)
  - stream/process items incrementally
  - avoid loading huge history into memory at once

### `get_chat_members` pattern

- Goal: enumerate participants.
- Shape:
  - iterate over members generator
  - process user/member attributes safely
  - keep permissions/privacy edge cases in mind

### `get_dialogs` pattern

- Goal: enumerate open conversations/chats.
- Shape:
  - iterate dialogs
  - branch behavior by chat type
  - cache IDs/usernames for later operations

### `callback_queries` pattern

- Goal: handle inline keyboard button clicks.
- Shape:
  - create inline keyboard with callback data
  - handle `on_callback_query`
  - answer callback promptly, then edit/send follow-up if needed

### `inline_queries` pattern

- Goal: implement inline mode search results.
- Shape:
  - handle `on_inline_query`
  - return typed inline results list
  - tune caching and result relevance

### `use_inline_bots` pattern

- Goal: invoke another inline bot from user context.
- Shape:
  - request inline bot results
  - select result
  - send selected result to target chat

### `bot_keyboards` pattern

- Goal: send reply and inline keyboards.
- Shape:
  - build keyboard markup object
  - attach via `reply_markup`
  - pair with message/callback handlers as needed

### `raw_updates` legacy pattern

- Goal: inspect low-level updates for edge cases.
- Notes:
  - useful for diagnostics and unsupported high-level flows
  - prefer high-level handlers in normal application code

## First production-ready bot checklist

- [ ] Install Pyrofork + optional speedups (`tgcrypto-pyrofork`, `uvloop`)
- [ ] Complete initial auth and persist a dedicated session name
- [ ] Implement one health command (`/start` or `/ping`)
- [ ] Add flood-wait handling and structured logging
- [ ] Verify with private chat and one group/supergroup scenario

## Error hierarchy essentials

- Root: `RPCError`
- Category classes: `SeeOther`, `BadRequest`, `Unauthorized`, `Forbidden`, `NotAcceptable`, `Flood`, `InternalServerError`
- Specific exceptions subclass categories (e.g., `FloodWait`)

### Flood wait handling

- Catch `FloodWait` and `await asyncio.sleep(e.value)`

## Practical checklist

- [ ] Session naming strategy chosen
- [ ] Auth mode chosen (user or bot)
- [ ] Async vs sync mode intentionally selected
- [ ] Error handling includes category/specific exceptions
- [ ] Flood wait backoff implemented
