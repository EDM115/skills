# Bound Methods API (`pyrogram.types`)

Sources:

- `compiler/docs/template/bound-methods.rst`
- type classes in `pyrogram/types/**`

Bound methods are instance-level convenience wrappers over `Client` methods.

## Message bound methods (46)

`wait_for_click`, `link`, `content`, `forward_from`, `forward_sender_name`, `forward_from_chat`, `forward_from_message_id`, `forward_signature`, `forward_date`, `get_media_group`, `reply_text`, `reply_animation`, `reply_audio`, `reply_cached_media`, `reply_chat_action`, `reply_contact`, `reply_document`, `reply_game`, `reply_inline_bot_result`, `reply_location`, `reply_media_group`, `reply_photo`, `reply_poll`, `reply_sticker`, `reply_venue`, `reply_video`, `reply_video_note`, `reply_voice`, `reply_web_page`, `edit_text`, `edit_caption`, `edit_media`, `edit_reply_markup`, `forward`, `copy`, `delete`, `click`, `react`, `retract_vote`, `download`, `vote`, `pin`, `unpin`, `ask`, `transcribe`, `translate`

## Story bound methods (20)

`reply_text`, `reply_animation`, `reply_audio`, `reply_cached_media`, `reply_media_group`, `reply_photo`, `reply_sticker`, `reply_video`, `reply_video_note`, `reply_voice`, `delete`, `edit_animation`, `edit`, `edit_caption`, `edit_photo`, `edit_privacy`, `edit_video`, `export_link`, `forward`, `download`

## Chat bound methods (22)

`full_name`, `listen`, `ask`, `stop_listening`, `archive`, `unarchive`, `set_title`, `set_description`, `set_photo`, `ban_member`, `unban_member`, `restrict_member`, `promote_member`, `join`, `leave`, `export_invite_link`, `get_member`, `get_members`, `add_members`, `mark_unread`, `set_protected_content`, `unpin_all_messages`

## User bound methods (10)

`full_name`, `mention`, `listen`, `ask`, `stop_listening`, `archive`, `unarchive`, `block`, `unblock`, `get_common_chats`

## CallbackQuery bound methods (5)

`answer`, `edit_message_text`, `edit_message_caption`, `edit_message_media`, `edit_message_reply_markup`

## InlineQuery bound methods (1)

`answer`

## PreCheckoutQuery bound methods (1)

`answer`

## ShippingQuery bound methods (1)

`answer`

## ChatJoinRequest bound methods (2)

`approve`, `decline`

## Folder bound methods (8)

`delete`, `update`, `include_chat`, `exclude_chat`, `update_color`, `pin_chat`, `remove_chat`, `export_link`

## Gift bound methods (7)

`link`, `show`, `hide`, `convert`, `upgrade`, `transfer`, `wear`
