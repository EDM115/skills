---
name: api-api-enums
description: Offline API backup extracted from Pyrofork source docstrings.
---

# Pyrofork API Backup: `enums`

Extracted from `sources/pyrofork/pyrogram/**.py` using AST parsing of module, class, function, and method docstrings.

## File: `enums/__init__.py`

---

## File: `enums/auto_name.py`

### Classes

#### `class AutoName(Enum)`

_No docstring._

##### Methods

###### `def _generate_next_value_(self, *args)`

_No docstring._

###### `def __repr__(self)`

_No docstring._

---

## File: `enums/business_schedule.py`

### Classes

#### `class BusinessSchedule(AutoName)`

```text
Business away enumeration used in :obj:`~pyrogram.types.BusinessInfo`.
```

---

## File: `enums/chat_action.py`

### Classes

#### `class ChatAction(AutoName)`

```text
Chat action enumeration used in :obj:`~pyrogram.types.ChatEvent`.
```

---

## File: `enums/chat_event_action.py`

### Classes

#### `class ChatEventAction(AutoName)`

```text
Chat event action enumeration used in :meth:`~pyrogram.Client.get_chat_event_log`.
```

---

## File: `enums/chat_join_type.py`

### Classes

#### `class ChatJoinType(AutoName)`

```text
How the service message :obj:`~pyrogram.enums.MessageServiceType.NEW_CHAT_MEMBERS` was used for the member to join the chat.
```

---

## File: `enums/chat_member_status.py`

### Classes

#### `class ChatMemberStatus(AutoName)`

```text
Chat member status enumeration used in :obj:`~pyrogram.types.ChatMember`.
```

---

## File: `enums/chat_members_filter.py`

### Classes

#### `class ChatMembersFilter(AutoName)`

```text
Chat members filter enumeration used in :meth:`~pyrogram.Client.get_chat_members`
```

---

## File: `enums/chat_type.py`

### Classes

#### `class ChatType(AutoName)`

```text
Chat type enumeration used in :obj:`~pyrogram.types.Chat`.
```

---

## File: `enums/client_platform.py`

### Classes

#### `class ClientPlatform(AutoName)`

```text
Valid platforms for a :obj:`~pyrogram.Client`.
```

---

## File: `enums/folder_color.py`

### Classes

#### `class FolderColor(AutoName)`

```text
Folder color enumeration used in :obj:`~pyrogram.types.Folder`.
```

---

## File: `enums/gift_attribute_type.py`

### Classes

#### `class GiftAttributeType(AutoName)`

```text
Star gift attribute type enumeration used in :obj:`~pyrogram.types.GiftAttribute`.
```

---

## File: `enums/gift_for_resale_order.py`

### Classes

#### `class GiftForResaleOrder(AutoName)`

```text
Describes order in which upgraded gifts for resale will be sorted. Used in :meth:`~pyrogram.Client.search_gifts_for_resale`.
```

---

## File: `enums/listerner_types.py`

### Classes

#### `class ListenerTypes(AutoName)`

```text
Listener type enumeration used in :obj:`~pyrogram.types.Client`.
```

---

## File: `enums/message_entity_type.py`

### Classes

#### `class MessageEntityType(AutoName)`

```text
Message entity type enumeration used in :obj:`~pyrogram.types.MessageEntity`.
```

---

## File: `enums/message_media_type.py`

### Classes

#### `class MessageMediaType(AutoName)`

```text
Message media type enumeration used in :obj:`~pyrogram.types.Message`.
```

---

## File: `enums/message_origin_type.py`

### Classes

#### `class MessageOriginType(AutoName)`

```text
Message origin type enumeration used in :obj:`~pyrogram.types.MessageOrigin`.
```

---

## File: `enums/message_service_type.py`

### Classes

#### `class MessageServiceType(AutoName)`

```text
Message service type enumeration used in :obj:`~pyrogram.types.Message`.
```

---

## File: `enums/messages_filter.py`

### Classes

#### `class MessagesFilter(AutoName)`

```text
Messages filter enumeration used in :meth:`~pyrogram.Client.search_messages` and :meth:`~pyrogram.Client.search_global`
```

---

## File: `enums/next_code_type.py`

### Classes

#### `class NextCodeType(AutoName)`

```text
Next code type enumeration used in :obj:`~pyrogram.types.SentCode`.
```

---

## File: `enums/parse_mode.py`

### Classes

#### `class ParseMode(AutoName)`

```text
Parse mode enumeration used in various places to set a specific parse mode
```

---

## File: `enums/poll_type.py`

### Classes

#### `class PollType(AutoName)`

```text
Poll type enumeration used in :obj:`~pyrogram.types.Poll`.
```

---

## File: `enums/profile_color.py`

### Classes

#### `class ProfileColor(AutoName)`

```text
Profile color enumeration used in :meth:`~pyrogram.Client.update_color` and :obj:`~pyrogram.types.ChatColor`.
```

---

## File: `enums/reaction_type.py`

### Classes

#### `class ReactionType(AutoName)`

```text
Reaction type enumeration used in :obj:`~pyrogram.types.ReactionType`.
```

---

## File: `enums/reply_color.py`

### Classes

#### `class ReplyColor(AutoName)`

```text
Reply color enumeration used in :meth:`~pyrogram.Client.update_color` and :obj:`~pyrogram.types.ChatColor`.
```

---

## File: `enums/sent_code_type.py`

### Classes

#### `class SentCodeType(AutoName)`

```text
Sent code type enumeration used in :obj:`~pyrogram.types.SentCode`.
```

---

## File: `enums/stories_privacy_rules.py`

### Classes

#### `class StoriesPrivacyRules(AutoName)`

```text
Stories privacy rules type enumeration used in :meth:`~pyrogram.Client.send_story` and :meth:`~pyrogram.Client.edit_story`.
```

---

## File: `enums/story_privacy.py`

### Classes

#### `class StoryPrivacy(AutoName)`

```text
Story privacy type enumeration used in :obj:`~pyrogram.types.Story`.
```

---

## File: `enums/user_status.py`

### Classes

#### `class UserStatus(AutoName)`

```text
User status enumeration used in :obj:`~pyrogram.types.User`.
```

---
