# Methods API (`pyrogram.methods` / `pyrogram.Client`)

Sources:

- `pyrogram/methods/**`
- `pyrogram/methods/__init__.py` (`Methods` mixin composition)
- `compiler/docs/template/methods.rst`

`Client` inherits `Methods`, which aggregates domains listed below.

## Domain composition (`Methods`)

- `Advanced`
- `Auth`
- `Bots`
- `Contacts`
- `Password`
- `Pyromod`
- `Payments`
- `Phone`
- `Chats`
- `Forums`
- `Stickers`
- `Users`
- `Messages`
- `Decorators`
- `Utilities`
- `InviteLinks`
- `TelegramBusiness`

## Complete method inventory by domain

### advanced (3)

`invoke`, `resolve_peer`, `save_file`

### auth (15)

`check_password`, `connect`, `disconnect`, `get_active_sessions`, `get_password_hint`, `initialize`, `log_out`, `recover_password`, `resend_code`, `send_code`, `send_recovery_code`, `sign_in`, `sign_in_bot`, `sign_in_qrcode`, `terminate`

### bots (21)

`answer_callback_query`, `answer_inline_query`, `answer_web_app_query`, `delete_bot_commands`, `get_bot_commands`, `get_bot_default_privileges`, `get_bot_info`, `get_chat_menu_button`, `get_collectible_item_info`, `get_game_high_scores`, `get_inline_bot_results`, `get_owned_bots`, `get_similar_bots`, `request_callback_answer`, `send_game`, `send_inline_bot_result`, `set_bot_commands`, `set_bot_default_privileges`, `set_bot_info`, `set_chat_menu_button`, `set_game_score`

### business (7)

`answer_pre_checkout_query`, `answer_shipping_query`, `delete_business_messages`, `get_business_account_gifts`, `get_business_account_star_balance`, `get_business_connection`, `transfer_business_account_stars`

### chats (44)

`add_chat_members`, `archive_chats`, `ban_chat_member`, `create_channel`, `create_group`, `create_supergroup`, `delete_channel`, `delete_chat_photo`, `delete_folder`, `delete_supergroup`, `delete_user_history`, `export_folder_link`, `get_chat`, `get_chat_event_log`, `get_chat_member`, `get_chat_members`, `get_chat_members_count`, `get_chat_online_count`, `get_dialogs`, `get_dialogs_count`, `get_folders`, `get_send_as_chats`, `join_chat`, `leave_chat`, `mark_chat_unread`, `pin_chat_message`, `promote_chat_member`, `restrict_chat_member`, `set_administrator_title`, `set_chat_description`, `set_chat_permissions`, `set_chat_photo`, `set_chat_protected_content`, `set_chat_title`, `set_chat_username`, `set_send_as_chat`, `set_slow_mode`, `transfer_chat_ownership`, `unarchive_chats`, `unban_chat_member`, `unpin_all_chat_messages`, `unpin_chat_message`, `update_color`, `update_folder`

### contacts (5)

`add_contact`, `delete_contacts`, `get_contacts`, `get_contacts_count`, `import_contacts`

### decorators (23)

`on_bot_business_connect`, `on_bot_business_message`, `on_callback_query`, `on_chat_join_request`, `on_chat_member_updated`, `on_chosen_inline_result`, `on_deleted_bot_business_messages`, `on_deleted_messages`, `on_disconnect`, `on_edited_bot_business_message`, `on_edited_message`, `on_error`, `on_inline_query`, `on_message`, `on_message_reaction_count_updated`, `on_message_reaction_updated`, `on_poll`, `on_pre_checkout_query`, `on_purchased_paid_media`, `on_raw_update`, `on_shipping_query`, `on_story`, `on_user_status`

### forums (13)

`close_forum_topic`, `close_general_topic`, `create_forum_topic`, `delete_forum_topic`, `edit_forum_topic`, `edit_general_topic`, `get_forum_topics`, `get_forum_topics_by_id`, `get_forum_topics_count`, `hide_general_topic`, `reopen_forum_topic`, `reopen_general_topic`, `unhide_general_topic`

### invite_links (17)

`approve_all_chat_join_requests`, `approve_chat_join_request`, `create_chat_invite_link`, `decline_all_chat_join_requests`, `decline_chat_join_request`, `delete_chat_admin_invite_links`, `delete_chat_invite_link`, `edit_chat_invite_link`, `export_chat_invite_link`, `get_chat_admin_invite_links`, `get_chat_admin_invite_links_count`, `get_chat_admins_with_invite_links`, `get_chat_invite_link`, `get_chat_invite_link_joiners`, `get_chat_invite_link_joiners_count`, `get_chat_join_requests`, `revoke_chat_invite_link`

### messages (63)

`add_task_to_todo`, `copy_media_group`, `copy_message`, `delete_chat_history`, `delete_messages`, `delete_scheduled_messages`, `download_media`, `edit_inline_caption`, `edit_inline_media`, `edit_inline_reply_markup`, `edit_inline_text`, `edit_message_caption`, `edit_message_media`, `edit_message_reply_markup`, `edit_message_text`, `forward_media_group`, `forward_messages`, `get_available_effects`, `get_chat_history`, `get_chat_history_count`, `get_custom_emoji_stickers`, `get_discussion_message`, `get_discussion_replies`, `get_discussion_replies_count`, `get_media_group`, `get_message_read_participants`, `get_messages`, `get_scheduled_messages`, `read_chat_history`, `retract_vote`, `search_global`, `search_global_count`, `search_global_hashtag_messages`, `search_global_hashtag_messages_count`, `search_messages`, `search_messages_count`, `send_animation`, `send_audio`, `send_cached_media`, `send_chat_action`, `send_contact`, `send_dice`, `send_document`, `send_location`, `send_media_group`, `send_message`, `send_photo`, `send_poll`, `send_reaction`, `send_sticker`, `send_todo`, `send_venue`, `send_video`, `send_video_note`, `send_voice`, `send_web_page`, `set_todo_tasks_completion`, `start_bot`, `stop_poll`, `stream_media`, `transcribe_audio`, `translate_message_text`, `vote_poll`

### password (3)

`change_cloud_password`, `enable_cloud_password`, `remove_cloud_password`

### payments (26)

`apply_gift_code`, `check_gift_code`, `convert_gift`, `create_invoice_link`, `get_available_gifts`, `get_chat_gifts`, `get_chat_gifts_count`, `get_payment_form`, `get_stars_balance`, `get_stars_transactions`, `get_stars_transactions_by_id`, `get_upgraded_gift`, `hide_gift`, `refund_star_payment`, `search_gifts_for_resale`, `send_gift`, `send_invoice`, `send_paid_media`, `send_paid_reaction`, `send_payment_form`, `send_resold_gift`, `set_gift_resale_price`, `set_pinned_gifts`, `show_gift`, `transfer_gift`, `upgrade_gift`

### phone (1)

`get_call_members`

### pyromod (12)

`ask`, `get_listener_matching_with_data`, `get_listener_matching_with_identifier_pattern`, `get_many_listeners_matching_with_data`, `get_many_listeners_matching_with_identifier_pattern`, `listen`, `register_next_step_handler`, `remove_listener`, `stop_listener`, `stop_listening`, `wait_for_callback_query`, `wait_for_message`

### stickers (3)

`add_sticker_to_set`, `create_sticker_set`, `get_sticker_set`

### users (24)

`block_user`, `delete_profile_photos`, `delete_stories`, `edit_story`, `export_story_link`, `forward_story`, `get_all_stories`, `get_chat_photos`, `get_chat_photos_count`, `get_common_chats`, `get_default_emoji_statuses`, `get_me`, `get_peer_stories`, `get_stories`, `get_stories_history`, `get_users`, `send_story`, `set_emoji_status`, `set_profile_photo`, `set_username`, `unblock_user`, `update_birthday`, `update_personal_chat`, `update_profile`

### utilities (11)

`add_handler`, `export_session_string`, `ping`, `remove_error_handler`, `remove_handler`, `restart`, `run`, `run_sync`, `start`, `stop`, `stop_transmission`
