# Pyrofork Reference Map

Use this file to quickly locate the right concept or API family.

## Core documentation topology

- Introduction:
  - install
  - quickstart
- Getting started:
  - setup
  - auth
  - invoking methods
  - handling updates
  - error handling
  - examples
- API reference:
  - `Client`
  - methods
  - types
  - bound methods
  - enums
  - handlers
  - decorators
  - filters
  - RPC errors
- Topic guides:
  - filters usage/creation
  - updates propagation/groups
  - client settings
  - speedups
  - text formatting
  - synchronous mode
  - smart plugins
  - storage engines
  - serialization
  - proxy
  - scheduling
  - MTProto vs Bot API
  - debugging
  - test servers
  - advanced raw API
  - voice calls
- Meta:
  - FAQ
  - support

## Complete topic and FAQ content

For full self-contained documentation (not summaries), read:

- `topics-complete.md` — complete coverage of every `docs/source/topics/*.rst` file
- `faq-complete.md` — complete coverage of every `docs/source/faq/*.rst` file

## Examples catalog (ready-to-adapt patterns)

- `hello_world`: minimal API call flow
- `echo_bot`: basic text handler
- `welcome_bot`: welcoming logic
- `get_chat_history`: history iteration
- `get_chat_members`: member traversal
- `get_dialogs`: dialog listing
- `callback_queries`: inline button callback handling
- `inline_queries`: inline mode response
- `use_inline_bots`: user-side inline bot usage
- `bot_keyboards`: keyboard markup usage
- `raw_updates`: low-level updates (legacy pattern)

## Handler/decorator index (high-level)

- Message, edited message, deleted messages
- Business connect/message variants
- Callback query, shipping query, pre-checkout query
- Message reaction updates (single/count)
- Inline query, chosen inline result
- Chat member updated, chat join request
- User status, story, poll
- Disconnect, raw update, error

## Error category map

- 303: SeeOther
- 400: BadRequest
- 401: Unauthorized
- 403: Forbidden
- 406: NotAcceptable
- 420: Flood
- 500: InternalServerError

## Enum families (selected)

- Parsing/formatting: `ParseMode`
- Chat/message typing: `ChatType`, `MessageMediaType`, `MessageEntityType`, `MessageServiceType`
- User/chat state: `UserStatus`, `ChatMemberStatus`, `ChatMembersFilter`
- Interaction and reaction: `ChatAction`, `ReactionType`
- Additional platform constants: `ClientPlatform`, colors/privacy-related enums
