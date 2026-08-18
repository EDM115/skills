# Types API (`pyrogram.types`)

Sources:

- `pyrogram/types/**`
- `pyrogram/types/__init__.py`
- `compiler/docs/template/types.rst`

## Package composition

`pyrogram.types` re-exports:

- `authorization`
- `bots_and_keyboards`
- `business`
- `inline_mode`
- `input_media`
- `input_message_content`
- `messages_and_media`
- `user_and_chats`
- `payments`
- `pyromod`
- plus core `Object`, `Update`, `List`

## Complete type inventory by area

### authorization (5)

`ActiveSession`, `ActiveSessions`, `LoginToken`, `SentCode`, `TermsOfService`

### bots_and_keyboards (37)

`BotAllowed`, `BotApp`, `BotBusinessConnection`, `BotCommand`, `BotCommandScope`, `BotCommandScopeAllChatAdministrators`, `BotCommandScopeAllGroupChats`, `BotCommandScopeAllPrivateChats`, `BotCommandScopeChat`, `BotCommandScopeChatAdministrators`, `BotCommandScopeChatMember`, `BotCommandScopeDefault`, `BotInfo`, `CallbackGame`, `CallbackQuery`, `CollectibleItemInfo`, `ForceReply`, `GameHighScore`, `InlineKeyboardButton`, `InlineKeyboardButtonBuy`, `InlineKeyboardMarkup`, `KeyboardButton`, `LoginUrl`, `MenuButton`, `MenuButtonCommands`, `MenuButtonDefault`, `MenuButtonWebApp`, `ReplyKeyboardMarkup`, `ReplyKeyboardRemove`, `RequestPeerTypeChannel`, `RequestPeerTypeChat`, `RequestPeerTypeUser`, `RequestedChat`, `RequestedChats`, `RequestedUser`, `SentWebAppMessage`, `WebAppInfo`

### business (4)

`PreCheckoutQuery`, `ShippingAddress`, `ShippingOption`, `ShippingQuery`

### inline_mode (20)

`ChosenInlineResult`, `InlineQuery`, `InlineQueryResult`, `InlineQueryResultAnimation`, `InlineQueryResultArticle`, `InlineQueryResultAudio`, `InlineQueryResultCachedAnimation`, `InlineQueryResultCachedAudio`, `InlineQueryResultCachedDocument`, `InlineQueryResultCachedPhoto`, `InlineQueryResultCachedSticker`, `InlineQueryResultCachedVideo`, `InlineQueryResultCachedVoice`, `InlineQueryResultContact`, `InlineQueryResultDocument`, `InlineQueryResultLocation`, `InlineQueryResultPhoto`, `InlineQueryResultVenue`, `InlineQueryResultVideo`, `InlineQueryResultVoice`

### input_media (9)

`InputMedia`, `InputMediaAnimation`, `InputMediaArea`, `InputMediaAreaChannelPost`, `InputMediaAudio`, `InputMediaDocument`, `InputMediaPhoto`, `InputMediaVideo`, `InputPhoneContact`

### input_message_content (10)

`InputContactMessageContent`, `InputInvoiceMessageContent`, `InputLocationMessageContent`, `InputMessageContent`, `InputReplyToMessage`, `InputReplyToMonoforum`, `InputReplyToStory`, `InputTextMessageContent`, `InputTodoTask`, `InputVenueMessageContent`

### messages_and_media (68)

`AlternativeVideo`, `Animation`, `Audio`, `AvailableEffect`, `ChatTheme`, `ChatWallpaper`, `Contact`, `ContactRegistered`, `Dice`, `Document`, `ExportedStoryLink`, `ExternalReplyInfo`, `Game`, `Giveaway`, `GiveawayLaunched`, `GiveawayResult`, `Location`, `MediaArea`, `MediaAreaChannelPost`, `MediaAreaCoordinates`, `Message`, `MessageEntity`, `MessageOrigin`, `MessageOriginChannel`, `MessageOriginChat`, `MessageOriginHiddenUser`, `MessageOriginImport`, `MessageOriginUser`, `MessageReactionCountUpdated`, `MessageReactionUpdated`, `MessageReactions`, `MessageReactor`, `MessageStory`, `Photo`, `Poll`, `PollOption`, `Reaction`, `ReadParticipant`, `ScreenshotTaken`, `Sticker`, `StickerSet`, `StoriesPrivacyRules`, `Story`, `StoryDeleted`, `StoryForwardHeader`, `StorySkipped`, `StoryViews`, `Str`, `StrippedThumbnail`, `TextQuote`, `Thumbnail`, `TodoList`, `TodoTask`, `TodoTasksAdded`, `TodoTasksCompleted`, `TodoTasksIncompleted`, `TranscribedAudio`, `TranslatedText`, `Venue`, `Video`, `VideoNote`, `Voice`, `Wallpaper`, `WallpaperSettings`, `WebAppData`, `WebPage`, `WebPageEmpty`, `WebPagePreview`

### payments (18)

`CheckedGiftCode`, `ExtendedMediaPreview`, `Gift`, `GiftAttribute`, `GiftCode`, `GiftedPremium`, `InputStarsTransaction`, `Invoice`, `LabeledPrice`, `PaidMedia`, `PaidMessagePriceChanged`, `PaymentForm`, `PaymentInfo`, `PaymentRefunded`, `PurchasedPaidMedia`, `StarsStatus`, `StarsTransaction`, `SuccessfulPayment`

### pyromod (2)

`Identifier`, `Listener`

### user_and_chats (47)

`Birthday`, `BotVerification`, `BusinessInfo`, `BusinessMessage`, `BusinessRecipients`, `BusinessWeeklyOpen`, `BusinessWorkingHours`, `Chat`, `ChatAdminWithInviteLinks`, `ChatColor`, `ChatEvent`, `ChatEventFilter`, `ChatInviteLink`, `ChatJoinRequest`, `ChatJoinedByRequest`, `ChatJoiner`, `ChatMember`, `ChatMemberUpdated`, `ChatPermissions`, `ChatPhoto`, `ChatPreview`, `ChatPrivileges`, `ChatReactions`, `Dialog`, `EmojiStatus`, `ExportedFolderLink`, `Folder`, `ForumTopic`, `ForumTopicClosed`, `ForumTopicCreated`, `ForumTopicDeleted`, `ForumTopicEdited`, `ForumTopicReopened`, `GeneralTopicHidden`, `GeneralTopicUnhidden`, `GroupCallMember`, `InviteLinkImporter`, `Link`, `PeerChannel`, `PeerUser`, `Restriction`, `User`, `Username`, `VideoChatEnded`, `VideoChatMembersInvited`, `VideoChatScheduled`, `VideoChatStarted`

---

## Deep coverage: `Message` class

Source: `pyrogram/types/messages_and_media/message.py`

### Class role

- `Message` is the central high-level update/data object for text/media/service events.
- Inherits from `Object` and `Update`.
- Supports bound methods for replying/editing/forwarding/downloading and more.

### Constructor signature (exact parameters)

`Message(*, client=None, id, message_thread_id=None, business_connection_id=None, from_user=None, sender_chat=None, sender_business_bot=None, date=None, chat=None, topic=None, forward_origin=None, is_topic_message=None, reply_to_chat_id=None, reply_to_message_id=None, reply_to_story_id=None, reply_to_story_user_id=None, reply_to_story_chat_id=None, reply_to_top_message_id=None, reply_to_message=None, reply_to_story=None, mentioned=None, empty=None, service=None, scheduled=None, from_scheduled=None, edit_hide=None, media=None, edit_date=None, media_group_id=None, author_signature=None, has_protected_content=None, has_media_spoiler=None, text=None, entities=None, caption_entities=None, quote=None, effect_id=None, invert_media=None, audio=None, document=None, photo=None, paid_media=None, todo=None, sticker=None, animation=None, game=None, giveaway=None, giveaway_result=None, boosts_applied=None, chat_theme_updated=None, chat_wallpaper_updated=None, contact_registered=None, gift_code=None, gift=None, screenshot_taken=None, paid_message_price_changed=None, todo_tasks_added=None, todo_tasks_completed=None, todo_tasks_incompleted=None, invoice=None, story=None, alternative_videos=None, video=None, voice=None, video_note=None, web_page_preview=None, caption=None, contact=None, location=None, venue=None, poll=None, dice=None, new_chat_members=None, chat_joined_by_request=None, left_chat_member=None, new_chat_title=None, new_chat_photo=None, delete_chat_photo=None, group_chat_created=None, supergroup_chat_created=None, channel_chat_created=None, migrate_to_chat_id=None, migrate_from_chat_id=None, pinned_message=None, game_high_score=None, views=None, forwards=None, via_bot=None, outgoing=None, external_reply=None, matches=None, command=None, bot_allowed=None, chats_shared=None, forum_topic_created=None, forum_topic_closed=None, forum_topic_reopened=None, forum_topic_edited=None, general_topic_hidden=None, general_topic_unhidden=None, gifted_premium=None, giveaway_launched=None, video_chat_scheduled=None, video_chat_started=None, video_chat_ended=None, video_chat_members_invited=None, web_app_data=None, successful_payment=None, payment_refunded=None, reply_markup=None, reactions=None, chat_join_type=None, raw=None)`

### Key semantic field groups

- Identity/threading: `id`, `message_thread_id`, `chat`, `topic`
- Sender/origin: `from_user`, `sender_chat`, `sender_business_bot`, `forward_origin`
- Reply linkage: `reply_to_*`, `quote`, `external_reply`
- Text/media core: `text`, `caption`, `entities`, `caption_entities`, `media`, `service`
- Media payloads: `audio`, `document`, `photo`, `video`, `animation`, `voice`, `video_note`, `sticker`, `poll`, `dice`, etc.
- Service payloads: member join/leave, forum actions, video chat, gifts/payments, todo actions
- Meta: `views`, `forwards`, `outgoing`, `scheduled`, `from_scheduled`, `has_protected_content`, `has_media_spoiler`
- Interaction parse helpers: `matches` (regex), `command` (command filter)
- Low-level object: `raw`

### Properties

- `link` — message deep link generation for private/group/channel contexts.
- `content` — unified text-or-caption accessor.

### Deprecated compatibility properties

- `forward_from`
- `forward_sender_name`
- `forward_from_chat`
- `forward_from_message_id`
- `forward_signature`
- `forward_date`

Deprecated fields proxy modern `forward_origin` data.
