# Decorators API (`pyrogram.Client.on_*`)

Sources:

- `pyrogram/methods/decorators/*.py`
- API page: `docs/source/api/decorators.rst`

Decorator methods register callback handlers by internally constructing the corresponding handler and calling `add_handler`.

## Common signature pattern

Most decorators use:

- `(filters=None, group=0)`

Exception:

- `on_error(errors=None, group=0)`

## Complete decorator list

- `on_bot_business_connect(filters=None, group=0)`
  - handles bot business connection updates
- `on_message(filters=None, group=0)`
  - handles new messages
- `on_bot_business_message(filters=None, group=0)`
  - handles bot business messages
- `on_edited_message(filters=None, group=0)`
  - handles edited messages
- `on_edited_bot_business_message(filters=None, group=0)`
  - handles edited bot business messages
- `on_callback_query(filters=None, group=0)`
  - handles callback queries
- `on_shipping_query(filters=None, group=0)`
  - handles shipping queries
- `on_pre_checkout_query(filters=None, group=0)`
  - handles pre-checkout queries
- `on_message_reaction_updated(filters=None, group=0)`
  - handles message reaction updates
- `on_message_reaction_count_updated(filters=None, group=0)`
  - handles anonymous/count reaction updates
- `on_inline_query(filters=None, group=0)`
  - handles inline queries
- `on_chosen_inline_result(filters=None, group=0)`
  - handles chosen inline results
- `on_chat_member_updated(filters=None, group=0)`
  - handles chat member status changes
- `on_chat_join_request(filters=None, group=0)`
  - handles join requests
- `on_deleted_messages(filters=None, group=0)`
  - handles deleted messages
- `on_deleted_bot_business_messages(filters=None, group=0)`
  - handles deleted bot business messages
- `on_user_status(filters=None, group=0)`
  - handles user online/offline status updates
- `on_story(filters=None, group=0)`
  - handles story updates
- `on_poll(filters=None, group=0)`
  - handles poll updates
- `on_disconnect(filters=None, group=0)`
  - handles disconnect events
- `on_raw_update(filters=None, group=0)`
  - handles raw MTProto updates
- `on_error(errors=None, group=0)`
  - handles raised errors routed through dispatcher
- `on_purchased_paid_media(filters=None, group=0)`
  - present in source mixin set (not listed in current API rst index)

## Notes for autonomous agents

- `group` controls dispatch priority (lower number = higher priority).
- `filters` controls update admission before callback invocation.
- callbacks must match expected update type for the associated handler.
