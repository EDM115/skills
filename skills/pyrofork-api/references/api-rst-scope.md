# docs/source/api scope (exact)

This file maps every `docs/source/api` page to the source symbol(s) it documents.

## Top-level API pages

- `api/client.rst`
  - `.. autoclass:: pyrogram.Client()`
- `api/filters.rst`
  - `.. automodule:: pyrogram.filters`
  - `:members:`
- `api/handlers.rst`
  - explicit handler classes via `.. autoclass:: <HandlerName>()`
- `api/decorators.rst`
  - explicit decorator methods via `.. autodecorator:: pyrogram.Client.on_*()`

## Generated API sections (template-backed)

The repository ships API generation templates under `compiler/docs/template` for additional API pages:

- `methods.rst` template -> `api/methods/*`
- `types.rst` template -> `api/types/*`
- `bound-methods.rst` template -> `api/bound-methods/*`

These pages are generated during docs compilation and may not all exist as static files in `docs/source/api`.
This is why tree-only scanning of `docs/source/api` under-reports API coverage.

## Enumerations (`api/enums/*.rst`)

Each page uses:

- `.. autoclass:: pyrogram.enums.<EnumName>()`
- `:members:`

Enum index file: `api/enums/index.rst`.

## RPC Errors (`api/errors/*.rst`)

- `api/errors/index.rst` is category index.
- Category files use `.. csv-table::` pointing to generated TSV catalogs:
  - `compiler/errors/source/303_SEE_OTHER.tsv`
  - `compiler/errors/source/400_BAD_REQUEST.tsv`
  - `compiler/errors/source/401_UNAUTHORIZED.tsv`
  - `compiler/errors/source/403_FORBIDDEN.tsv`
  - `compiler/errors/source/406_NOT_ACCEPTABLE.tsv`
  - `compiler/errors/source/420_FLOOD.tsv`
  - `compiler/errors/source/500_INTERNAL_SERVER_ERROR.tsv`

## Decorators documented by API page

- `on_bot_business_connect`
- `on_message`
- `on_bot_business_message`
- `on_edited_message`
- `on_edited_bot_business_message`
- `on_callback_query`
- `on_shipping_query`
- `on_pre_checkout_query`
- `on_message_reaction_updated`
- `on_message_reaction_count_updated`
- `on_inline_query`
- `on_chosen_inline_result`
- `on_chat_member_updated`
- `on_chat_join_request`
- `on_deleted_messages`
- `on_deleted_bot_business_message` (docs label; code exposes plural form)
- `on_user_status`
- `on_story`
- `on_poll`
- `on_disconnect`
- `on_raw_update`
- `on_error`

## Handler classes documented by API page

- `BotBusinessConnectHandler`
- `MessageHandler`
- `BotBusinessMessageHandler`
- `EditedMessageHandler`
- `EditedBotBusinessMessageHandler`
- `DeletedMessagesHandler`
- `DeletedBotBusinessMessagesHandler`
- `CallbackQueryHandler`
- `PreCheckoutQueryHandler`
- `ShippingQueryHandler`
- `MessageReactionUpdatedHandler`
- `MessageReactionCountUpdatedHandler`
- `InlineQueryHandler`
- `ChosenInlineResultHandler`
- `ChatMemberUpdatedHandler`
- `UserStatusHandler`
- `StoryHandler`
- `PollHandler`
- `DisconnectHandler`
- `RawUpdateHandler`
- `ErrorHandler`
