# Handlers API (`pyrogram.handlers`)

Sources:

- `pyrogram/handlers/*_handler.py`
- API page: `docs/source/api/handlers.rst`

## Base constructor contracts

Most handlers:

- `(callback, filters=None)`

Special cases:

- `DisconnectHandler(callback)`
- `ConversationHandler()` (special-purpose orchestration handler)

## Complete handler list

- `BotBusinessConnectHandler(callback, filters=None)`
- `MessageHandler(callback, filters=None)`
- `BotBusinessMessageHandler(callback, filters=None)`
- `EditedMessageHandler(callback, filters=None)`
- `EditedBotBusinessMessageHandler(callback, filters=None)`
- `DeletedMessagesHandler(callback, filters=None)`
- `DeletedBotBusinessMessagesHandler(callback, filters=None)`
- `CallbackQueryHandler(callback, filters=None)`
- `PreCheckoutQueryHandler(callback, filters=None)`
- `ShippingQueryHandler(callback, filters=None)`
- `MessageReactionUpdatedHandler(callback, filters=None)`
- `MessageReactionCountUpdatedHandler(callback, filters=None)`
- `InlineQueryHandler(callback, filters=None)`
- `ChosenInlineResultHandler(callback, filters=None)`
- `ChatMemberUpdatedHandler(callback, filters=None)`
- `UserStatusHandler(callback, filters=None)`
- `StoryHandler(callback, filters=None)`
- `PollHandler(callback, filters=None)`
- `DisconnectHandler(callback)`
- `RawUpdateHandler(callback, filters=None)`
- `ErrorHandler(callback, filters=None)`

## Additional exported handlers (source-level)

- `ChatJoinRequestHandler(callback, filters=None)`
- `PurchasedPaidMediaHandler(callback, filters=None)`

These are present in `pyrogram.handlers` exports; API rst page may lag their inclusion.

## Callback typing expectations (high level)

- message-like handlers -> callback `(client, message)`
- callback query handlers -> `(client, callback_query)`
- inline query handlers -> `(client, inline_query)`
- shipping/pre-checkout -> `(client, query)`
- raw update handler -> `(client, update, users, chats)` style low-level payload usage
- error handler -> `(client, update, error)` style error channel handling

## Dispatch behavior interaction

- handler instances are registered with `add_handler(handler, group=0)`.
- filters are evaluated before callback invocation.
- group ordering and propagation behavior follows dispatcher rules.
