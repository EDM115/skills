# Filters API (`pyrogram.filters`)

Source: `pyrogram/filters.py`.

## Core filter classes

- `Filter`
  - callable protocol: `await filter(client, update) -> bool`
  - supports inversion/composition operators: `~`, `&`, `|`
- `InvertFilter(base)`
- `AndFilter(base, other)`
- `OrFilter(base, other)`

## Custom filter factory

- `create(func, name=None, **kwargs) -> Filter`

`func` signature:

- `(filter, client, update) -> bool`

## Built-in singleton filters (attribute aliases)

Each of these is created via `create(...)` and exposed as module-level filter object.

- `all`
- `me`
- `bot`
- `incoming`
- `outgoing`
- `text`
- `reply`
- `react`
- `forwarded`
- `caption`
- `audio`
- `document`
- `photo`
- `sticker`
- `animation`
- `game`
- `giveaway`
- `giveaway_result`
- `gift_code`
- `star_gift`
- `video`
- `media_group`
- `voice`
- `video_note`
- `contact`
- `location`
- `venue`
- `web_page`
- `poll`
- `dice`
- `media_spoiler`
- `private`
- `group`
- `channel`
- `new_chat_members`
- `left_chat_member`
- `new_chat_title`
- `new_chat_photo`
- `delete_chat_photo`
- `group_chat_created`
- `supergroup_chat_created`
- `channel_chat_created`
- `migrate_to_chat_id`
- `migrate_from_chat_id`
- `pinned_message`
- `game_high_score`
- `reply_keyboard`
- `inline_keyboard`
- `mentioned`
- `via_bot`
- `video_chat_started`
- `video_chat_ended`
- `video_chat_members_invited`
- `successful_payment`
- `service`
- `media`
- `scheduled`
- `from_scheduled`
- `linked_channel`
- `forum_topic_closed`
- `forum_topic_created`
- `forum_topic_edited`
- `forum_topic_reopened`
- `general_forum_topic_hidden`
- `general_forum_topic_unhidden`

## Advanced parameterized filters

### `command(commands, prefixes='/', case_sensitive=False)`

- Parses command messages from text/caption.
- Sets `message.command` list: `[command, arg1, arg2, ...]`.
- Supports multiple prefixes and optional case sensitivity.
- Handles bot username suffix matching in command forms.

### `regex(pattern, flags=0)`

Supports updates:

- `Message` (`text` or `caption`)
- `CallbackQuery` (`data`)
- `InlineQuery` (`query`)
- `PreCheckoutQuery` (`payload`)

On match, stores `update.matches` with `re.Match` objects.

## Set-backed dynamic filter classes

### `user(users=None)`

- Tracks allowed user IDs/usernames.
- Supports special aliases `"me"` / `"self"`.

### `chat(chats=None)`

- Tracks allowed chat IDs/usernames.
- Supports saved messages alias handling.
- Handles both `Message` and `Story` flows.

### `topic(topics=None)`

- Tracks allowed topic IDs.
- Supports general topic (`1`) handling.

## Composition behavior

- `~flt` returns inversion filter.
- `flt1 & flt2` short-circuits false first operand.
- `flt1 | flt2` short-circuits true first operand.
- Both coroutine and non-coroutine filter callables are supported.
