---
name: api-api-types
description: Offline API backup extracted from Pyrofork source docstrings.
---

# Pyrofork API Backup: `types`

Extracted from `sources/pyrofork/pyrogram/**.py` using AST parsing of module, class, function, and method docstrings.

## File: `types/__init__.py`

---

## File: `types/authorization/__init__.py`

---

## File: `types/authorization/active_session.py`

### Classes

#### `class ActiveSession(Object)`

```text
Contains information about one session in a Telegram application used by the current user. Sessions must be shown to the user in the returned order.

Parameters:
    id (``int``):
        Session identifier.

    device_model (``str``):
        Model of the device the application has been run or is running on, as provided by the application.

    platform (``str``):
        Operating system the application has been run or is running on, as provided by the application.

    system_version (``str``):
        Version of the operating system the application has been run or is running on, as provided by the application.

    api_id (``int``):
        Telegram API identifier, as provided by the application.

    application_name (``str``):
        Name of the application, as provided by the application.

    application_version (``str``):
        The version of the application, as provided by the application.

    log_in_date (:py:obj:`~datetime.datetime`, *optional*):
        Point in time (Unix timestamp) when the user has logged in.

    last_active_date (:py:obj:`~datetime.datetime`, *optional*):
        Point in time (Unix timestamp) when the session was last used.

    ip_address (``str``):
        IP address from which the session was created, in human-readable format.

    location (``str``):
        A human-readable description of the location from which the session was created, based on the IP address.

    country (``str``):
        Country.

    is_current (``bool``):
        True, if this session is the current session.

    is_password_pending (``bool``):
        True, if a 2-step verification password is needed to complete authorization of the session.

    is_unconfirmed (``bool``):
        True, if the session wasn't confirmed from another session.

    can_accept_secret_chats (``bool``):
        True, if incoming secret chats can be accepted by the session.

    can_accept_calls (``bool``):
        True, if incoming calls can be accepted by the session.

    is_official_application (``bool``):
        True, if the application is an official application or uses the api_id of an official application.
```

##### Methods

###### `def __init__(self, *, id: int = None, device_model: str = None, platform: str = None, system_version: str = None, api_id: int = None, application_name: str = None, application_version: str = None, log_in_date: datetime = None, last_active_date: datetime = None, ip_address: str = None, location: str = None, country: str = None, is_current: bool = None, is_password_pending: bool = None, is_unconfirmed: bool = None, can_accept_secret_chats: bool = None, can_accept_calls: bool = None, is_official_application: bool = None)`

_No docstring._

###### `def _parse(session: 'raw.types.Authorization') -> 'ActiveSession'`

_No docstring._

---

## File: `types/authorization/active_sessions.py`

### Classes

#### `class ActiveSessions(Object)`

```text
Contains a list of sessions

Parameters:
    inactive_session_ttl_days (``int``):
        Number of days of inactivity before sessions will automatically be terminated; 1-366 days.

    active_sessions (List of :obj:`~pyrogram.types.ActiveSession`):
        List of sessions.
```

##### Methods

###### `def __init__(self, *, inactive_session_ttl_days: int = None, active_sessions: List['types.ActiveSession'] = None)`

_No docstring._

###### `def _parse(authorizations: 'raw.types.account.Authorizations') -> 'ActiveSessions'`

_No docstring._

---

## File: `types/authorization/login_token.py`

### Classes

#### `class LoginToken(Object)`

```text
Contains info on a login token.

Parameters:
    token (``str``):
        The login token.

    expires (``int``):
        The expiration date of the token in UNIX format.
```

##### Methods

###### `def __init__(self, *, token: str, expires: int)`

_No docstring._

###### `def _parse(login_token: 'raw.base.LoginToken') -> 'LoginToken'`

_No docstring._

---

## File: `types/authorization/sent_code.py`

### Classes

#### `class SentCode(Object)`

```text
Contains info on a sent confirmation code.

Parameters:
    type (:obj:`~pyrogram.enums.SentCodeType`):
        Type of the current sent code.

    phone_code_hash (``str``):
        Confirmation code identifier useful for the next authorization steps (either
        :meth:`~pyrogram.Client.sign_in` or :meth:`~pyrogram.Client.sign_up`).

    next_type (:obj:`~pyrogram.enums.NextCodeType`, *optional*):
        Type of the next code to be sent with :meth:`~pyrogram.Client.resend_code`.

    timeout (``int``, *optional*):
        Delay in seconds before calling :meth:`~pyrogram.Client.resend_code`.
```

##### Methods

###### `def __init__(self, *, type: 'enums.SentCodeType', phone_code_hash: str, next_type: 'enums.NextCodeType' = None, timeout: int = None)`

_No docstring._

###### `def _parse(sent_code: raw.types.auth.SentCode) -> 'SentCode'`

_No docstring._

---

## File: `types/authorization/terms_of_service.py`

### Classes

#### `class TermsOfService(Object)`

```text
Telegram's Terms of Service returned by :meth:`~pyrogram.Client.sign_in`.

Parameters:
    id (``str``):
        Terms of Service identifier.

    text (``str``):
        Terms of Service text.

    entities (List of :obj:`~pyrogram.types.MessageEntity`):
        Special entities like URLs that appear in the text.
```

##### Methods

###### `def __init__(self, *, id: str, text: str, entities: List['types.MessageEntity'])`

_No docstring._

###### `def _parse(terms_of_service: 'raw.types.help.TermsOfService') -> 'TermsOfService'`

_No docstring._

---

## File: `types/bots_and_keyboards/__init__.py`

---

## File: `types/bots_and_keyboards/bot_allowed.py`

### Classes

#### `class BotAllowed(Object)`

```text
Contains information about a allowed bot.

Parameters:
    attach_menu (``bool``, *optional*):
        True, if the bot can attach to menu.

    from_request (``bool``, *optional*):
        True, if the bot is allowed from request.

    domain (``str``, *optional*):
        The domain of the bot.

    app (:obj:`~pyrogram.types.BotApp`, *optional*):
        The app of the bot.
```

##### Methods

###### `def __init__(self, *, attach_menu: Optional[bool] = None, from_request: Optional[bool] = None, domain: Optional[str] = None, app: Optional['types.BotApp'] = None)`

_No docstring._

###### `def _parse(client: 'pyrogram.Client', bot_allowed: 'raw.types.BotAllowed') -> 'BotAllowed'`

_No docstring._

---

## File: `types/bots_and_keyboards/bot_app.py`

### Classes

#### `class BotApp(Object)`

```text
Contains information about a bot app.

Parameters:
    id (``int``):
        The id of the app.

    short_name (``str``):
        The short name of the app.

    title (``str``):
        The title of the app.

    description (``str``):
        The description of the app.

    photo (``types.Photo``):
        The photo of the app.

    document (:obj:`~pyrogram.types.Document`, *optional*):
        The document of the app.
```

##### Methods

###### `def __init__(self, id: int, short_name: str, title: str, description: str, photo: 'types.Photo', document: Optional['types.Document'] = None)`

_No docstring._

###### `def _parse(client: 'pyrogram.Client', bot_app: 'raw.types.BotApp') -> 'BotApp'`

_No docstring._

---

## File: `types/bots_and_keyboards/bot_business_connection.py`

### Classes

#### `class BotBusinessConnection(Object)`

```text
A bot business connection Information.

Parameters:
    bot_connection_id (``str``):
        The business connection identifier.

    user (:obj:`~pyrogram.types.User`):
        The user that connected to the bot.

    dc_id (``int``):
        The user datacenter.

    date (:py:obj:`~datetime.datetime`):
        Date the connection was established in Unix time.

    can_reply (``bool``, *optional*):
        Whether the bot can reply.

    is_disabled (``bool``, *optional*):
        Whether the connection is disabled.
```

##### Methods

###### `def __init__(self, *, client: 'pyrogram.Client' = None, bot_connection_id: str, user: 'pyrogram.types.User', dc_id: int, date: 'datetime.datetime', can_reply: bool = None, is_disabled: bool = None)`

_No docstring._

###### `async def _parse(client: 'pyrogram.Client', bot_connection: 'raw.types.BotBusinessConnection') -> 'BotBusinessConnection'`

_No docstring._

---

## File: `types/bots_and_keyboards/bot_command.py`

### Classes

#### `class BotCommand(Object)`

```text
A bot command with the standard slash "/" prefix.

Parameters:
    command (``str``):
        Text of the command; 1-32 characters.
        Can contain only lowercase English letters, digits and underscores.

    description (``str``):
        Description of the command; 1-256 characters.
```

##### Methods

###### `def __init__(self, command: str, description: str)`

_No docstring._

###### `def write(self) -> 'raw.types.BotCommand'`

_No docstring._

###### `def read(c: 'raw.types.BotCommand') -> 'BotCommand'`

_No docstring._

---

## File: `types/bots_and_keyboards/bot_command_scope.py`

### Classes

#### `class BotCommandScope(Object)`

```text
Represents the scope to which bot commands are applied.

Currently, the following 7 scopes are supported:

- :obj:`~pyrogram.types.BotCommandScopeDefault`
- :obj:`~pyrogram.types.BotCommandScopeAllPrivateChats`
- :obj:`~pyrogram.types.BotCommandScopeAllGroupChats`
- :obj:`~pyrogram.types.BotCommandScopeAllChatAdministrators`
- :obj:`~pyrogram.types.BotCommandScopeChat`
- :obj:`~pyrogram.types.BotCommandScopeChatAdministrators`
- :obj:`~pyrogram.types.BotCommandScopeChatMember`

**Determining list of commands**

The following algorithm is used to determine the list of commands for a particular user viewing the bot menu.
The first list of commands which is set is returned:

**Commands in the chat with the bot**:

- BotCommandScopeChat + language_code
- BotCommandScopeChat
- BotCommandScopeAllPrivateChats + language_code
- BotCommandScopeAllPrivateChats
- BotCommandScopeDefault + language_code
- BotCommandScopeDefault

**Commands in group and supergroup chats**

- BotCommandScopeChatMember + language_code
- BotCommandScopeChatMember
- BotCommandScopeChatAdministrators + language_code (administrators only)
- BotCommandScopeChatAdministrators (administrators only)
- BotCommandScopeChat + language_code
- BotCommandScopeChat
- BotCommandScopeAllChatAdministrators + language_code (administrators only)
- BotCommandScopeAllChatAdministrators (administrators only)
- BotCommandScopeAllGroupChats + language_code
- BotCommandScopeAllGroupChats
- BotCommandScopeDefault + language_code
- BotCommandScopeDefault
```

##### Methods

###### `def __init__(self, type: str)`

_No docstring._

###### `async def write(self, client: 'pyrogram.Client') -> 'raw.base.BotCommandScope'`

_No docstring._

---

## File: `types/bots_and_keyboards/bot_command_scope_all_chat_administrators.py`

### Classes

#### `class BotCommandScopeAllChatAdministrators(BotCommandScope)`

```text
Represents the scope of bot commands, covering all group and supergroup chat administrators.
```

##### Methods

###### `def __init__(self)`

_No docstring._

###### `async def write(self, client: 'pyrogram.Client') -> 'raw.base.BotCommandScope'`

_No docstring._

---

## File: `types/bots_and_keyboards/bot_command_scope_all_group_chats.py`

### Classes

#### `class BotCommandScopeAllGroupChats(BotCommandScope)`

```text
Represents the scope of bot commands, covering all group and supergroup chats.
```

##### Methods

###### `def __init__(self)`

_No docstring._

###### `async def write(self, client: 'pyrogram.Client') -> 'raw.base.BotCommandScope'`

_No docstring._

---

## File: `types/bots_and_keyboards/bot_command_scope_all_private_chats.py`

### Classes

#### `class BotCommandScopeAllPrivateChats(BotCommandScope)`

```text
Represents the scope of bot commands, covering all private chats.
```

##### Methods

###### `def __init__(self)`

_No docstring._

###### `async def write(self, client: 'pyrogram.Client') -> 'raw.base.BotCommandScope'`

_No docstring._

---

## File: `types/bots_and_keyboards/bot_command_scope_chat.py`

### Classes

#### `class BotCommandScopeChat(BotCommandScope)`

```text
Represents the scope of bot commands, covering a specific chat.

Parameters:
    chat_id (``int`` | ``str``):
        Unique identifier for the target chat or username of the target supergroup (in the format
        @supergroupusername).
```

##### Methods

###### `def __init__(self, chat_id: Union[int, str])`

_No docstring._

###### `async def write(self, client: 'pyrogram.Client') -> 'raw.base.BotCommandScope'`

_No docstring._

---

## File: `types/bots_and_keyboards/bot_command_scope_chat_administrators.py`

### Classes

#### `class BotCommandScopeChatAdministrators(BotCommandScope)`

```text
Represents the scope of bot commands, covering all administrators of a specific group or supergroup chat.

Parameters:
    chat_id (``int`` | ``str``):
        Unique identifier for the target chat or username of the target supergroup (in the format
        @supergroupusername).
```

##### Methods

###### `def __init__(self, chat_id: Union[int, str])`

_No docstring._

###### `async def write(self, client: 'pyrogram.Client') -> 'raw.base.BotCommandScope'`

_No docstring._

---

## File: `types/bots_and_keyboards/bot_command_scope_chat_member.py`

### Classes

#### `class BotCommandScopeChatMember(BotCommandScope)`

```text
Represents the scope of bot commands, covering a specific member of a group or supergroup chat.

Parameters:
    chat_id (``int`` | ``str``):
        Unique identifier for the target chat or username of the target supergroup (in the format
        @supergroupusername).

    user_id (``int`` | ``str``):
        Unique identifier of the target user.
```

##### Methods

###### `def __init__(self, chat_id: Union[int, str], user_id: Union[int, str])`

_No docstring._

###### `async def write(self, client: 'pyrogram.Client') -> 'raw.base.BotCommandScope'`

_No docstring._

---

## File: `types/bots_and_keyboards/bot_command_scope_default.py`

### Classes

#### `class BotCommandScopeDefault(BotCommandScope)`

```text
Represents the default scope of bot commands.
Default commands are used if no commands with a narrower scope are specified for the user.
```

##### Methods

###### `def __init__(self)`

_No docstring._

###### `async def write(self, client: 'pyrogram.Client') -> 'raw.base.BotCommandScope'`

_No docstring._

---

## File: `types/bots_and_keyboards/bot_info.py`

### Classes

#### `class BotInfo(Object)`

```text
A bot Information.

Parameters:
    name (``str``):
        The bot name.

    about (``str``):
        The bot bio.

    description (``str``):
        Description of the bot;

    privacy_policy_url (``str``, *optional*):
        Privacy policy URL of the bot.
```

##### Methods

###### `def __init__(self, name: str, about: str, description: str, privacy_policy_url: str = None)`

_No docstring._

###### `def _parse(bot_info: 'raw.types.bots.BotInfo') -> 'BotInfo'`

_No docstring._

---

## File: `types/bots_and_keyboards/callback_game.py`

### Classes

#### `class CallbackGame(Object)`

```text
Placeholder, currently holds no information.

Use BotFather to set up your game.
```

##### Methods

###### `def __init__(self)`

_No docstring._

---

## File: `types/bots_and_keyboards/callback_query.py`

### Classes

#### `class CallbackQuery(Object, Update)`

```text
An incoming callback query from a callback button in an inline keyboard.

If the button that originated the query was attached to a message sent by the bot, the field *message*
will be present. If the button was attached to a message sent via the bot (in inline mode), the field
*inline_message_id* will be present. Exactly one of the fields *data* or *game_short_name* will be present.

Parameters:
    id (``str``):
        Unique identifier for this query.

    from_user (:obj:`~pyrogram.types.User`):
        Sender.

    chat_instance (``str``, *optional*):
        Global identifier, uniquely corresponding to the chat to which the message with the callback button was
        sent. Useful for high scores in games.

    message (:obj:`~pyrogram.types.Message`, *optional*):
        Message with the callback button that originated the query. Note that message content and message date will
        not be available if the message is too old.

    inline_message_id (``str``):
        Identifier of the message sent via the bot in inline mode, that originated the query.

    data (``str`` | ``bytes``, *optional*):
        Data associated with the callback button. Be aware that a bad client can send arbitrary data in this field.

    game_short_name (``str``, *optional*):
        Short name of a Game to be returned, serves as the unique identifier for the game.

    matches (List of regex Matches, *optional*):
        A list containing all `Match Objects <https://docs.python.org/3/library/re.html#match-objects>`_ that match
        the data of this callback query. Only applicable when using :obj:`Filters.regex <pyrogram.Filters.regex>`.
```

##### Methods

###### `def __init__(self, *, client: 'pyrogram.Client' = None, id: str, from_user: 'types.User', chat_instance: str, message: 'types.Message' = None, inline_message_id: str = None, data: Union[str, bytes] = None, game_short_name: str = None, matches: List[Match] = None)`

_No docstring._

###### `async def _parse(client: 'pyrogram.Client', callback_query, users) -> 'CallbackQuery'`

_No docstring._

###### `async def answer(self, text: str = None, show_alert: bool = None, url: str = None, cache_time: int = 0)`

```text
Bound method *answer* of :obj:`~pyrogram.types.CallbackQuery`.

Use this method as a shortcut for:

.. code-block:: python

    await client.answer_callback_query(
        callback_query.id,
        text="Hello",
        show_alert=True
    )

Example:
    .. code-block:: python

        await callback_query.answer("Hello", show_alert=True)

Parameters:
    text (``str``, *optional*):
        Text of the notification. If not specified, nothing will be shown to the user, 0-200 characters.

    show_alert (``bool`` *optional*):
        If true, an alert will be shown by the client instead of a notification at the top of the chat screen.
        Defaults to False.

    url (``str`` *optional*):
        URL that will be opened by the user's client.
        If you have created a Game and accepted the conditions via @Botfather, specify the URL that opens your
        game – note that this will only work if the query comes from a callback_game button.
        Otherwise, you may use links like t.me/your_bot?start=XXXX that open your bot with a parameter.

    cache_time (``int`` *optional*):
        The maximum amount of time in seconds that the result of the callback query may be cached client-side.
        Telegram apps will support caching starting in version 3.14. Defaults to 0.
```

###### `async def edit_message_text(self, text: str, parse_mode: Optional['enums.ParseMode'] = None, disable_web_page_preview: bool = None, reply_markup: 'types.InlineKeyboardMarkup' = None, business_connection_id: Optional[str] = None) -> Union['types.Message', bool]`

```text
Edit the text of messages attached to callback queries.

Bound method *edit_message_text* of :obj:`~pyrogram.types.CallbackQuery`.

Parameters:
    text (``str``):
        New text of the message.

    parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
        By default, texts are parsed using both Markdown and HTML styles.
        You can combine both syntaxes together.

    disable_web_page_preview (``bool``, *optional*):
        Disables link previews for links in this message.

    reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup`, *optional*):
        An InlineKeyboardMarkup object.

    business_connection_id (``str``, *optional*):
        Unique identifier of the business connection.
        for business bots only.

Returns:
    :obj:`~pyrogram.types.Message` | ``bool``: On success, if the edited message was sent by the bot, the edited
    message is returned, otherwise True is returned (message sent via the bot, as inline query result).

Raises:
    RPCError: In case of a Telegram RPC error.
```

###### `async def edit_message_caption(self, caption: str, parse_mode: Optional['enums.ParseMode'] = None, reply_markup: 'types.InlineKeyboardMarkup' = None, business_connection_id: Optional[str] = None) -> Union['types.Message', bool]`

```text
Edit the caption of media messages attached to callback queries.

Bound method *edit_message_caption* of :obj:`~pyrogram.types.CallbackQuery`.

Parameters:
    caption (``str``):
        New caption of the message.

    parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
        By default, texts are parsed using both Markdown and HTML styles.
        You can combine both syntaxes together.

    reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup`, *optional*):
        An InlineKeyboardMarkup object.

    business_connection_id (``str``, *optional*):
        Unique identifier of the business connection.
        for business bots only.

Returns:
    :obj:`~pyrogram.types.Message` | ``bool``: On success, if the edited message was sent by the bot, the edited
    message is returned, otherwise True is returned (message sent via the bot, as inline query result).

Raises:
    RPCError: In case of a Telegram RPC error.
```

###### `async def edit_message_media(self, media: 'types.InputMedia', reply_markup: 'types.InlineKeyboardMarkup' = None, business_connection_id: Optional[str] = None) -> Union['types.Message', bool]`

```text
Edit animation, audio, document, photo or video messages attached to callback queries.

Bound method *edit_message_media* of :obj:`~pyrogram.types.CallbackQuery`.

Parameters:
    media (:obj:`~pyrogram.types.InputMedia`):
        One of the InputMedia objects describing an animation, audio, document, photo or video.

    reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup`, *optional*):
        An InlineKeyboardMarkup object.

    business_connection_id (``str``, *optional*):
        Unique identifier of the business connection.
        for business bots only.

Returns:
    :obj:`~pyrogram.types.Message` | ``bool``: On success, if the edited message was sent by the bot, the edited
    message is returned, otherwise True is returned (message sent via the bot, as inline query result).

Raises:
    RPCError: In case of a Telegram RPC error.
```

###### `async def edit_message_reply_markup(self, reply_markup: 'types.InlineKeyboardMarkup' = None, business_connection_id: Optional[str] = None) -> Union['types.Message', bool]`

```text
Edit only the reply markup of messages attached to callback queries.

Bound method *edit_message_reply_markup* of :obj:`~pyrogram.types.CallbackQuery`.

Parameters:
    reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup`):
        An InlineKeyboardMarkup object.

    business_connection_id (``str``, *optional*):
        Unique identifier of the business connection.
        for business bots only.

Returns:
    :obj:`~pyrogram.types.Message` | ``bool``: On success, if the edited message was sent by the bot, the edited
    message is returned, otherwise True is returned (message sent via the bot, as inline query result).

Raises:
    RPCError: In case of a Telegram RPC error.
```

---

## File: `types/bots_and_keyboards/collectible_item_info.py`

### Classes

#### `class CollectibleItemInfo(Object)`

```text
Contains information about a collectible item and its last purchase.
Parameters:
    purchase_date (``datetime``):
        Point in time (Unix timestamp) when the item was purchased
    currency (``str``):
        Currency for the paid amount
    amount (``float``):
        The paid amount, in the smallest units of the currency
    cryptocurrency (``str``):
        Cryptocurrency used to pay for the item
    cryptocurrency_amount (``float``):
        The paid amount, in the smallest units of the cryptocurrency
    url (``str``):
        Individual URL for the item on https://fragment.com
```

##### Methods

###### `def __init__(self, *, purchase_date: datetime, currency: str, amount: float, cryptocurrency: str, cryptocurrency_amount: float, url: str)`

_No docstring._

###### `def _parse(collectible_info: 'raw.types.fragment.CollectibleInfo') -> 'CollectibleItemInfo'`

_No docstring._

---

## File: `types/bots_and_keyboards/force_reply.py`

### Classes

#### `class ForceReply(Object)`

```text
Object used to force clients to show a reply interface.

Upon receiving a message with this object, Telegram clients will display a reply interface to the user.

This acts as if the user has selected the bot's message and tapped "Reply".
This can be extremely useful if you want to create user-friendly step-by-step interfaces without having to
sacrifice privacy mode.

Parameters:
    selective (``bool``, *optional*):
        Use this parameter if you want to force reply from specific users only. Targets:
        1) users that are @mentioned in the text of the Message object;
        2) if the bot's message is a reply (has reply_to_message_id), sender of the original message.

    placeholder (``str``, *optional*):
        The placeholder to be shown in the input field when the reply is active; 1-64 characters.
```

##### Methods

###### `def __init__(self, selective: bool = None, placeholder: str = None)`

_No docstring._

###### `def read(b)`

_No docstring._

###### `async def write(self, _: 'pyrogram.Client')`

_No docstring._

---

## File: `types/bots_and_keyboards/game_high_score.py`

### Classes

#### `class GameHighScore(Object)`

```text
One row of the high scores table for a game.

Parameters:
    user (:obj:`~pyrogram.types.User`):
        User.

    score (``int``):
        Score.

    position (``int``, *optional*):
        Position in high score table for the game.
```

##### Methods

###### `def __init__(self, *, client: 'pyrogram.Client' = None, user: 'types.User', score: int, position: int = None)`

_No docstring._

###### `def _parse(client, game_high_score: raw.types.HighScore, users: Dict[int, 'raw.types.User']) -> 'GameHighScore'`

_No docstring._

###### `def _parse_action(client, service: raw.types.MessageService, users: Dict[int, 'raw.types.User']) -> 'GameHighScore'`

_No docstring._

---

## File: `types/bots_and_keyboards/inline_keyboard_button.py`

### Classes

#### `class InlineKeyboardButton(Object)`

```text
One button of an inline keyboard.

You must use exactly one of the optional fields.

Parameters:
    text (``str``):
        Label text on the button.

    callback_data (``str`` | ``bytes``, *optional*):
        Data to be sent in a callback query to the bot when button is pressed, 1-64 bytes.

    url (``str``, *optional*):
        HTTP url to be opened when button is pressed.

    web_app (:obj:`~pyrogram.types.WebAppInfo`, *optional*):
        Description of the `Web App <https://core.telegram.org/bots/webapps>`_ that will be launched when the user
        presses the button. The Web App will be able to send an arbitrary message on behalf of the user using the
        method :meth:`~pyrogram.Client.answer_web_app_query`. Available only in private chats between a user and the
        bot.

    login_url (:obj:`~pyrogram.types.LoginUrl`, *optional*):
         An HTTP URL used to automatically authorize the user. Can be used as a replacement for
         the `Telegram Login Widget <https://core.telegram.org/widgets/login>`_.

    user_id (``int``, *optional*):
        User id, for links to the user profile.

    switch_inline_query (``str``, *optional*):
        If set, pressing the button will prompt the user to select one of their chats, open that chat and insert
        the bot's username and the specified inline query in the input field. Can be empty, in which case just
        the bot's username will be inserted.Note: This offers an easy way for users to start using your bot in
        inline mode when they are currently in a private chat with it. Especially useful when combined with
        switch_pm… actions – in this case the user will be automatically returned to the chat they switched from,
        skipping the chat selection screen.

    switch_inline_query_current_chat (``str``, *optional*):
        If set, pressing the button will insert the bot's username and the specified inline query in the current
        chat's input field. Can be empty, in which case only the bot's username will be inserted.This offers a
        quick way for the user to open your bot in inline mode in the same chat – good for selecting something
        from multiple options.

    callback_game (:obj:`~pyrogram.types.CallbackGame`, *optional*):
        Description of the game that will be launched when the user presses the button.
        **NOTE**: This type of button **must** always be the first button in the first row.

    callback_data_with_password (``bytes``, *optional*):
        A button that asks for the 2-step verification password of the current user and then sends a callback query to a bot Data to be sent to the bot via a callback query.

    copy_text (``str``, *optional*):
        A button that copies the text to the clipboard.
```

##### Methods

###### `def __init__(self, text: str, callback_data: Optional[Union[str, bytes]] = None, url: Optional[str] = None, web_app: Optional['types.WebAppInfo'] = None, login_url: Optional['types.LoginUrl'] = None, user_id: Optional[int] = None, switch_inline_query: Optional[str] = None, switch_inline_query_current_chat: Optional[str] = None, callback_game: Optional['types.CallbackGame'] = None, requires_password: Optional[bool] = None, copy_text: Optional[str] = None)`

_No docstring._

###### `def read(b: 'raw.base.KeyboardButton')`

_No docstring._

###### `async def write(self, client: 'pyrogram.Client')`

_No docstring._

---

## File: `types/bots_and_keyboards/inline_keyboard_button_buy.py`

### Classes

#### `class InlineKeyboardButtonBuy(Object)`

```text
One button of the inline keyboard.
For simple invoice buttons.

Parameters:
    text (``str``):
        Text of the button. If none of the optional fields are used, it will be sent as a message when
        the button is pressed.
```

##### Methods

###### `def __init__(self, text: str)`

_No docstring._

###### `def read(b)`

_No docstring._

###### `async def write(self, _: 'pyrogram.Client')`

_No docstring._

---

## File: `types/bots_and_keyboards/inline_keyboard_markup.py`

### Classes

#### `class InlineKeyboardMarkup(Object)`

```text
An inline keyboard that appears right next to the message it belongs to.

Parameters:
    inline_keyboard (List of List of :obj:`~pyrogram.types.InlineKeyboardButton` | :obj:`~pyrogram.types.InlineKeyboardButtonBuy`):
        List of button rows, each represented by a List of InlineKeyboardButton objects.
        :obj:`~pyrogram.types.InlineKeyboardButtonBuy` objects is only for :meth:`~pyrogram.Client.send_invoice`.
        and only one needed in the first row.
```

##### Methods

###### `def __init__(self, inline_keyboard: List[List[Union['types.InlineKeyboardButton', 'types.InlineKeyboardButtonBuy']]])`

_No docstring._

###### `def read(o)`

_No docstring._

###### `async def write(self, client: 'pyrogram.Client')`

_No docstring._

---

## File: `types/bots_and_keyboards/keyboard_button.py`

### Classes

#### `class KeyboardButton(Object)`

```text
One button of the reply keyboard.
For simple text buttons String can be used instead of this object to specify text of the button.
Optional fields are mutually exclusive.

Parameters:
    text (``str``):
        Text of the button. If none of the optional fields are used, it will be sent as a message when
        the button is pressed.

    request_contact (``bool``, *optional*):
        If True, the user's phone number will be sent as a contact when the button is pressed.
        Available in private chats only.

    request_location (``bool``, *optional*):
        If True, the user's current location will be sent when the button is pressed.
        Available in private chats only.

    request_chat (:obj:`~pyrogram.types.RequestPeerTypeChannel` | :obj:`~pyrogram.types.RequestPeerTypeChat`, *optional*):
        If specified, defines the criteria used to request a suitable chats/channels.
        The identifier of the selected chats will be shared with the bot when the corresponding button is pressed.

    request_user (:obj:`~pyrogram.types.RequestPeerTypeUser`, *optional*):
        If specified, defines the criteria used to request a suitable users.
        The identifier of the selected users will be shared with the bot when the corresponding button is pressed.

    web_app (:obj:`~pyrogram.types.WebAppInfo`, *optional*):
        If specified, the described `Web App <https://core.telegram.org/bots/webapps>`_ will be launched when the
        button is pressed. The Web App will be able to send a “web_app_data” service message. Available in private
        chats only.
```

##### Methods

###### `def __init__(self, text: str, request_contact: bool = None, request_location: bool = None, request_chat: Union['types.RequestPeerTypeChat', 'types.RequestPeerTypeChannel'] = None, request_user: 'types.RequestPeerTypeUser' = None, web_app: 'types.WebAppInfo' = None)`

_No docstring._

###### `def read(b)`

_No docstring._

###### `def write(self)`

_No docstring._

---

## File: `types/bots_and_keyboards/login_url.py`

### Classes

#### `class LoginUrl(Object)`

```text
Represents a parameter of the inline keyboard button used to automatically authorize a user.

Serves as a great replacement for the Telegram Login Widget when the user is coming from Telegram.
All the user needs to do is tap/click a button and confirm that they want to log in.

Parameters:
    url (``str``):
        An HTTP URL to be opened with user authorization data added to the query string when the button is pressed.
        If the user refuses to provide authorization data, the original URL without information about the user will
        be opened. The data added is the same as described in
        `Receiving authorization data <https://core.telegram.org/widgets/login#receiving-authorization-data>`.

        **NOTE**: You **must** always check the hash of the received data to verify the authentication and the
        integrity of the data as described in
        `Checking authorization <https://core.telegram.org/widgets/login#checking-authorization>`_.

    forward_text (``str``, *optional*):
        New text of the button in forwarded messages.

    bot_username (``str``, *optional*):
        Username of a bot, which will be used for user authorization.
        See `Setting up a bot <https://core.telegram.org/widgets/login#setting-up-a-bot>`_ for more details.
        If not specified, the current bot's username will be assumed. The url's domain must be the same as the
        domain linked with the bot.
        See `Linking your domain to the bot <https://core.telegram.org/widgets/login#linking-your-domain-to-the-bot>`_
        for more details.

    request_write_access (``str``, *optional*):
        Pass True to request the permission for your bot to send messages to the user.

    button_id (``int``):
        Button identifier.
```

##### Methods

###### `def __init__(self, *, url: str, forward_text: str = None, bot_username: str = None, request_write_access: str = None, button_id: int = None)`

_No docstring._

###### `def read(b: 'raw.types.KeyboardButtonUrlAuth') -> 'LoginUrl'`

_No docstring._

###### `def write(self, text: str, bot: 'raw.types.InputUser')`

_No docstring._

---

## File: `types/bots_and_keyboards/menu_button.py`

### Classes

#### `class MenuButton(Object)`

```text
Describes the bot's menu button in a private chat.

It should be one of:

- :obj:`~pyrogram.types.MenuButtonCommands`
- :obj:`~pyrogram.types.MenuButtonWebApp`
- :obj:`~pyrogram.types.MenuButtonDefault`

If a menu button other than :obj:`~pyrogram.types.MenuButtonDefault` is set for a private chat, then it is applied
in the chat. Otherwise the default menu button is applied. By default, the menu button opens the list of bot
commands.
```

##### Methods

###### `def __init__(self, type: str)`

_No docstring._

###### `async def write(self, client: 'pyrogram.Client') -> 'raw.base.BotMenuButton'`

_No docstring._

---

## File: `types/bots_and_keyboards/menu_button_commands.py`

### Classes

#### `class MenuButtonCommands(MenuButton)`

```text
A menu button, which opens the bot's list of commands.
```

##### Methods

###### `def __init__(self)`

_No docstring._

###### `async def write(self, client: 'pyrogram.Client') -> 'raw.types.BotMenuButtonCommands'`

_No docstring._

---

## File: `types/bots_and_keyboards/menu_button_default.py`

### Classes

#### `class MenuButtonDefault(MenuButton)`

```text
Describes that no specific value for the menu button was set.
```

##### Methods

###### `def __init__(self)`

_No docstring._

###### `async def write(self, client: 'pyrogram.Client') -> 'raw.types.BotMenuButtonDefault'`

_No docstring._

---

## File: `types/bots_and_keyboards/menu_button_web_app.py`

### Classes

#### `class MenuButtonWebApp(MenuButton)`

```text
A menu button, which launches a `Web App <https://core.telegram.org/bots/webapps>`_.

Parameters:
    text (``str``):
        Text on the button

    web_app (:obj:`~pyrogram.types.WebAppInfo`):
        Description of the Web App that will be launched when the user presses the button.
        The Web App will be able to send an arbitrary message on behalf of the user using the method
        :meth:`~pyrogram.Client.answer_web_app_query`.
```

##### Methods

###### `def __init__(self, text: str, web_app: 'types.WebAppInfo')`

_No docstring._

###### `async def write(self, client: 'pyrogram.Client') -> 'raw.types.BotMenuButton'`

_No docstring._

---

## File: `types/bots_and_keyboards/reply_keyboard_markup.py`

### Classes

#### `class ReplyKeyboardMarkup(Object)`

```text
A custom keyboard with reply options.

Parameters:
    keyboard (List of List of :obj:`~pyrogram.types.KeyboardButton`):
        List of button rows, each represented by a List of KeyboardButton objects.

    is_persistent (``bool``, *optional*):
        Requests clients to always show the keyboard when the regular keyboard is hidden.
        Defaults to false, in which case the custom keyboard can be hidden and opened with a keyboard icon.

    resize_keyboard (``bool``, *optional*):
        Requests clients to resize the keyboard vertically for optimal fit (e.g., make the keyboard smaller if
        there are just two rows of buttons). Defaults to false, in which case the custom keyboard is always of
        the same height as the app's standard keyboard.

    one_time_keyboard (``bool``, *optional*):
        Requests clients to hide the keyboard as soon as it's been used. The keyboard will still be available,
        but clients will automatically display the usual letter-keyboard in the chat – the user can press a
        special button in the input field to see the custom keyboard again. Defaults to false.

    selective (``bool``, *optional*):
        Use this parameter if you want to show the keyboard to specific users only. Targets:
        1) users that are @mentioned in the text of the Message object;
        2) if the bot's message is a reply (has reply_to_message_id), sender of the original message.
        Example: A user requests to change the bot's language, bot replies to the request with a keyboard to
        select the new language. Other users in the group don't see the keyboard.

    placeholder (``str``, *optional*):
        The placeholder to be shown in the input field when the keyboard is active; 1-64 characters.
```

##### Methods

###### `def __init__(self, keyboard: List[List[Union['types.KeyboardButton', str]]], is_persistent: bool = None, resize_keyboard: bool = None, one_time_keyboard: bool = None, selective: bool = None, placeholder: str = None)`

_No docstring._

###### `def read(kb: 'raw.base.ReplyMarkup')`

_No docstring._

###### `async def write(self, _: 'pyrogram.Client')`

_No docstring._

---

## File: `types/bots_and_keyboards/reply_keyboard_remove.py`

### Classes

#### `class ReplyKeyboardRemove(Object)`

```text
Object used to tell clients to remove a bot keyboard.

Upon receiving a message with this object, Telegram clients will remove the current custom keyboard and display
the default letter-keyboard. By default, custom keyboards are displayed until a new keyboard is sent by a bot.
An exception is made for one-time keyboards that are hidden immediately after the user presses a button
(see ReplyKeyboardMarkup).

Parameters:
    selective (``bool``, *optional*):
        Use this parameter if you want to remove the keyboard for specific users only. Targets:
        1) users that are @mentioned in the text of the Message object;
        2) if the bot's message is a reply (has reply_to_message_id), sender of the original message.
        Example: A user votes in a poll, bot returns confirmation message in reply to the vote and removes the
        keyboard for that user, while still showing the keyboard with poll options to users who haven't voted yet.
```

##### Methods

###### `def __init__(self, selective: bool = None)`

_No docstring._

###### `def read(b)`

_No docstring._

###### `async def write(self, _: 'pyrogram.Client')`

_No docstring._

---

## File: `types/bots_and_keyboards/request_peer_type_channel.py`

### Classes

#### `class RequestPeerTypeChannel(Object)`

```text
Object used to request clients to send a channel identifier.

Parameters:
    button_id (``int``, *optional*):
        Button identifier.

    is_creator (``bool``, *optional*):
        If True, show only Channel which user is the owner.

    is_username (``bool``, *optional*):
        If True, show only Channel which has username.

    max (``int``, *optional*):
        Maximum number of channels to be returned.
        default 1.

    is_name_requested (``bool``, *optional*):
        If True, Channel name is requested.
        default True.

    is_username_requested (``bool``, *optional*):
        If True, Channel username is requested.
        default True.

    is_photo_requested (``bool``, *optional*):
        If True, Channel photo is requested.
        default True.

    user_privileges (:obj:`~pyrogram.types.ChatPrivileges`, *optional*):
        Privileged actions that an user administrator is able to take.

    bot_privileges (:obj:`~pyrogram.types.ChatPrivileges`, *optional*):
        Privileged actions that a bot administrator is able to take.
```

##### Methods

###### `def __init__(self, button_id: int = 0, is_creator: bool = None, is_username: bool = None, max: int = 1, is_name_requested: bool = True, is_username_requested: bool = True, is_photo_requested: bool = True, user_privileges: 'types.ChatPrivileges' = None, bot_privileges: 'types.ChatPrivileges' = None)`

_No docstring._

---

## File: `types/bots_and_keyboards/request_peer_type_chat.py`

### Classes

#### `class RequestPeerTypeChat(Object)`

```text
Object used to request clients to send a chat identifier.

Parameters:
    button_id (``int``, *optional*):
        Button identifier.

    is_creator (``bool``, *optional*):
        If True, show only Chat which user is the owner.

    is_bot_participant (``bool``, *optional*):
        If True, show only Chat where bot is a participant.

    is_username (``bool``, *optional*):
        If True, show only Chat which has username.

    is_forum (``bool``, *optional*):
        If True, show only Chat which is a forum.

    max (``int``, *optional*):
        Maximum number of chats to be returned.
        default 1.

    is_name_requested (``bool``, *optional*):
        If True, Chat name is requested.
        default True.

    is_username_requested (``bool``, *optional*):
        If True, Chat username is requested.
        default True.

    is_photo_requested (``bool``, *optional*):
        If True, Chat photo is requested.
        default True.

    user_privileges (:obj:`~pyrogram.types.ChatPrivileges`, *optional*):
        Privileged actions that an user administrator is able to take.

    bot_privileges (:obj:`~pyrogram.types.ChatPrivileges`, *optional*):
        Privileged actions that a bot administrator is able to take.
```

##### Methods

###### `def __init__(self, button_id: int = 0, is_creator: bool = None, is_bot_participant: bool = None, is_username: bool = None, is_forum: bool = None, max: int = 1, is_name_requested: bool = True, is_username_requested: bool = True, is_photo_requested: bool = True, user_privileges: 'types.ChatPrivileges' = None, bot_privileges: 'types.ChatPrivileges' = None)`

_No docstring._

---

## File: `types/bots_and_keyboards/request_peer_type_user.py`

### Classes

#### `class RequestPeerTypeUser(Object)`

```text
Object used to request clients to send a user identifier.

Parameters:
    button_id (``int``, *optional*):
        Button identifier.

    is_bot (``bool``, *optional*):
        If True, show only Bots.

    is_premium (``bool``, *optional*):
        If True, show only Premium Users.

    max (``int``, *optional*):
        Maximum number of users to be returned.
        default 1.

    is_name_requested (``bool``, *optional*):
        If True, User name is requested.
        default True.

    is_username_requested (``bool``, *optional*):
        If True, User username is requested.
        default True.

    is_photo_requested (``bool``, *optional*):
        If True, User photo is requested.
        default True.
```

##### Methods

###### `def __init__(self, button_id: int = 0, is_bot: bool = None, is_premium: bool = None, max: int = 1, is_name_requested: bool = True, is_username_requested: bool = True, is_photo_requested: bool = True)`

_No docstring._

---

## File: `types/bots_and_keyboards/requested_chat.py`

### Classes

#### `class RequestedChat(Object)`

```text
Contains information about a requested chat.

Parameters:
    chat_id (``int``):
        Identifier of the chat.

    chat_type (``enums.ChatType``):
        Type of the chat.

    name (``str``, *optional*):
        Name of the chat.

    username (``str``, *optional*):
        Username of the chat.

    photo (``types.ChatPhoto``, *optional*):
        Chat photo.
```

##### Methods

###### `def __init__(self, chat_id: int, chat_type: enums.ChatType, name: str = None, username: str = None, photo: 'types.ChatPhoto' = None)`

_No docstring._

###### `async def _parse(client, request: Union['raw.types.RequestedPeerChat', 'raw.types.RequestedPeerChannel', 'raw.types.PeerChat', 'raw.types.PeerChannel']) -> 'RequestedChat'`

_No docstring._

---

## File: `types/bots_and_keyboards/requested_chats.py`

### Classes

#### `class RequestedChats(Object)`

```text
Contains information about requested chats.

Parameters:
    button_id (``int``):
        Button identifier.

    chats (List of :obj:`~pyrogram.types.RequestedChat`, *optional*):
        List of chats.

    users (List of :obj:`~pyrogram.types.RequestedUser` *optional*):
        List of users.
```

##### Methods

###### `def __init__(self, button_id: int, chats: List['types.RequestedChat'] = None, users: List['types.RequestedUser'] = None)`

_No docstring._

###### `async def _parse(client, request: Union['raw.types.MessageActionRequestedPeer', 'raw.types.MessageActionRequestedPeerSentMe']) -> 'RequestedChats'`

_No docstring._

---

## File: `types/bots_and_keyboards/requested_user.py`

### Classes

#### `class RequestedUser(Object)`

```text
Contains information about a requested user.

Parameters:
    user_id (``int``):
        Identifier of the user.

    first_name (``str``, *optional*):
        First name of the user.

    last_name (``str``, *optional*):
        Last name of the user.

    username (``str``, *optional*):
        Username of the user.

    photo (``types.UserProfilePhoto``, *optional*):
        User photo.

    full_name (``str``, *optional*):
        User's full name.
```

##### Methods

###### `def __init__(self, user_id: int, first_name: str = None, last_name: str = None, username: str = None, photo: 'types.ChatPhoto' = None)`

_No docstring._

###### `async def _parse(client, request: Union['raw.types.RequestedPeerUser', 'raw.types.PeerUser']) -> 'RequestedUser'`

_No docstring._

###### `def full_name(self) -> str`

_No docstring._

---

## File: `types/bots_and_keyboards/sent_web_app_message.py`

### Classes

#### `class SentWebAppMessage(Object)`

```text
Contains information about an inline message sent by a `Web App <https://core.telegram.org/bots/webapps>`_ on behalf of a user.

Parameters:
    inline_message_id (``str``):
        Identifier of the sent inline message.
        Available only if there is an inline keyboard attached to the message.
```

##### Methods

###### `def __init__(self, *, inline_message_id: str)`

_No docstring._

###### `def _parse(obj: 'raw.types.WebViewMessageSent')`

_No docstring._

---

## File: `types/bots_and_keyboards/web_app_info.py`

### Classes

#### `class WebAppInfo(Object)`

```text
Contains information about a `Web App <https://core.telegram.org/bots/webapps>`_.

Parameters:
    url (``str``):
        An HTTPS URL of a Web App to be opened with additional data as specified in
        `Initializing Web Apps <https://core.telegram.org/bots/webapps#initializing-web-apps>`_.
```

##### Methods

###### `def __init__(self, *, url: str)`

_No docstring._

---

## File: `types/business/__init__.py`

---

## File: `types/business/pre_checkout_query.py`

### Classes

#### `class PreCheckoutQuery(Object, Update)`

```text
An incoming pre-checkout query from a buy button in an inline keyboard.

Parameters:
    id (``str``):
        Unique identifier for this query.

    from_user (:obj:`~pyrogram.types.User`):
        User who sent the query.

    currency (``str``):
        Three-letter ISO 4217 currency code.

    total_amount (``int``):
        Total price in the smallest units of the currency.

    payload (``str``):
        Bot specified invoice payload.

    shipping_option_id (``str``, *optional*):
        Identifier of the shipping option chosen by the user.

    payment_info (:obj:`~pyrogram.types.PaymentInfo`, *optional*):
        Payment information provided by the user.
```

##### Methods

###### `def __init__(self, *, client: 'pyrogram.Client' = None, id: str, from_user: 'types.User', currency: str, total_amount: int, payload: str, shipping_option_id: str = None, payment_info: 'types.PaymentInfo' = None)`

_No docstring._

###### `async def _parse(client: 'pyrogram.Client', pre_checkout_query: 'raw.types.UpdateBotPrecheckoutQuery', users: Dict[int, 'raw.types.User'] = None) -> 'PreCheckoutQuery'`

_No docstring._

###### `async def answer(self, success: bool = None, error: str = None)`

```text
Bound method *answer* of :obj:`~pyrogram.types.PreCheckoutQuery`.

Use this method as a shortcut for:

.. code-block:: python

    await client.answer_pre_checkout_query(
        pre_checkout_query.id,
        success=True
    )

Example:
    .. code-block:: python

        await pre_checkout_query.answer(success=True)

Parameters:
    success (``bool`` *optional*):
        If true, an alert will be shown by the client instead of a notification at the top of the chat screen.
        Defaults to False.

    error (``bool`` *optional*):
        If true, an alert will be shown by the client instead of a notification at the top of the chat screen.
        Defaults to False.
```

---

## File: `types/business/shipping_address.py`

### Classes

#### `class ShippingAddress(Object)`

```text
Contains information about a shipping address.

Parameters:
    street_line1 (``str``):
        First line for the address.

    street_line1 (``str``):
        Second line for the address.

    city (``str``):
        City for the address.

    state (``str``):
        State for the address, if applicable.

    post_code (``str``):
        Post code for the address.

    country_code (``str``):
        Two-letter ISO 3166-1 alpha-2 country code.
```

##### Methods

###### `def __init__(self, *, street_line1: str, street_line2: str, city: str, state: str, post_code: str, country_code: str)`

_No docstring._

###### `def _parse(shipping_address: 'raw.types.raw.types.PostAddress') -> 'ShippingAddress'`

_No docstring._

---

## File: `types/business/shipping_option.py`

### Classes

#### `class ShippingOption(Object)`

```text
This object represents one shipping option.

Parameters:
    id (``str``):
        Shipping option identifier.

    title (``str``):
        Option title.

    prices (List of :obj:`~pyrogram.types.LabeledPrice`):
        List of price portions.
```

##### Methods

###### `def __init__(self, id: str, title: str, prices: 'types.LabeledPrice')`

_No docstring._

###### `def _parse(shipping_option: 'raw.types.ShippingOption') -> 'ShippingOption'`

_No docstring._

###### `def write(self)`

_No docstring._

---

## File: `types/business/shipping_query.py`

### Classes

#### `class ShippingQuery(Object, Update)`

```text
This object contains information about an incoming shipping query.

Parameters:
    id (``str``):
        Unique query identifier.

    from_user (:obj:`~pyrogram.types.User`):
        User who sent the query.

    invoice_payload (``str``):
        Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user, use for your internal processes.

    shipping_address (:obj:`~pyrogram.types.ShippingAddress`):
        User specified shipping address. Only available to the bot that received the payment.
```

##### Methods

###### `def __init__(self, *, client: 'pyrogram.Client' = None, id: str, from_user: 'types.User', payload: str, shipping_address: 'types.ShippingAddress' = None)`

_No docstring._

###### `async def _parse(client: 'pyrogram.Client', shipping_query: 'raw.types.UpdateBotShippingQuery', users: Dict[int, 'raw.types.User']) -> 'types.PreCheckoutQuery'`

_No docstring._

###### `async def answer(self, ok: bool, shipping_options: 'types.ShippingOptions' = None, error_message: str = None)`

```text
Bound method *answer* of :obj:`~pyrogram.types.ShippingQuery`.

Use this method as a shortcut for:

.. code-block:: python

    await client.answer_shipping_query(
        shipping_query.id,
        ok=True
    )

Example:
    .. code-block:: python

        await shipping_query.answer(ok=True)

Parameters:
    ok (``bool``):
        Pass True if delivery to the specified address is possible and False if there are any problems (for example, if delivery to the specified address is not possible).

    shipping_options (:obj:`~pyrogram.types.ShippingOptions`, *optional*):
        Required if ok is True. A JSON-serialized array of available shipping options.

    error_message (``str``, *optional*):
        Required if ok is False. Error message in human readable form that explains why it is impossible to complete the order (e.g. "Sorry, delivery to your desired address is unavailable'). Telegram will display this message to the user.

Returns:
    ``bool``: True, on success.
```

---

## File: `types/inline_mode/__init__.py`

---

## File: `types/inline_mode/chosen_inline_result.py`

### Classes

#### `class ChosenInlineResult(Object, Update)`

```text
A :doc:`result <InlineQueryResult>` of an inline query chosen by the user and sent to their chat partner.

.. note::

    In order to receive these updates, your bot must have "inline feedback" enabled. You can enable this feature
    with `@BotFather <https://t.me/botfather>`_.

Parameters:
    result_id (``str``):
        The unique identifier for the result that was chosen.

    from_user (:obj:`~pyrogram.types.User`):
        The user that chose the result.

    query (``str``):
        The query that was used to obtain the result.

    location (:obj:`~pyrogram.types.Location`, *optional*):
        Sender location, only for bots that require user location.

    inline_message_id (``str``, *optional*):
        Identifier of the sent inline message.
        Available only if there is an :doc:`inline keyboard <InlineKeyboardMarkup>` attached to the message.
        Will be also received in :doc:`callback queries <CallbackQuery>` and can be used to edit the message.
```

##### Methods

###### `def __init__(self, *, client: 'pyrogram.Client' = None, result_id: str, from_user: 'types.User', query: str, location: 'types.Location' = None, inline_message_id: str = None)`

_No docstring._

###### `def _parse(client, chosen_inline_result: raw.types.UpdateBotInlineSend, users) -> 'ChosenInlineResult'`

_No docstring._

---

## File: `types/inline_mode/inline_query.py`

### Classes

#### `class InlineQuery(Object, Update)`

```text
An incoming inline query.

When the user sends an empty query, your bot could return some default or trending results.

Parameters:
    id (``str``):
        Unique identifier for this query.

    from_user (:obj:`~pyrogram.types.User`):
        Sender.

    query (``str``):
        Text of the query (up to 512 characters).

    offset (``str``):
        Offset of the results to be returned, can be controlled by the bot.

    chat_type (:obj:`~pyrogram.enums.ChatType`, *optional*):
        Type of the chat, from which the inline query was sent.

    location (:obj:`~pyrogram.types.Location`. *optional*):
        Sender location, only for bots that request user location.

    matches (List of regex Matches, *optional*):
        A list containing all `Match Objects <https://docs.python.org/3/library/re.html#match-objects>`_ that match
        the query of this inline query. Only applicable when using :obj:`Filters.regex <pyrogram.Filters.regex>`.
```

##### Methods

###### `def __init__(self, *, client: 'pyrogram.Client' = None, id: str, from_user: 'types.User', query: str, offset: str, chat_type: 'enums.ChatType', location: 'types.Location' = None, matches: List[Match] = None)`

_No docstring._

###### `def _parse(client, inline_query: raw.types.UpdateBotInlineQuery, users: Dict[int, 'raw.types.User']) -> 'InlineQuery'`

_No docstring._

###### `async def answer(self, results: List['types.InlineQueryResult'], cache_time: int = 300, is_gallery: bool = False, is_personal: bool = False, next_offset: str = '', switch_pm_text: str = '', switch_pm_parameter: str = '')`

```text
Bound method *answer* of :obj:`~pyrogram.types.InlineQuery`.

Use this method as a shortcut for:

.. code-block:: python

    await client.answer_inline_query(
        inline_query.id,
        results=[...]
    )

Example:
    .. code-block:: python

        await inline_query.answer([...])

Parameters:
    results (List of :obj:`~pyrogram.types.InlineQueryResult`):
        A list of results for the inline query.

    cache_time (``int``, *optional*):
        The maximum amount of time in seconds that the result of the inline query may be cached on the server.
        Defaults to 300.

    is_gallery (``bool``, *optional*):
        Pass True, if results should be displayed in gallery mode instead of list mode.
        Defaults to False.

    is_personal (``bool``, *optional*):
        Pass True, if results may be cached on the server side only for the user that sent the query.
        By default (False), results may be returned to any user who sends the same query.

    next_offset (``str``, *optional*):
        Pass the offset that a client should send in the next query with the same text to receive more results.
        Pass an empty string if there are no more results or if you don‘t support pagination.
        Offset length can’t exceed 64 bytes.

    switch_pm_text (``str``, *optional*):
        If passed, clients will display a button with specified text that switches the user to a private chat
        with the bot and sends the bot a start message with the parameter switch_pm_parameter

    switch_pm_parameter (``str``, *optional*):
        `Deep-linking <https://core.telegram.org/bots#deep-linking>`_ parameter for the /start message sent to
        the bot when user presses the switch button. 1-64 characters, only A-Z, a-z, 0-9, _ and - are allowed.

        Example: An inline bot that sends YouTube videos can ask the user to connect the bot to their YouTube
        account to adapt search results accordingly. To do this, it displays a "Connect your YouTube account"
        button above the results, or even before showing any. The user presses the button, switches to a private
        chat with the bot and, in doing so, passes a start parameter that instructs the bot to return an oauth
        link. Once done, the bot can offer a switch_inline button so that the user can easily return to the chat
        where they wanted to use the bot's inline capabilities.
```

---

## File: `types/inline_mode/inline_query_result.py`

### Classes

#### `class InlineQueryResult(Object)`

```text
One result of an inline query.

- :obj:`~pyrogram.types.InlineQueryResultCachedAudio`
- :obj:`~pyrogram.types.InlineQueryResultCachedDocument`
- :obj:`~pyrogram.types.InlineQueryResultCachedAnimation`
- :obj:`~pyrogram.types.InlineQueryResultCachedPhoto`
- :obj:`~pyrogram.types.InlineQueryResultCachedSticker`
- :obj:`~pyrogram.types.InlineQueryResultCachedVideo`
- :obj:`~pyrogram.types.InlineQueryResultCachedVoice`
- :obj:`~pyrogram.types.InlineQueryResultArticle`
- :obj:`~pyrogram.types.InlineQueryResultAudio`
- :obj:`~pyrogram.types.InlineQueryResultContact`
- :obj:`~pyrogram.types.InlineQueryResultDocument`
- :obj:`~pyrogram.types.InlineQueryResultAnimation`
- :obj:`~pyrogram.types.InlineQueryResultLocation`
- :obj:`~pyrogram.types.InlineQueryResultPhoto`
- :obj:`~pyrogram.types.InlineQueryResultVenue`
- :obj:`~pyrogram.types.InlineQueryResultVideo`
- :obj:`~pyrogram.types.InlineQueryResultVoice`
```

##### Methods

###### `def __init__(self, type: str, id: str, input_message_content: 'types.InputMessageContent', reply_markup: 'types.InlineKeyboardMarkup')`

_No docstring._

###### `async def write(self, client: 'pyrogram.Client')`

_No docstring._

---

## File: `types/inline_mode/inline_query_result_animation.py`

### Classes

#### `class InlineQueryResultAnimation(InlineQueryResult)`

```text
Link to an animated GIF file.

By default, this animated GIF file will be sent by the user with optional caption.
Alternatively, you can use *input_message_content* to send a message with the specified content instead of the
animation.

Parameters:
    animation_url (``str``):
        A valid URL for the animated GIF file.
        File size must not exceed 1 MB.

    animation_width (``int``, *optional*)
        Width of the animation.

    animation_height (``int``, *optional*)
        Height of the animation.

    animation_duration (``int``, *optional*)
        Duration of the animation in seconds.

    thumb_url (``str``, *optional*):
        URL of the static thumbnail for the result (jpeg or gif)
        Defaults to the value passed in *animation_url*.

    thumb_mime_type (``str``, *optional*)
        MIME type of the thumbnail, must be one of "image/jpeg", "image/gif", or "video/mp4".
        Defaults to "image/jpeg".

    id (``str``, *optional*):
        Unique identifier for this result, 1-64 bytes.
        Defaults to a randomly generated UUID4.

    title (``str``, *optional*):
        Title for the result.

    caption (``str``, *optional*):
        Caption of the animation to be sent, 0-1024 characters.

    parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
        By default, texts are parsed using both Markdown and HTML styles.
        You can combine both syntaxes together.

    caption_entities (List of :obj:`~pyrogram.types.MessageEntity`):
        List of special entities that appear in the caption, which can be specified instead of *parse_mode*.

    reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup`, *optional*):
        An InlineKeyboardMarkup object.

    input_message_content (:obj:`~pyrogram.types.InputMessageContent`):
        Content of the message to be sent instead of the photo.
```

##### Methods

###### `def __init__(self, animation_url: str, animation_width: int = 0, animation_height: int = 0, animation_duration: int = 0, thumb_url: str = None, thumb_mime_type: str = 'image/jpeg', id: str = None, title: str = None, description: str = None, caption: str = '', parse_mode: Optional['enums.ParseMode'] = None, caption_entities: List['types.MessageEntity'] = None, reply_markup: 'types.InlineKeyboardMarkup' = None, input_message_content: 'types.InputMessageContent' = None)`

_No docstring._

###### `async def write(self, client: 'pyrogram.Client')`

_No docstring._

---

## File: `types/inline_mode/inline_query_result_article.py`

### Classes

#### `class InlineQueryResultArticle(InlineQueryResult)`

```text
Link to an article or web page.

Parameters:
    title (``str``):
        Title for the result.

    input_message_content (:obj:`~pyrogram.types.InputMessageContent`):
        Content of the message to be sent.

    id (``str``, *optional*):
        Unique identifier for this result, 1-64 bytes.
        Defaults to a randomly generated UUID4.

    url (``str``, *optional*):
        URL of the result.

    description (``str``, *optional*):
        Short description of the result.

    reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup`, *optional*):
        Inline keyboard attached to the message.

    thumb_url (``str``, *optional*):
        Url of the thumbnail for the result.

    thumb_width (``int``, *optional*):
        Thumbnail width.

    thumb_height (``int``, *optional*):
        Thumbnail height
```

##### Methods

###### `def __init__(self, title: str, input_message_content: 'types.InputMessageContent', id: str = None, url: str = None, description: str = None, reply_markup: 'types.InlineKeyboardMarkup' = None, thumb_url: str = None, thumb_width: int = 0, thumb_height: int = 0)`

_No docstring._

###### `async def write(self, client: 'pyrogram.Client')`

_No docstring._

---

## File: `types/inline_mode/inline_query_result_audio.py`

### Classes

#### `class InlineQueryResultAudio(InlineQueryResult)`

```text
Link to an audio file.

By default, this audio file will be sent by the user with optional caption.
Alternatively, you can use *input_message_content* to send a message with the specified content instead of the
audio.

Parameters:
    audio_url (``str``):
        A valid URL for the audio file.

    title (``str``):
        Title for the result.

    id (``str``, *optional*):
        Unique identifier for this result, 1-64 bytes.
        Defaults to a randomly generated UUID4.

    performer (``str``, *optional*):
        Audio performer.

    audio_duration (``int``, *optional*):
        Audio duration in seconds.

    caption (``str``, *optional*):
        Caption of the audio to be sent, 0-1024 characters.

    parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
        By default, texts are parsed using both Markdown and HTML styles.
        You can combine both syntaxes together.

    caption_entities (List of :obj:`~pyrogram.types.MessageEntity`):
        List of special entities that appear in the caption, which can be specified instead of *parse_mode*.

    description (``str``, *optional*):
        Short description of the result.

    reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup`, *optional*):
        Inline keyboard attached to the message.

    input_message_content (:obj:`~pyrogram.types.InputMessageContent`, *optional*):
        Content of the message to be sent instead of the audio.

    thumb_url (``str``, *optional*):
        Url of the thumbnail for the result.
```

##### Methods

###### `def __init__(self, audio_url: str, title: str, id: str = None, performer: str = '', audio_duration: int = 0, caption: str = '', parse_mode: Optional['enums.ParseMode'] = None, caption_entities: List['types.MessageEntity'] = None, description: str = None, reply_markup: 'types.InlineKeyboardMarkup' = None, input_message_content: 'types.InputMessageContent' = None, thumb_url: str = None)`

_No docstring._

###### `async def write(self, client: 'pyrogram.Client')`

_No docstring._

---

## File: `types/inline_mode/inline_query_result_cached_animation.py`

### Classes

#### `class InlineQueryResultCachedAnimation(InlineQueryResult)`

```text
A link to an animation file stored on the Telegram servers.

By default, this animation file will be sent by the user with an optional caption.
Alternatively, you can use *input_message_content* to send a message with specified content instead of the
animation.

Parameters:
    animation_file_id (``str``):
        A valid file identifier for the animation file.

    id (``str``, *optional*):
        Unique identifier for this result, 1-64 bytes.
        Defaults to a randomly generated UUID4.

    title (``str``, *optional*):
        Title for the result.

    caption (``str``, *optional*):
        Caption of the photo to be sent, 0-1024 characters.

    parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
        By default, texts are parsed using both Markdown and HTML styles.
        You can combine both syntaxes together.

    caption_entities (List of :obj:`~pyrogram.types.MessageEntity`):
        List of special entities that appear in the caption, which can be specified instead of *parse_mode*.

    reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup`, *optional*):
        An InlineKeyboardMarkup object.

    input_message_content (:obj:`~pyrogram.types.InputMessageContent`):
        Content of the message to be sent instead of the photo.
```

##### Methods

###### `def __init__(self, animation_file_id: str, id: str = None, title: str = None, caption: str = '', parse_mode: Optional['enums.ParseMode'] = None, caption_entities: List['types.MessageEntity'] = None, reply_markup: 'types.InlineKeyboardMarkup' = None, input_message_content: 'types.InputMessageContent' = None)`

_No docstring._

###### `async def write(self, client: 'pyrogram.Client')`

_No docstring._

---

## File: `types/inline_mode/inline_query_result_cached_audio.py`

### Classes

#### `class InlineQueryResultCachedAudio(InlineQueryResult)`

```text
A link to an MP3 audio file stored on the Telegram servers

By default, this audio file will be sent by the user. Alternatively, you can use *input_message_content* to send a
message with the specified content instead of the audio.

Parameters:
    audio_file_id (``str``):
        A valid file identifier for the audio file.

    id (``str``, *optional*):
        Unique identifier for this result, 1-64 bytes.
        Defaults to a randomly generated UUID4.

    caption (``str``, *optional*):
        Caption of the photo to be sent, 0-1024 characters.

    parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
        By default, texts are parsed using both Markdown and HTML styles.
        You can combine both syntaxes together.

    caption_entities (List of :obj:`~pyrogram.types.MessageEntity`):
        List of special entities that appear in the caption, which can be specified instead of *parse_mode*.

    reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup`, *optional*):
        An InlineKeyboardMarkup object.

    input_message_content (:obj:`~pyrogram.types.InputMessageContent`):
        Content of the message to be sent instead of the photo.
```

##### Methods

###### `def __init__(self, audio_file_id: str, id: str = None, caption: str = '', parse_mode: Optional['enums.ParseMode'] = None, caption_entities: List['types.MessageEntity'] = None, reply_markup: 'types.InlineKeyboardMarkup' = None, input_message_content: 'types.InputMessageContent' = None)`

_No docstring._

###### `async def write(self, client: 'pyrogram.Client')`

_No docstring._

---

## File: `types/inline_mode/inline_query_result_cached_document.py`

### Classes

#### `class InlineQueryResultCachedDocument(InlineQueryResult)`

```text
A link to a file stored on the Telegram servers.

By default, this file will be sent by the user with an optional caption. Alternatively, you can use
*input_message_content* to send a message with the specified content instead of the file.

Parameters:
    document_file_id (``str``):
        A valid file identifier for the file.

    title (``str``):
        Title for the result.

    id (``str``, *optional*):
        Unique identifier for this result, 1-64 bytes.
        Defaults to a randomly generated UUID4.

    description (``str``, *optional*):
        Short description of the result.

    caption (``str``, *optional*):
        Caption of the photo to be sent, 0-1024 characters.

    parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
        By default, texts are parsed using both Markdown and HTML styles.
        You can combine both syntaxes together.

    caption_entities (List of :obj:`~pyrogram.types.MessageEntity`):
        List of special entities that appear in the caption, which can be specified instead of *parse_mode*.

    reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup`, *optional*):
        An InlineKeyboardMarkup object.

    input_message_content (:obj:`~pyrogram.types.InputMessageContent`):
        Content of the message to be sent instead of the photo.
```

##### Methods

###### `def __init__(self, document_file_id: str, title: str, id: str = None, description: str = None, caption: str = '', parse_mode: Optional['enums.ParseMode'] = None, caption_entities: List['types.MessageEntity'] = None, reply_markup: 'types.InlineKeyboardMarkup' = None, input_message_content: 'types.InputMessageContent' = None)`

_No docstring._

###### `async def write(self, client: 'pyrogram.Client')`

_No docstring._

---

## File: `types/inline_mode/inline_query_result_cached_photo.py`

### Classes

#### `class InlineQueryResultCachedPhoto(InlineQueryResult)`

```text
A link to a photo stored on the Telegram servers.

By default, this photo will be sent by the user with an optional caption. Alternatively, you can use
*input_message_content* to send a message with the specified content instead of the photo.

Parameters:
    photo_file_id (``str``):
        A valid file identifier of the photo.

    id (``str``, *optional*):
        Unique identifier for this result, 1-64 bytes.
        Defaults to a randomly generated UUID4.

    title (``str``, *optional*):
        Title for the result.

    description (``str``, *optional*):
        Short description of the result.

    caption (``str``, *optional*):
        Caption of the photo to be sent, 0-1024 characters.

    parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
        By default, texts are parsed using both Markdown and HTML styles.
        You can combine both syntaxes together.

    caption_entities (List of :obj:`~pyrogram.types.MessageEntity`):
        List of special entities that appear in the caption, which can be specified instead of *parse_mode*.

    reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup`, *optional*):
        An InlineKeyboardMarkup object.

    input_message_content (:obj:`~pyrogram.types.InputMessageContent`):
        Content of the message to be sent instead of the photo.
```

##### Methods

###### `def __init__(self, photo_file_id: str, id: str = None, title: str = None, description: str = None, caption: str = '', parse_mode: Optional['enums.ParseMode'] = None, caption_entities: List['types.MessageEntity'] = None, reply_markup: 'types.InlineKeyboardMarkup' = None, input_message_content: 'types.InputMessageContent' = None)`

_No docstring._

###### `async def write(self, client: 'pyrogram.Client')`

_No docstring._

---

## File: `types/inline_mode/inline_query_result_cached_sticker.py`

### Classes

#### `class InlineQueryResultCachedSticker(InlineQueryResult)`

```text
A link to a sticker stored on the Telegram servers

By default, this sticker will be sent by the user. Alternatively, you can use *input_message_content* to send a
message with the specified content instead of the sticker.

Parameters:
    sticker_file_id (``str``):
        A valid file identifier of the sticker.

    id (``str``, *optional*):
        Unique identifier for this result, 1-64 bytes.
        Defaults to a randomly generated UUID4.

    reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup`, *optional*):
        An InlineKeyboardMarkup object.

    input_message_content (:obj:`~pyrogram.types.InputMessageContent`):
        Content of the message to be sent instead of the photo.
```

##### Methods

###### `def __init__(self, sticker_file_id: str, id: str = None, reply_markup: 'types.InlineKeyboardMarkup' = None, input_message_content: 'types.InputMessageContent' = None)`

_No docstring._

###### `async def write(self, client: 'pyrogram.Client')`

_No docstring._

---

## File: `types/inline_mode/inline_query_result_cached_video.py`

### Classes

#### `class InlineQueryResultCachedVideo(InlineQueryResult)`

```text
A link to a video file stored on the Telegram servers.

By default, this video file will be sent by the user with an optional caption.
Alternatively, you can use *input_message_content* to send a message with the specified content instead of the
video.

Parameters:
    video_file_id (``str``):
        A valid file identifier for the video file.

    title (``str``):
        Title for the result.

    id (``str``, *optional*):
        Unique identifier for this result, 1-64 bytes.
        Defaults to a randomly generated UUID4.

    description (``str``, *optional*):
        Short description of the result.

    caption (``str``, *optional*):
        Caption of the photo to be sent, 0-1024 characters.

    parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
        By default, texts are parsed using both Markdown and HTML styles.
        You can combine both syntaxes together.

    caption_entities (List of :obj:`~pyrogram.types.MessageEntity`):
        List of special entities that appear in the caption, which can be specified instead of *parse_mode*.

    reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup`, *optional*):
        An InlineKeyboardMarkup object.

    input_message_content (:obj:`~pyrogram.types.InputMessageContent`):
        Content of the message to be sent instead of the photo.
```

##### Methods

###### `def __init__(self, video_file_id: str, title: str, id: str = None, description: str = None, caption: str = '', parse_mode: Optional['enums.ParseMode'] = None, caption_entities: List['types.MessageEntity'] = None, reply_markup: 'types.InlineKeyboardMarkup' = None, input_message_content: 'types.InputMessageContent' = None)`

_No docstring._

###### `async def write(self, client: 'pyrogram.Client')`

_No docstring._

---

## File: `types/inline_mode/inline_query_result_cached_voice.py`

### Classes

#### `class InlineQueryResultCachedVoice(InlineQueryResult)`

```text
A link to a voice message stored on the Telegram servers.

By default, this voice message will be sent by the user.
Alternatively, you can use *input_message_content* to send a message with the specified content instead of the voice
message.

Parameters:
    voice_file_id (``str``):
        A valid file identifier for the voice message.

    id (``str``, *optional*):
        Unique identifier for this result, 1-64 bytes.
        Defaults to a randomly generated UUID4.

    title (``str``, *optional*):
        Title for the result.

    caption (``str``, *optional*):
        Caption of the photo to be sent, 0-1024 characters.

    parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
        By default, texts are parsed using both Markdown and HTML styles.
        You can combine both syntaxes together.

    caption_entities (List of :obj:`~pyrogram.types.MessageEntity`):
        List of special entities that appear in the caption, which can be specified instead of *parse_mode*.

    reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup`, *optional*):
        An InlineKeyboardMarkup object.

    input_message_content (:obj:`~pyrogram.types.InputMessageContent`):
        Content of the message to be sent instead of the photo.
```

##### Methods

###### `def __init__(self, voice_file_id: str, id: str = None, title: str = None, caption: str = '', parse_mode: Optional['enums.ParseMode'] = None, caption_entities: List['types.MessageEntity'] = None, reply_markup: 'types.InlineKeyboardMarkup' = None, input_message_content: 'types.InputMessageContent' = None)`

_No docstring._

###### `async def write(self, client: 'pyrogram.Client')`

_No docstring._

---

## File: `types/inline_mode/inline_query_result_contact.py`

### Classes

#### `class InlineQueryResultContact(InlineQueryResult)`

```text
Contact with a phone number

By default, this contact will be sent by the user.
Alternatively, you can use *input_message_content* to send a message with the specified content instead of the
contact.

Parameters:
    phone_number (``str``):
        Contact's phone number.

    first_name (``str``):
        Contact's first name.

    last_name (``str``, *optional*):
        Contact's last name.

    vcard (``str``, *optional*):
        Additional data about the contact in the form of a `vCard <https://en.wikipedia.org/wiki/VCard>`_.

    id (``str``, *optional*):
        Unique identifier for this result, 1-64 bytes.
        Defaults to a randomly generated UUID4.

    reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup`, *optional*):
        Inline keyboard attached to the message.

    input_message_content (:obj:`~pyrogram.types.InputMessageContent`, *optional*):
        Content of the message to be sent instead of the contact.

    thumb_url (``str``, *optional*):
        Url of the thumbnail for the result.

    thumb_width (``int``, *optional*):
        Thumbnail width.

    thumb_height (``int``, *optional*):
        Thumbnail height.
```

##### Methods

###### `def __init__(self, phone_number: str, first_name: str, last_name: str = '', vcard: str = '', id: str = None, reply_markup: 'types.InlineKeyboardMarkup' = None, input_message_content: 'types.InputMessageContent' = None, thumb_url: str = None, thumb_width: int = 0, thumb_height: int = 0)`

_No docstring._

###### `async def write(self, client: 'pyrogram.Client')`

_No docstring._

---

## File: `types/inline_mode/inline_query_result_document.py`

### Classes

#### `class InlineQueryResultDocument(InlineQueryResult)`

```text
Link to a file.

By default, this file will be sent by the user with an optional caption.
Alternatively, you can use *input_message_content* to send a message with the specified content instead of the file.

Parameters:
    document_url (``str``):
        A valid URL for the file.

    title (``str``):
        Title for the result.

    mime_type (``str``, *optional*):
        Mime type of the content of the file, either “application/pdf” or “application/zip”.
        Defaults to "application/zip".

    id (``str``, *optional*):
        Unique identifier for this result, 1-64 bytes.
        Defaults to a randomly generated UUID4.

    caption (``str``, *optional*):
        Caption of the video to be sent, 0-1024 characters.

    parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
        By default, texts are parsed using both Markdown and HTML styles.
        You can combine both syntaxes together.

    caption_entities (List of :obj:`~pyrogram.types.MessageEntity`):
        List of special entities that appear in the caption, which can be specified instead of *parse_mode*.

    description (``str``, *optional*):
        Short description of the result.

    reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup`, *optional*):
        Inline keyboard attached to the message.

    input_message_content (:obj:`~pyrogram.types.InputMessageContent`):
        Content of the message to be sent instead of the file.

    thumb_url (``str``, *optional*):
        Url of the thumbnail for the result.

    thumb_width (``int``, *optional*):
        Thumbnail width.

    thumb_height (``int``, *optional*):
        Thumbnail height.
```

##### Methods

###### `def __init__(self, document_url: str, title: str, mime_type: str = 'application/zip', id: str = None, caption: str = '', parse_mode: Optional['enums.ParseMode'] = None, caption_entities: List['types.MessageEntity'] = None, description: str = '', reply_markup: 'types.InlineKeyboardMarkup' = None, input_message_content: 'types.InputMessageContent' = None, thumb_url: str = None, thumb_width: int = 0, thumb_height: int = 0)`

_No docstring._

###### `async def write(self, client: 'pyrogram.Client')`

_No docstring._

---

## File: `types/inline_mode/inline_query_result_location.py`

### Classes

#### `class InlineQueryResultLocation(InlineQueryResult)`

```text
A location on a map.

By default, the location will be sent by the user. Alternatively, you can use *input_message_content* to send a
message with the specified content instead of the location.

Parameters:
    title (``str``):
        Title for the result.

    latitude (``float``):
        Location latitude in degrees.

    longitude (``float``):
        Location longitude in degrees.

    id (``str``, *optional*):
        Unique identifier for this result, 1-64 bytes.
        Defaults to a randomly generated UUID4.

    horizontal_accuracy (``float``, *optional*)
        The radius of uncertainty for the location, measured in meters; 0-1500.

    live_period (``int``, *optional*):
        Period in seconds for which the location can be updated, should be between 60 and 86400.

    heading (``int``, *optional*):
        For live locations, a direction in which the user is moving, in degrees.
        Must be between 1 and 360 if specified.

    proximity_alert_radius (``int``, *optional*):
        For live locations, a maximum distance for proximity alerts about approaching another chat member,
        in meters. Must be between 1 and 100000 if specified.

    reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup`, *optional*):
        Inline keyboard attached to the message.

    input_message_content (:obj:`~pyrogram.types.InputMessageContent`):
        Content of the message to be sent instead of the file.

    thumb_url (``str``, *optional*):
        Url of the thumbnail for the result.

    thumb_width (``int``, *optional*):
        Thumbnail width.

    thumb_height (``int``, *optional*):
        Thumbnail height.
```

##### Methods

###### `def __init__(self, title: str, latitude: float, longitude: float, horizontal_accuracy: float = None, live_period: int = None, heading: int = None, proximity_alert_radius: int = None, id: str = None, reply_markup: 'types.InlineKeyboardMarkup' = None, input_message_content: 'types.InputMessageContent' = None, thumb_url: str = None, thumb_width: int = 0, thumb_height: int = 0)`

_No docstring._

###### `async def write(self, client: 'pyrogram.Client')`

_No docstring._

---

## File: `types/inline_mode/inline_query_result_photo.py`

### Classes

#### `class InlineQueryResultPhoto(InlineQueryResult)`

```text
Link to a photo.

By default, this photo will be sent by the user with optional caption.
Alternatively, you can use *input_message_content* to send a message with the specified content instead of the
photo.

Parameters:
    photo_url (``str``):
        A valid URL of the photo.
        Photo must be in jpeg format an must not exceed 5 MB.

    thumb_url (``str``, *optional*):
        URL of the thumbnail for the photo.
        Defaults to the value passed in *photo_url*.

    photo_width (``int``, *optional*):
        Width of the photo.

    photo_height (``int``, *optional*):
        Height of the photo

    id (``str``, *optional*):
        Unique identifier for this result, 1-64 bytes.
        Defaults to a randomly generated UUID4.

    title (``str``, *optional*):
        Title for the result.

    description (``str``, *optional*):
        Short description of the result.

    caption (``str``, *optional*):
        Caption of the photo to be sent, 0-1024 characters.

    parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
        By default, texts are parsed using both Markdown and HTML styles.
        You can combine both syntaxes together.

    caption_entities (List of :obj:`~pyrogram.types.MessageEntity`):
        List of special entities that appear in the caption, which can be specified instead of *parse_mode*.

    reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup`, *optional*):
        An InlineKeyboardMarkup object.

    input_message_content (:obj:`~pyrogram.types.InputMessageContent`):
        Content of the message to be sent instead of the photo.
```

##### Methods

###### `def __init__(self, photo_url: str, thumb_url: str = None, photo_width: int = 0, photo_height: int = 0, id: str = None, title: str = None, description: str = None, caption: str = '', parse_mode: Optional['enums.ParseMode'] = None, caption_entities: List['types.MessageEntity'] = None, reply_markup: 'types.InlineKeyboardMarkup' = None, input_message_content: 'types.InputMessageContent' = None)`

_No docstring._

###### `async def write(self, client: 'pyrogram.Client')`

_No docstring._

---

## File: `types/inline_mode/inline_query_result_venue.py`

### Classes

#### `class InlineQueryResultVenue(InlineQueryResult)`

```text
A venue.

By default, the venue will be sent by the user. Alternatively, you can use *input_message_content* to send a message
with the specified content instead of the venue.

Parameters:
    title (``str``):
        Title for the result.

    address (``str``):
        Address of the venue.

    latitude (``float``):
        Location latitude in degrees.

    longitude (``float``):
        Location longitude in degrees.

    id (``str``, *optional*):
        Unique identifier for this result, 1-64 bytes.
        Defaults to a randomly generated UUID4.

    foursquare_id (``str``, *optional*):
        Foursquare identifier of the venue if known.

    foursquare_type (``str``, *optional*):
        Foursquare type of the venue, if known.

    google_place_id (``str``, *optional*):
        Google Places identifier of the venue.

    google_place_type (``str``, *optional*):
        Google Places type of the venue.

    reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup`, *optional*):
        Inline keyboard attached to the message.

    input_message_content (:obj:`~pyrogram.types.InputMessageContent`):
        Content of the message to be sent instead of the file.

    thumb_url (``str``, *optional*):
        Url of the thumbnail for the result.

    thumb_width (``int``, *optional*):
        Thumbnail width.

    thumb_height (``int``, *optional*):
        Thumbnail height.
```

##### Methods

###### `def __init__(self, title: str, address: str, latitude: float, longitude: float, id: str = None, foursquare_id: str = None, foursquare_type: str = None, google_place_id: str = None, google_place_type: str = None, reply_markup: 'types.InlineKeyboardMarkup' = None, input_message_content: 'types.InputMessageContent' = None, thumb_url: str = None, thumb_width: int = 0, thumb_height: int = 0)`

_No docstring._

###### `async def write(self, client: 'pyrogram.Client')`

_No docstring._

---

## File: `types/inline_mode/inline_query_result_video.py`

### Classes

#### `class InlineQueryResultVideo(InlineQueryResult)`

```text
Link to a page containing an embedded video player or a video file.

By default, this video file will be sent by the user with an optional caption.
Alternatively, you can use *input_message_content* to send a message with the specified content instead of the
video.

Parameters:
    video_url (``str``):
        A valid URL for the embedded video player or video file.

    thumb_url (``str``):
        URL of the thumbnail (jpeg only) for the video.

    title (``str``):
        Title for the result.

    id (``str``, *optional*):
        Unique identifier for this result, 1-64 bytes.
        Defaults to a randomly generated UUID4.

    mime_type (``str``):
        Mime type of the content of video url, "text/html" or "video/mp4".
        Defaults to "video/mp4".

    video_width (``int``):
        Video width.

    video_height (``int``):
        Video height.

    video_duration (``int``):
        Video duration in seconds.

    description (``str``, *optional*):
        Short description of the result.

    caption (``str``, *optional*):
        Caption of the video to be sent, 0-1024 characters.

    parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
        By default, texts are parsed using both Markdown and HTML styles.
        You can combine both syntaxes together.

    caption_entities (List of :obj:`~pyrogram.types.MessageEntity`):
        List of special entities that appear in the caption, which can be specified instead of *parse_mode*.

    reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup`, *optional*):
        Inline keyboard attached to the message

    input_message_content (:obj:`~pyrogram.types.InputMessageContent`):
        Content of the message to be sent instead of the video. This field is required if InlineQueryResultVideo is
        used to send an HTML-page as a result (e.g., a YouTube video).
```

##### Methods

###### `def __init__(self, video_url: str, thumb_url: str, title: str, id: str = None, mime_type: str = 'video/mp4', video_width: int = 0, video_height: int = 0, video_duration: int = 0, description: str = None, caption: str = '', parse_mode: Optional['enums.ParseMode'] = None, caption_entities: List['types.MessageEntity'] = None, reply_markup: 'types.InlineKeyboardMarkup' = None, input_message_content: 'types.InputMessageContent' = None)`

_No docstring._

###### `async def write(self, client: 'pyrogram.Client')`

_No docstring._

---

## File: `types/inline_mode/inline_query_result_voice.py`

### Classes

#### `class InlineQueryResultVoice(InlineQueryResult)`

```text
Link to a voice recording in an .OGG container encoded with OPUS.

By default, this voice recording will be sent by the user.
Alternatively, you can use *input_message_content* to send a message with the specified content instead of the
voice message.

Parameters:
    voice_url (``str``):
        A valid URL for the voice recording.

    title (``str``):
        Title for the result.

    id (``str``, *optional*):
        Unique identifier for this result, 1-64 bytes.
        Defaults to a randomly generated UUID4.

    voice_duration (``int``, *optional*):
        Recording duration in seconds.

    caption (``str``, *optional*):
        Caption of the audio to be sent, 0-1024 characters.

    parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
        By default, texts are parsed using both Markdown and HTML styles.
        You can combine both syntaxes together.

    caption_entities (List of :obj:`~pyrogram.types.MessageEntity`):
        List of special entities that appear in the caption, which can be specified instead of *parse_mode*.

    reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup`, *optional*):
        Inline keyboard attached to the message.

    input_message_content (:obj:`~pyrogram.types.InputMessageContent`, *optional*):
        Content of the message to be sent instead of the audio.
```

##### Methods

###### `def __init__(self, voice_url: str, title: str, id: str = None, voice_duration: int = 0, caption: str = '', parse_mode: Optional['enums.ParseMode'] = None, caption_entities: List['types.MessageEntity'] = None, reply_markup: 'types.InlineKeyboardMarkup' = None, input_message_content: 'types.InputMessageContent' = None)`

_No docstring._

###### `async def write(self, client: 'pyrogram.Client')`

_No docstring._

---

## File: `types/input_media/__init__.py`

---

## File: `types/input_media/input_media.py`

### Classes

#### `class InputMedia(Object)`

```text
Content of a media message to be sent.

It should be one of:

- :obj:`~pyrogram.types.InputMediaAnimation`
- :obj:`~pyrogram.types.InputMediaDocument`
- :obj:`~pyrogram.types.InputMediaAudio`
- :obj:`~pyrogram.types.InputMediaPhoto`
- :obj:`~pyrogram.types.InputMediaVideo`
```

##### Methods

###### `def __init__(self, media: Union[str, BinaryIO], caption: str = '', parse_mode: str = None, caption_entities: List[MessageEntity] = None)`

_No docstring._

---

## File: `types/input_media/input_media_animation.py`

### Classes

#### `class InputMediaAnimation(InputMedia)`

```text
An animation file (GIF or H.264/MPEG-4 AVC video without sound) to be sent inside an album.

Parameters:
    media (``str`` | ``BinaryIO``):
        Animation to send.
        Pass a file_id as string to send a file that exists on the Telegram servers or
        pass a file path as string to upload a new file that exists on your local machine or
        pass a binary file-like object with its attribute “.name” set for in-memory uploads or
        pass an HTTP URL as a string for Telegram to get an animation from the Internet.

    thumb (``str``, *optional*):
        Thumbnail of the animation file sent.
        The thumbnail should be in JPEG format and less than 200 KB in size.
        A thumbnail's width and height should not exceed 320 pixels.
        Thumbnails can't be reused and can be only uploaded as a new file.

    caption (``str``, *optional*):
        Caption of the animation to be sent, 0-1024 characters.
        If not specified, the original caption is kept. Pass "" (empty string) to remove the caption.

    parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
        By default, texts are parsed using both Markdown and HTML styles.
        You can combine both syntaxes together.

    caption_entities (List of :obj:`~pyrogram.types.MessageEntity`):
        List of special entities that appear in the caption, which can be specified instead of *parse_mode*.

    width (``int``, *optional*):
        Animation width.

    height (``int``, *optional*):
        Animation height.

    duration (``int``, *optional*):
        Animation duration.

    has_spoiler (``bool``, *optional*):
        Pass True if the photo needs to be covered with a spoiler animation.
```

##### Methods

###### `def __init__(self, media: Union[str, BinaryIO], thumb: str = None, caption: str = '', parse_mode: Optional['enums.ParseMode'] = None, caption_entities: List[MessageEntity] = None, width: int = 0, height: int = 0, duration: int = 0, has_spoiler: bool = None)`

_No docstring._

---

## File: `types/input_media/input_media_area.py`

### Classes

#### `class InputMediaArea(Object)`

```text
Content of a media area to be included in story.

Pyrofork currently supports the following types:

- :obj:`~pyrogram.types.InputMediaAreaChannelPost`
```

##### Methods

###### `def __init__(self, coordinates: 'types.MediaAreaCoordinates')`

_No docstring._

---

## File: `types/input_media/input_media_area_channel_post.py`

### Classes

#### `class InputMediaAreaChannelPost(InputMediaArea)`

```text
A channel post media area.

Parameters:
    coordinates (:obj:`~pyrogram.types.MediaAreaCoordinates`):
        Media area coordinates.

    chat_id (``int`` | ``str``):
        Unique identifier (int) or username (str) of the target channel.

    message_id (``int``):
        A single message id.
```

##### Methods

###### `def __init__(self, coordinates: 'types.MediaAreaCoordinates', chat_id: Union[int, str], message_id: int)`

_No docstring._

###### `async def write(self, client: 'pyrogram.Client')`

_No docstring._

---

## File: `types/input_media/input_media_audio.py`

### Classes

#### `class InputMediaAudio(InputMedia)`

```text
An audio to be sent inside an album.

It is intended to be used with :meth:`~pyrogram.Client.send_media_group`.

Parameters:
    media (``str`` | ``BinaryIO``):
        Audio to send.
        Pass a file_id as string to send an audio that exists on the Telegram servers or
        pass a file path as string to upload a new audio that exists on your local machine or
        pass a binary file-like object with its attribute “.name” set for in-memory uploads or
        pass an HTTP URL as a string for Telegram to get an audio file from the Internet.

    thumb (``str``, *optional*):
        Thumbnail of the music file album cover.
        The thumbnail should be in JPEG format and less than 200 KB in size.
        A thumbnail's width and height should not exceed 320 pixels.
        Thumbnails can't be reused and can be only uploaded as a new file.

    caption (``str``, *optional*):
        Caption of the audio to be sent, 0-1024 characters.
        If not specified, the original caption is kept. Pass "" (empty string) to remove the caption.

    parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
        By default, texts are parsed using both Markdown and HTML styles.
        You can combine both syntaxes together.

    caption_entities (List of :obj:`~pyrogram.types.MessageEntity`):
        List of special entities that appear in the caption, which can be specified instead of *parse_mode*.

    duration (``int``, *optional*):
        Duration of the audio in seconds

    performer (``str``, *optional*):
        Performer of the audio

    title (``str``, *optional*):
        Title of the audio

    file_name (``str``, *optional*):
        File name of the audio sent.
        Defaults to file's path basename.
```

##### Methods

###### `def __init__(self, media: Union[str, BinaryIO], thumb: str = None, caption: str = '', parse_mode: Optional['enums.ParseMode'] = None, caption_entities: List[MessageEntity] = None, duration: int = 0, performer: str = '', title: str = '', file_name: str = None)`

_No docstring._

---

## File: `types/input_media/input_media_document.py`

### Classes

#### `class InputMediaDocument(InputMedia)`

```text
A generic file to be sent inside an album.

Parameters:
    media (``str`` | ``BinaryIO``):
        File to send.
        Pass a file_id as string to send a file that exists on the Telegram servers or
        pass a file path as string to upload a new file that exists on your local machine or
        pass a binary file-like object with its attribute “.name” set for in-memory uploads or
        pass an HTTP URL as a string for Telegram to get a file from the Internet.

    thumb (``str``):
        Thumbnail of the file sent.
        The thumbnail should be in JPEG format and less than 200 KB in size.
        A thumbnail's width and height should not exceed 320 pixels.
        Thumbnails can't be reused and can be only uploaded as a new file.

    caption (``str``, *optional*):
        Caption of the document to be sent, 0-1024 characters.
        If not specified, the original caption is kept. Pass "" (empty string) to remove the caption.

    parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
        By default, texts are parsed using both Markdown and HTML styles.
        You can combine both syntaxes together.

    caption_entities (List of :obj:`~pyrogram.types.MessageEntity`):
        List of special entities that appear in the caption, which can be specified instead of *parse_mode*.

    file_name (``str``, *optional*):
        File name of the document sent.
        Defaults to file's path basename.
```

##### Methods

###### `def __init__(self, media: Union[str, BinaryIO], thumb: str = None, caption: str = '', parse_mode: Optional['enums.ParseMode'] = None, caption_entities: List[MessageEntity] = None, file_name: str = None)`

_No docstring._

---

## File: `types/input_media/input_media_photo.py`

### Classes

#### `class InputMediaPhoto(InputMedia)`

```text
A photo to be sent inside an album.
It is intended to be used with :obj:`~pyrogram.Client.send_media_group`.

Parameters:
    media (``str`` | ``BinaryIO``):
        Photo to send.
        Pass a file_id as string to send a photo that exists on the Telegram servers or
        pass a file path as string to upload a new photo that exists on your local machine or
        pass a binary file-like object with its attribute “.name” set for in-memory uploads or
        pass an HTTP URL as a string for Telegram to get a photo from the Internet.

    caption (``str``, *optional*):
        Caption of the photo to be sent, 0-1024 characters.
        If not specified, the original caption is kept. Pass "" (empty string) to remove the caption.

    parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
        By default, texts are parsed using both Markdown and HTML styles.
        You can combine both syntaxes together.

    caption_entities (List of :obj:`~pyrogram.types.MessageEntity`):
        List of special entities that appear in the caption, which can be specified instead of *parse_mode*.

    has_spoiler (``bool``, *optional*):
        Pass True if the photo needs to be covered with a spoiler animation.
```

##### Methods

###### `def __init__(self, media: Union[str, BinaryIO], caption: str = '', parse_mode: Optional['enums.ParseMode'] = None, caption_entities: List[MessageEntity] = None, has_spoiler: bool = None)`

_No docstring._

---

## File: `types/input_media/input_media_video.py`

### Classes

#### `class InputMediaVideo(InputMedia)`

```text
A video to be sent inside an album.
It is intended to be used with :obj:`~pyrogram.Client.send_media_group`.

Parameters:
    media (``str`` | ``BinaryIO``):
        Video to send.
        Pass a file_id as string to send a video that exists on the Telegram servers or
        pass a file path as string to upload a new video that exists on your local machine or
        pass a binary file-like object with its attribute “.name” set for in-memory uploads or
        pass an HTTP URL as a string for Telegram to get a video from the Internet.

    thumb (``str``):
        Thumbnail of the video sent.
        The thumbnail should be in JPEG format and less than 200 KB in size.
        A thumbnail's width and height should not exceed 320 pixels.
        Thumbnails can't be reused and can be only uploaded as a new file.

    caption (``str``, *optional*):
        Caption of the video to be sent, 0-1024 characters.
        If not specified, the original caption is kept. Pass "" (empty string) to remove the caption.

    parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
        By default, texts are parsed using both Markdown and HTML styles.
        You can combine both syntaxes together.

    caption_entities (List of :obj:`~pyrogram.types.MessageEntity`):
        List of special entities that appear in the caption, which can be specified instead of *parse_mode*.

    width (``int``, *optional*):
        Video width.

    height (``int``, *optional*):
        Video height.

    duration (``int``, *optional*):
        Video duration.

    file_name (``str``, *optional*):
        File name of the video sent.
        Defaults to file's path basename.

    supports_streaming (``bool``, *optional*):
        Pass True, if the uploaded video is suitable for streaming.

    has_spoiler (``bool``, *optional*):
        Pass True if the photo needs to be covered with a spoiler animation.
```

##### Methods

###### `def __init__(self, media: Union[str, BinaryIO], thumb: str = None, caption: str = '', parse_mode: Optional['enums.ParseMode'] = None, caption_entities: List[MessageEntity] = None, width: int = 0, height: int = 0, duration: int = 0, file_name: str = None, supports_streaming: bool = True, has_spoiler: bool = None)`

_No docstring._

---

## File: `types/input_media/input_phone_contact.py`

### Classes

#### `class InputPhoneContact(Object)`

```text
A Phone Contact to be added in your Telegram address book.
It is intended to be used with :meth:`~pyrogram.Client.add_contacts()`

Parameters:
    phone (``str``):
        Contact's phone number

    first_name (``str``):
        Contact's first name

    last_name (``str``, *optional*):
        Contact's last name
```

##### Methods

###### `def __init__(self, phone: str, first_name: str, last_name: str = '')`

_No docstring._

###### `def __new__(cls, phone: str, first_name: str, last_name: str = '')`

_No docstring._

---

## File: `types/input_message_content/__init__.py`

---

## File: `types/input_message_content/input_contact_message_content.py`

### Classes

#### `class InputContactMessageContent(InputMessageContent)`

```text
Content of a contact message to be sent as the result of an inline query.

Parameters:
    phone_number (``str``):
        Contact's phone number.

    first_name (``str``):
        Contact's first name.

    last_name (``str``, *optional*):
        Contact's last name.

    vcard (``str``, *optional*):
        Additional data about the contact in the form of a `vCard <https://en.wikipedia.org/wiki/VCard>`_, 0-2048 bytes.
```

##### Methods

###### `def __init__(self, phone_number: str, first_name: str, last_name: Optional[str] = None, vcard: Optional[str] = None)`

_No docstring._

###### `async def write(self, client: 'pyrogram.Client', reply_markup)`

_No docstring._

---

## File: `types/input_message_content/input_invoice_message_content.py`

### Classes

#### `class InputInvoiceMessageContent(InputMessageContent)`

```text
Content of an invoice message to be sent as the result of an inline query.

Parameters:
    title (``str``):
        Product name, 1-32 characters.

    description (``str``):
        Product description, 1-255 characters

    payload (``str`` | ``bytes``):
        Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user, use for your internal processes.

    currency (``str``):
        Three-letter ISO 4217 currency code, see `more on currencies <https://core.telegram.org/bots/payments#supported-currencies>`_. Pass ``XTR`` for payments in `Telegram Stars <https://t.me/BotNews/90>`_.

    prices (List of :obj:`~pyrogram.types.LabeledPrice`):
        Price breakdown, a JSON-serialized list of components (e.g. product price, tax, discount, delivery cost, delivery tax, bonus, etc.). Must contain exactly one item for payments in `Telegram Stars <https://t.me/BotNews/90>`_.

    provider_token (``str``, *optional*):
        Payment provider token, obtained via `@BotFather <https://t.me/botfather>`_. Pass an empty string for payments in `Telegram Stars <https://t.me/BotNews/90>`_.

    max_tip_amount (``int``, *optional*):
        The maximum accepted amount for tips in the smallest units of the currency (integer, **not** float/double). For example, for a maximum tip of ``US$ 1.45`` pass ``max_tip_amount = 145``. See the exp parameter in `currencies.json <https://core.telegram.org/bots/payments/currencies.json>`_, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies). Defaults to 0. Not supported for payments in `Telegram Stars <https://t.me/BotNews/90>`_.

    suggested_tip_amounts (List of ``int``, *optional*):
        An array of suggested amounts of tips in the smallest units of the currency (integer, **not** float/double). At most 4 suggested tip amounts can be specified. The suggested tip amounts must be positive, passed in a strictly increased order and must not exceed ``max_tip_amount``.

    provider_data (``str``, *optional*):
        JSON-serialized data about the invoice, which will be shared with the payment provider. A detailed description of required fields should be provided by the payment provider.

    photo_url (``str``, *optional*):
        URL of the product photo for the invoice. Can be a photo of the goods or a marketing image for a service. People like it better when they see what they are paying for.

    photo_size (``int``, *optional*):
        Photo size in bytes

    photo_width (``int``, *optional*):
        Photo width

    photo_height (``int``, *optional*):
        Photo height

    need_name (``bool``, *optional*):
        Pass True if you require the user's full name to complete the order. Ignored for payments in `Telegram Stars <https://t.me/BotNews/90>`_.

    need_phone_number (``bool``, *optional*):
        Pass True if you require the user's phone number to complete the order. Ignored for payments in `Telegram Stars <https://t.me/BotNews/90>`_.

    need_email (``bool``, *optional*):
        Pass True if you require the user's email address to complete the order. Ignored for payments in `Telegram Stars <https://t.me/BotNews/90>`_.

    need_shipping_address (``bool``, *optional*):
        Pass True if you require the user's shipping address to complete the order. Ignored for payments in `Telegram Stars <https://t.me/BotNews/90>`_.

    send_phone_number_to_provider (``bool``, *optional*):
        Pass True if the user's phone number should be sent to the provider. Ignored for payments in `Telegram Stars <https://t.me/BotNews/90>`_.

    send_email_to_provider (``bool``, *optional*):
        Pass True if the user's email address should be sent to the provider. Ignored for payments in `Telegram Stars <https://t.me/BotNews/90>`_.

    is_flexible (``bool``, *optional*):
        Pass True if the final price depends on the shipping method. Ignored for payments in `Telegram Stars <https://t.me/BotNews/90>`_.
```

##### Methods

###### `def __init__(self, title: str, description: str, payload: Union[str, bytes], currency: str, prices: List['types.LabeledPrice'], provider_token: Optional[str] = None, max_tip_amount: Optional[int] = None, suggested_tip_amounts: List[int] = None, provider_data: Optional[str] = None, photo_url: Optional[str] = None, photo_size: Optional[int] = None, photo_width: Optional[int] = None, photo_height: Optional[int] = None, need_name: Optional[bool] = None, need_phone_number: Optional[bool] = None, need_email: Optional[bool] = None, need_shipping_address: Optional[bool] = None, send_phone_number_to_provider: Optional[bool] = None, send_email_to_provider: Optional[bool] = None, is_flexible: Optional[bool] = None)`

_No docstring._

###### `async def write(self, client: 'pyrogram.Client', reply_markup)`

_No docstring._

---

## File: `types/input_message_content/input_location_message_content.py`

### Classes

#### `class InputLocationMessageContent(InputMessageContent)`

```text
Content of a location message to be sent as the result of an inline query.

Parameters:
    latitude (``float``):
        Latitude of the location.

    longitude (``float``):
        Longitude of the location.

    horizontal_accuracy (``float``, *optional*):
        The radius of uncertainty for the location, measured in meters; 0-1500.

    live_period (``int``, *optional*):
        Period in seconds during which the location can be updated, should be between 60 and 86400, or 0x7FFFFFFF for live locations that can be edited indefinitely.

    heading (``int``, *optional*):
        For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified.

    proximity_alert_radius (``int``, *optional*):
        For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified.
```

##### Methods

###### `def __init__(self, latitude: float, longitude: float, horizontal_accuracy: Optional[float] = None, live_period: Optional[int] = None, heading: Optional[int] = None, proximity_alert_radius: Optional[int] = None)`

_No docstring._

###### `async def write(self, client: 'pyrogram.Client', reply_markup)`

_No docstring._

---

## File: `types/input_message_content/input_message_content.py`

### Classes

#### `class InputMessageContent(Object)`

```text
Content of a message to be sent as a result of an inline query.

Telegram clients currently support the following 5 types:

- :obj:`~pyrogram.types.InputTextMessageContent`
- :obj:`~pyrogram.types.InputLocationMessageContent`
- :obj:`~pyrogram.types.InputVenueMessageContent`
- :obj:`~pyrogram.types.InputContactMessageContent`
- :obj:`~pyrogram.types.InputInvoiceMessageContent`
```

##### Methods

###### `def __init__(self)`

_No docstring._

###### `async def write(self, client: 'pyrogram.Client', reply_markup)`

_No docstring._

---

## File: `types/input_message_content/input_reply_to_message.py`

### Classes

#### `class InputReplyToMessage(Object)`

```text
Contains information about a target replied message.


Parameters:
    reply_to_message_id (``int``, *optional*):
        ID of the original message you want to reply.

    message_thread_id (``int``, *optional*):
        Unique identifier for the target message thread (topic) of the forum.
        for forum supergroups only.

    reply_to_chat (:obj:`~pyrogram.raw.InputPeer`, *optional*):
        Unique identifier for the origin chat.
        for reply to message from another chat.

    quote_text (``str``, *optional*):
        Text to quote.
        for reply_to_message only.

    quote_entities (List of :obj:`~pyrogram.raw.base.MessageEntity`):
        Entities to quote.
        for reply_to_message only.
```

##### Methods

###### `def __init__(self, *, reply_to_message_id: int = None, message_thread_id: int = None, reply_to_chat: Union['raw.types.InputPeerChannel', 'raw.types.InputPeerUser'] = None, quote_text: str = None, quote_entities: List['raw.base.MessageEntity'] = None, quote_offset: int = None)`

_No docstring._

###### `def write(self)`

_No docstring._

---

## File: `types/input_message_content/input_reply_to_monoforum.py`

### Classes

#### `class InputReplyToMonoforum(Object)`

```text
Contains information about a target replied monoforum.


Parameters:
    monoforum_peer (:obj:`~pyrogram.raw.types.InputPeer`):
        An InputPeer.
```

##### Methods

###### `def __init__(self, *, monoforum_peer: 'raw.types.InputPeer')`

_No docstring._

###### `def write(self)`

_No docstring._

---

## File: `types/input_message_content/input_reply_to_story.py`

### Classes

#### `class InputReplyToStory(Object)`

```text
Contains information about a target replied story.


Parameters:
    peer (:obj:`~pyrogram.raw.types.InputPeer`):
        An InputPeer.

    story_id (``int``):
        Unique identifier for the target story.
```

##### Methods

###### `def __init__(self, *, peer: 'raw.types.InputPeer' = None, story_id: int = None)`

_No docstring._

###### `def write(self)`

_No docstring._

---

## File: `types/input_message_content/input_text_message_content.py`

### Classes

#### `class InputTextMessageContent(InputMessageContent)`

```text
Content of a text message to be sent as the result of an inline query.

Parameters:
    message_text (``str``):
        Text of the message to be sent, 1-4096 characters.

    parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
        By default, texts are parsed using both Markdown and HTML styles.
        You can combine both syntaxes together.

    entities (List of :obj:`~pyrogram.types.MessageEntity`):
        List of special entities that appear in message text, which can be specified instead of *parse_mode*.

    disable_web_page_preview (``bool``, *optional*):
        Disables link previews for links in this message.
```

##### Methods

###### `def __init__(self, message_text: str, parse_mode: Optional['enums.ParseMode'] = None, entities: List['types.MessageEntity'] = None, disable_web_page_preview: bool = None)`

_No docstring._

###### `async def write(self, client: 'pyrogram.Client', reply_markup)`

_No docstring._

---

## File: `types/input_message_content/input_todo_task.py`

### Classes

#### `class InputTodoTask(Object)`

```text
Contains information about a todo task.

Parameters:
    title (``str``):
        Title of the task.

    entities (List of :obj:`~pyrogram.types.MessageEntity`):
        Entities in the title of the task.
```

##### Methods

###### `def __init__(self, *, title: str, entities: list = None)`

_No docstring._

---

## File: `types/input_message_content/input_venue_message_content.py`

### Classes

#### `class InputVenueMessageContent(InputMessageContent)`

```text
Content of a venue message to be sent as the result of an inline query.

Parameters:
    latitude (``float``):
        Latitude of the location.

    longitude (``float``):
        Longitude of the location.

    title (``str``):
        Name of the venue.

    address (``str``):
        Address of the venue.

    foursquare_id (``str``, *optional*):
        Foursquare identifier of the venue, if known.

    foursquare_type (``str``, *optional*):
        Foursquare type of the venue, if known. (For example, “arts_entertainment/default”, “arts_entertainment/aquarium” or “food/icecream”.)
```

##### Methods

###### `def __init__(self, latitude: float, longitude: float, title: str, address: str, foursquare_id: Optional[str] = None, foursquare_type: Optional[str] = None, google_place_id: Optional[str] = None, google_place_type: Optional[str] = None)`

_No docstring._

###### `async def write(self, client: 'pyrogram.Client', reply_markup)`

_No docstring._

---

## File: `types/list.py`

### Classes

#### `class List(list)`

_No docstring._

##### Methods

###### `def __str__(self)`

_No docstring._

###### `def __repr__(self)`

_No docstring._

---

## File: `types/messages_and_media/__init__.py`

---

## File: `types/messages_and_media/alternative_video.py`

### Classes

#### `class AlternativeVideo(Object)`

```text
Describes an alternative reencoded quality of a video file.

Parameters:
    file_id (``str``):
        Identifier for this file, which can be used to download or reuse the file.

    file_unique_id (``str``):
        Unique identifier for this file, which is supposed to be the same over time and for different accounts.
        Can't be used to download or reuse the file.

    width (``int``):
        Video width as defined by sender.

    height (``int``):
        Video height as defined by sender.

    codec (``str``):
        Codec used for video file encoding, for example, "h264", "h265", or "av1".

    duration (``int``):
        Duration of the video in seconds as defined by sender.

    file_name (``str``, *optional*):
        Video file name.

    mime_type (``str``, *optional*):
        Mime type of a file as defined by sender.

    file_size (``int``, *optional*):
        File size.

    supports_streaming (``bool``, *optional*):
        True, if the video was uploaded with streaming support.

    date (:py:obj:`~datetime.datetime`, *optional*):
        Date the video was sent.

    thumbs (List of :obj:`~pyrogram.types.Thumbnail`, *optional*):
        Video thumbnails.
```

##### Methods

###### `def __init__(self, *, client: 'pyrogram.Client' = None, file_id: str, file_unique_id: str, width: int, height: int, codec: str, duration: int, file_name: str = None, mime_type: str = None, file_size: int = None, supports_streaming: bool = None, date: datetime = None, thumbs: List['types.Thumbnail'] = None)`

_No docstring._

###### `def _parse(client, video: 'raw.types.Document', video_attributes: 'raw.types.DocumentAttributeVideo', file_name: str) -> 'AlternativeVideo'`

_No docstring._

---

## File: `types/messages_and_media/animation.py`

### Classes

#### `class Animation(Object)`

```text
An animation file (GIF or H.264/MPEG-4 AVC video without sound).

Parameters:
    file_id (``str``):
        Identifier for this file, which can be used to download or reuse the file.

    file_unique_id (``str``):
        Unique identifier for this file, which is supposed to be the same over time and for different accounts.
        Can't be used to download or reuse the file.

    width (``int``):
        Animation width as defined by sender.

    height (``int``):
        Animation height as defined by sender.

    duration (``int``, *optional*):
        Duration of the animation in seconds as defined by sender.

    file_name (``str``, *optional*):
        Animation file name.

    mime_type (``str``, *optional*):
        Mime type of a file as defined by sender.

    file_size (``int``, *optional*):
        File size.

    date (:py:obj:`~datetime.datetime`, *optional*):
        Date the animation was sent.

    thumbs (List of :obj:`~pyrogram.types.Thumbnail`, *optional*):
        Animation thumbnails.
```

##### Methods

###### `def __init__(self, *, client: 'pyrogram.Client' = None, file_id: str, file_unique_id: str, width: int, height: int, duration: int = None, file_name: str = None, mime_type: str = None, file_size: int = None, date: datetime = None, thumbs: List['types.Thumbnail'] = None)`

_No docstring._

###### `def _parse(client, animation: 'raw.types.Document', video_attributes: 'raw.types.DocumentAttributeVideo', file_name: str) -> 'Animation'`

_No docstring._

###### `def _parse_chat_animation(client, video: 'raw.types.Photo') -> 'Animation'`

_No docstring._

---

## File: `types/messages_and_media/audio.py`

### Classes

#### `class Audio(Object)`

```text
An audio file to be treated as music by the Telegram clients.

Parameters:
    file_id (``str``):
        Identifier for this file, which can be used to download or reuse the file.

    file_unique_id (``str``):
        Unique identifier for this file, which is supposed to be the same over time and for different accounts.
        Can't be used to download or reuse the file.

    duration (``int``):
        Duration of the audio in seconds as defined by sender.

    performer (``str``, *optional*):
        Performer of the audio as defined by sender or by audio tags.

    title (``str``, *optional*):
        Title of the audio as defined by sender or by audio tags.

    file_name (``str``, *optional*):
        Audio file name.

    mime_type (``str``, *optional*):
        MIME type of the file as defined by sender.

    file_size (``int``, *optional*):
        File size.

    date (:py:obj:`~datetime.datetime`, *optional*):
        Date the audio was originally sent.

    thumbs (List of :obj:`~pyrogram.types.Thumbnail`, *optional*):
        Thumbnails of the music file album cover.
```

##### Methods

###### `def __init__(self, *, client: 'pyrogram.Client' = None, file_id: str, file_unique_id: str, duration: int, performer: str = None, title: str = None, file_name: str = None, mime_type: str = None, file_size: int = None, date: datetime = None, thumbs: List['types.Thumbnail'] = None)`

_No docstring._

###### `def _parse(client, audio: 'raw.types.Document', audio_attributes: 'raw.types.DocumentAttributeAudio', file_name: str) -> 'Audio'`

_No docstring._

---

## File: `types/messages_and_media/available_effect.py`

### Classes

#### `class AvailableEffect(Object)`

```text
Contains information about available effect.

Parameters:
    id (``int``):
        Unique effect identifier.

    emoji (``str``):
        Emoji that represents the effect.

    effect_sticker_id (``int``):
        sticker identifier that represents the effect.

    sticker (:obj:`~pyrogram.types.Sticker`, *optional*):
        Sticker that represents the effect.

    is_premium (``bool``, *optional*):
        Whether the effect is available only for premium users.

    static_icon_id (``int``, *optional*):
        Static icon identifier that represents the effect.

    effect_animation_id (``int``, *optional*):
        Animation identifier that represents the effect.
```

##### Methods

###### `def __init__(self, *, id: int, emoji: str, effect_sticker_id: int, sticker: Optional['types.Sticker'] = None, is_premium: Optional[bool] = None, static_icon_id: Optional[int] = None, effect_animation_id: Optional[int] = None)`

_No docstring._

###### `async def _parse(client, effect: 'raw.types.AvailableEffect', document: 'raw.types.Document' = None) -> 'AvailableEffect'`

_No docstring._

---

## File: `types/messages_and_media/chat_theme.py`

### Classes

#### `class ChatTheme(Object)`

```text
A service message about a chat theme.

parameters:
    emoticon (``str``):
        The emoticon of the chat theme.
```

##### Methods

###### `def __init__(self, emoticon: str)`

_No docstring._

###### `def _parse(chat_theme: 'raw.types.MessageActionSetChatTheme') -> 'ChatTheme'`

_No docstring._

---

## File: `types/messages_and_media/chat_wallpaper.py`

### Classes

#### `class ChatWallpaper(Object)`

```text
A service message about a chat wallpaper.

parameters:
    wallpaper (:obj:`types.Wallpaper`):
        The chat wallpaper.

    is_same (``bool``, *optional*):
        True, if the chat wallpaper is the same as the previous one.

    is_both (``bool``, *optional*):
        True, if the chat wallpaper is for both side.
```

##### Methods

###### `def __init__(self, wallpaper: 'types.Wallpaper', is_same: bool = None, is_both: bool = None)`

_No docstring._

###### `def _parse(client: 'pyrogram.Client', chat_wallpaper: 'raw.types.ChatWallpaper') -> 'ChatWallpaper'`

_No docstring._

---

## File: `types/messages_and_media/contact.py`

### Classes

#### `class Contact(Object)`

```text
A phone contact.

Parameters:
    phone_number (``str``):
        Contact's phone number.

    first_name (``str``):
        Contact's first name.

    last_name (``str``, *optional*):
        Contact's last name.

    user_id (``int``, *optional*):
        Contact's user identifier in Telegram.

    vcard (``str``, *optional*):
        Additional data about the contact in the form of a vCard.
```

##### Methods

###### `def __init__(self, *, client: 'pyrogram.Client' = None, phone_number: str, first_name: str, last_name: str = None, user_id: int = None, vcard: str = None)`

_No docstring._

###### `def _parse(client: 'pyrogram.Client', contact: 'raw.types.MessageMediaContact') -> 'Contact'`

_No docstring._

---

## File: `types/messages_and_media/contact_registered.py`

### Classes

#### `class ContactRegistered(Object)`

```text
A service message about a contact registered.

Currently holds no information.
```

##### Methods

###### `def __init__(self)`

_No docstring._

---

## File: `types/messages_and_media/dice.py`

### Classes

#### `class Dice(Object)`

```text
A dice with a random value from 1 to 6 for currently supported base emoji.

Parameters:
    emoji (``string``):
        Emoji on which the dice throw animation is based.

    value (``int``):
        Value of the dice, 1-6 for currently supported base emoji.
```

##### Methods

###### `def __init__(self, *, client: 'pyrogram.Client' = None, emoji: str, value: int)`

_No docstring._

###### `def _parse(client, dice: 'raw.types.MessageMediaDice') -> 'Dice'`

_No docstring._

---

## File: `types/messages_and_media/document.py`

### Classes

#### `class Document(Object)`

```text
A generic file (as opposed to photos, voice messages, audio files, ...).

Parameters:
    file_id (``str``):
        Identifier for this file, which can be used to download or reuse the file.

    file_unique_id (``str``):
        Unique identifier for this file, which is supposed to be the same over time and for different accounts.
        Can't be used to download or reuse the file.

    file_name (``str``, *optional*):
        Original filename as defined by sender.

    mime_type (``str``, *optional*):
        MIME type of the file as defined by sender.

    file_size (``int``, *optional*):
        File size.

    date (:py:obj:`~datetime.datetime`, *optional*):
        Date the document was sent.

    thumbs (List of :obj:`~pyrogram.types.Thumbnail`, *optional*):
        Document thumbnails as defined by sender.
```

##### Methods

###### `def __init__(self, *, client: 'pyrogram.Client' = None, file_id: str, file_unique_id: str, file_name: str = None, mime_type: str = None, file_size: int = None, date: datetime = None, thumbs: List['types.Thumbnail'] = None)`

_No docstring._

###### `def _parse(client, document: 'raw.types.Document', file_name: str) -> 'Document'`

_No docstring._

---

## File: `types/messages_and_media/exported_story_link.py`

### Classes

#### `class ExportedStoryLink(Object)`

```text
Contains information about a story viewers.


Parameters:
    link (``str``):
        The link of the story.
```

##### Methods

###### `def __init__(self, *, link: str)`

_No docstring._

###### `def _parse(exportedstorylink: 'raw.types.ExportedStoryLink') -> 'ExportedStoryLink'`

_No docstring._

---

## File: `types/messages_and_media/external_reply_info.py`

### Classes

#### `class ExternalReplyInfo(Object)`

```text
This object contains information about a message that is being replied to, which may come from another chat or forum topic.

Parameters:
    origin (:obj:`~pyrogram.types.MessageOrigin`, *optional*):
        Origin of the message replied to by the given message.

    chat (:obj:`~pyrogram.types.Chat`, *optional*):
        Chat the original message belongs to.
        Available only if the chat is a supergroup or a channel.

    message_id  (``int``, *optional*):
        Unique message identifier inside the original chat.
        Available only if the original chat is a supergroup or a channel.

    media (:obj:`~pyrogram.enums.MessageMediaType`, *optional*):
        The message is a media message.
        This field will contain the enumeration type of the media message.
        You can use ``media = getattr(message, message.media.value)`` to access the media message.

    animation (:obj:`~pyrogram.types.Animation`, *optional*):
        Message is an animation, information about the animation.

    audio (:obj:`~pyrogram.types.Audio`, *optional*):
        Message is an audio file, information about the file.

    document (:obj:`~pyrogram.types.Document`, *optional*):
        Message is a general file, information about the file.

    paid_media (:obj:`~pyrogram.types.PaidMediaInfo`, *optional*):
        Message contains paid media; information about the paid media.

    photo (:obj:`~pyrogram.types.Photo`, *optional*):
        Message is a photo, information about the photo.

    sticker (:obj:`~pyrogram.types.Sticker`, *optional*):
        Message is a sticker, information about the sticker.

    story (:obj:`~pyrogram.types.Story`, *optional*):
        Message is a forwarded story.

    video (:obj:`~pyrogram.types.Video`, *optional*):
        Message is a video, information about the video.

    video_note (:obj:`~pyrogram.types.VideoNote`, *optional*):
        Message is a video note, information about the video message.

    voice (:obj:`~pyrogram.types.Voice`, *optional*):
        Message is a voice message, information about the file.

    has_media_spoiler (``bool``, *optional*):
        True, if the message media is covered by a spoiler animation.

    contact (:obj:`~pyrogram.types.Contact`, *optional*):
        Message is a shared contact, information about the contact.

    dice (:obj:`~pyrogram.types.Dice`, *optional*):
        A dice containing a value that is randomly generated by Telegram.

    game (:obj:`~pyrogram.types.Game`, *optional*):
        Message is a game, information about the game.

    giveaway (:obj:`~pyrogram.types.Giveaway`, *optional*):
        Message is a scheduled giveaway, information about the giveaway.

    giveaway_result (:obj:`~pyrogram.types.GiveawayResult`, *optional*):
        Message is a giveaway result, information about the giveaway result.

    invoice (:obj:`~pyrogram.types.Invoice`, *optional*):
        Message is a invoice, information about the invoice.
        `More about payments » <https://core.telegram.org/bots/api#payments>`_

    location (:obj:`~pyrogram.types.Location`, *optional*):
        Message is a shared location, information about the location.

    poll (:obj:`~pyrogram.types.Poll`, *optional*):
        Message is a native poll, information about the poll.

    venue (:obj:`~pyrogram.types.Venue`, *optional*):
        Message is a venue, information about the venue.
```

##### Methods

###### `def __init__(self, *, client: 'pyrogram.Client' = None, origin: 'types.MessageOrigin' = None, chat: 'types.Chat' = None, message_id: int, media: Optional['enums.MessageMediaType'] = None, animation: Optional['types.Animation'] = None, audio: Optional['types.Audio'] = None, document: Optional['types.Document'] = None, paid_media: Optional['types.PaidMediaInfo'] = None, photo: Optional['types.Photo'] = None, sticker: Optional['types.Sticker'] = None, story: Optional['types.Story'] = None, video: Optional['types.Video'] = None, video_note: Optional['types.VideoNote'] = None, voice: Optional['types.Voice'] = None, has_media_spoiler: Optional[bool] = None, contact: Optional['types.Contact'] = None, dice: Optional['types.Dice'] = None, game: Optional['types.Game'] = None, giveaway: Optional['types.Giveaway'] = None, giveaway_result: Optional['types.GiveawayResult'] = None, invoice: Optional['types.Invoice'] = None, location: Optional['types.Location'] = None, poll: Optional['types.Poll'] = None, venue: Optional['types.Venue'] = None)`

_No docstring._

###### `async def _parse(client, reply: 'raw.types.MessageReplyHeader', users: Dict[int, 'raw.types.User'], chats: Dict[int, 'raw.types.Chat']) -> Optional['ExternalReplyInfo']`

_No docstring._

---

## File: `types/messages_and_media/game.py`

### Classes

#### `class Game(Object)`

```text
A game.
Use BotFather to create and edit games, their short names will act as unique identifiers.

Parameters:
    id (``int``):
        Unique identifier of the game.

    title (``str``):
        Title of the game.

    short_name (``str``):
        Unique short name of the game.

    description (``str``):
        Description of the game.

    photo (:obj:`~pyrogram.types.Photo`):
        Photo that will be displayed in the game message in chats.

    animation (:obj:`~pyrogram.types.Animation`, *optional*):
        Animation that will be displayed in the game message in chats.
        Upload via BotFather.
```

##### Methods

###### `def __init__(self, *, client: 'pyrogram.Client' = None, id: int, title: str, short_name: str, description: str, photo: 'types.Photo', animation: 'types.Animation' = None)`

_No docstring._

###### `def _parse(client, media: 'raw.types.MessageMediaGame') -> 'Game'`

_No docstring._

---

## File: `types/messages_and_media/giveaway.py`

### Classes

#### `class Giveaway(Object)`

```text
A giveaway.

Parameters:
    chats (List of :obj:`~pyrogram.types.Chat`):
        List of channel(s) which host the giveaway.

    quantity (``int``):
        Quantity of the giveaway prize.

    months (``int``, *optional*):
        How long the telegram premium last (in month).

    stars (``int``, *optional*):
        How many stars the giveaway winner(s) get.

    expire_date (:py:obj:`~datetime.datetime`):
        Date the giveaway winner(s) will be choosen.

    new_subscribers (``bool``):
        True, if the giveaway only for new subscribers.

    additional_price (``str``, *optional*):
        Additional prize for the giveaway winner(s).

    allowed_countries (List of ``str``, *optional*):
        List of ISO country codes which eligible to join the giveaway.

    private_channel_ids (List of ``int``, *optional*):
        List of Unique channel identifier of private channel which host the giveaway.

    is_winners_hidden (``bool``):
        True, if the giveaway winners are hidden.
```

##### Methods

###### `def __init__(self, *, client: 'pyrogram.Client' = None, chats: List['types.Chat'], quantity: int, expire_date: datetime, new_subscribers: bool, months: int = None, stars: int = None, additional_price: str = None, allowed_countries: List[str] = None, is_winners_hidden: bool = None)`

_No docstring._

###### `async def _parse(client, message: 'raw.types.Message', chats: Dict[int, 'raw.types.Chat'] = None) -> 'Giveaway'`

_No docstring._

---

## File: `types/messages_and_media/giveaway_launched.py`

### Classes

#### `class GiveawayLaunched(Object)`

```text
A service message about a giveaway started in the channel.

Parameters:
    stars (``int``, *optional*):
        How many stars the giveaway winner(s) get.
```

##### Methods

###### `def __init__(self, *, client: 'pyrogram.Client' = None, stars: int = None)`

_No docstring._

###### `def _parse(client: 'pyrogram.Client', giveaway_launched: 'raw.types.MessageActionGiveawayLaunch') -> 'GiveawayLaunched'`

_No docstring._

---

## File: `types/messages_and_media/giveaway_result.py`

### Classes

#### `class GiveawayResult(Object)`

```text
A giveaway result.

Parameters:
    chat (:obj:`~pyrogram.types.Chat`, *optional*):
        Channel which host the giveaway.

    giveaway_message (:obj:`~pyrogram.types.Message`, *optional*):
        The original giveaway message.

    quantity (``int``):
        Quantity of the giveaway prize.

    unclaimed_quantity (``int``):
        Quantity of unclaimed giveaway prize.

    winners (List of :obj:`~pyrogram.types.User`, *optional*):
        The giveaway winners.

    months (``int``, *optional*):
        How long the telegram premium last (in month).

    stars (``int``, *optional*):
        How many stars the giveaway winner(s) get.

    expire_date (:py:obj:`~datetime.datetime`, *optional*):
        Date the giveaway winner(s) choosen.

    new_subscribers (``bool``, *optional*):
        True, if the giveaway only for new subscribers.

    is_refunded (``bool``, *optional*):
        True, if the giveaway was refunded.

    is_star_giveaway (``bool``, *optional*):
        True, if the giveaway is a star giveaway.

    is_winners_hidden (``bool``):
        True, if the giveaway winners are hidden.
```

##### Methods

###### `def __init__(self, *, client: 'pyrogram.Client' = None, chat: 'types.Chat' = None, giveaway_message: 'types.Message' = None, quantity: int, unclaimed_quantity: int, winners: List['types.User'] = None, months: int = None, stars: int = None, expire_date: datetime = None, new_subscribers: bool = None, is_refunded: bool = None, is_star_giveaway: bool = None, is_winners_hidden: bool)`

_No docstring._

###### `async def _parse(client, giveaway_result: Union['raw.types.MessageActionGiveawayResults', 'raw.types.MessageMediaGiveawayResults'], hide_winners: bool = False, users: Dict[int, 'raw.types.User'] = None, chats: Dict[int, 'raw.types.Chat'] = None) -> 'GiveawayResult'`

_No docstring._

---

## File: `types/messages_and_media/location.py`

### Classes

#### `class Location(Object)`

```text
A point on the map.

Parameters:
    longitude (``float``):
        Longitude as defined by sender.

    latitude (``float``):
        Latitude as defined by sender.
```

##### Methods

###### `def __init__(self, *, client: 'pyrogram.Client' = None, longitude: float, latitude: float)`

_No docstring._

###### `def _parse(client, geo_point: 'raw.types.GeoPoint') -> 'Location'`

_No docstring._

---

## File: `types/messages_and_media/media_area.py`

### Classes

#### `class MediaArea(Object)`

```text
Content of a media areas in story.

It should be one of:

- :obj:`~pyrogram.types.MediaAreaChannelPost`
```

##### Methods

###### `def __init__(self, coordinates: 'types.MediaAreaCoordinates')`

_No docstring._

###### `async def _parse(client: 'pyrogram.Client', media_area: 'raw.base.MediaArea') -> 'MediaArea'`

_No docstring._

---

## File: `types/messages_and_media/media_area_channel_post.py`

### Classes

#### `class MediaAreaChannelPost(MediaArea)`

```text
A channel post media area.

Parameters:
    coordinates (:obj:`~pyrogram.types.MediaAreaCoordinates`):
        Media area coordinates.

    chat (:obj:`~pyrogram.types.Chat`):
        Information about origin channel.

    message_id (``int``):
        The channel post message id.
```

##### Methods

###### `def __init__(self, coordinates: 'types.MediaAreaCoordinates', chat: 'types.Chat', message_id: int)`

_No docstring._

###### `async def _parse(client: 'pyrogram.Client', media_area: 'raw.types.MediaAreaChannelPost') -> 'MediaAreaChannelPost'`

_No docstring._

---

## File: `types/messages_and_media/media_area_coordinates.py`

### Classes

#### `class MediaAreaCoordinates(Object)`

```text
A coordinates of media area.

Parameters:
    x (``float``, *optional*):
        X position of media area.

    y (``float``, *optional*):
        Y position of media area.

    width (``float``, *optional*):
        Media area width.

    height (``float``, *optional*):
        Media area height.

    rotation (``float``, *optional*):
        Media area rotation.
```

##### Methods

###### `def __init__(self, x: float = None, y: float = None, width: float = None, height: float = None, rotation: float = None)`

_No docstring._

###### `def _parse(media_area_cordinates: 'raw.types.MediaAreaCoordinates') -> 'MediaAreaCoordinates'`

_No docstring._

###### `def write(self)`

_No docstring._

---

## File: `types/messages_and_media/message.py`

### Classes

#### `class Str(str)`

_No docstring._

##### Methods

###### `def __init__(self, *args)`

_No docstring._

###### `def init(self, entities)`

_No docstring._

###### `def markdown(self)`

_No docstring._

###### `def html(self)`

_No docstring._

###### `def __getitem__(self, item)`

_No docstring._

#### `class Message(Object, Update)`

```text
A message.

Parameters:
    id (``int``):
        Unique message identifier inside this chat.

    message_thread_id (``int``, *optional*):
        Unique identifier of a message thread to which the message belongs.
        for supergroups only

    from_user (:obj:`~pyrogram.types.User`, *optional*):
        Sender, empty for messages sent to channels.

    sender_chat (:obj:`~pyrogram.types.Chat`, *optional*):
        Sender of the message, sent on behalf of a chat.
        The channel itself for channel messages.
        The supergroup itself for messages from anonymous group administrators.
        The linked channel for messages automatically forwarded to the discussion group.

    sender_business_bot (:obj:`~pyrogram.types.User`, *optional*):
        Sender of the message, sent on behalf of a business bot.

    date (:py:obj:`~datetime.datetime`, *optional*):
        Date the message was sent.

    chat (:obj:`~pyrogram.types.Chat`, *optional*):
        Conversation the message belongs to.

    topic (:obj:`~pyrogram.types.ForumTopic`, *optional*):
        Topic the message belongs to.
        only returned when using client.get_messages.

    forward_origin (:obj:`~pyrogram.types.MessageOrigin`, *optional*):
        Information about the original message for forwarded messages.

    is_topic_message (``bool``, *optional*):
        True, if the message is sent to a forum topic

    reply_to_chat_id (``int``, *optional*):
        Unique identifier of the chat where the replied message belongs to.

    reply_to_message_id (``int``, *optional*):
        The id of the message which this message directly replied to.

    reply_to_story_id (``int``, *optional*):
        The id of the story which this message directly replied to.

    reply_to_story_user_id (``int``, *optional*):
        The id of the story sender which this message directly replied to.

    reply_to_story_chat_id (``int``, *optional*):
        The id of the chat where the story was sent which this message directly replied to.

    reply_to_top_message_id (``int``, *optional*):
        The id of the first message which started this message thread.

    reply_to_message (:obj:`~pyrogram.types.Message`, *optional*):
        For replies, the original message. Note that the Message object in this field will not contain
        further reply_to_message fields even if it itself is a reply.

    reply_to_story (:obj:`~pyrogram.types.Story`, *optional*):
        For replies, the original story.

    business_connection_id (``str``, *optional*):
        The business connection identifier.

    mentioned (``bool``, *optional*):
        The message contains a mention.

    empty (``bool``, *optional*):
        The message is empty.
        A message can be empty in case it was deleted or you tried to retrieve a message that doesn't exist yet.

    service (:obj:`~pyrogram.enums.MessageServiceType`, *optional*):
        The message is a service message.
        This field will contain the enumeration type of the service message.
        You can use ``service = getattr(message, message.service.value)`` to access the service message.

    media (:obj:`~pyrogram.enums.MessageMediaType`, *optional*):
        The message is a media message.
        This field will contain the enumeration type of the media message.
        You can use ``media = getattr(message, message.media.value)`` to access the media message.

    edit_date (:py:obj:`~datetime.datetime`, *optional*):
        Date the message was last edited.

    edit_hide (``bool``, *optional*):
        The message shown as not modified.
        A message can be not modified in case it has received a reaction.

    media_group_id (``str``, *optional*):
        The unique identifier of a media message group this message belongs to.

    author_signature (``str``, *optional*):
        Signature of the post author for messages in channels, or the custom title of an anonymous group
        administrator.

    has_protected_content (``bool``, *optional*):
        True, if the message can't be forwarded.

    has_media_spoiler (``bool``, *optional*):
        True, if the message media is covered by a spoiler animation.

    text (``str``, *optional*):
        For text messages, the actual UTF-8 text of the message, 0-4096 characters.
        If the message contains entities (bold, italic, ...) you can access *text.markdown* or
        *text.html* to get the marked up message text. In case there is no entity, the fields
        will contain the same text as *text*.

    entities (List of :obj:`~pyrogram.types.MessageEntity`, *optional*):
        For text messages, special entities like usernames, URLs, bot commands, etc. that appear in the text.

    caption_entities (List of :obj:`~pyrogram.types.MessageEntity`, *optional*):
        For messages with a caption, special entities like usernames, URLs, bot commands, etc. that appear
        in the caption.

    quote (:obj:`~pyrogram.types.TextQuote`, *optional*):
        Chosen quote from the replied message.

    effect_id (``str``, *optional*):
        Unique identifier of the message effect added to the message.

    invert_media (``bool``, *optional*):
        True, If the media position is inverted.
        only animation, photo, video, and webpage preview messages.

    audio (:obj:`~pyrogram.types.Audio`, *optional*):
        Message is an audio file, information about the file.

    document (:obj:`~pyrogram.types.Document`, *optional*):
        Message is a general file, information about the file.

    photo (:obj:`~pyrogram.types.Photo`, *optional*):
        Message is a photo, information about the photo.

    paid_media (:obj:`~pyrogram.types.PaidMedia`, *optional*):
        Message is a paid media, information about the paid media.

    todo (:obj:`~pyrogram.types.Todo`, *optional*):
        Message is a todo list, information about the todo list.

    sticker (:obj:`~pyrogram.types.Sticker`, *optional*):
        Message is a sticker, information about the sticker.

    animation (:obj:`~pyrogram.types.Animation`, *optional*):
        Message is an animation, information about the animation.

    game (:obj:`~pyrogram.types.Game`, *optional*):
        Message is a game, information about the game.

    giveaway (:obj:`~pyrogram.types.Giveaway`, *optional*):
        Message is a giveaway, information about the giveaway.

    giveaway_result (:obj:`~pyrogram.types.GiveawayResult`, *optional*):
        Message is a giveaway result, information about the giveaway result.

    invoice (:obj:`~pyrogram.types.Invoice`, *optional*):
        Message is an invoice for a payment, information about the invoice.

    story (:obj:`~pyrogram.types.MessageStory` | :obj:`~pyrogram.types.Story`, *optional*):
        Message is a forwarded story, information about the forwarded story.

    video (:obj:`~pyrogram.types.Video`, *optional*):
        Message is a video, information about the video.

    voice (:obj:`~pyrogram.types.Voice`, *optional*):
        Message is a voice message, information about the file.

    video_note (:obj:`~pyrogram.types.VideoNote`, *optional*):
        Message is a video note, information about the video message.

    web_page_preview (:obj:`~pyrogram.types.WebPagePreview`, *optional*):
        Message is a web page preview, information about the web page preview message.

    caption (``str``, *optional*):
        Caption for the audio, document, photo, video or voice, 0-1024 characters.
        If the message contains caption entities (bold, italic, ...) you can access *caption.markdown* or
        *caption.html* to get the marked up caption text. In case there is no caption entity, the fields
        will contain the same text as *caption*.

    contact (:obj:`~pyrogram.types.Contact`, *optional*):
        Message is a shared contact, information about the contact.

    location (:obj:`~pyrogram.types.Location`, *optional*):
        Message is a shared location, information about the location.

    venue (:obj:`~pyrogram.types.Venue`, *optional*):
        Message is a venue, information about the venue.

    poll (:obj:`~pyrogram.types.Poll`, *optional*):
        Message is a native poll, information about the poll.

    dice (:obj:`~pyrogram.types.Dice`, *optional*):
        A dice containing a value that is randomly generated by Telegram.

    new_chat_members (List of :obj:`~pyrogram.types.User`, *optional*):
        New members that were added to the group or supergroup and information about them
        (the bot itself may be one of these members).

    chat_joined_by_request (:obj:`~pyrogram.types.ChatJoinedByRequest`, *optional*):
        New members chat join request has been approved in group or supergroup.

    left_chat_member (:obj:`~pyrogram.types.User`, *optional*):
        A member was removed from the group, information about them (this member may be the bot itself).

    new_chat_title (``str``, *optional*):
        A chat title was changed to this value.

    new_chat_photo (:obj:`~pyrogram.types.Photo`, *optional*):
        A chat photo was change to this value.

    delete_chat_photo (``bool``, *optional*):
        Service message: the chat photo was deleted.

    group_chat_created (``bool``, *optional*):
        Service message: the group has been created.

    supergroup_chat_created (``bool``, *optional*):
        Service message: the supergroup has been created.
        This field can't be received in a message coming through updates, because bot can't be a member of a
        supergroup when it is created. It can only be found in reply_to_message if someone replies to a very
        first message in a directly created supergroup.

    channel_chat_created (``bool``, *optional*):
        Service message: the channel has been created.
        This field can't be received in a message coming through updates, because bot can't be a member of a
        channel when it is created. It can only be found in reply_to_message if someone replies to a very
        first message in a channel.

    migrate_to_chat_id (``int``, *optional*):
        The group has been migrated to a supergroup with the specified identifier.
        This number may be greater than 32 bits and some programming languages may have difficulty/silent defects
        in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float
        type are safe for storing this identifier.

    migrate_from_chat_id (``int``, *optional*):
        The supergroup has been migrated from a group with the specified identifier.
        This number may be greater than 32 bits and some programming languages may have difficulty/silent defects
        in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float
        type are safe for storing this identifier.

    pinned_message (:obj:`~pyrogram.types.Message`, *optional*):
        Specified message was pinned.
        Note that the Message object in this field will not contain further reply_to_message fields even if it
        is itself a reply.

    game_high_score (:obj:`~pyrogram.types.GameHighScore`, *optional*):
        The game score for a user.
        The reply_to_message field will contain the game Message.

    views (``int``, *optional*):
        Channel post views.

    forwards (``int``, *optional*):
        Channel post forwards.

    via_bot (:obj:`~pyrogram.types.User`):
        The information of the bot that generated the message from an inline query of a user.

    outgoing (``bool``, *optional*):
        Whether the message is incoming or outgoing.
        Messages received from other chats are incoming (*outgoing* is False).
        Messages sent from yourself to other chats are outgoing (*outgoing* is True).
        An exception is made for your own personal chat; messages sent there will be incoming.

    external_reply (:obj:`~pyrogram.types.ExternalReplyInfo`, *optional*):
        Information about the message that is being replied to, which may come from another chat or forum topic.

    matches (List of regex Matches, *optional*):
        A list containing all `Match Objects <https://docs.python.org/3/library/re.html#match-objects>`_ that match
        the text of this message. Only applicable when using :obj:`Filters.regex <pyrogram.Filters.regex>`.

    command (List of ``str``, *optional*):
        A list containing the command and its arguments, if any.
        E.g.: "/start 1 2 3" would produce ["start", "1", "2", "3"].
        Only applicable when using :obj:`~pyrogram.filters.command`.

    bot_allowed (:obj:`~pyrogram.types.BotAllowed`, *optional*):
        Contains information about a allowed bot.

    chats_shared (List of :obj:`~pyrogram.types.RequestedChats`, *optional*):
        Service message: chats shared

    forum_topic_created (:obj:`~pyrogram.types.ForumTopicCreated`, *optional*):
        Service message: forum topic created

    forum_topic_closed (:obj:`~pyrogram.types.ForumTopicClosed`, *optional*):
        Service message: forum topic closed

    forum_topic_reopened (:obj:`~pyrogram.types.ForumTopicReopened`, *optional*):
        Service message: forum topic reopened

    forum_topic_edited (:obj:`~pyrogram.types.ForumTopicEdited`, *optional*):
        Service message: forum topic edited

    general_topic_hidden (:obj:`~pyrogram.types.GeneralTopicHidden`, *optional*):
        Service message: forum general topic hidden

    general_topic_unhidden (:obj:`~pyrogram.types.GeneralTopicUnhidden`, *optional*):
        Service message: forum general topic unhidden

    gifted_premium (:obj:`~pyrogram.types.GiftedPremium`, *optional*):
        Info about a gifted Telegram Premium subscription

    giveaway_launcheded (:obj:`~pyrogram.types.GiveawayLaunched`, *optional*):
        Service message: giveaway launched.

    video_chat_scheduled (:obj:`~pyrogram.types.VideoChatScheduled`, *optional*):
        Service message: voice chat scheduled.

    video_chat_started (:obj:`~pyrogram.types.VideoChatStarted`, *optional*):
        Service message: the voice chat started.

    video_chat_ended (:obj:`~pyrogram.types.VideoChatEnded`, *optional*):
        Service message: the voice chat has ended.

    video_chat_members_invited (:obj:`~pyrogram.types.VoiceChatParticipantsInvited`, *optional*):
        Service message: new members were invited to the voice chat.

    web_app_data (:obj:`~pyrogram.types.WebAppData`, *optional*):
        Service message: web app data sent to the bot.

    successful_payment (:obj:`~pyrogram.types.SuccessfulPayment`, *optional*):
        Service message: successful payment.

    payment_refunded (:obj:`~pyrogram.types.PaymentRefunded`, *optional*):
        Service message: payment refunded.

    boosts_applied (``int``, *optional*):
        Service message: how many boosts were applied.

    reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardRemove` | :obj:`~pyrogram.types.ForceReply`, *optional*):
        Additional interface options. An object for an inline keyboard, custom reply keyboard,
        instructions to remove reply keyboard or to force a reply from the user.

    reactions (List of :obj:`~pyrogram.types.Reaction`):
        List of the reactions to this message.

    raw (``pyrogram.raw.types.Message``, *optional*):
        The raw message object, as received from the Telegram API.

    gift_code (:obj:`~pyrogram.types.GiftCode`, *optional*):
        Service message: gift code information.
        Contains a `Telegram Premium giftcode link <https://core.telegram.org/api/links#premium-giftcode-links>`_.

    gift (:obj:`~pyrogram.types.Gift`, *optional*):
        Service message: star gift information.

    gifted_premium (:obj:`~pyrogram.types.GiftedPremium`, *optional*):
        Info about a gifted Telegram Premium subscription

    screenshot_taken (:obj:`~pyrogram.types.ScreenshotTaken`, *optional*):
        Service message: screenshot taken.

    paid_message_price_changed (:obj:`~pyrogram.types.PaidMessagePriceChanged`, *optional*):
        Service message: paid message price changed.

    todo_tasks_added (:obj:`~pyrogram.types.TodoTasksAdded`, *optional*):
        Service message: todo tasks added.

    todo_tasks_completed (:obj:`~pyrogram.types.TodoTasksCompleted`, *optional*):
        Service message: todo tasks completed.

    todo_tasks_incompleted (:obj:`~pyrogram.types.TodoTasksIncompleted`, *optional*):
        Service message: todo tasks incompleted.

    link (``str``, *property*):
        Generate a link to this message, only for groups and channels.

    content (``str``, *property*):
        The text or caption content of the message.

    scheduled (``bool``, *optional*):
        Message is a scheduled message and still in schedule.

    from_scheduled (``bool``, *optional*):
        Message is a scheduled message and has been sent.

    chat_join_type (:obj:`~pyrogram.enums.ChatJoinType`, *optional*):
        The message is a service message of the type :obj:`~pyrogram.enums.MessageServiceType.NEW_CHAT_MEMBERS`.
        This field will contain the enumeration type of how the user had joined the chat.
```

##### Methods

###### `def __init__(self, *, client: 'pyrogram.Client' = None, id: int, message_thread_id: int = None, business_connection_id: str = None, from_user: 'types.User' = None, sender_chat: 'types.Chat' = None, sender_business_bot: 'types.User' = None, date: datetime = None, chat: 'types.Chat' = None, topic: 'types.ForumTopic' = None, forward_origin: 'types.MessageOrigin' = None, is_topic_message: bool = None, reply_to_chat_id: int = None, reply_to_message_id: int = None, reply_to_story_id: int = None, reply_to_story_user_id: int = None, reply_to_story_chat_id: int = None, reply_to_top_message_id: int = None, reply_to_message: 'Message' = None, reply_to_story: 'types.Story' = None, mentioned: bool = None, empty: bool = None, service: 'enums.MessageServiceType' = None, scheduled: bool = None, from_scheduled: bool = None, edit_hide: bool = None, media: 'enums.MessageMediaType' = None, edit_date: datetime = None, media_group_id: str = None, author_signature: str = None, has_protected_content: bool = None, has_media_spoiler: bool = None, text: Str = None, entities: List['types.MessageEntity'] = None, caption_entities: List['types.MessageEntity'] = None, quote: 'types.TextQuote' = None, effect_id: str = None, invert_media: bool = None, audio: 'types.Audio' = None, document: 'types.Document' = None, photo: 'types.Photo' = None, paid_media: 'types.PaidMedia' = None, todo: 'types.Todo' = None, sticker: 'types.Sticker' = None, animation: 'types.Animation' = None, game: 'types.Game' = None, giveaway: 'types.Giveaway' = None, giveaway_result: 'types.GiveawayResult' = None, boosts_applied: int = None, chat_theme_updated: 'types.ChatTheme' = None, chat_wallpaper_updated: 'types.ChatWallpaper' = None, contact_registered: 'types.ContactRegistered' = None, gift_code: 'types.GiftCode' = None, gift: 'types.Gift' = None, screenshot_taken: 'types.ScreenshotTaken' = None, paid_message_price_changed: 'types.PaidMessagePriceChanged' = None, todo_tasks_added: 'types.TodoTasksAdded' = None, todo_tasks_completed: 'types.TodoTasksCompleted' = None, todo_tasks_incompleted: 'types.TodoTasksIncompleted' = None, invoice: 'types.Invoice' = None, story: Union['types.MessageStory', 'types.Story'] = None, alternative_videos: List['types.AlternativeVideo'] = None, video: 'types.Video' = None, voice: 'types.Voice' = None, video_note: 'types.VideoNote' = None, web_page_preview: 'types.WebPagePreview' = None, caption: Str = None, contact: 'types.Contact' = None, location: 'types.Location' = None, venue: 'types.Venue' = None, poll: 'types.Poll' = None, dice: 'types.Dice' = None, new_chat_members: List['types.User'] = None, chat_joined_by_request: 'types.ChatJoinedByRequest' = None, left_chat_member: 'types.User' = None, new_chat_title: str = None, new_chat_photo: 'types.Photo' = None, delete_chat_photo: bool = None, group_chat_created: bool = None, supergroup_chat_created: bool = None, channel_chat_created: bool = None, migrate_to_chat_id: int = None, migrate_from_chat_id: int = None, pinned_message: 'Message' = None, game_high_score: int = None, views: int = None, forwards: int = None, via_bot: 'types.User' = None, outgoing: bool = None, external_reply: Optional['types.ExternalReplyInfo'] = None, matches: List[Match] = None, command: List[str] = None, bot_allowed: 'types.BotAllowed' = None, chats_shared: List['types.RequestedChats'] = None, forum_topic_created: 'types.ForumTopicCreated' = None, forum_topic_closed: 'types.ForumTopicClosed' = None, forum_topic_reopened: 'types.ForumTopicReopened' = None, forum_topic_edited: 'types.ForumTopicEdited' = None, general_topic_hidden: 'types.GeneralTopicHidden' = None, general_topic_unhidden: 'types.GeneralTopicUnhidden' = None, gifted_premium: 'types.GiftedPremium' = None, giveaway_launched: 'types.GiveawayLaunched' = None, video_chat_scheduled: 'types.VideoChatScheduled' = None, video_chat_started: 'types.VideoChatStarted' = None, video_chat_ended: 'types.VideoChatEnded' = None, video_chat_members_invited: 'types.VideoChatMembersInvited' = None, web_app_data: 'types.WebAppData' = None, successful_payment: 'types.SuccessfulPayment' = None, payment_refunded: 'types.PaymentRefunded' = None, reply_markup: Union['types.InlineKeyboardMarkup', 'types.ReplyKeyboardMarkup', 'types.ReplyKeyboardRemove', 'types.ForceReply'] = None, reactions: List['types.Reaction'] = None, chat_join_type: 'enums.ChatJoinType' = None, raw: 'raw.types.Message' = None)`

_No docstring._

###### `async def wait_for_click(self, from_user_id: Optional[Union[Union[int, str], List[Union[int, str]]]] = None, timeout: Optional[int] = None, filters = None, alert: Union[str, bool] = True)`

```text
Waits for a callback query to be clicked on the message.

Parameters:
    user_id (``int`` | ``str`` | Iterable of ``int`` | Iterable of ``str``, *optional*):
        The user ID to listen for.

    timeout (``int``, *optional*):
        The maximum amount of time to wait for a message.

    filters (:obj:`~pyrogram.filters`, *optional*):
        A filter to check the incoming message against.

    alert (``str`` | ``bool``):
        The alert to show when the button is clicked by users that are not allowed in from_user_id.

Returns:
    :obj:`~pyrogram.types.CallbackQuery`: The callback query that was clicked.
```

###### `async def _parse(client: 'pyrogram.Client', message: raw.base.Message, users: Dict[int, 'raw.types.User'], chats: Dict[int, 'raw.types.Chat'], topics: Dict[int, 'raw.types.ForumTopic'] = None, is_scheduled: bool = False, business_connection_id: str = None, replies: int = 1)`

_No docstring._

###### `def link(self) -> str`

_No docstring._

###### `def content(self) -> str`

_No docstring._

###### `def forward_from(self) -> Optional['types.User']`

_No docstring._

###### `def forward_sender_name(self) -> Optional[str]`

_No docstring._

###### `def forward_from_chat(self) -> Optional['types.Chat']`

_No docstring._

###### `def forward_from_message_id(self) -> Optional[int]`

_No docstring._

###### `def forward_signature(self) -> Optional[str]`

_No docstring._

###### `def forward_date(self) -> Optional[datetime]`

_No docstring._

###### `async def get_media_group(self) -> List['types.Message']`

```text
Bound method *get_media_group* of :obj:`~pyrogram.types.Message`.

Use as a shortcut for:

.. code-block:: python

    await client.get_media_group(
        chat_id=message.chat.id,
        message_id=message.id
    )

Example:
    .. code-block:: python

        await message.get_media_group()

Returns:
    List of :obj:`~pyrogram.types.Message`: On success, a list of messages of the media group is returned.

Raises:
    ValueError: In case the passed message id doesn't belong to a media group.
```

###### `async def reply_text(self, text: str, quote: bool = None, parse_mode: Optional['enums.ParseMode'] = None, entities: List['types.MessageEntity'] = None, disable_web_page_preview: bool = None, disable_notification: bool = None, reply_to_message_id: int = None, business_connection_id: str = None, reply_in_chat_id: Union[int, str] = None, quote_text: str = None, quote_entities: List['types.MessageEntity'] = None, schedule_date: datetime = None, protect_content: bool = None, allow_paid_broadcast: bool = None, message_effect_id: int = None, invert_media: bool = None, reply_markup = None) -> 'Message'`

```text
Bound method *reply_text* of :obj:`~pyrogram.types.Message`.

An alias exists as *reply*.

Use as a shortcut for:

.. code-block:: python

    await client.send_message(
        chat_id=message.chat.id,
        text="hello",
        reply_to_message_id=message.id
    )

Example:
    .. code-block:: python

        await message.reply_text("hello", quote=True)

Parameters:
    text (``str``):
        Text of the message to be sent.

    quote (``bool``, *optional*):
        If ``True``, the message will be sent as a reply to this message.
        If *reply_to_message_id* is passed, this parameter will be ignored.
        Defaults to ``True`` in group chats and ``False`` in private chats.

    parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
        By default, texts are parsed using both Markdown and HTML styles.
        You can combine both syntaxes together.

    entities (List of :obj:`~pyrogram.types.MessageEntity`):
        List of special entities that appear in message text, which can be specified instead of *parse_mode*.

    disable_web_page_preview (``bool``, *optional*):
        Disables link previews for links in this message.

    disable_notification (``bool``, *optional*):
        Sends the message silently.
        Users will receive a notification with no sound.

    reply_to_message_id (``int``, *optional*):
        If the message is a reply, ID of the original message.

    business_connection_id (``str``, *optional*):
        Business connection identifier.
        for business bots only.

    reply_in_chat_id (``int`` | ``str``, *optional*):
        Unique identifier for the origin chat.
        for reply to message from another chat.
        You can also use chat public link in form of *t.me/<username>* (str).

    quote_text (``str``, *optional*):
        Text to quote.
        for reply_to_message only.

    quote_entities (List of :obj:`~pyrogram.types.MessageEntity`, *optional*):
        List of special entities that appear in quote_text, which can be specified instead of *parse_mode*.
        for reply_to_message only.

    schedule_date (:py:obj:`~datetime.datetime`, *optional*):
        Date when the message will be automatically sent.

    protect_content (``bool``, *optional*):
        Protects the contents of the sent message from forwarding and saving.

    allow_paid_broadcast (``bool``, *optional*):
        Pass True to allow the message to ignore regular broadcast limits for a small fee; for bots.

    message_effect_id (``int`` ``64-bit``, *optional*):
        Unique identifier of the message effect to be added to the message; for private chats only.

    invert_media (``bool``, *optional*):
        Move web page preview to above the message.

    reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardRemove` | :obj:`~pyrogram.types.ForceReply`, *optional*):
        Additional interface options. An object for an inline keyboard, custom reply keyboard,
        instructions to remove reply keyboard or to force a reply from the user.

Returns:
    On success, the sent Message is returned.

Raises:
    RPCError: In case of a Telegram RPC error.
```

###### `async def reply_animation(self, animation: Union[str, BinaryIO], quote: bool = None, caption: str = '', parse_mode: Optional['enums.ParseMode'] = None, caption_entities: List['types.MessageEntity'] = None, has_spoiler: bool = None, duration: int = 0, width: int = 0, height: int = 0, thumb: Union[str, BinaryIO] = None, file_name: str = None, disable_notification: bool = None, invert_media: bool = None, reply_markup: Union['types.InlineKeyboardMarkup', 'types.ReplyKeyboardMarkup', 'types.ReplyKeyboardRemove', 'types.ForceReply'] = None, reply_to_message_id: int = None, business_connection_id: str = None, reply_in_chat_id: Union[int, str] = None, quote_text: str = None, quote_entities: List['types.MessageEntity'] = None, allow_paid_broadcast: bool = None, message_effect_id: int = None, progress: Callable = None, progress_args: tuple = ()) -> 'Message'`

```text
Bound method *reply_animation* :obj:`~pyrogram.types.Message`.

Use as a shortcut for:

.. code-block:: python

    await client.send_animation(
        chat_id=message.chat.id,
        animation=animation
    )

Example:
    .. code-block:: python

        await message.reply_animation(animation)

Parameters:
    animation (``str``):
        Animation to send.
        Pass a file_id as string to send an animation that exists on the Telegram servers,
        pass an HTTP URL as a string for Telegram to get an animation from the Internet, or
        pass a file path as string to upload a new animation that exists on your local machine.

    quote (``bool``, *optional*):
        If ``True``, the message will be sent as a reply to this message.
        If *reply_to_message_id* is passed, this parameter will be ignored.
        Defaults to ``True`` in group chats and ``False`` in private chats.

    caption (``str``, *optional*):
        Animation caption, 0-1024 characters.

    parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
        By default, texts are parsed using both Markdown and HTML styles.
        You can combine both syntaxes together.

    caption_entities (List of :obj:`~pyrogram.types.MessageEntity`):
        List of special entities that appear in the caption, which can be specified instead of *parse_mode*.

    has_spoiler (``bool``, *optional*):
        Pass True if the animation needs to be covered with a spoiler animation.

    duration (``int``, *optional*):
        Duration of sent animation in seconds.

    width (``int``, *optional*):
        Animation width.

    height (``int``, *optional*):
        Animation height.

    thumb (``str`` | ``BinaryIO``, *optional*):
        Thumbnail of the animation file sent.
        The thumbnail should be in JPEG format and less than 200 KB in size.
        A thumbnail's width and height should not exceed 320 pixels.
        Thumbnails can't be reused and can be only uploaded as a new file.

    file_name (``str``, *optional*):
        File name of the animation sent.
        Defaults to file's path basename.

    disable_notification (``bool``, *optional*):
        Sends the message silently.
        Users will receive a notification with no sound.

    reply_to_message_id (``int``, *optional*):
        If the message is a reply, ID of the original message.

    business_connection_id (``str``, *optional*):
        Business connection identifier.
        for business bots only.

    reply_in_chat_id (``int`` | ``str``, *optional*):
        Unique identifier for the origin chat.
        for reply to message from another chat.
        You can also use chat public link in form of *t.me/<username>* (str).

    quote_text (``str``, *optional*):
        Text to quote.
        for reply_to_message only.

    quote_entities (List of :obj:`~pyrogram.types.MessageEntity`, *optional*):
        List of special entities that appear in quote_text, which can be specified instead of *parse_mode*.
        for reply_to_message only.

    allow_paid_broadcast (``bool``, *optional*):
        Pass True to allow the message to ignore regular broadcast limits for a small fee; for bots.

    message_effect_id (``int`` ``64-bit``, *optional*):
        Unique identifier of the message effect to be added to the message; for private chats only.

    invert_media (``bool``, *optional*):
        True to invert the animation and caption position..

    reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardRemove` | :obj:`~pyrogram.types.ForceReply`, *optional*):
        Additional interface options. An object for an inline keyboard, custom reply keyboard,
        instructions to remove reply keyboard or to force a reply from the user.

    progress (``Callable``, *optional*):
        Pass a callback function to view the file transmission progress.
        The function must take *(current, total)* as positional arguments (look at Other Parameters below for a
        detailed description) and will be called back each time a new file chunk has been successfully
        transmitted.

    progress_args (``tuple``, *optional*):
        Extra custom arguments for the progress callback function.
        You can pass anything you need to be available in the progress callback scope; for example, a Message
        object or a Client instance in order to edit the message with the updated progress status.

Other Parameters:
    current (``int``):
        The amount of bytes transmitted so far.

    total (``int``):
        The total size of the file.

    *args (``tuple``, *optional*):
        Extra custom arguments as defined in the ``progress_args`` parameter.
        You can either keep ``*args`` or add every single extra argument in your function signature.

Returns:
    On success, the sent :obj:`~pyrogram.types.Message` is returned.
    In case the upload is deliberately stopped with :meth:`~pyrogram.Client.stop_transmission`, None is returned
    instead.

Raises:
    RPCError: In case of a Telegram RPC error.
```

###### `async def reply_audio(self, audio: Union[str, BinaryIO], quote: bool = None, caption: str = '', parse_mode: Optional['enums.ParseMode'] = None, caption_entities: List['types.MessageEntity'] = None, duration: int = 0, performer: str = None, title: str = None, thumb: Union[str, BinaryIO] = None, file_name: str = None, disable_notification: bool = None, reply_to_message_id: int = None, business_connection_id: str = None, reply_in_chat_id: Union[int, str] = None, quote_text: str = None, quote_entities: List['types.MessageEntity'] = None, allow_paid_broadcast: bool = None, message_effect_id: int = None, reply_markup: Union['types.InlineKeyboardMarkup', 'types.ReplyKeyboardMarkup', 'types.ReplyKeyboardRemove', 'types.ForceReply'] = None, progress: Callable = None, progress_args: tuple = ()) -> 'Message'`

```text
Bound method *reply_audio* of :obj:`~pyrogram.types.Message`.

Use as a shortcut for:

.. code-block:: python

    await client.send_audio(
        chat_id=message.chat.id,
        audio=audio
    )

Example:
    .. code-block:: python

        await message.reply_audio(audio)

Parameters:
    audio (``str``):
        Audio file to send.
        Pass a file_id as string to send an audio file that exists on the Telegram servers,
        pass an HTTP URL as a string for Telegram to get an audio file from the Internet, or
        pass a file path as string to upload a new audio file that exists on your local machine.

    quote (``bool``, *optional*):
        If ``True``, the message will be sent as a reply to this message.
        If *reply_to_message_id* is passed, this parameter will be ignored.
        Defaults to ``True`` in group chats and ``False`` in private chats.

    caption (``str``, *optional*):
        Audio caption, 0-1024 characters.

    parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
        By default, texts are parsed using both Markdown and HTML styles.
        You can combine both syntaxes together.

    caption_entities (List of :obj:`~pyrogram.types.MessageEntity`):
        List of special entities that appear in the caption, which can be specified instead of *parse_mode*.

    duration (``int``, *optional*):
        Duration of the audio in seconds.

    performer (``str``, *optional*):
        Performer.

    title (``str``, *optional*):
        Track name.

    thumb (``str`` | ``BinaryIO``, *optional*):
        Thumbnail of the music file album cover.
        The thumbnail should be in JPEG format and less than 200 KB in size.
        A thumbnail's width and height should not exceed 320 pixels.
        Thumbnails can't be reused and can be only uploaded as a new file.

    file_name (``str``, *optional*):
        File name of the audio sent.
        Defaults to file's path basename.

    disable_notification (``bool``, *optional*):
        Sends the message silently.
        Users will receive a notification with no sound.

    reply_to_message_id (``int``, *optional*):
        If the message is a reply, ID of the original message.

    business_connection_id (``str``, *optional*):
        Business connection identifier.
        for business bots only.

    reply_in_chat_id: Union[int, str] = None,
        Unique identifier of target chat.
        for reply message in another chat.

    quote_text (``str``, *optional*):
        Text to quote.
        for reply_to_message only.

    quote_entities (List of :obj:`~pyrogram.types.MessageEntity`, *optional*):
        List of special entities that appear in quote_text, which can be specified instead of *parse_mode*.
        for reply_to_message only.

    allow_paid_broadcast (``bool``, *optional*):
        Pass True to allow the message to ignore regular broadcast limits for a small fee; for bots.

    message_effect_id (``int`` ``64-bit``, *optional*):
        Unique identifier of the message effect to be added to the message; for private chats only.

    reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardRemove` | :obj:`~pyrogram.types.ForceReply`, *optional*):
        Additional interface options. An object for an inline keyboard, custom reply keyboard,
        instructions to remove reply keyboard or to force a reply from the user.

    progress (``Callable``, *optional*):
        Pass a callback function to view the file transmission progress.
        The function must take *(current, total)* as positional arguments (look at Other Parameters below for a
        detailed description) and will be called back each time a new file chunk has been successfully
        transmitted.

    progress_args (``tuple``, *optional*):
        Extra custom arguments for the progress callback function.
        You can pass anything you need to be available in the progress callback scope; for example, a Message
        object or a Client instance in order to edit the message with the updated progress status.

Other Parameters:
    current (``int``):
        The amount of bytes transmitted so far.

    total (``int``):
        The total size of the file.

    *args (``tuple``, *optional*):
        Extra custom arguments as defined in the ``progress_args`` parameter.
        You can either keep ``*args`` or add every single extra argument in your function signature.

Returns:
    On success, the sent :obj:`~pyrogram.types.Message` is returned.
    In case the upload is deliberately stopped with :meth:`~pyrogram.Client.stop_transmission`, None is returned
    instead.

Raises:
    RPCError: In case of a Telegram RPC error.
```

###### `async def reply_cached_media(self, file_id: str, quote: bool = None, caption: str = '', parse_mode: Optional['enums.ParseMode'] = None, caption_entities: List['types.MessageEntity'] = None, disable_notification: bool = None, reply_to_message_id: int = None, reply_in_chat_id: Union[int, str] = None, quote_text: str = None, quote_entities: List['types.MessageEntity'] = None, allow_paid_broadcast: bool = None, reply_markup: Union['types.InlineKeyboardMarkup', 'types.ReplyKeyboardMarkup', 'types.ReplyKeyboardRemove', 'types.ForceReply'] = None) -> 'Message'`

```text
Bound method *reply_cached_media* of :obj:`~pyrogram.types.Message`.

Use as a shortcut for:

.. code-block:: python

    await client.send_cached_media(
        chat_id=message.chat.id,
        file_id=file_id
    )

Example:
    .. code-block:: python

        await message.reply_cached_media(file_id)

Parameters:
    file_id (``str``):
        Media to send.
        Pass a file_id as string to send a media that exists on the Telegram servers.

    quote (``bool``, *optional*):
        If ``True``, the message will be sent as a reply to this message.
        If *reply_to_message_id* is passed, this parameter will be ignored.
        Defaults to ``True`` in group chats and ``False`` in private chats.

    caption (``bool``, *optional*):
        Media caption, 0-1024 characters.

    parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
        By default, texts are parsed using both Markdown and HTML styles.
        You can combine both syntaxes together.

    caption_entities (List of :obj:`~pyrogram.types.MessageEntity`):
        List of special entities that appear in the caption, which can be specified instead of *parse_mode*.

    disable_notification (``bool``, *optional*):
        Sends the message silently.
        Users will receive a notification with no sound.

    reply_to_message_id (``int``, *optional*):
        If the message is a reply, ID of the original message.

    reply_in_chat_id: Union[int, str] = None,
        Unique identifier of target chat.
        for reply message in another chat.

    quote_text (``str``, *optional*):
        Text to quote.
        for reply_to_message only.

    quote_entities (List of :obj:`~pyrogram.types.MessageEntity`, *optional*):
        List of special entities that appear in quote_text, which can be specified instead of *parse_mode*.
        for reply_to_message only.

    allow_paid_broadcast (``bool``, *optional*):
        Pass True to allow the message to ignore regular broadcast limits for a small fee; for bots.

    reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardRemove` | :obj:`~pyrogram.types.ForceReply`, *optional*):
        Additional interface options. An object for an inline keyboard, custom reply keyboard,
        instructions to remove reply keyboard or to force a reply from the user.

Returns:
    On success, the sent :obj:`~pyrogram.types.Message` is returned.

Raises:
    RPCError: In case of a Telegram RPC error.
```

###### `async def reply_chat_action(self, action: 'enums.ChatAction', business_connection_id: str = None, emoji: str = None, emoji_message_id: int = None, emoji_message_interaction: 'raw.types.DataJSON' = None) -> bool`

```text
Bound method *reply_chat_action* of :obj:`~pyrogram.types.Message`.

Use as a shortcut for:

.. code-block:: python

    from pyrogram import enums

    await client.send_chat_action(
        chat_id=message.chat.id,
        action=enums.ChatAction.TYPING
    )

Example:
    .. code-block:: python

        from pyrogram import enums

        await message.reply_chat_action(enums.ChatAction.TYPING)

Parameters:
    action (:obj:`~pyrogram.enums.ChatAction`):
        Type of action to broadcast.

    business_connection_id (``str``, *optional*):
        Business connection identifier.
        for business bots only.

    emoji (``str``, *optional*):
        The animated emoji. Only supported for :obj:`~pyrogram.enums.ChatAction.TRIGGER_EMOJI_ANIMATION` and :obj:`~pyrogram.enums.ChatAction.WATCH_EMOJI_ANIMATION`.

    emoji_message_id (``int``, *optional*):
        Message identifier of the message containing the animated emoji. Only supported for :obj:`~pyrogram.enums.ChatAction.TRIGGER_EMOJI_ANIMATION`.

    emoji_message_interaction (:obj:`raw.types.DataJSON`, *optional*):
        Only supported for :obj:`~pyrogram.enums.ChatAction.TRIGGER_EMOJI_ANIMATION`.

Returns:
    ``bool``: On success, True is returned.

Raises:
    RPCError: In case of a Telegram RPC error.
    ValueError: In case the provided string is not a valid chat action.
```

###### `async def reply_contact(self, phone_number: str, first_name: str, quote: bool = None, last_name: str = '', vcard: str = '', disable_notification: bool = None, reply_to_message_id: int = None, business_connection_id: str = None, reply_in_chat_id: Union[int, str] = None, quote_text: str = None, quote_entities: List['types.MessageEntity'] = None, allow_paid_broadcast: bool = None, parse_mode: Optional['enums.ParseMode'] = None, reply_markup: Union['types.InlineKeyboardMarkup', 'types.ReplyKeyboardMarkup', 'types.ReplyKeyboardRemove', 'types.ForceReply'] = None) -> 'Message'`

```text
Bound method *reply_contact* of :obj:`~pyrogram.types.Message`.

Use as a shortcut for:

.. code-block:: python

    await client.send_contact(
        chat_id=message.chat.id,
        phone_number=phone_number,
        first_name=first_name
    )

Example:
    .. code-block:: python

        await message.reply_contact("+1-123-456-7890", "Name")

Parameters:
    phone_number (``str``):
        Contact's phone number.

    first_name (``str``):
        Contact's first name.

    quote (``bool``, *optional*):
        If ``True``, the message will be sent as a reply to this message.
        If *reply_to_message_id* is passed, this parameter will be ignored.
        Defaults to ``True`` in group chats and ``False`` in private chats.

    last_name (``str``, *optional*):
        Contact's last name.

    vcard (``str``, *optional*):
        Additional data about the contact in the form of a vCard, 0-2048 bytes

    disable_notification (``bool``, *optional*):
        Sends the message silently.
        Users will receive a notification with no sound.

    reply_to_message_id (``int``, *optional*):
        If the message is a reply, ID of the original message.

    business_connection_id (``str``, *optional*):
        Business connection identifier.
        for business bots only.

    reply_in_chat_id: Union[int, str] = None,
        Unique identifier of target chat.
        for reply message in another chat.

    quote_text (``str``, *optional*):
        Text to quote.
        for reply_to_message only.

    quote_entities (List of :obj:`~pyrogram.types.MessageEntity`, *optional*):
        List of special entities that appear in quote_text, which can be specified instead of *parse_mode*.
        for reply_to_message only.

    allow_paid_broadcast (``bool``, *optional*):
        Pass True to allow the message to ignore regular broadcast limits for a small fee; for bots

    parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
        By default, quote_text are parsed using both Markdown and HTML styles.
        You can combine both syntaxes together.
        For quote_text.

    reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardRemove` | :obj:`~pyrogram.types.ForceReply`, *optional*):
        Additional interface options. An object for an inline keyboard, custom reply keyboard,
        instructions to remove reply keyboard or to force a reply from the user.

Returns:
    On success, the sent :obj:`~pyrogram.types.Message` is returned.

Raises:
    RPCError: In case of a Telegram RPC error.
```

###### `async def reply_document(self, document: Union[str, BinaryIO], quote: bool = None, thumb: Union[str, BinaryIO] = None, caption: str = '', parse_mode: Optional['enums.ParseMode'] = None, caption_entities: List['types.MessageEntity'] = None, file_name: str = None, force_document: bool = None, disable_notification: bool = None, reply_to_message_id: int = None, business_connection_id: str = None, reply_in_chat_id: Union[int, str] = None, quote_text: str = None, quote_entities: List['types.MessageEntity'] = None, allow_paid_broadcast: bool = None, message_effect_id: int = None, schedule_date: datetime = None, reply_markup: Union['types.InlineKeyboardMarkup', 'types.ReplyKeyboardMarkup', 'types.ReplyKeyboardRemove', 'types.ForceReply'] = None, progress: Callable = None, progress_args: tuple = ()) -> 'Message'`

```text
Bound method *reply_document* of :obj:`~pyrogram.types.Message`.

Use as a shortcut for:

.. code-block:: python

    await client.send_document(
        chat_id=message.chat.id,
        document=document
    )

Example:
    .. code-block:: python

        await message.reply_document(document)

Parameters:
    document (``str``):
        File to send.
        Pass a file_id as string to send a file that exists on the Telegram servers,
        pass an HTTP URL as a string for Telegram to get a file from the Internet, or
        pass a file path as string to upload a new file that exists on your local machine.

    quote (``bool``, *optional*):
        If ``True``, the message will be sent as a reply to this message.
        If *reply_to_message_id* is passed, this parameter will be ignored.
        Defaults to ``True`` in group chats and ``False`` in private chats.

    thumb (``str`` | ``BinaryIO``, *optional*):
        Thumbnail of the file sent.
        The thumbnail should be in JPEG format and less than 200 KB in size.
        A thumbnail's width and height should not exceed 320 pixels.
        Thumbnails can't be reused and can be only uploaded as a new file.

    caption (``str``, *optional*):
        Document caption, 0-1024 characters.

    parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
        By default, texts are parsed using both Markdown and HTML styles.
        You can combine both syntaxes together.

    caption_entities (List of :obj:`~pyrogram.types.MessageEntity`):
        List of special entities that appear in the caption, which can be specified instead of *parse_mode*.

    file_name (``str``, *optional*):
        File name of the document sent.
        Defaults to file's path basename.

    force_document (``bool``, *optional*):
        Pass True to force sending files as document. Useful for video files that need to be sent as
        document messages instead of video messages.
        Defaults to False.

    disable_notification (``bool``, *optional*):
        Sends the message silently.
        Users will receive a notification with no sound.

    reply_to_message_id (``int``, *optional*):
        If the message is a reply, ID of the original message.

    business_connection_id (``str``, *optional*):
        Business connection identifier.
        for business bots only.

    reply_in_chat_id: Union[int, str] = None,
        Unique identifier of target chat.
        for reply message in another chat.

    quote_text (``str``, *optional*):
        Text to quote.
        for reply_to_message only.

    quote_entities (List of :obj:`~pyrogram.types.MessageEntity`, *optional*):
        List of special entities that appear in quote_text, which can be specified instead of *parse_mode*.
        for reply_to_message only.

    allow_paid_broadcast (``bool``, *optional*):
        Pass True to allow the message to ignore regular broadcast limits for a small fee; for bots.

    message_effect_id (``int`` ``64-bit``, *optional*):
        Unique identifier of the message effect to be added to the message; for private chats only.

    schedule_date (:py:obj:`~datetime.datetime`, *optional*):
        Date when the message will be automatically sent.

    reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardRemove` | :obj:`~pyrogram.types.ForceReply`, *optional*):
        Additional interface options. An object for an inline keyboard, custom reply keyboard,
        instructions to remove reply keyboard or to force a reply from the user.

    progress (``Callable``, *optional*):
        Pass a callback function to view the file transmission progress.
        The function must take *(current, total)* as positional arguments (look at Other Parameters below for a
        detailed description) and will be called back each time a new file chunk has been successfully
        transmitted.

    progress_args (``tuple``, *optional*):
        Extra custom arguments for the progress callback function.
        You can pass anything you need to be available in the progress callback scope; for example, a Message
        object or a Client instance in order to edit the message with the updated progress status.

Other Parameters:
    current (``int``):
        The amount of bytes transmitted so far.

    total (``int``):
        The total size of the file.

    *args (``tuple``, *optional*):
        Extra custom arguments as defined in the ``progress_args`` parameter.
        You can either keep ``*args`` or add every single extra argument in your function signature.

Returns:
    On success, the sent :obj:`~pyrogram.types.Message` is returned.
    In case the upload is deliberately stopped with :meth:`~pyrogram.Client.stop_transmission`, None is returned
    instead.

Raises:
    RPCError: In case of a Telegram RPC error.
```

###### `async def reply_game(self, game_short_name: str, quote: bool = None, disable_notification: bool = None, reply_to_message_id: int = None, business_connection_id: str = None, allow_paid_broadcast: bool = None, reply_markup: Union['types.InlineKeyboardMarkup', 'types.ReplyKeyboardMarkup', 'types.ReplyKeyboardRemove', 'types.ForceReply'] = None) -> 'Message'`

```text
Bound method *reply_game* of :obj:`~pyrogram.types.Message`.

Use as a shortcut for:

.. code-block:: python

    await client.send_game(
        chat_id=message.chat.id,
        game_short_name="lumberjack"
    )

Example:
    .. code-block:: python

        await message.reply_game("lumberjack")

Parameters:
    game_short_name (``str``):
        Short name of the game, serves as the unique identifier for the game. Set up your games via Botfather.

    quote (``bool``, *optional*):
        If ``True``, the message will be sent as a reply to this message.
        If *reply_to_message_id* is passed, this parameter will be ignored.
        Defaults to ``True`` in group chats and ``False`` in private chats.

    disable_notification (``bool``, *optional*):
        Sends the message silently.
        Users will receive a notification with no sound.

    reply_to_message_id (``int``, *optional*):
        If the message is a reply, ID of the original message.

    business_connection_id (``str``, *optional*):
        Business connection identifier.
        for business bots only.

    allow_paid_broadcast (``bool``, *optional*):
        Pass True to allow the message to ignore regular broadcast limits for a small fee; for bots.

    reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup`, *optional*):
        An object for an inline keyboard. If empty, one ‘Play game_title’ button will be shown automatically.
        If not empty, the first button must launch the game.

Returns:
    On success, the sent :obj:`~pyrogram.types.Message` is returned.

Raises:
    RPCError: In case of a Telegram RPC error.
```

###### `async def reply_inline_bot_result(self, query_id: int, result_id: str, quote: bool = None, disable_notification: bool = None, reply_to_message_id: int = None, quote_text: str = None, quote_entities: List['types.MessageEntity'] = None, parse_mode: Optional['enums.ParseMode'] = None) -> 'Message'`

```text
Bound method *reply_inline_bot_result* of :obj:`~pyrogram.types.Message`.

Use as a shortcut for:

.. code-block:: python

    await client.send_inline_bot_result(
        chat_id=message.chat.id,
        query_id=query_id,
        result_id=result_id
    )

Example:
    .. code-block:: python

        await message.reply_inline_bot_result(query_id, result_id)

Parameters:
    query_id (``int``):
        Unique identifier for the answered query.

    result_id (``str``):
        Unique identifier for the result that was chosen.

    quote (``bool``, *optional*):
        If ``True``, the message will be sent as a reply to this message.
        If *reply_to_message_id* is passed, this parameter will be ignored.
        Defaults to ``True`` in group chats and ``False`` in private chats.

    disable_notification (``bool``, *optional*):
        Sends the message silently.
        Users will receive a notification with no sound.

    reply_to_message_id (``bool``, *optional*):
        If the message is a reply, ID of the original message.

    quote_text (``str``, *optional*):
        Text to quote.
        for reply_to_message only.

    quote_entities (List of :obj:`~pyrogram.types.MessageEntity`, *optional*):
        List of special entities that appear in quote_text, which can be specified instead of *parse_mode*.
        for reply_to_message only.

Returns:
    On success, the sent Message is returned.

Raises:
    RPCError: In case of a Telegram RPC error.
```

###### `async def reply_location(self, latitude: float, longitude: float, quote: bool = None, horizontal_accuracy: float = None, disable_notification: bool = None, reply_to_message_id: int = None, business_connection_id: str = None, reply_in_chat_id: Union[int, str] = None, quote_text: str = None, quote_entities: List['types.MessageEntity'] = None, allow_paid_broadcast: bool = None, parse_mode: Optional['enums.ParseMode'] = None, reply_markup: Union['types.InlineKeyboardMarkup', 'types.ReplyKeyboardMarkup', 'types.ReplyKeyboardRemove', 'types.ForceReply'] = None) -> 'Message'`

```text
Bound method *reply_location* of :obj:`~pyrogram.types.Message`.

Use as a shortcut for:

.. code-block:: python

    await client.send_location(
        chat_id=message.chat.id,
        latitude=latitude,
        longitude=longitude
    )

Example:
    .. code-block:: python

        await message.reply_location(latitude, longitude)

Parameters:
    latitude (``float``):
        Latitude of the location.

    longitude (``float``):
        Longitude of the location.

    quote (``bool``, *optional*):
        If ``True``, the message will be sent as a reply to this message.
        If *reply_to_message_id* is passed, this parameter will be ignored.
        Defaults to ``True`` in group chats and ``False`` in private chats.

    horizontal_accuracy (``float``, *optional*):
        The radius of uncertainty for the location, measured in meters; 0-1500.

    disable_notification (``bool``, *optional*):
        Sends the message silently.
        Users will receive a notification with no sound.

    reply_to_message_id (``int``, *optional*):
        If the message is a reply, ID of the original message

    business_connection_id (``str``, *optional*):
        Business connection identifier.
        for business bots only.

    reply_in_chat_id: Union[int, str] = None,
        Unique identifier of target chat.
        for reply message in another chat.

    quote_text (``str``, *optional*):
        Text to quote.
        for reply_to_message only.

    quote_entities (List of :obj:`~pyrogram.types.MessageEntity`, *optional*):
        List of special entities that appear in quote_text, which can be specified instead of *parse_mode*.
        for reply_to_message only.

    allow_paid_broadcast (``bool``, *optional*):
        Pass True to allow the message to ignore regular broadcast limits for a small fee; for bots

    parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
        By default, quote_text are parsed using both Markdown and HTML styles.
        You can combine both syntaxes together.
        For quote_text.

    reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardRemove` | :obj:`~pyrogram.types.ForceReply`, *optional*):
        Additional interface options. An object for an inline keyboard, custom reply keyboard,
        instructions to remove reply keyboard or to force a reply from the user.

Returns:
    On success, the sent :obj:`~pyrogram.types.Message` is returned.

Raises:
    RPCError: In case of a Telegram RPC error.
```

###### `async def reply_media_group(self, media: List[Union['types.InputMediaPhoto', 'types.InputMediaVideo', 'types.InputMediaAudio', 'types.InputMediaDocument']], quote: bool = None, disable_notification: bool = None, reply_to_message_id: int = None, reply_in_chat_id: Union[int, str] = None, business_connection_id: str = None, quote_text: str = None, quote_entities: List['types.MessageEntity'] = None, allow_paid_broadcast: bool = None, message_effect_id: int = None, parse_mode: Optional['enums.ParseMode'] = None, invert_media: bool = None, progress: Callable = None, progress_args: tuple = ()) -> List['types.Message']`

```text
Bound method *reply_media_group* of :obj:`~pyrogram.types.Message`.

Use as a shortcut for:

.. code-block:: python

    await client.send_media_group(
        chat_id=message.chat.id,
        media=list_of_media
    )

Example:
    .. code-block:: python

        await message.reply_media_group(list_of_media)

Parameters:
    media (``list``):
        A list containing either :obj:`~pyrogram.types.InputMediaPhoto` or
        :obj:`~pyrogram.types.InputMediaVideo` objects
        describing photos and videos to be sent, must include 2–10 items.

    quote (``bool``, *optional*):
        If ``True``, the message will be sent as a reply to this message.
        If *reply_to_message_id* is passed, this parameter will be ignored.
        Defaults to ``True`` in group chats and ``False`` in private chats.

    disable_notification (``bool``, *optional*):
        Sends the message silently.
        Users will receive a notification with no sound.

    reply_to_message_id (``int``, *optional*):
        If the message is a reply, ID of the original message.

    business_connection_id (``str``, *optional*):
        Business connection identifier.
        for business bots only.

    reply_in_chat_id: Union[int, str] = None,
        Unique identifier of target chat.
        for reply message in another chat.

    quote_text (``str``, *optional*):
        Text to quote.
        for reply_to_message only.

    quote_entities (List of :obj:`~pyrogram.types.MessageEntity`, *optional*):
        List of special entities that appear in quote_text, which can be specified instead of *parse_mode*.
        for reply_to_message only.

    allow_paid_broadcast (``bool``, *optional*):
        Pass True to allow the message to ignore regular broadcast limits for a small fee; for bots

    message_effect_id (``int``, *optional*):
        Unique identifier of the message effect to be added to the message; for private chats only.

    invert_media (``bool``, *optional*):
        Inverts the position of the media and caption.

    progress (``Callable``, *optional*):
        Pass a callback function to view the file transmission progress.
        The function must take *(current, total)* as positional arguments (look at Other Parameters below for a
        detailed description) and will be called back each time a new file chunk has been successfully
        transmitted.

    progress_args (``tuple``, *optional*):
        Extra custom arguments for the progress callback function.
        You can pass anything you need to be available in the progress callback scope; for example, a Message
        object or a Client instance in order to edit the message with the updated progress status.

Other Parameters:
    current (``int``):
        The amount of bytes transmitted so far.

    total (``int``):
        The total size of the file.

    *args (``tuple``, *optional*):
        Extra custom arguments as defined in the ``progress_args`` parameter.
        You can either keep ``*args`` or add every single extra argument in your function signature.

Returns:
    On success, a :obj:`~pyrogram.types.Messages` object is returned containing all the
    single messages sent.

Raises:
    RPCError: In case of a Telegram RPC error.
```

###### `async def reply_photo(self, photo: Union[str, BinaryIO], quote: bool = None, caption: str = '', parse_mode: Optional['enums.ParseMode'] = None, caption_entities: List['types.MessageEntity'] = None, has_spoiler: bool = None, ttl_seconds: int = None, disable_notification: bool = None, reply_to_message_id: int = None, business_connection_id: str = None, reply_in_chat_id: Union[int, str] = None, quote_text: str = None, quote_entities: List['types.MessageEntity'] = None, schedule_date: datetime = None, protect_content: bool = None, allow_paid_broadcast: bool = None, message_effect_id: int = None, view_once: bool = None, invert_media: bool = None, reply_markup: Union['types.InlineKeyboardMarkup', 'types.ReplyKeyboardMarkup', 'types.ReplyKeyboardRemove', 'types.ForceReply'] = None, progress: Callable = None, progress_args: tuple = ()) -> 'Message'`

```text
Bound method *reply_photo* of :obj:`~pyrogram.types.Message`.

Use as a shortcut for:

.. code-block:: python

    await client.send_photo(
        chat_id=message.chat.id,
        photo=photo
    )

Example:
    .. code-block:: python

        await message.reply_photo(photo)

Parameters:
    photo (``str``):
        Photo to send.
        Pass a file_id as string to send a photo that exists on the Telegram servers,
        pass an HTTP URL as a string for Telegram to get a photo from the Internet, or
        pass a file path as string to upload a new photo that exists on your local machine.

    quote (``bool``, *optional*):
        If ``True``, the message will be sent as a reply to this message.
        If *reply_to_message_id* is passed, this parameter will be ignored.
        Defaults to ``True`` in group chats and ``False`` in private chats.

    caption (``str``, *optional*):
        Photo caption, 0-1024 characters.

    parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
        By default, texts are parsed using both Markdown and HTML styles.
        You can combine both syntaxes together.

    caption_entities (List of :obj:`~pyrogram.types.MessageEntity`):
        List of special entities that appear in the caption, which can be specified instead of *parse_mode*.

    has_spoiler (``bool``, *optional*):
        Pass True if the photo needs to be covered with a spoiler animation.

    ttl_seconds (``int``, *optional*):
        Self-Destruct Timer.
        If you set a timer, the photo will self-destruct in *ttl_seconds*
        seconds after it was viewed.

    disable_notification (``bool``, *optional*):
        Sends the message silently.
        Users will receive a notification with no sound.

    reply_to_message_id (``int``, *optional*):
        If the message is a reply, ID of the original message.

    view_once (``bool``, *optional*):
        Self-Destruct Timer.
        If True, the photo will self-destruct after it was viewed.

    invert_media (``bool``, *optional*):
        Pass True to invert the photo and caption position.

    business_connection_id (``str``, *optional*):
        Business connection identifier.
        for business bots only.

    reply_in_chat_id: Union[int, str] = None,
        Unique identifier of target chat.
        for reply message in another chat.

    quote_text (``str``, *optional*):
        Text to quote.
        for reply_to_message only.

    quote_entities (List of :obj:`~pyrogram.types.MessageEntity`, *optional*):
        List of special entities that appear in quote_text, which can be specified instead of *parse_mode*.
        for reply_to_message only.

    schedule_date (:py:obj:`~datetime.datetime`, *optional*):
        Date when the message will be automatically sent.

    protect_content (``bool``, *optional*):
        Protects the contents of the sent message from forwarding and saving.

    allow_paid_broadcast (``bool``, *optional*):
        Pass True to allow the message to ignore regular broadcast limits for a small fee; for bots

    message_effect_id (``int`` ``64-bit``, *optional*):
        Unique identifier of the message effect to be added to the message; for private chats only.

    reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardRemove` | :obj:`~pyrogram.types.ForceReply`, *optional*):
        Additional interface options. An object for an inline keyboard, custom reply keyboard,
        instructions to remove reply keyboard or to force a reply from the user.

    progress (``Callable``, *optional*):
        Pass a callback function to view the file transmission progress.
        The function must take *(current, total)* as positional arguments (look at Other Parameters below for a
        detailed description) and will be called back each time a new file chunk has been successfully
        transmitted.

    progress_args (``tuple``, *optional*):
        Extra custom arguments for the progress callback function.
        You can pass anything you need to be available in the progress callback scope; for example, a Message
        object or a Client instance in order to edit the message with the updated progress status.

Other Parameters:
    current (``int``):
        The amount of bytes transmitted so far.

    total (``int``):
        The total size of the file.

    *args (``tuple``, *optional*):
        Extra custom arguments as defined in the ``progress_args`` parameter.
        You can either keep ``*args`` or add every single extra argument in your function signature.

Returns:
    On success, the sent :obj:`~pyrogram.types.Message` is returned.
    In case the upload is deliberately stopped with :meth:`~pyrogram.Client.stop_transmission`, None is returned
    instead.

Raises:
    RPCError: In case of a Telegram RPC error.
```

###### `async def reply_poll(self, question: str, options: List['types.PollOption'], question_entities: List['types.MessageEntity'] = None, is_anonymous: bool = True, type: 'enums.PollType' = enums.PollType.REGULAR, allows_multiple_answers: bool = None, correct_option_id: int = None, explanation: str = None, explanation_parse_mode: 'enums.ParseMode' = None, explanation_entities: List['types.MessageEntity'] = None, open_period: int = None, close_date: datetime = None, is_closed: bool = None, quote: bool = None, disable_notification: bool = None, protect_content: bool = None, reply_to_message_id: int = None, business_connection_id: str = None, reply_in_chat_id: Union[int, str] = None, quote_text: str = None, quote_entities: List['types.MessageEntity'] = None, allow_paid_broadcast: bool = None, parse_mode: Optional['enums.ParseMode'] = None, schedule_date: datetime = None, reply_markup: Union['types.InlineKeyboardMarkup', 'types.ReplyKeyboardMarkup', 'types.ReplyKeyboardRemove', 'types.ForceReply'] = None) -> 'Message'`

```text
Bound method *reply_poll* of :obj:`~pyrogram.types.Message`.

Use as a shortcut for:

.. code-block:: python

    await client.send_poll(
        chat_id=message.chat.id,
        question="This is a poll",
        options=[
            PollOption("A"),
            PollOption("B"),
            PollOption("C")
        ]
    )

Example:
    .. code-block:: python

        await message.reply_poll(
            "This is a poll",
            [
                PollOption("A"),
                PollOption("B"),
                PollOption("C")
            ]
        )

Parameters:
    question (``str``):
        Poll question, 1-255 characters.

    options (List of :obj:`~pyrogram.types.PollOption`):
        List of PollOption.

    question_entities (List of :obj:`~pyrogram.types.MessageEntity`, *optional*):
        List of special entities that appear in the poll question, which can be specified instead of *parse_mode*.

    is_anonymous (``bool``, *optional*):
        True, if the poll needs to be anonymous.
        Defaults to True.

    type (:obj`~pyrogram.enums.PollType`, *optional*):
        Poll type, :obj:`~pyrogram.enums.PollType.QUIZ` or :obj:`~pyrogram.enums.PollType.REGULAR`.
        Defaults to :obj:`~pyrogram.enums.PollType.REGULAR`.

    allows_multiple_answers (``bool``, *optional*):
        True, if the poll allows multiple answers, ignored for polls in quiz mode.
        Defaults to False.

    correct_option_id (``int``, *optional*):
        0-based identifier of the correct answer option, required for polls in quiz mode.

    explanation (``str``, *optional*):
        Text that is shown when a user chooses an incorrect answer or taps on the lamp icon in a quiz-style
        poll, 0-200 characters with at most 2 line feeds after entities parsing.

    explanation_parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
        By default, texts are parsed using both Markdown and HTML styles.
        You can combine both syntaxes together.

    explanation_entities (List of :obj:`~pyrogram.types.MessageEntity`):
        List of special entities that appear in the poll explanation, which can be specified instead of
        *parse_mode*.

    open_period (``int``, *optional*):
        Amount of time in seconds the poll will be active after creation, 5-600.
        Can't be used together with *close_date*.

    close_date (:py:obj:`~datetime.datetime`, *optional*):
        Point in time when the poll will be automatically closed.
        Must be at least 5 and no more than 600 seconds in the future.
        Can't be used together with *open_period*.

    is_closed (``bool``, *optional*):
        Pass True, if the poll needs to be immediately closed.
        This can be useful for poll preview.

    quote (``bool``, *optional*):
        If ``True``, the message will be sent as a reply to this message.
        If *reply_to_message_id* is passed, this parameter will be ignored.
        Defaults to ``True`` in group chats and ``False`` in private chats.

    disable_notification (``bool``, *optional*):
        Sends the message silently.
        Users will receive a notification with no sound.

    protect_content (``bool``, *optional*):
        Protects the contents of the sent message from forwarding and saving.

    reply_to_message_id (``int``, *optional*):
        If the message is a reply, ID of the original message.

    business_connection_id (``str``, *optional*):
        Business connection identifier.
        for business bots only.

    reply_in_chat_id: Union[int, str] = None,
        Unique identifier of target chat.
        for reply message in another chat.

    quote_text (``str``, *optional*):
        Text to quote.
        for reply_to_message only.

    quote_entities (List of :obj:`~pyrogram.types.MessageEntity`, *optional*):
        List of special entities that appear in quote_text, which can be specified instead of *parse_mode*.
        for reply_to_message only.

    allow_paid_broadcast (``bool``, *optional*):
        Pass True to allow the message to ignore regular broadcast limits for a small fee; for bots.

    parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
        By default, quote_text are parsed using both Markdown and HTML styles.
        You can combine both syntaxes together.
        For quote_text.

    schedule_date (:py:obj:`~datetime.datetime`, *optional*):
        Date when the message will be automatically sent.

    reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardRemove` | :obj:`~pyrogram.types.ForceReply`, *optional*):
        Additional interface options. An object for an inline keyboard, custom reply keyboard,
        instructions to remove reply keyboard or to force a reply from the user.

Returns:
    On success, the sent :obj:`~pyrogram.types.Message` is returned.

Raises:
    RPCError: In case of a Telegram RPC error.
```

###### `async def reply_sticker(self, sticker: Union[str, BinaryIO], quote: bool = None, emoji: str = None, disable_notification: bool = None, reply_to_message_id: int = None, business_connection_id: str = None, reply_in_chat_id: Union[int, str] = None, quote_text: str = None, quote_entities: List['types.MessageEntity'] = None, allow_paid_broadcast: bool = None, message_effect_id: int = None, parse_mode: Optional['enums.ParseMode'] = None, reply_markup: Union['types.InlineKeyboardMarkup', 'types.ReplyKeyboardMarkup', 'types.ReplyKeyboardRemove', 'types.ForceReply'] = None, progress: Callable = None, progress_args: tuple = ()) -> 'Message'`

```text
Bound method *reply_sticker* of :obj:`~pyrogram.types.Message`.

Use as a shortcut for:

.. code-block:: python

    await client.send_sticker(
        chat_id=message.chat.id,
        sticker=sticker
    )

Example:
    .. code-block:: python

        await message.reply_sticker(sticker)

Parameters:
    sticker (``str``):
        Sticker to send.
        Pass a file_id as string to send a sticker that exists on the Telegram servers,
        pass an HTTP URL as a string for Telegram to get a .webp sticker file from the Internet, or
        pass a file path as string to upload a new sticker that exists on your local machine.

    quote (``bool``, *optional*):
        If ``True``, the message will be sent as a reply to this message.
        If *reply_to_message_id* is passed, this parameter will be ignored.
        Defaults to ``True`` in group chats and ``False`` in private chats.

    emoji (``str``, *optional*):
        Emoji associated with the sticker; only for just uploaded stickers

    disable_notification (``bool``, *optional*):
        Sends the message silently.
        Users will receive a notification with no sound.

    reply_to_message_id (``int``, *optional*):
        If the message is a reply, ID of the original message.

    business_connection_id (``str``, *optional*):
        Business connection identifier.
        for business bots only.

    reply_in_chat_id: Union[int, str] = None,
        Unique identifier of target chat.
        for reply message in another chat.

    quote_text (``str``, *optional*):
        Text to quote.
        for reply_to_message only.

    quote_entities (List of :obj:`~pyrogram.types.MessageEntity`, *optional*):
        List of special entities that appear in quote_text, which can be specified instead of *parse_mode*.
        for reply_to_message only.

    allow_paid_broadcast (``bool``, *optional*):
        Pass True to allow the message to ignore regular broadcast limits for a small fee; for bots

    message_effect_id (``int`` ``64-bit``, *optional*):
        Unique identifier of the message effect to be added to the message; for private chats only.

    parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
        By default, quote_text are parsed using both Markdown and HTML styles.
        You can combine both syntaxes together.
        For quote_text.

    reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardRemove` | :obj:`~pyrogram.types.ForceReply`, *optional*):
        Additional interface options. An object for an inline keyboard, custom reply keyboard,
        instructions to remove reply keyboard or to force a reply from the user.

    progress (``Callable``, *optional*):
        Pass a callback function to view the file transmission progress.
        The function must take *(current, total)* as positional arguments (look at Other Parameters below for a
        detailed description) and will be called back each time a new file chunk has been successfully
        transmitted.

    progress_args (``tuple``, *optional*):
        Extra custom arguments for the progress callback function.
        You can pass anything you need to be available in the progress callback scope; for example, a Message
        object or a Client instance in order to edit the message with the updated progress status.

Other Parameters:
    current (``int``):
        The amount of bytes transmitted so far.

    total (``int``):
        The total size of the file.

    *args (``tuple``, *optional*):
        Extra custom arguments as defined in the ``progress_args`` parameter.
        You can either keep ``*args`` or add every single extra argument in your function signature.

Returns:
    On success, the sent :obj:`~pyrogram.types.Message` is returned.
    In case the upload is deliberately stopped with :meth:`~pyrogram.Client.stop_transmission`, None is returned
    instead.

Raises:
    RPCError: In case of a Telegram RPC error.
```

###### `async def reply_venue(self, latitude: float, longitude: float, title: str, address: str, quote: bool = None, foursquare_id: str = '', foursquare_type: str = '', disable_notification: bool = None, reply_to_message_id: int = None, business_connection_id: str = None, reply_in_chat_id: Union[int, str] = None, quote_text: str = None, quote_entities: List['types.MessageEntity'] = None, allow_paid_broadcast: bool = None, parse_mode: Optional['enums.ParseMode'] = None, reply_markup: Union['types.InlineKeyboardMarkup', 'types.ReplyKeyboardMarkup', 'types.ReplyKeyboardRemove', 'types.ForceReply'] = None) -> 'Message'`

```text
Bound method *reply_venue* of :obj:`~pyrogram.types.Message`.

Use as a shortcut for:

.. code-block:: python

    await client.send_venue(
        chat_id=message.chat.id,
        latitude=latitude,
        longitude=longitude,
        title="Venue title",
        address="Venue address"
    )

Example:
    .. code-block:: python

        await message.reply_venue(latitude, longitude, "Venue title", "Venue address")

Parameters:
    latitude (``float``):
        Latitude of the venue.

    longitude (``float``):
        Longitude of the venue.

    title (``str``):
        Name of the venue.

    address (``str``):
        Address of the venue.

    quote (``bool``, *optional*):
        If ``True``, the message will be sent as a reply to this message.
        If *reply_to_message_id* is passed, this parameter will be ignored.
        Defaults to ``True`` in group chats and ``False`` in private chats.

    foursquare_id (``str``, *optional*):
        Foursquare identifier of the venue.

    foursquare_type (``str``, *optional*):
        Foursquare type of the venue, if known.
        (For example, "arts_entertainment/default", "arts_entertainment/aquarium" or "food/icecream".)

    disable_notification (``bool``, *optional*):
        Sends the message silently.
        Users will receive a notification with no sound.

    reply_to_message_id (``int``, *optional*):
        If the message is a reply, ID of the original message

    business_connection_id (``str``, *optional*):
        Business connection identifier.
        for business bots only.

    reply_in_chat_id: Union[int, str] = None,
        Unique identifier of target chat.
        for reply message in another chat.

    quote_text (``str``, *optional*):
        Text to quote.
        for reply_to_message only.

    quote_entities (List of :obj:`~pyrogram.types.MessageEntity`, *optional*):
        List of special entities that appear in quote_text, which can be specified instead of *parse_mode*.
        for reply_to_message only.

    allow_paid_broadcast (``bool``, *optional*):
        Pass True to allow the message to ignore regular broadcast limits for a small fee; for bots

    parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
        By default, quote_text are parsed using both Markdown and HTML styles.
        You can combine both syntaxes together.
        For quote_text.

    reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardRemove` | :obj:`~pyrogram.types.ForceReply`, *optional*):
        Additional interface options. An object for an inline keyboard, custom reply keyboard,
        instructions to remove reply keyboard or to force a reply from the user.

Returns:
    On success, the sent :obj:`~pyrogram.types.Message` is returned.

Raises:
    RPCError: In case of a Telegram RPC error.
```

###### `async def reply_video(self, video: Union[str, BinaryIO], quote: bool = None, caption: str = '', parse_mode: Optional['enums.ParseMode'] = None, caption_entities: List['types.MessageEntity'] = None, has_spoiler: bool = None, ttl_seconds: int = None, duration: int = 0, width: int = 0, height: int = 0, thumb: Union[str, BinaryIO] = None, file_name: str = None, supports_streaming: bool = True, disable_notification: bool = None, reply_to_message_id: int = None, business_connection_id: str = None, reply_in_chat_id: Union[int, str] = None, quote_text: str = None, quote_entities: List['types.MessageEntity'] = None, allow_paid_broadcast: bool = None, message_effect_id: int = None, view_once: bool = None, cover: Union[str, BinaryIO] = None, start_timestamp: int = None, schedule_date: datetime = None, protect_content: bool = None, invert_media: bool = None, reply_markup: Union['types.InlineKeyboardMarkup', 'types.ReplyKeyboardMarkup', 'types.ReplyKeyboardRemove', 'types.ForceReply'] = None, progress: Callable = None, progress_args: tuple = ()) -> 'Message'`

```text
Bound method *reply_video* of :obj:`~pyrogram.types.Message`.

Use as a shortcut for:

.. code-block:: python

    await client.send_video(
        chat_id=message.chat.id,
        video=video
    )

Example:
    .. code-block:: python

        await message.reply_video(video)

Parameters:
    video (``str``):
        Video to send.
        Pass a file_id as string to send a video that exists on the Telegram servers,
        pass an HTTP URL as a string for Telegram to get a video from the Internet, or
        pass a file path as string to upload a new video that exists on your local machine.

    quote (``bool``, *optional*):
        If ``True``, the message will be sent as a reply to this message.
        If *reply_to_message_id* is passed, this parameter will be ignored.
        Defaults to ``True`` in group chats and ``False`` in private chats.

    caption (``str``, *optional*):
        Video caption, 0-1024 characters.

    parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
        By default, texts are parsed using both Markdown and HTML styles.
        You can combine both syntaxes together.

    caption_entities (List of :obj:`~pyrogram.types.MessageEntity`):
        List of special entities that appear in the caption, which can be specified instead of *parse_mode*.

    has_spoiler (``bool``, *optional*):
        Pass True if the video needs to be covered with a spoiler animation.

    ttl_seconds (``int``, *optional*):
        Self-Destruct Timer.
        If you set a timer, the video will self-destruct in *ttl_seconds*
        seconds after it was viewed.

    duration (``int``, *optional*):
        Duration of sent video in seconds.

    width (``int``, *optional*):
        Video width.

    height (``int``, *optional*):
        Video height.

    thumb (``str`` | ``BinaryIO``, *optional*):
        Thumbnail of the video sent.
        The thumbnail should be in JPEG format and less than 200 KB in size.
        A thumbnail's width and height should not exceed 320 pixels.
        Thumbnails can't be reused and can be only uploaded as a new file.

    file_name (``str``, *optional*):
        File name of the video sent.
        Defaults to file's path basename.

    supports_streaming (``bool``, *optional*):
        Pass True, if the uploaded video is suitable for streaming.

    disable_notification (``bool``, *optional*):
        Sends the message silently.
        Users will receive a notification with no sound.

    reply_to_message_id (``int``, *optional*):
        If the message is a reply, ID of the original message.

    business_connection_id (``str``, *optional*):
        Business connection identifier.
        for business bots only.

    reply_in_chat_id: Union[int, str] = None,
        Unique identifier of target chat.
        for reply message in another chat.

    quote_text (``str``, *optional*):
        Text to quote.
        for reply_to_message only.

    quote_entities (List of :obj:`~pyrogram.types.MessageEntity`, *optional*):
        List of special entities that appear in quote_text, which can be specified instead of *parse_mode*.
        for reply_to_message only.

    allow_paid_broadcast (``bool``, *optional*):
        Pass True to allow the message to ignore regular broadcast limits for a small fee; for bots.

    cover (``str`` | ``BinaryIO``, *optional*):
        Video cover.
        Pass a file_id as string to attach a photo that exists on the Telegram servers,
        pass a HTTP URL as a string for Telegram to get a video from the Internet,
        pass a file path as string to upload a new photo civer that exists on your local machine, or
        pass a binary file-like object with its attribute ".name" set for in-memory uploads.

    start_timestamp (``int``, *optional*):
        Timestamp from which the video playing must start, in seconds.

    schedule_date (:py:obj:`~datetime.datetime`, *optional*):
        Date when the message will be automatically sent.

    protect_content (``bool``, *optional*):
        Protects the contents of the sent message from forwarding and saving.

    message_effect_id (``int`` ``64-bit``, *optional*):
        Unique identifier of the message effect to be added to the message; for private chats only.

    view_once (``bool``, *optional*):
        Pass True to send the video as a view-once message.

    invert_media (``bool``, *optional*):
        Pass True to invert the video and caption position.

    reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardRemove` | :obj:`~pyrogram.types.ForceReply`, *optional*):
        Additional interface options. An object for an inline keyboard, custom reply keyboard,
        instructions to remove reply keyboard or to force a reply from the user.

    progress (``Callable``, *optional*):
        Pass a callback function to view the file transmission progress.
        The function must take *(current, total)* as positional arguments (look at Other Parameters below for a
        detailed description) and will be called back each time a new file chunk has been successfully
        transmitted.

    progress_args (``tuple``, *optional*):
        Extra custom arguments for the progress callback function.
        You can pass anything you need to be available in the progress callback scope; for example, a Message
        object or a Client instance in order to edit the message with the updated progress status.

Other Parameters:
    current (``int``):
        The amount of bytes transmitted so far.

    total (``int``):
        The total size of the file.

    *args (``tuple``, *optional*):
        Extra custom arguments as defined in the ``progress_args`` parameter.
        You can either keep ``*args`` or add every single extra argument in your function signature.

Returns:
    On success, the sent :obj:`~pyrogram.types.Message` is returned.
    In case the upload is deliberately stopped with :meth:`~pyrogram.Client.stop_transmission`, None is returned
    instead.

Raises:
    RPCError: In case of a Telegram RPC error.
```

###### `async def reply_video_note(self, video_note: Union[str, BinaryIO], quote: bool = None, duration: int = 0, length: int = 1, thumb: Union[str, BinaryIO] = None, disable_notification: bool = None, reply_to_message_id: int = None, business_connection_id: str = None, reply_in_chat_id: Union[int, str] = None, quote_text: str = None, quote_entities: List['types.MessageEntity'] = None, parse_mode: Optional['enums.ParseMode'] = None, protect_content: bool = None, allow_paid_broadcast: bool = None, message_effect_id: int = None, ttl_seconds: int = None, reply_markup: Union['types.InlineKeyboardMarkup', 'types.ReplyKeyboardMarkup', 'types.ReplyKeyboardRemove', 'types.ForceReply'] = None, progress: Callable = None, progress_args: tuple = ()) -> 'Message'`

```text
Bound method *reply_video_note* of :obj:`~pyrogram.types.Message`.

Use as a shortcut for:

.. code-block:: python

    await client.send_video_note(
        chat_id=message.chat.id,
        video_note=video_note
    )

Example:
    .. code-block:: python

        await message.reply_video_note(video_note)

Parameters:
    video_note (``str``):
        Video note to send.
        Pass a file_id as string to send a video note that exists on the Telegram servers, or
        pass a file path as string to upload a new video note that exists on your local machine.
        Sending video notes by a URL is currently unsupported.

    quote (``bool``, *optional*):
        If ``True``, the message will be sent as a reply to this message.
        If *reply_to_message_id* is passed, this parameter will be ignored.
        Defaults to ``True`` in group chats and ``False`` in private chats.

    duration (``int``, *optional*):
        Duration of sent video in seconds.

    length (``int``, *optional*):
        Video width and height.

    thumb (``str`` | ``BinaryIO``, *optional*):
        Thumbnail of the video sent.
        The thumbnail should be in JPEG format and less than 200 KB in size.
        A thumbnail's width and height should not exceed 320 pixels.
        Thumbnails can't be reused and can be only uploaded as a new file.

    disable_notification (``bool``, *optional*):
        Sends the message silently.
        Users will receive a notification with no sound.

    reply_to_message_id (``int``, *optional*):
        If the message is a reply, ID of the original message

    business_connection_id (``str``, *optional*):
        Business connection identifier.
        for business bots only.

    reply_in_chat_id: Union[int, str] = None,
        Unique identifier of target chat.
        for reply message in another chat.

    quote_text (``str``, *optional*):
        Text to quote.
        for reply_to_message only.

    quote_entities (List of :obj:`~pyrogram.types.MessageEntity`, *optional*):
        List of special entities that appear in quote_text, which can be specified instead of *parse_mode*.
        for reply_to_message only.

    protect_content (``bool``, *optional*):
        Protects the contents of the sent message from forwarding and saving.

    allow_paid_broadcast (``bool``, *optional*):
        Pass True to allow the message to ignore regular broadcast limits for a small fee; for bots

    message_effect_id (``int`` ``64-bit``, *optional*):
        Unique identifier of the message effect to be added to the message; for private chats only.

    ttl_seconds (``int``, *optional*):
        Self-Destruct Timer.
        If you set a timer, the video note will self-destruct in *ttl_seconds*
        seconds after it was viewed.

    reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardRemove` | :obj:`~pyrogram.types.ForceReply`, *optional*):
        Additional interface options. An object for an inline keyboard, custom reply keyboard,
        instructions to remove reply keyboard or to force a reply from the user.

    progress (``Callable``, *optional*):
        Pass a callback function to view the file transmission progress.
        The function must take *(current, total)* as positional arguments (look at Other Parameters below for a
        detailed description) and will be called back each time a new file chunk has been successfully
        transmitted.

    progress_args (``tuple``, *optional*):
        Extra custom arguments for the progress callback function.
        You can pass anything you need to be available in the progress callback scope; for example, a Message
        object or a Client instance in order to edit the message with the updated progress status.

Other Parameters:
    current (``int``):
        The amount of bytes transmitted so far.

    total (``int``):
        The total size of the file.

    *args (``tuple``, *optional*):
        Extra custom arguments as defined in the ``progress_args`` parameter.
        You can either keep ``*args`` or add every single extra argument in your function signature.

Returns:
    On success, the sent :obj:`~pyrogram.types.Message` is returned.
    In case the upload is deliberately stopped with :meth:`~pyrogram.Client.stop_transmission`, None is returned
    instead.

Raises:
    RPCError: In case of a Telegram RPC error.
```

###### `async def reply_voice(self, voice: Union[str, BinaryIO], quote: bool = None, caption: str = '', parse_mode: Optional['enums.ParseMode'] = None, caption_entities: List['types.MessageEntity'] = None, duration: int = 0, disable_notification: bool = None, reply_to_message_id: int = None, business_connection_id: str = None, reply_in_chat_id: Union[int, str] = None, quote_text: str = None, quote_entities: List['types.MessageEntity'] = None, allow_paid_broadcast: bool = None, message_effect_id: int = None, reply_markup: Union['types.InlineKeyboardMarkup', 'types.ReplyKeyboardMarkup', 'types.ReplyKeyboardRemove', 'types.ForceReply'] = None, progress: Callable = None, progress_args: tuple = ()) -> 'Message'`

```text
Bound method *reply_voice* of :obj:`~pyrogram.types.Message`.

Use as a shortcut for:

.. code-block:: python

    await client.send_voice(
        chat_id=message.chat.id,
        voice=voice
    )

Example:
    .. code-block:: python

        await message.reply_voice(voice)

Parameters:
    voice (``str``):
        Audio file to send.
        Pass a file_id as string to send an audio that exists on the Telegram servers,
        pass an HTTP URL as a string for Telegram to get an audio from the Internet, or
        pass a file path as string to upload a new audio that exists on your local machine.

    quote (``bool``, *optional*):
        If ``True``, the message will be sent as a reply to this message.
        If *reply_to_message_id* is passed, this parameter will be ignored.
        Defaults to ``True`` in group chats and ``False`` in private chats.

    caption (``str``, *optional*):
        Voice message caption, 0-1024 characters.

    parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
        By default, texts are parsed using both Markdown and HTML styles.
        You can combine both syntaxes together.

    caption_entities (List of :obj:`~pyrogram.types.MessageEntity`):
        List of special entities that appear in the caption, which can be specified instead of *parse_mode*.

    duration (``int``, *optional*):
        Duration of the voice message in seconds.

    disable_notification (``bool``, *optional*):
        Sends the message silently.
        Users will receive a notification with no sound.

    reply_to_message_id (``int``, *optional*):
        If the message is a reply, ID of the original message

    business_connection_id (``str``, *optional*):
        Business connection identifier.
        for business bots only.

    reply_in_chat_id: Union[int, str] = None,
        Unique identifier of target chat.
        for reply message in another chat.

    quote_text (``str``, *optional*):
        Text to quote.
        for reply_to_message only.

    quote_entities (List of :obj:`~pyrogram.types.MessageEntity`, *optional*):
        List of special entities that appear in quote_text, which can be specified instead of *parse_mode*.
        for reply_to_message only.

    allow_paid_broadcast (``bool``, *optional*):
        Pass True to allow the message to ignore regular broadcast limits for a small fee; for bots

    message_effect_id (``int`` ``64-bit``, *optional*):
        Unique identifier of the message effect to be added to the message; for private chats only.

    reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardRemove` | :obj:`~pyrogram.types.ForceReply`, *optional*):
        Additional interface options. An object for an inline keyboard, custom reply keyboard,
        instructions to remove reply keyboard or to force a reply from the user.

    progress (``Callable``, *optional*):
        Pass a callback function to view the file transmission progress.
        The function must take *(current, total)* as positional arguments (look at Other Parameters below for a
        detailed description) and will be called back each time a new file chunk has been successfully
        transmitted.

    progress_args (``tuple``, *optional*):
        Extra custom arguments for the progress callback function.
        You can pass anything you need to be available in the progress callback scope; for example, a Message
        object or a Client instance in order to edit the message with the updated progress status.

Other Parameters:
    current (``int``):
        The amount of bytes transmitted so far.

    total (``int``):
        The total size of the file.

    *args (``tuple``, *optional*):
        Extra custom arguments as defined in the ``progress_args`` parameter.
        You can either keep ``*args`` or add every single extra argument in your function signature.

Returns:
    On success, the sent :obj:`~pyrogram.types.Message` is returned.
    In case the upload is deliberately stopped with :meth:`~pyrogram.Client.stop_transmission`, None is returned
    instead.

Raises:
    RPCError: In case of a Telegram RPC error.
```

###### `async def reply_web_page(self, url: str, text: str = '', quote: bool = None, parse_mode: Optional['enums.ParseMode'] = None, entities: List['types.MessageEntity'] = None, large_media: bool = None, invert_media: bool = None, disable_notification: bool = None, reply_to_message_id: int = None, business_connection_id: str = None, reply_in_chat_id: Union[int, str] = None, quote_text: str = None, quote_entities: List['types.MessageEntity'] = None, schedule_date: datetime = None, protect_content: bool = None, allow_paid_broadcast: bool = None, message_effect_id: int = None, reply_markup = None) -> 'Message'`

```text
Bound method *reply_web_page* of :obj:`~pyrogram.types.Message`.

Use as a shortcut for:

.. code-block:: python

    await client.send_web_page(
        chat_id=message.chat.id,
        url="https://github.com/Mayuri-Chan/pyrofork",
        reply_to_message_id=message.id
    )

Example:
    .. code-block:: python

        await message.reply_web_page("https://github.com/Mayuri-Chan/pyrofork")

Parameters:
    url (``str``):
        Link that will be previewed.

    text (``str``):
        Text of the message to be sent.

    quote (``bool``, *optional*):
        If ``True``, the message will be sent as a reply to this message.
        If *reply_to_message_id* is passed, this parameter will be ignored.
        Defaults to ``True`` in group chats and ``False`` in private chats.

    parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
        By default, texts are parsed using both Markdown and HTML styles.
        You can combine both syntaxes together.

    entities (List of :obj:`~pyrogram.types.MessageEntity`):
        List of special entities that appear in message text, which can be specified instead of *parse_mode*.

    large_media (``bool``, *optional*):
        Make web page preview image larger.

    invert_media (``bool``, *optional*):
        Move web page preview to above the message.

    disable_notification (``bool``, *optional*):
        Sends the message silently.
        Users will receive a notification with no sound.

    reply_to_message_id (``int``, *optional*):
        If the message is a reply, ID of the original message.

    business_connection_id (``str``, *optional*):
        Business connection identifier.
        for business bots only.

    reply_in_chat_id: Union[int, str] = None,
        Unique identifier of target chat.
        for reply message in another chat.

    quote_text (``str``, *optional*):
        Text to quote.
        for reply_to_message only.

    quote_entities (List of :obj:`~pyrogram.types.MessageEntity`, *optional*):
        List of special entities that appear in quote_text, which can be specified instead of *parse_mode*.
        for reply_to_message only.

    schedule_date (:py:obj:`~datetime.datetime`, *optional*):
        Date when the message will be automatically sent.

    protect_content (``bool``, *optional*):
        Protects the contents of the sent message from forwarding and saving.

    allow_paid_broadcast (``bool``, *optional*):
        Pass True to allow the message to ignore regular broadcast limits for a small fee; for bots

    message_effect_id (``int`` ``64-bit``, *optional*):
        Unique identifier of the message effect to be added to the message; for private chats only.

    reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardRemove` | :obj:`~pyrogram.types.ForceReply`, *optional*):
        Additional interface options. An object for an inline keyboard, custom reply keyboard,
        instructions to remove reply keyboard or to force a reply from the user.

Returns:
    On success, the sent Message is returned.

Raises:
    RPCError: In case of a Telegram RPC error.
```

###### `async def edit_text(self, text: str, parse_mode: Optional['enums.ParseMode'] = None, entities: List['types.MessageEntity'] = None, disable_web_page_preview: bool = None, invert_media: bool = None, reply_markup: 'types.InlineKeyboardMarkup' = None, business_connection_id: str = None) -> 'Message'`

```text
Bound method *edit_text* of :obj:`~pyrogram.types.Message`.

An alias exists as *edit*.

Use as a shortcut for:

.. code-block:: python

    await client.edit_message_text(
        chat_id=message.chat.id,
        message_id=message.id,
        text="hello"
    )

Example:
    .. code-block:: python

        await message.edit_text("hello")

Parameters:
    text (``str``):
        New text of the message.

    parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
        By default, texts are parsed using both Markdown and HTML styles.
        You can combine both syntaxes together.

    entities (List of :obj:`~pyrogram.types.MessageEntity`):
        List of special entities that appear in message text, which can be specified instead of *parse_mode*.

    disable_web_page_preview (``bool``, *optional*):
        Disables link previews for links in this message.

    invert_media (``bool``, *optional*):
        Inverts the position of the media and caption.

    reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup`, *optional*):
        An InlineKeyboardMarkup object.

    business_connection_id (``str``, *optional*):
        Unique identifier of the business connection.
        for business bots only.

Returns:
    On success, the edited :obj:`~pyrogram.types.Message` is returned.

Raises:
    RPCError: In case of a Telegram RPC error.
```

###### `async def edit_caption(self, caption: str, parse_mode: Optional['enums.ParseMode'] = None, caption_entities: List['types.MessageEntity'] = None, invert_media: bool = None, reply_markup: 'types.InlineKeyboardMarkup' = None, business_connection_id: str = None) -> 'Message'`

```text
Bound method *edit_caption* of :obj:`~pyrogram.types.Message`.

Use as a shortcut for:

.. code-block:: python

    await client.edit_message_caption(
        chat_id=message.chat.id,
        message_id=message.id,
        caption="hello"
    )

Example:
    .. code-block:: python

        await message.edit_caption("hello")

Parameters:
    caption (``str``):
        New caption of the message.

    parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
        By default, texts are parsed using both Markdown and HTML styles.
        You can combine both syntaxes together.

    caption_entities (List of :obj:`~pyrogram.types.MessageEntity`):
        List of special entities that appear in the caption, which can be specified instead of *parse_mode*.

    invert_media (``bool``, *optional*):
        Inverts the position of the media and caption.

    reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup`, *optional*):
        An InlineKeyboardMarkup object.

    business_connection_id (``str``, *optional*):
        Unique identifier of the business connection.
        for business bots only.

Returns:
    On success, the edited :obj:`~pyrogram.types.Message` is returned.

Raises:
    RPCError: In case of a Telegram RPC error.
```

###### `async def edit_media(self, media: 'types.InputMedia', invert_media: bool = None, reply_markup: 'types.InlineKeyboardMarkup' = None, business_connection_id: str = None) -> 'Message'`

```text
Bound method *edit_media* of :obj:`~pyrogram.types.Message`.

Use as a shortcut for:

.. code-block:: python

    await client.edit_message_media(
        chat_id=message.chat.id,
        message_id=message.id,
        media=media
    )

Example:
    .. code-block:: python

        await message.edit_media(media)

Parameters:
    media (:obj:`~pyrogram.types.InputMedia`):
        One of the InputMedia objects describing an animation, audio, document, photo or video.

    invert_media (``bool``, *optional*):
        Inverts the position of the media and caption.

    reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup`, *optional*):
        An InlineKeyboardMarkup object.

    business_connection_id (``str``, *optional*):
        Unique identifier of the business connection.
        for business bots only.

Returns:
    On success, the edited :obj:`~pyrogram.types.Message` is returned.

Raises:
    RPCError: In case of a Telegram RPC error.
```

###### `async def edit_reply_markup(self, reply_markup: 'types.InlineKeyboardMarkup' = None, business_connection_id: str = None) -> 'Message'`

```text
Bound method *edit_reply_markup* of :obj:`~pyrogram.types.Message`.

Use as a shortcut for:

.. code-block:: python

    await client.edit_message_reply_markup(
        chat_id=message.chat.id,
        message_id=message.id,
        reply_markup=inline_reply_markup
    )

Example:
    .. code-block:: python

        await message.edit_reply_markup(inline_reply_markup)

Parameters:
    reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup`):
        An InlineKeyboardMarkup object.

    business_connection_id (``str``, *optional*):
        Unique identifier of the business connection.
        for business bots only.

Returns:
    On success, if edited message is sent by the bot, the edited
    :obj:`~pyrogram.types.Message` is returned, otherwise True is returned.

Raises:
    RPCError: In case of a Telegram RPC error.
```

###### `async def forward(self, chat_id: Union[int, str], message_thread_id: int = None, disable_notification: bool = None, schedule_date: datetime = None, protect_content: bool = None, allow_paid_broadcast: bool = None, drop_author: bool = None, remove_caption: bool = None, new_video_start_timestamp: int = None) -> Union['types.Message', List['types.Message']]`

```text
Bound method *forward* of :obj:`~pyrogram.types.Message`.

Use as a shortcut for:

.. code-block:: python

    await client.forward_messages(
        chat_id=chat_id,
        from_chat_id=message.chat.id,
        message_ids=message.id
    )

Example:
    .. code-block:: python

        await message.forward(chat_id)

Parameters:
    chat_id (``int`` | ``str``):
        Unique identifier (int) or username (str) of the target chat.
        For your personal cloud (Saved Messages) you can simply use "me" or "self".
        For a contact that exists in your Telegram address book you can use his phone number (str).
        You can also use chat public link in form of *t.me/<username>* (str).

    message_thread_id (``int``, *optional*):
        Unique identifier of a message thread to which the message belongs; for supergroups only

    disable_notification (``bool``, *optional*):
        Sends the message silently.
        Users will receive a notification with no sound.

    schedule_date (:py:obj:`~datetime.datetime`, *optional*):
        Date when the message will be automatically sent.

    protect_content (``bool``, *optional*):
        Protects the contents of the sent message from forwarding and saving.

    allow_paid_broadcast (``bool``, *optional*):
        Pass True to allow the message to ignore regular broadcast limits for a small fee; for bots

    drop_author (``bool``, *optional*):
        Forwards messages without quoting the original author.

    remove_caption (``bool``, *optional*):
        Pass True to remove media captions of message copies.

    new_video_start_timestamp (``int``, *optional*):
        The new video start timestamp. Pass time to replace video start timestamp in the forwarded message.

Returns:
    On success, the forwarded Message is returned.

Raises:
    RPCError: In case of a Telegram RPC error.
```

###### `async def copy(self, chat_id: Union[int, str], caption: str = None, parse_mode: Optional['enums.ParseMode'] = None, caption_entities: List['types.MessageEntity'] = None, has_spoiler: bool = None, disable_notification: bool = None, message_thread_id: int = None, quote_text: str = None, quote_entities: List['types.MessageEntity'] = None, reply_to_message_id: int = None, reply_to_chat_id: int = None, schedule_date: datetime = None, protect_content: bool = None, allow_paid_broadcast: bool = None, invert_media: bool = None, reply_markup: Union['types.InlineKeyboardMarkup', 'types.ReplyKeyboardMarkup', 'types.ReplyKeyboardRemove', 'types.ForceReply'] = object) -> Union['types.Message', List['types.Message']]`

```text
Bound method *copy* of :obj:`~pyrogram.types.Message`.

Use as a shortcut for:

.. code-block:: python

    await client.copy_message(
        chat_id=chat_id,
        from_chat_id=message.chat.id,
        message_id=message.id
    )

Example:
    .. code-block:: python

        await message.copy(chat_id)

Parameters:
    chat_id (``int`` | ``str``):
        Unique identifier (int) or username (str) of the target chat.
        For your personal cloud (Saved Messages) you can simply use "me" or "self".
        For a contact that exists in your Telegram address book you can use his phone number (str).
        You can also use chat public link in form of *t.me/<username>* (str).

    caption (``string``, *optional*):
        New caption for media, 0-1024 characters after entities parsing.
        If not specified, the original caption is kept.
        Pass "" (empty string) to remove the caption.

    parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
        By default, texts are parsed using both Markdown and HTML styles.
        You can combine both syntaxes together.

    caption_entities (List of :obj:`~pyrogram.types.MessageEntity`):
        List of special entities that appear in the new caption, which can be specified instead of *parse_mode*.

    has_spoiler (``bool``, *optional*):
        Pass True if the photo needs to be covered with a spoiler animation.

    disable_notification (``bool``, *optional*):
        Sends the message silently.
        Users will receive a notification with no sound.

    message_thread_id (``int``, *optional*):
        Unique identifier for the target message thread (topic) of the forum.
        for forum supergroups only.

    quote_text (``str``, *optional*):
        Text to quote.
        for reply_to_message only.

    quote_entities (List of :obj:`~pyrogram.types.MessageEntity`, *optional*):
        List of special entities that appear in quote_text, which can be specified instead of *parse_mode*.
        for reply_to_message only.

    reply_to_message_id (``int``, *optional*):
        If the message is a reply, ID of the original message.

    reply_to_chat_id (``int``, *optional*):
        Unique identifier for the origin chat.
        for reply to message from another chat.
        You can also use chat public link in form of *t.me/<username>* (str).

    schedule_date (:py:obj:`~datetime.datetime`, *optional*):
        Date when the message will be automatically sent.

    protect_content (``bool``, *optional*):
        Protects the contents of the sent message from forwarding and saving.

    allow_paid_broadcast (``bool``, *optional*):
        Pass True to allow the message to ignore regular broadcast limits for a small fee; for bots

    invert_media (``bool``, *optional*):
        Inverts the position of the media and caption.

    reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardRemove` | :obj:`~pyrogram.types.ForceReply`, *optional*):
        Additional interface options. An object for an inline keyboard, custom reply keyboard,
        instructions to remove reply keyboard or to force a reply from the user.
        If not specified, the original reply markup is kept.
        Pass None to remove the reply markup.

Returns:
    :obj:`~pyrogram.types.Message`: On success, the copied message is returned.

Raises:
    RPCError: In case of a Telegram RPC error.
```

###### `async def delete(self, revoke: bool = True)`

```text
Bound method *delete* of :obj:`~pyrogram.types.Message`.

Use as a shortcut for:

.. code-block:: python

    await client.delete_messages(
        chat_id=chat_id,
        message_ids=message.id
    )

Example:
    .. code-block:: python

        await message.delete()

Parameters:
    revoke (``bool``, *optional*):
        Deletes messages on both parts.
        This is only for private cloud chats and normal groups, messages on
        channels and supergroups are always revoked (i.e.: deleted for everyone).
        Defaults to True.

Returns:
    True on success, False otherwise.

Raises:
    RPCError: In case of a Telegram RPC error.
```

###### `async def click(self, x: Union[int, str] = 0, y: int = None, quote: bool = None, timeout: int = 10, request_write_access: bool = True, password: str = None)`

```text
Bound method *click* of :obj:`~pyrogram.types.Message`.

Use as a shortcut for clicking a button attached to the message instead of:

- Clicking inline buttons:

.. code-block:: python

    await client.request_callback_answer(
        chat_id=message.chat.id,
        message_id=message.id,
        callback_data=message.reply_markup[i][j].callback_data
    )

- Clicking normal buttons:

.. code-block:: python

    await client.send_message(
        chat_id=message.chat.id,
        text=message.reply_markup[i][j].text
    )

Example:
    This method can be used in three different ways:

    1.  Pass one integer argument only (e.g.: ``.click(2)``, to click a button at index 2).
        Buttons are counted left to right, starting from the top.

    2.  Pass two integer arguments (e.g.: ``.click(1, 0)``, to click a button at position (1, 0)).
        The origin (0, 0) is top-left.

    3.  Pass one string argument only (e.g.: ``.click("Settings")``, to click a button by using its label).
        Only the first matching button will be pressed.

Parameters:
    x (``int`` | ``str``):
        Used as integer index, integer abscissa (in pair with y) or as string label.
        Defaults to 0 (first button).

    y (``int``, *optional*):
        Used as ordinate only (in pair with x).

    quote (``bool``, *optional*):
        Useful for normal buttons only, where pressing it will result in a new message sent.
        If ``True``, the message will be sent as a reply to this message.
        Defaults to ``True`` in group chats and ``False`` in private chats.

    timeout (``int``, *optional*):
        Timeout in seconds.

    request_write_access (``bool``, *optional*):
        Only used in case of :obj:`~pyrogram.types.LoginUrl` button.
        True, if the bot can send messages to the user.
        Defaults to ``True``.

    password (``str``, *optional*):
        When clicking certain buttons (such as BotFather's confirmation button to transfer ownership), if your account has 2FA enabled, you need to provide your account's password.
        The 2-step verification password for the current user. Only applicable, if the :obj:`~pyrogram.types.InlineKeyboardButton` contains ``requires_password``.

Returns:
    -   The result of :meth:`~pyrogram.Client.request_callback_answer` in case of inline callback button clicks.
    -   The result of :meth:`~Message.reply()` in case of normal button clicks.
    -   A string in case the inline button is a URL, a *switch_inline_query* or a
        *switch_inline_query_current_chat* button.
    -   A string URL with the user details, in case of a WebApp button.
    -   A :obj:`~pyrogram.types.Chat` object in case of a ``KeyboardButtonUserProfile`` button.

Raises:
    RPCError: In case of a Telegram RPC error.
    ValueError: In case the provided index or position is out of range or the button label was not found.
    TimeoutError: In case, after clicking an inline button, the bot fails to answer within the timeout.
```

###### `async def react(self, emoji: str = '', big: bool = False, add_to_recent: bool = True) -> 'types.MessageReactions'`

```text
Bound method *react* of :obj:`~pyrogram.types.Message`.

Use as a shortcut for:

.. code-block:: python

    await client.send_reaction(
        chat_id=chat_id,
        message_id=message.id,
        emoji="🔥"
    )

Example:
    .. code-block:: python

        await message.react(emoji="🔥")

Parameters:
    emoji (``str``, *optional*):
        Reaction emoji.
        Pass "" as emoji (default) to retract the reaction.

    big (``bool``, *optional*):
        Pass True to show a bigger and longer reaction.
        Defaults to False.

    add_to_recent (``bool``, *optional*):
        Pass True if the reaction should appear in the recently used reactions.
        This option is applicable only for users.

Returns:
    :obj: :obj:`~pyrogram.types.MessageReactions`: On success, True is returned.

Raises:
    RPCError: In case of a Telegram RPC error.
```

###### `async def retract_vote(self) -> 'types.Poll'`

```text
Bound method *retract_vote* of :obj:`~pyrogram.types.Message`.

Use as a shortcut for:

.. code-block:: python

    client.retract_vote(
        chat_id=message.chat.id,
        message_id=message_id,
    )

Example:
    .. code-block:: python

        message.retract_vote()

Returns:
    :obj:`~pyrogram.types.Poll`: On success, the poll with the retracted vote is returned.

Raises:
    RPCError: In case of a Telegram RPC error.
```

###### `async def download(self, file_name: str = '', in_memory: bool = False, block: bool = True, progress: Callable = None, progress_args: tuple = ()) -> str`

```text
Bound method *download* of :obj:`~pyrogram.types.Message`.

Use as a shortcut for:

.. code-block:: python

    await client.download_media(message)

Example:
    .. code-block:: python

        await message.download()

Parameters:
    file_name (``str``, *optional*):
        A custom *file_name* to be used instead of the one provided by Telegram.
        By default, all files are downloaded in the *downloads* folder in your working directory.
        You can also specify a path for downloading files in a custom location: paths that end with "/"
        are considered directories. All non-existent folders will be created automatically.

    in_memory (``bool``, *optional*):
        Pass True to download the media in-memory.
        A binary file-like object with its attribute ".name" set will be returned.
        Defaults to False.

    block (``bool``, *optional*):
        Blocks the code execution until the file has been downloaded.
        Defaults to True.

    progress (``Callable``, *optional*):
        Pass a callback function to view the file transmission progress.
        The function must take *(current, total)* as positional arguments (look at Other Parameters below for a
        detailed description) and will be called back each time a new file chunk has been successfully
        transmitted.

    progress_args (``tuple``, *optional*):
        Extra custom arguments for the progress callback function.
        You can pass anything you need to be available in the progress callback scope; for example, a Message
        object or a Client instance in order to edit the message with the updated progress status.

Other Parameters:
    current (``int``):
        The amount of bytes transmitted so far.

    total (``int``):
        The total size of the file.

    *args (``tuple``, *optional*):
        Extra custom arguments as defined in the ``progress_args`` parameter.
        You can either keep ``*args`` or add every single extra argument in your function signature.

Returns:
    On success, the absolute path of the downloaded file as string is returned, None otherwise.

Raises:
    RPCError: In case of a Telegram RPC error.
    ``ValueError``: If the message doesn't contain any downloadable media
```

###### `async def vote(self, option: int) -> 'types.Poll'`

```text
Bound method *vote* of :obj:`~pyrogram.types.Message`.

Use as a shortcut for:

.. code-block:: python

    client.vote_poll(
        chat_id=message.chat.id,
        message_id=message.id,
        option=1
    )

Example:
    .. code-block:: python

        message.vote(6)

Parameters:
    option (``int``):
        Index of the poll option you want to vote for (0 to 9).

Returns:
    :obj:`~pyrogram.types.Poll`: On success, the poll with the chosen option is returned.

Raises:
    RPCError: In case of a Telegram RPC error.
```

###### `async def pin(self, disable_notification: bool = False, both_sides: bool = False) -> 'types.Message'`

```text
Bound method *pin* of :obj:`~pyrogram.types.Message`.

Use as a shortcut for:

.. code-block:: python

    await client.pin_chat_message(
        chat_id=message.chat.id,
        message_id=message_id
    )

Example:
    .. code-block:: python

        await message.pin()

Parameters:
    disable_notification (``bool``):
        Pass True, if it is not necessary to send a notification to all chat members about the new pinned
        message. Notifications are always disabled in channels.

    both_sides (``bool``, *optional*):
        Pass True to pin the message for both sides (you and recipient).
        Applicable to private chats only. Defaults to False.

Returns:
    :obj:`~pyrogram.types.Message`: On success, the service message is returned.

Raises:
    RPCError: In case of a Telegram RPC error.
```

###### `async def unpin(self) -> bool`

```text
Bound method *unpin* of :obj:`~pyrogram.types.Message`.

Use as a shortcut for:

.. code-block:: python

    await client.unpin_chat_message(
        chat_id=message.chat.id,
        message_id=message_id
    )

Example:
    .. code-block:: python

        await message.unpin()

Returns:
    True on success.

Raises:
    RPCError: In case of a Telegram RPC error.
```

###### `async def ask(self, text: str, quote: bool = None, parse_mode: Optional['enums.ParseMode'] = None, entities: List['types.MessageEntity'] = None, disable_web_page_preview: bool = None, disable_notification: bool = None, reply_to_message_id: int = None, reply_markup = None, filters = None, timeout: int = None) -> 'Message'`

```text
Bound method *ask* of :obj:`~pyrogram.types.Message`.

Use as a shortcut for:

.. code-block:: python

    client.send_message(chat_id, "What is your name?")

    client.wait_for_message(chat_id)

Parameters:
    text (``str``):
        Text of the message to be sent.

    quote (``bool``, *optional*):
        If ``True``, the message will be sent as a reply to this message.
        If *reply_to_message_id* is passed, this parameter will be ignored.
        Defaults to ``True`` in group chats and ``False`` in private chats.

    parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
        By default, texts are parsed using both Markdown and HTML styles.
        You can combine both syntaxes together.
        Pass "markdown" or "md" to enable Markdown-style parsing only.
        Pass "html" to enable HTML-style parsing only.
        Pass None to completely disable style parsing.

    entities (List of :obj:`~pyrogram.types.MessageEntity`):
        List of special entities that appear in message text, which can be specified instead of *parse_mode*.

    disable_web_page_preview (``bool``, *optional*):
        Disables link previews for links in this message.

    disable_notification (``bool``, *optional*):
        Sends the message silently.
        Users will receive a notification with no sound.

    reply_to_message_id (``int``, *optional*):
        If the message is a reply, ID of the original message.

    reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardRemove` | :obj:`~pyrogram.types.ForceReply`, *optional*):
        Additional interface options. An object for an inline keyboard, custom reply keyboard,
        instructions to remove reply keyboard or to force a reply from the user.

    filters (:obj:`Filters`):
        Pass one or more filters to allow only a subset of callback queries to be passed
        in your callback function.

    timeout (``int``, *optional*):
        Timeout in seconds.

Example:
    .. code-block:: python

        message.ask("What is your name?")

Returns:
    :obj:`~pyrogram.types.Message`: On success, the reply message is returned.

Raises:
    RPCError: In case of a Telegram RPC error.
    asyncio.TimeoutError: In case reply not received within the timeout.
```

###### `async def transcribe(self) -> 'types.TranscribeAudio'`

```text
Bound method *transcribe* of :obj:`~pyrogram.types.Message`.

Use as a shortcut for:

.. code-block:: python

    await client.transcribe_audio(
        chat_id=message.chat.id,
        message_id=message.id
        )

Example:
    .. code-block:: python

    await message.transcribe()

Returns:
    :obj:`~pyrogram.types.TranscribeAudio`: On success.

Raises:
    RPCError: In case of a Telegram RPC error.
```

###### `async def translate(self, to_language_code: str) -> 'types.TranslatedText'`

```text
Bound method *translate* of :obj:`~pyrogram.types.Message`.

Use as a shortcut for:
    .. code-block:: python

        await client.translate_message_text(
            chat_id=message.chat.id,
            message_ids=message_id,
            to_language_code="en"
        )

Example:
    .. code-block:: python

        await Message.translate("en")

Parameters:
    to_language_code (``str``):
        Language code of the language to which the message is translated.
        Must be one of "af", "sq", "am", "ar", "hy", "az", "eu", "be", "bn", "bs", "bg", "ca", "ceb", "zh-CN", "zh", "zh-Hans", "zh-TW", "zh-Hant", "co", "hr", "cs", "da", "nl", "en", "eo", "et", "fi", "fr", "fy", "gl", "ka", "de", "el", "gu", "ht", "ha", "haw", "he", "iw", "hi", "hmn", "hu", "is", "ig", "id", "in", "ga", "it", "ja", "jv", "kn", "kk", "km", "rw", "ko", "ku", "ky", "lo", "la", "lv", "lt", "lb", "mk", "mg", "ms", "ml", "mt", "mi", "mr", "mn", "my", "ne", "no", "ny", "or", "ps", "fa", "pl", "pt", "pa", "ro", "ru", "sm", "gd", "sr", "st", "sn", "sd", "si", "sk", "sl", "so", "es", "su", "sw", "sv", "tl", "tg", "ta", "tt", "te", "th", "tr", "tk", "uk", "ur", "ug", "uz", "vi", "cy", "xh", "yi", "ji", "yo", "zu".

Returns:
    :obj:`~pyrogram.types.TranslatedText`: The translated result is returned.

Raises:
    RPCError: In case of a Telegram RPC error.
```

---

## File: `types/messages_and_media/message_entity.py`

### Classes

#### `class MessageEntity(Object)`

```text
One special entity in a text message.

For example, hashtags, usernames, URLs, etc.

Parameters:
    type (:obj:`~pyrogram.enums.MessageEntityType`):
        Type of the entity.

    offset (``int``):
        Offset in UTF-16 code units to the start of the entity.

    length (``int``):
        Length of the entity in UTF-16 code units.

    url (``str``, *optional*):
        For :obj:`~pyrogram.enums.MessageEntityType.TEXT_LINK` only, url that will be opened after user taps on the text.

    user (:obj:`~pyrogram.types.User`, *optional*):
        For :obj:`~pyrogram.enums.MessageEntityType.TEXT_MENTION` only, the mentioned user.

    language (``str``, *optional*):
        For "pre" only, the programming language of the entity text.

    custom_emoji_id (``int``, *optional*):
        For :obj:`~pyrogram.enums.MessageEntityType.CUSTOM_EMOJI` only, unique identifier of the custom emoji.
        Use :meth:`~pyrogram.Client.get_custom_emoji_stickers` to get full information about the sticker.

    collapsed (``bool``, *optional*):
        For :obj:`~pyrogram.enums.MessageEntityType.BLOCKQUOTE` only, whether the blockquote expandable.
```

##### Methods

###### `def __init__(self, *, client: 'pyrogram.Client' = None, type: 'enums.MessageEntityType', offset: int, length: int, url: str = None, user: 'types.User' = None, language: str = None, custom_emoji_id: int = None, collapsed: bool = None)`

_No docstring._

###### `def _parse(client, entity: 'raw.base.MessageEntity', users: Dict[int, 'raw.types.User'] = None) -> Optional['MessageEntity']`

_No docstring._

###### `async def write(self)`

_No docstring._

---

## File: `types/messages_and_media/message_origin.py`

### Classes

#### `class MessageOrigin(Object)`

```text
This object describes the origin of a message.

It can be one of:

- :obj:`~pyrogram.types.MessageOriginChannel`
- :obj:`~pyrogram.types.MessageOriginChat`
- :obj:`~pyrogram.types.MessageOriginHiddenUser`
- :obj:`~pyrogram.types.MessageOriginImport`
- :obj:`~pyrogram.types.MessageOriginUser`
```

##### Methods

###### `def __init__(self, type: 'enums.MessageOriginType', date: Optional[datetime] = None)`

_No docstring._

###### `def _parse(client: 'pyrogram.Client', fwd_from: 'raw.types.MessageFwdHeader', users: Dict[int, 'raw.base.User'], chats: Dict[int, 'raw.base.Chat']) -> Optional['MessageOrigin']`

_No docstring._

---

## File: `types/messages_and_media/message_origin_channel.py`

### Classes

#### `class MessageOriginChannel(MessageOrigin)`

```text
The message was originally sent to a channel chat.

Parameters:
    type (:obj:`~pyrogram.enums.MessageOriginType`):
        Type of the message origin.

    date (:py:obj:`~datetime.datetime`):
        Date the message was sent originally.

    chat (:obj:`~pyrogram.types.Chat`):
        Channel chat to which the message was originally sent.

    message_id (``int``):
        Unique message identifier inside the chat.

    author_signature (``str``, *optional*):
        Signature of the original post author.
```

##### Methods

###### `def __init__(self, *, type: 'enums.MessageOriginType' = enums.MessageOriginType.CHANNEL, date: datetime = None, chat: 'types.Chat' = None, message_id: int = None, author_signature: str = None)`

_No docstring._

---

## File: `types/messages_and_media/message_origin_chat.py`

### Classes

#### `class MessageOriginChat(MessageOrigin)`

```text
The message was originally sent on behalf of a chat to a group chat.

Parameters:
    type (:obj:`~pyrogram.enums.MessageOriginType`):
        Type of the message origin.

    date (:py:obj:`~datetime.datetime`):
        Date the message was sent originally.

    sender_chat (:obj:`~pyrogram.types.Chat`):
        Chat that sent the message originally.

    author_signature (``str``, *optional*):
        For messages originally sent by an anonymous chat administrator, original message author signature.
```

##### Methods

###### `def __init__(self, *, type: 'enums.MessageOriginType' = enums.MessageOriginType.CHAT, date: datetime = None, sender_chat: 'types.Chat' = None, author_signature: str = None)`

_No docstring._

---

## File: `types/messages_and_media/message_origin_hidden_user.py`

### Classes

#### `class MessageOriginHiddenUser(MessageOrigin)`

```text
The message was originally sent by an unknown user.

Parameters:
    type (:obj:`~pyrogram.enums.MessageOriginType`):
        Type of the message origin.

    date (:py:obj:`~datetime.datetime`):
        Date the message was sent originally.

    sender_user_name (``str``):
        Name of the user that sent the message originally.
```

##### Methods

###### `def __init__(self, *, type: 'enums.MessageOriginType' = enums.MessageOriginType.HIDDEN_USER, date: datetime = None, sender_user_name: str = None)`

_No docstring._

---

## File: `types/messages_and_media/message_origin_import.py`

### Classes

#### `class MessageOriginImport(MessageOrigin)`

```text
Contains information about a message imported from a foreign chat service.

Parameters:
    type (:obj:`~pyrogram.enums.MessageOriginType`):
        Type of the message origin.

    date (:py:obj:`~datetime.datetime`):
        Date the message was sent originally.

    sender_user_name (``str``):
        Name of the original sender.
```

##### Methods

###### `def __init__(self, *, date: datetime = None, sender_user_name: str = None)`

_No docstring._

---

## File: `types/messages_and_media/message_origin_user.py`

### Classes

#### `class MessageOriginUser(MessageOrigin)`

```text
The message was originally sent by a known user.

Parameters:
    type (:obj:`~pyrogram.enums.MessageOriginType`):
        Type of the message origin.

    date (:py:obj:`~datetime.datetime`):
        Date the message was sent originally.

    sender_user (:obj:`~pyrogram.types.User`):
        User that sent the message originally.
```

##### Methods

###### `def __init__(self, *, type: 'enums.MessageOriginType' = enums.MessageOriginType.USER, date: datetime = None, sender_user: 'types.User' = None)`

_No docstring._

---

## File: `types/messages_and_media/message_reaction_count_updated.py`

### Classes

#### `class MessageReactionCountUpdated(Object, Update)`

```text
Reactions to a message with anonymous reactions were changed.

These updates are heavy and their changes may be delayed by a few minutes.

Parameters:
    chat (:obj:`~pyrogram.types.Chat`):
        The chat containing the message the user reacted to

    message_id (``int``):
        Unique identifier of the message inside the chat

    date (:py:obj:`~datetime.datetime`):
        Date of change of the reaction

    reactions (:obj:`~pyrogram.types.Reaction`):
        List of reactions that are present on the message
```

##### Methods

###### `def __init__(self, *, client: 'pyrogram.Client' = None, chat: 'types.Chat', message_id: int, date: datetime, reactions: List['types.Reaction'])`

_No docstring._

###### `def _parse(client: 'pyrogram.Client', update: 'raw.types.UpdateBotMessageReactions', users: Dict[int, 'raw.types.User'], chats: Dict[int, 'raw.types.Chat']) -> 'MessageReactionCountUpdated'`

_No docstring._

---

## File: `types/messages_and_media/message_reaction_updated.py`

### Classes

#### `class MessageReactionUpdated(Object, Update)`

```text
This object represents a change of a reaction on a message performed by a user.
A reaction to a message was changed by a user.
The update isn't received for reactions set by bots.

These updates are heavy and their changes may be delayed by a few minutes.

Parameters:
    id (``int``):
        Unique identifier of the message inside the chat

    chat (:obj:`~pyrogram.types.Chat`):
        The chat containing the message the user reacted to

    from_user (:obj:`~pyrogram.types.User`, *optional*):
        The user that changed the reaction, if the user isn't anonymous

    actor_chat (:obj:`~pyrogram.types.Chat`, *optional*):
        The chat on behalf of which the reaction was changed, if the user is anonymous

    date (:py:obj:`~datetime.datetime`):
        Date of change of the reaction

    old_reaction (:obj:`~pyrogram.types.Reaction`):
        Previous list of reaction types that were set by the user

    new_reaction (:obj:`~pyrogram.types.Reaction`):
        New list of reaction types that have been set by the user
```

##### Methods

###### `def __init__(self, *, client: 'pyrogram.Client' = None, id: int, from_user: 'types.User', actor_chat: 'types.Chat', date: datetime, chat: 'types.Chat', old_reaction: List['types.Reaction'], new_reaction: List['types.Reaction'])`

_No docstring._

###### `def _parse(client: 'pyrogram.Client', update: 'raw.types.UpdateBotMessageReaction', users: Dict[int, 'raw.types.User'], chats: Dict[int, 'raw.types.Chat']) -> 'MessageReactionUpdated'`

_No docstring._

---

## File: `types/messages_and_media/message_reactions.py`

### Classes

#### `class MessageReactions(Object)`

```text
Contains information about a message reactions.

Parameters:
    reactions (List of :obj:`~pyrogram.types.Reaction`):
        Reactions list.

    top_reactors (List of :obj:`~pyrogram.types.MessageReactor`):
        Top reactors.
```

##### Methods

###### `def __init__(self, *, client: 'pyrogram.Client' = None, reactions: Optional[List['types.Reaction']] = None, top_reactors: Optional[List['types.MessageReactor']] = None)`

_No docstring._

###### `def _parse(client: 'pyrogram.Client', message_reactions: Optional['raw.base.MessageReactions'] = None, users: Optional[Dict[int, 'raw.types.User']] = None, chats: Dict[int, 'raw.types.Chat'] = None) -> Optional['MessageReactions']`

_No docstring._

---

## File: `types/messages_and_media/message_reactor.py`

### Classes

#### `class MessageReactor(Object)`

```text
Contains information about a message reactor.

Parameters:
    amount (``int``):
        Stars amount.

    is_top (``bool``, *optional*):
        True, if reactor is top.

    is_my (``bool``, *optional*):
        True, if the reaction is mine.

    is_anonymous (``bool``, *optional*):
        True, if reactor is anonymous.

    from_user (:obj:`~pyrogram.types.User`, *optional*):
        Information about the reactor.

    sender_chat (:obj:`~pyrogram.types.Chat`, *optional*):
        Information about the sender chat.
```

##### Methods

###### `def __init__(self, *, client: 'pyrogram.Client' = None, amount: int, is_top: bool = None, is_my: bool = None, is_anonymous: bool = None, from_user: 'types.User' = None, sender_chat: 'types.Chat' = None)`

_No docstring._

###### `def _parse(client: 'pyrogram.Client', message_reactor: Optional['raw.base.MessageReactor'] = None, users: Dict[int, 'raw.types.User'] = None, chats: Dict[int, 'raw.types.Chat'] = None) -> Optional['MessageReactor']`

_No docstring._

---

## File: `types/messages_and_media/message_story.py`

### Classes

#### `class MessageStory(Object)`

```text
Contains information about a forwarded story.

Parameters:
    from_user (:obj:`~pyrogram.types.User`, *optional*):
        Sender of the story.

    sender_chat (:obj:`~pyrogram.types.Chat`, *optional*):
        Sender of the story. If the story is from channel.

    story_id (``int``):
        Unique story identifier.
```

##### Methods

###### `def __init__(self, *, from_user: 'types.User' = None, sender_chat: 'types.Chat' = None, story_id: int)`

_No docstring._

###### `async def _parse(client: 'pyrogram.Client', message_story: 'raw.types.MessageMediaStory') -> Union['MessageStory', 'types.Story']`

_No docstring._

---

## File: `types/messages_and_media/photo.py`

### Classes

#### `class Photo(Object)`

```text
A Photo.

Parameters:
    file_id (``str``):
        Identifier for this file, which can be used to download or reuse the file.

    file_unique_id (``str``):
        Unique identifier for this file, which is supposed to be the same over time and for different accounts.
        Can't be used to download or reuse the file.

    width (``int``):
        Photo width.

    height (``int``):
        Photo height.

    file_size (``int``):
        File size.

    date (:py:obj:`~datetime.datetime`):
        Date the photo was sent.

    ttl_seconds (``int``, *optional*):
        Time-to-live seconds, for secret photos.

    thumbs (List of :obj:`~pyrogram.types.Thumbnail`, *optional*):
        Available thumbnails of this photo.
```

##### Methods

###### `def __init__(self, *, client: 'pyrogram.Client' = None, file_id: str, file_unique_id: str, width: int, height: int, file_size: int, date: datetime, ttl_seconds: int = None, thumbs: List['types.Thumbnail'] = None)`

_No docstring._

###### `def _parse(client, photo: 'raw.types.Photo', ttl_seconds: int = None) -> 'Photo'`

_No docstring._

---

## File: `types/messages_and_media/poll.py`

### Classes

#### `class Poll(Object, Update)`

```text
A Poll.

Parameters:
    id (``str``):
        Unique poll identifier.

    question (``str``):
        Poll question, 1-255 characters.

    options (List of :obj:`~pyrogram.types.PollOption`):
        List of poll options.

    question_entities (List of :obj:`~pyrogram.types.MessageEntity`, *optional*):
        Special entities like usernames, URLs, bot commands, etc. that appear in the poll question.

    total_voter_count (``int``):
        Total number of users that voted in the poll.

    is_closed (``bool``):
        True, if the poll is closed.

    is_anonymous (``bool``, *optional*):
        True, if the poll is anonymous

    type (:obj:`~pyrogram.enums.PollType`, *optional*):
        Poll type.

    allows_multiple_answers (``bool``, *optional*):
        True, if the poll allows multiple answers.

    chosen_option_id (``int``, *optional*):
        0-based index of the chosen option), None in case of no vote yet.

    correct_option_id (``int``, *optional*):
        0-based identifier of the correct answer option.
        Available only for polls in the quiz mode, which are closed, or was sent (not forwarded) by the bot or to
        the private chat with the bot.

    explanation (``str``, *optional*):
        Text that is shown when a user chooses an incorrect answer or taps on the lamp icon in a quiz-style poll,
        0-200 characters.

    explanation_entities (List of :obj:`~pyrogram.types.MessageEntity`, *optional*):
        Special entities like usernames, URLs, bot commands, etc. that appear in the explanation.

    open_period (``int``, *optional*):
        Amount of time in seconds the poll will be active after creation.

    close_date (:py:obj:`~datetime.datetime`, *optional*):
        Point in time when the poll will be automatically closed.

    recent_voters (List of :obj:`~pyrogram.types.User`, *optional*):
        List of user whos recently vote.
```

##### Methods

###### `def __init__(self, *, client: 'pyrogram.Client' = None, id: str, question: str, options: List['types.PollOption'], question_entities: List['types.MessageEntity'] = None, total_voter_count: int, is_closed: bool, is_anonymous: bool = None, type: 'enums.PollType' = None, allows_multiple_answers: bool = None, chosen_option_id: Optional[int] = None, correct_option_id: Optional[int] = None, explanation: Optional[str] = None, explanation_entities: Optional[List['types.MessageEntity']] = None, open_period: Optional[int] = None, close_date: Optional[datetime] = None, recent_voters: List['types.User'] = None)`

_No docstring._

###### `async def _parse(client, media_poll: Union['raw.types.MessageMediaPoll', 'raw.types.UpdateMessagePoll'], users: List['raw.base.User']) -> 'Poll'`

_No docstring._

###### `async def _parse_update(client, update: 'raw.types.UpdateMessagePoll', users: List['raw.base.User']) -> 'Poll'`

_No docstring._

---

## File: `types/messages_and_media/poll_option.py`

### Classes

#### `class PollOption(Object)`

```text
Contains information about one answer option in a poll.

Parameters:
    text (``str``):
        Option text, 1-100 characters.

    voter_count (``int``, *optional*):
        Number of users that voted for this option.
        Equals to 0 until you vote.

    data (``bytes``, *optional*):
        The data this poll option is holding.

    entities (List of :obj:`~pyrogram.types.MessageEntity`, *optional*):
        Special entities like usernames, URLs, bot commands, etc. that appear in the option text.
```

##### Methods

###### `def __init__(self: 'pyrogram.Client', text: str, voter_count: int = 0, data: bytes = None, entities: Optional[List['pyrogram.types.MessageEntity']] = None)`

_No docstring._

###### `async def write(self, client, i)`

_No docstring._

---

## File: `types/messages_and_media/reaction.py`

### Classes

#### `class Reaction(Object)`

```text
Contains information about a reaction.

Parameters:
    type (``enums.ReactionType``):
        Reaction type.

    emoji (``str``, *optional*):
        Reaction emoji.

    custom_emoji_id (``int``, *optional*):
        Custom emoji id.

    count (``int``, *optional*):
        Reaction count.

    chosen_order (``int``, *optional*):
        Chosen reaction order.
        Available for chosen reactions.
```

##### Methods

###### `def __init__(self, *, client: 'pyrogram.Client' = None, type: 'enums.ReactionType', emoji: Optional[str] = None, custom_emoji_id: Optional[int] = None, count: Optional[int] = None, chosen_order: Optional[int] = None)`

_No docstring._

###### `def _parse(client: 'pyrogram.Client', reaction: 'raw.base.Reaction') -> 'Reaction'`

_No docstring._

###### `def _parse_count(client: 'pyrogram.Client', reaction_count: 'raw.base.ReactionCount') -> 'Reaction'`

_No docstring._

---

## File: `types/messages_and_media/read_participant.py`

### Classes

#### `class ReadParticipant(Object)`

```text
Contains information about a read participant.

Parameters:
    user (:obj:`~pyrogram.types.User`):
        User who read the message.

    date (:py:obj:`~datetime.datetime`):
        Date the message was read.
```

##### Methods

###### `def __init__(self, *, client: 'pyrogram.Client' = None, user_id: 'pyrogram.types.User', date: 'datetime')`

_No docstring._

###### `async def _parse(client, read_participant: 'raw.base.ReadParticipantDate') -> 'ReadParticipant'`

_No docstring._

---

## File: `types/messages_and_media/screenshot_taken.py`

### Classes

#### `class ScreenshotTaken(Object)`

```text
A service message about a screenshot taken.

Currently holds no information.
```

##### Methods

###### `def __init__(self)`

_No docstring._

---

## File: `types/messages_and_media/sticker.py`

### Classes

#### `class Sticker(Object)`

```text
A sticker.

Parameters:
    file_id (``str``):
        Identifier for this file, which can be used to download or reuse the file.

    file_unique_id (``str``):
        Unique identifier for this file, which is supposed to be the same over time and for different accounts.
        Can't be used to download or reuse the file.

    width (``int``):
        Sticker width.

    height (``int``):
        Sticker height.

    is_animated (``bool``):
        True, if the sticker is animated

    is_video (``bool``):
        True, if the sticker is a video sticker

    needs_repainting (``bool``, *optional*):
        True, if the sticker needs repainting.
        if the sticker can repainted to a text color in messages,
        the color of the Telegram Premium badge in emoji status,
        white color on chat photos, or another appropriate color in other places.
        Only applicable to custom emoji stickers.

    file_name (``str``, *optional*):
        Sticker file name.

    mime_type (``str``, *optional*):
        MIME type of the file as defined by sender.

    file_size (``int``, *optional*):
        File size.

    date (:py:obj:`~datetime.datetime`, *optional*):
        Date the sticker was sent.

    emoji (``str``, *optional*):
        Emoji associated with the sticker.

    set_name (``str``, *optional*):
        Name of the sticker set to which the sticker belongs.

    thumbs (List of :obj:`~pyrogram.types.Thumbnail`, *optional*):
        Sticker thumbnails in the .webp or .jpg format.
```

##### Methods

###### `def __init__(self, *, client: 'pyrogram.Client' = None, file_id: str, file_unique_id: str, width: int, height: int, is_animated: bool, is_video: bool, needs_repainting: bool = False, file_name: str = None, mime_type: str = None, file_size: int = None, date: datetime = None, emoji: str = None, set_name: str = None, thumbs: List['types.Thumbnail'] = None)`

_No docstring._

###### `async def _get_sticker_set_name(invoke, input_sticker_set_id)`

_No docstring._

###### `async def _parse(client, sticker: 'raw.types.Document', document_attributes: Dict[Type['raw.base.DocumentAttribute'], 'raw.base.DocumentAttribute']) -> 'Sticker'`

_No docstring._

---

## File: `types/messages_and_media/stickerset.py`

### Classes

#### `class StickerSet(Object)`

```text
A stickerset.

Parameters:
    id (``Integer``):
        Identifier for this stickerset.

    title (``String``):
        Title of stickerset.

    short_name (``String``):
        Short name of stickerset, used when sharing stickerset using stickerset deep links.

    count (``Integer``):
        Number of stickers in stickerset.

    masks (``Boolean``):
        Is this a mask stickerset.

    emojis (``Boolean``):
        Is this a emojis stickerset.
```

##### Methods

###### `def __init__(self, *, id: int, title: str, short_name: str, count: int, masks: bool = None, emojis: bool = None)`

_No docstring._

###### `def _parse(stickerset: 'raw.types.StickerSet') -> 'StickerSet'`

_No docstring._

---

## File: `types/messages_and_media/stories_privacy_rules.py`

### Classes

#### `class StoriesPrivacyRules(Object)`

```text
A story privacy.

Parameters:
    type (:obj:`~pyrogram.enums.StoriesPrivacyRules`):
        Story privacy type.
```

##### Methods

###### `def __init__(self, *, type: 'enums.StoriesPrivacyRules')`

_No docstring._

###### `def write(self)`

_No docstring._

---

## File: `types/messages_and_media/story.py`

### Classes

#### `class Story(Object, Update)`

```text
A story.

Parameters:
    id (``int``):
        Unique story identifier.

    from_user (:obj:`~pyrogram.types.User`, *optional*):
        Sender of the story.

    sender_chat (:obj:`~pyrogram.types.Chat`, *optional*):
        Sender of the story. If the story is from channel.

    date (:py:obj:`~datetime.datetime`, *optional*):
        Date the story was sent.

    expire_date (:py:obj:`~datetime.datetime`, *optional*):
        Date the story will be expired.

    media (:obj:`~pyrogram.enums.MessageMediaType`, *optional*):
        The media type of the Story.
        This field will contain the enumeration type of the media message.
        You can use ``media = getattr(message, message.media.value)`` to access the media message.

    has_protected_content (``bool``, *optional*):
        True, if the story can't be forwarded.

    animation (:obj:`~pyrogram.types.Animation`, *optional*):
        Story is an animation, information about the animation.

    photo (:obj:`~pyrogram.types.Photo`, *optional*):
        Story is a photo, information about the photo.

    video (:obj:`~pyrogram.types.Video`, *optional*):
        Story is a video, information about the video.

    edited (``bool``, *optional*):
       True, if the Story has been edited.

    pinned (``bool``, *optional*):
       True, if the Story is pinned.

    public (``bool``, *optional*):
       True, if the Story is shared with public.

    close_friends (``bool``, *optional*):
       True, if the Story is shared with close_friends only.

    contacts (``bool``, *optional*):
       True, if the Story is shared with contacts only.

    selected_contacts (``bool``, *optional*):
       True, if the Story is shared with selected contacts only.

    caption (``str``, *optional*):
        Caption for the Story, 0-1024 characters.

    caption_entities (List of :obj:`~pyrogram.types.MessageEntity`, *optional*):
        For text messages, special entities like usernames, URLs, bot commands, etc. that appear in the caption.

    views (:obj:`~pyrogram.types.StoryViews`, *optional*):
        Stories views.

    forward_from (:obj:`~pyrogram.types.StoryForwardHeader`, *optional*):
        Story is a forwarded story.
        Information about the original story.

    privacy (:obj:`~pyrogram.enums.StoryPrivacy`, *optional*):
        Story privacy.

    allowed_users (List of ``int``, *optional*):
        List of user_id whos allowed to view the story.

    denied_users (List of ``int``, *optional*):
        List of user_id whos denied to view the story.

    media_areas (List of :obj:`~pyrogram.types.MediaArea`, *optional*):
        List of :obj:`~pyrogram.types.MediaArea` object in story.

    raw (``pyrogram.raw.types.StoryItem``, *optional*):
        The raw story object, as received from the Telegram API.
```

##### Methods

###### `def __init__(self, *, client: 'pyrogram.Client' = None, id: int, chat: 'types.Chat' = None, from_user: 'types.User' = None, sender_chat: 'types.Chat' = None, date: datetime, expire_date: datetime, media: 'enums.MessageMediaType', has_protected_content: bool = None, animation: 'types.Animation' = None, photo: 'types.Photo' = None, video: 'types.Video' = None, edited: bool = None, pinned: bool = None, public: bool = None, close_friends: bool = None, contacts: bool = None, selected_contacts: bool = None, caption: str = None, caption_entities: List['types.MessageEntity'] = None, views: 'types.StoryViews' = None, privacy: 'enums.StoryPrivacy' = None, forward_from: 'types.StoryForwardHeader' = None, allowed_users: List[int] = None, denied_users: List[int] = None, media_areas: List['types.MediaArea'] = None, raw: 'raw.types.StoryItem' = None)`

_No docstring._

###### `async def _parse(client: 'pyrogram.Client', stories: raw.base.StoryItem, peer: Union['raw.types.PeerChannel', 'raw.types.PeerUser', 'raw.types.InputPeerChannel', 'raw.types.InputPeerUser']) -> 'Story'`

_No docstring._

###### `async def reply_text(self, text: str, parse_mode: Optional['enums.ParseMode'] = None, entities: List['types.MessageEntity'] = None, disable_web_page_preview: bool = None, disable_notification: bool = None, reply_to_story_id: int = None, schedule_date: datetime = None, protect_content: bool = None, reply_markup = None) -> 'types.Message'`

```text
Bound method *reply_text* of :obj:`~pyrogram.types.Story`.

An alias exists as *reply*.

Use as a shortcut for:

.. code-block:: python

    await client.send_message(
        chat_id=message.chat.id,
        text="hello",
        reply_to_story_id=story.id
    )

Example:
    .. code-block:: python

        await story.reply_text("hello", quote=True)

Parameters:
    text (``str``):
        Text of the message to be sent.

    parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
        By default, texts are parsed using both Markdown and HTML styles.
        You can combine both syntaxes together.

    entities (List of :obj:`~pyrogram.types.MessageEntity`):
        List of special entities that appear in message text, which can be specified instead of *parse_mode*.

    disable_web_page_preview (``bool``, *optional*):
        Disables link previews for links in this message.

    disable_notification (``bool``, *optional*):
        Sends the message silently.
        Users will receive a notification with no sound.

    reply_to_story_id (``int``, *optional*):
        If the message is a reply, ID of the original story.

    schedule_date (:py:obj:`~datetime.datetime`, *optional*):
        Date when the message will be automatically sent.

    protect_content (``bool``, *optional*):
        Protects the contents of the sent message from forwarding and saving.

    reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardRemove` | :obj:`~pyrogram.types.ForceReply`, *optional*):
        Additional interface options. An object for an inline keyboard, custom reply keyboard,
        instructions to remove reply keyboard or to force a reply from the user.

Returns:
    On success, the sent Message is returned.

Raises:
    RPCError: In case of a Telegram RPC error.
```

###### `async def reply_animation(self, animation: Union[str, BinaryIO], caption: str = '', parse_mode: Optional['enums.ParseMode'] = None, caption_entities: List['types.MessageEntity'] = None, has_spoiler: bool = None, duration: int = 0, width: int = 0, height: int = 0, thumb: Union[str, BinaryIO] = None, file_name: str = None, disable_notification: bool = None, reply_markup: Union['types.InlineKeyboardMarkup', 'types.ReplyKeyboardMarkup', 'types.ReplyKeyboardRemove', 'types.ForceReply'] = None, reply_to_story_id: int = None, progress: Callable = None, progress_args: tuple = ()) -> 'types.Message'`

```text
Bound method *reply_animation* :obj:`~pyrogram.types.Story`.

Use as a shortcut for:

.. code-block:: python

    await client.send_animation(
        chat_id=story.from_user.id,
        animation=animation,
        reply_to_story_id=story.id
    )

Example:
    .. code-block:: python

        await story.reply_animation(animation)

Parameters:
    animation (``str``):
        Animation to send.
        Pass a file_id as string to send an animation that exists on the Telegram servers,
        pass an HTTP URL as a string for Telegram to get an animation from the Internet, or
        pass a file path as string to upload a new animation that exists on your local machine.

    caption (``str``, *optional*):
        Animation caption, 0-1024 characters.

    parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
        By default, texts are parsed using both Markdown and HTML styles.
        You can combine both syntaxes together.

    caption_entities (List of :obj:`~pyrogram.types.MessageEntity`):
        List of special entities that appear in the caption, which can be specified instead of *parse_mode*.

    has_spoiler (``bool``, *optional*):
        Pass True if the animation needs to be covered with a spoiler animation.

    duration (``int``, *optional*):
        Duration of sent animation in seconds.

    width (``int``, *optional*):
        Animation width.

    height (``int``, *optional*):
        Animation height.

    thumb (``str`` | ``BinaryIO``, *optional*):
        Thumbnail of the animation file sent.
        The thumbnail should be in JPEG format and less than 200 KB in size.
        A thumbnail's width and height should not exceed 320 pixels.
        Thumbnails can't be reused and can be only uploaded as a new file.

    file_name (``str``, *optional*):
        File name of the animation sent.
        Defaults to file's path basename.

    disable_notification (``bool``, *optional*):
        Sends the message silently.
        Users will receive a notification with no sound.

    reply_to_story_id (``int``, *optional*):
        If the message is a reply, ID of the original message.

    reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardRemove` | :obj:`~pyrogram.types.ForceReply`, *optional*):
        Additional interface options. An object for an inline keyboard, custom reply keyboard,
        instructions to remove reply keyboard or to force a reply from the user.

    progress (``Callable``, *optional*):
        Pass a callback function to view the file transmission progress.
        The function must take *(current, total)* as positional arguments (look at Other Parameters below for a
        detailed description) and will be called back each time a new file chunk has been successfully
        transmitted.

    progress_args (``tuple``, *optional*):
        Extra custom arguments for the progress callback function.
        You can pass anything you need to be available in the progress callback scope; for example, a Message
        object or a Client instance in order to edit the message with the updated progress status.

Other Parameters:
    current (``int``):
        The amount of bytes transmitted so far.

    total (``int``):
        The total size of the file.

    *args (``tuple``, *optional*):
        Extra custom arguments as defined in the ``progress_args`` parameter.
        You can either keep ``*args`` or add every single extra argument in your function signature.

Returns:
    On success, the sent :obj:`~pyrogram.types.Message` is returned.
    In case the upload is deliberately stopped with :meth:`~pyrogram.Client.stop_transmission`, None is returned
    instead.

Raises:
    RPCError: In case of a Telegram RPC error.
```

###### `async def reply_audio(self, audio: Union[str, BinaryIO], caption: str = '', parse_mode: Optional['enums.ParseMode'] = None, caption_entities: List['types.MessageEntity'] = None, duration: int = 0, performer: str = None, title: str = None, thumb: Union[str, BinaryIO] = None, file_name: str = None, disable_notification: bool = None, reply_to_story_id: int = None, reply_markup: Union['types.InlineKeyboardMarkup', 'types.ReplyKeyboardMarkup', 'types.ReplyKeyboardRemove', 'types.ForceReply'] = None, progress: Callable = None, progress_args: tuple = ()) -> 'types.Message'`

```text
Bound method *reply_audio* of :obj:`~pyrogram.types.Story`.

Use as a shortcut for:

.. code-block:: python

    await client.send_audio(
        chat_id=story.from_user.id,
        audio=audio,
        reply_to_story_id=story.id
    )

Example:
    .. code-block:: python

        await story.reply_audio(audio)

Parameters:
    audio (``str``):
        Audio file to send.
        Pass a file_id as string to send an audio file that exists on the Telegram servers,
        pass an HTTP URL as a string for Telegram to get an audio file from the Internet, or
        pass a file path as string to upload a new audio file that exists on your local machine.

    caption (``str``, *optional*):
        Audio caption, 0-1024 characters.

    parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
        By default, texts are parsed using both Markdown and HTML styles.
        You can combine both syntaxes together.

    caption_entities (List of :obj:`~pyrogram.types.MessageEntity`):
        List of special entities that appear in the caption, which can be specified instead of *parse_mode*.

    duration (``int``, *optional*):
        Duration of the audio in seconds.

    performer (``str``, *optional*):
        Performer.

    title (``str``, *optional*):
        Track name.

    thumb (``str`` | ``BinaryIO``, *optional*):
        Thumbnail of the music file album cover.
        The thumbnail should be in JPEG format and less than 200 KB in size.
        A thumbnail's width and height should not exceed 320 pixels.
        Thumbnails can't be reused and can be only uploaded as a new file.

    file_name (``str``, *optional*):
        File name of the audio sent.
        Defaults to file's path basename.

    disable_notification (``bool``, *optional*):
        Sends the message silently.
        Users will receive a notification with no sound.

    reply_to_story_id (``int``, *optional*):
        If the message is a reply, ID of the original message.

    reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardRemove` | :obj:`~pyrogram.types.ForceReply`, *optional*):
        Additional interface options. An object for an inline keyboard, custom reply keyboard,
        instructions to remove reply keyboard or to force a reply from the user.

    progress (``Callable``, *optional*):
        Pass a callback function to view the file transmission progress.
        The function must take *(current, total)* as positional arguments (look at Other Parameters below for a
        detailed description) and will be called back each time a new file chunk has been successfully
        transmitted.

    progress_args (``tuple``, *optional*):
        Extra custom arguments for the progress callback function.
        You can pass anything you need to be available in the progress callback scope; for example, a Message
        object or a Client instance in order to edit the message with the updated progress status.

Other Parameters:
    current (``int``):
        The amount of bytes transmitted so far.

    total (``int``):
        The total size of the file.

    *args (``tuple``, *optional*):
        Extra custom arguments as defined in the ``progress_args`` parameter.
        You can either keep ``*args`` or add every single extra argument in your function signature.

Returns:
    On success, the sent :obj:`~pyrogram.types.Message` is returned.
    In case the upload is deliberately stopped with :meth:`~pyrogram.Client.stop_transmission`, None is returned
    instead.

Raises:
    RPCError: In case of a Telegram RPC error.
```

###### `async def reply_cached_media(self, file_id: str, caption: str = '', parse_mode: Optional['enums.ParseMode'] = None, caption_entities: List['types.MessageEntity'] = None, disable_notification: bool = None, reply_to_story_id: int = None, reply_markup: Union['types.InlineKeyboardMarkup', 'types.ReplyKeyboardMarkup', 'types.ReplyKeyboardRemove', 'types.ForceReply'] = None) -> 'types.Message'`

```text
Bound method *reply_cached_media* of :obj:`~pyrogram.types.Story`.

Use as a shortcut for:

.. code-block:: python

    await client.send_cached_media(
        chat_id=story.from_user.id,
        file_id=file_id,
        reply_to_story_id=story.id
    )

Example:
    .. code-block:: python

        await story.reply_cached_media(file_id)

Parameters:
    file_id (``str``):
        Media to send.
        Pass a file_id as string to send a media that exists on the Telegram servers.

    caption (``bool``, *optional*):
        Media caption, 0-1024 characters.

    parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
        By default, texts are parsed using both Markdown and HTML styles.
        You can combine both syntaxes together.

    caption_entities (List of :obj:`~pyrogram.types.MessageEntity`):
        List of special entities that appear in the caption, which can be specified instead of *parse_mode*.

    disable_notification (``bool``, *optional*):
        Sends the message silently.
        Users will receive a notification with no sound.

    reply_to_story_id (``int``, *optional*):
        If the message is a reply, ID of the original message.

    reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardRemove` | :obj:`~pyrogram.types.ForceReply`, *optional*):
        Additional interface options. An object for an inline keyboard, custom reply keyboard,
        instructions to remove reply keyboard or to force a reply from the user.

Returns:
    On success, the sent :obj:`~pyrogram.types.Message` is returned.

Raises:
    RPCError: In case of a Telegram RPC error.
```

###### `async def reply_media_group(self, media: List[Union['types.InputMediaPhoto', 'types.InputMediaVideo', 'types.InputMediaAudio', 'types.InputMediaDocument']], disable_notification: bool = None, reply_to_story_id: int = None) -> List['types.Message']`

```text
Bound method *reply_media_group* of :obj:`~pyrogram.types.Story`.

Use as a shortcut for:

.. code-block:: python

    await client.send_media_group(
        chat_id=story.from_user.id,
        media=list_of_media,
        reply_to_story_id=story.id
    )

Example:
    .. code-block:: python

        await story.reply_media_group(list_of_media)

Parameters:
    media (``list``):
        A list containing either :obj:`~pyrogram.types.InputMediaPhoto` or
        :obj:`~pyrogram.types.InputMediaVideo` objects
        describing photos and videos to be sent, must include 2–10 items.

    disable_notification (``bool``, *optional*):
        Sends the message silently.
        Users will receive a notification with no sound.

    reply_to_story_id (``int``, *optional*):
        If the message is a reply, ID of the original message.

Returns:
    On success, a :obj:`~pyrogram.types.Messages` object is returned containing all the
    single messages sent.

Raises:
    RPCError: In case of a Telegram RPC error.
```

###### `async def reply_photo(self, photo: Union[str, BinaryIO], caption: str = '', parse_mode: Optional['enums.ParseMode'] = None, caption_entities: List['types.MessageEntity'] = None, has_spoiler: bool = None, ttl_seconds: int = None, view_once: bool = None, disable_notification: bool = None, reply_to_story_id: int = None, reply_markup: Union['types.InlineKeyboardMarkup', 'types.ReplyKeyboardMarkup', 'types.ReplyKeyboardRemove', 'types.ForceReply'] = None, progress: Callable = None, progress_args: tuple = ()) -> 'types.Message'`

```text
Bound method *reply_photo* of :obj:`~pyrogram.types.Story`.

Use as a shortcut for:

.. code-block:: python

    await client.send_photo(
        chat_id=story.from_user.id,
        photo=photo,
        reply_to_story_id=story.id
    )

Example:
    .. code-block:: python

        await story.reply_photo(photo)

Parameters:
    photo (``str``):
        Photo to send.
        Pass a file_id as string to send a photo that exists on the Telegram servers,
        pass an HTTP URL as a string for Telegram to get a photo from the Internet, or
        pass a file path as string to upload a new photo that exists on your local machine.

    caption (``str``, *optional*):
        Photo caption, 0-1024 characters.

    parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
        By default, texts are parsed using both Markdown and HTML styles.
        You can combine both syntaxes together.

    caption_entities (List of :obj:`~pyrogram.types.MessageEntity`):
        List of special entities that appear in the caption, which can be specified instead of *parse_mode*.

    has_spoiler (``bool``, *optional*):
        Pass True if the photo needs to be covered with a spoiler animation.

    ttl_seconds (``int``, *optional*):
        Self-Destruct Timer.
        If you set a timer, the photo will self-destruct in *ttl_seconds*
        seconds after it was viewed.

    view_once (``bool``, *optional*):
        Self-Destruct Timer.
        If True, the photo will self-destruct after it was viewed.

    disable_notification (``bool``, *optional*):
        Sends the message silently.
        Users will receive a notification with no sound.

    reply_to_story_id (``int``, *optional*):
        If the message is a reply, ID of the original message.

    reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardRemove` | :obj:`~pyrogram.types.ForceReply`, *optional*):
        Additional interface options. An object for an inline keyboard, custom reply keyboard,
        instructions to remove reply keyboard or to force a reply from the user.

    progress (``Callable``, *optional*):
        Pass a callback function to view the file transmission progress.
        The function must take *(current, total)* as positional arguments (look at Other Parameters below for a
        detailed description) and will be called back each time a new file chunk has been successfully
        transmitted.

    progress_args (``tuple``, *optional*):
        Extra custom arguments for the progress callback function.
        You can pass anything you need to be available in the progress callback scope; for example, a Message
        object or a Client instance in order to edit the message with the updated progress status.

Other Parameters:
    current (``int``):
        The amount of bytes transmitted so far.

    total (``int``):
        The total size of the file.

    *args (``tuple``, *optional*):
        Extra custom arguments as defined in the ``progress_args`` parameter.
        You can either keep ``*args`` or add every single extra argument in your function signature.

Returns:
    On success, the sent :obj:`~pyrogram.types.Message` is returned.
    In case the upload is deliberately stopped with :meth:`~pyrogram.Client.stop_transmission`, None is returned
    instead.

Raises:
    RPCError: In case of a Telegram RPC error.
```

###### `async def reply_sticker(self, sticker: Union[str, BinaryIO], disable_notification: bool = None, reply_to_story_id: int = None, reply_markup: Union['types.InlineKeyboardMarkup', 'types.ReplyKeyboardMarkup', 'types.ReplyKeyboardRemove', 'types.ForceReply'] = None, progress: Callable = None, progress_args: tuple = ()) -> 'types.Message'`

```text
Bound method *reply_sticker* of :obj:`~pyrogram.types.Story`.

Use as a shortcut for:

.. code-block:: python

    await client.send_sticker(
        chat_id=story.from_user.id,
        sticker=sticker,
        reply_to_story_id=story.id
    )

Example:
    .. code-block:: python

        await story.reply_sticker(sticker)

Parameters:
    sticker (``str``):
        Sticker to send.
        Pass a file_id as string to send a sticker that exists on the Telegram servers,
        pass an HTTP URL as a string for Telegram to get a .webp sticker file from the Internet, or
        pass a file path as string to upload a new sticker that exists on your local machine.

    disable_notification (``bool``, *optional*):
        Sends the message silently.
        Users will receive a notification with no sound.

    reply_to_story_id (``int``, *optional*):
        If the message is a reply, ID of the original message.

    reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardRemove` | :obj:`~pyrogram.types.ForceReply`, *optional*):
        Additional interface options. An object for an inline keyboard, custom reply keyboard,
        instructions to remove reply keyboard or to force a reply from the user.

    progress (``Callable``, *optional*):
        Pass a callback function to view the file transmission progress.
        The function must take *(current, total)* as positional arguments (look at Other Parameters below for a
        detailed description) and will be called back each time a new file chunk has been successfully
        transmitted.

    progress_args (``tuple``, *optional*):
        Extra custom arguments for the progress callback function.
        You can pass anything you need to be available in the progress callback scope; for example, a Message
        object or a Client instance in order to edit the message with the updated progress status.

Other Parameters:
    current (``int``):
        The amount of bytes transmitted so far.

    total (``int``):
        The total size of the file.

    *args (``tuple``, *optional*):
        Extra custom arguments as defined in the ``progress_args`` parameter.
        You can either keep ``*args`` or add every single extra argument in your function signature.

Returns:
    On success, the sent :obj:`~pyrogram.types.Message` is returned.
    In case the upload is deliberately stopped with :meth:`~pyrogram.Client.stop_transmission`, None is returned
    instead.

Raises:
    RPCError: In case of a Telegram RPC error.
```

###### `async def reply_video(self, video: Union[str, BinaryIO], caption: str = '', parse_mode: Optional['enums.ParseMode'] = None, caption_entities: List['types.MessageEntity'] = None, has_spoiler: bool = None, ttl_seconds: int = None, duration: int = 0, width: int = 0, height: int = 0, thumb: Union[str, BinaryIO] = None, file_name: str = None, supports_streaming: bool = True, disable_notification: bool = None, reply_to_story_id: int = None, reply_markup: Union['types.InlineKeyboardMarkup', 'types.ReplyKeyboardMarkup', 'types.ReplyKeyboardRemove', 'types.ForceReply'] = None, progress: Callable = None, progress_args: tuple = ()) -> 'types.Message'`

```text
Bound method *reply_video* of :obj:`~pyrogram.types.Story`.

Use as a shortcut for:

.. code-block:: python

    await client.send_video(
        chat_id=story.from_user.id,
        video=video,
        reply_to_story_id=story.id
    )

Example:
    .. code-block:: python

        await story.reply_video(video)

Parameters:
    video (``str``):
        Video to send.
        Pass a file_id as string to send a video that exists on the Telegram servers,
        pass an HTTP URL as a string for Telegram to get a video from the Internet, or
        pass a file path as string to upload a new video that exists on your local machine.

    caption (``str``, *optional*):
        Video caption, 0-1024 characters.

    parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
        By default, texts are parsed using both Markdown and HTML styles.
        You can combine both syntaxes together.

    caption_entities (List of :obj:`~pyrogram.types.MessageEntity`):
        List of special entities that appear in the caption, which can be specified instead of *parse_mode*.

    has_spoiler (``bool``, *optional*):
        Pass True if the video needs to be covered with a spoiler animation.

    ttl_seconds (``int``, *optional*):
        Self-Destruct Timer.
        If you set a timer, the video will self-destruct in *ttl_seconds*
        seconds after it was viewed.

    duration (``int``, *optional*):
        Duration of sent video in seconds.

    width (``int``, *optional*):
        Video width.

    height (``int``, *optional*):
        Video height.

    thumb (``str`` | ``BinaryIO``, *optional*):
        Thumbnail of the video sent.
        The thumbnail should be in JPEG format and less than 200 KB in size.
        A thumbnail's width and height should not exceed 320 pixels.
        Thumbnails can't be reused and can be only uploaded as a new file.

    file_name (``str``, *optional*):
        File name of the video sent.
        Defaults to file's path basename.

    supports_streaming (``bool``, *optional*):
        Pass True, if the uploaded video is suitable for streaming.

    disable_notification (``bool``, *optional*):
        Sends the message silently.
        Users will receive a notification with no sound.

    reply_to_story_id (``int``, *optional*):
        If the message is a reply, ID of the original message.

    reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardRemove` | :obj:`~pyrogram.types.ForceReply`, *optional*):
        Additional interface options. An object for an inline keyboard, custom reply keyboard,
        instructions to remove reply keyboard or to force a reply from the user.

    progress (``Callable``, *optional*):
        Pass a callback function to view the file transmission progress.
        The function must take *(current, total)* as positional arguments (look at Other Parameters below for a
        detailed description) and will be called back each time a new file chunk has been successfully
        transmitted.

    progress_args (``tuple``, *optional*):
        Extra custom arguments for the progress callback function.
        You can pass anything you need to be available in the progress callback scope; for example, a Message
        object or a Client instance in order to edit the message with the updated progress status.

Other Parameters:
    current (``int``):
        The amount of bytes transmitted so far.

    total (``int``):
        The total size of the file.

    *args (``tuple``, *optional*):
        Extra custom arguments as defined in the ``progress_args`` parameter.
        You can either keep ``*args`` or add every single extra argument in your function signature.

Returns:
    On success, the sent :obj:`~pyrogram.types.Message` is returned.
    In case the upload is deliberately stopped with :meth:`~pyrogram.Client.stop_transmission`, None is returned
    instead.

Raises:
    RPCError: In case of a Telegram RPC error.
```

###### `async def reply_video_note(self, video_note: Union[str, BinaryIO], duration: int = 0, length: int = 1, thumb: Union[str, BinaryIO] = None, disable_notification: bool = None, reply_to_story_id: int = None, reply_markup: Union['types.InlineKeyboardMarkup', 'types.ReplyKeyboardMarkup', 'types.ReplyKeyboardRemove', 'types.ForceReply'] = None, progress: Callable = None, progress_args: tuple = ()) -> 'types.Message'`

```text
Bound method *reply_video_note* of :obj:`~pyrogram.types.Story`.

Use as a shortcut for:

.. code-block:: python

    await client.send_video_note(
        chat_id=story.from_user.id,
        video_note=video_note,
        reply_to_story_id=story.id
    )

Example:
    .. code-block:: python

        await story.reply_video_note(video_note)

Parameters:
    video_note (``str``):
        Video note to send.
        Pass a file_id as string to send a video note that exists on the Telegram servers, or
        pass a file path as string to upload a new video note that exists on your local machine.
        Sending video notes by a URL is currently unsupported.

    duration (``int``, *optional*):
        Duration of sent video in seconds.

    length (``int``, *optional*):
        Video width and height.

    thumb (``str`` | ``BinaryIO``, *optional*):
        Thumbnail of the video sent.
        The thumbnail should be in JPEG format and less than 200 KB in size.
        A thumbnail's width and height should not exceed 320 pixels.
        Thumbnails can't be reused and can be only uploaded as a new file.

    disable_notification (``bool``, *optional*):
        Sends the message silently.
        Users will receive a notification with no sound.

    reply_to_story_id (``int``, *optional*):
        If the message is a reply, ID of the original message

    reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardRemove` | :obj:`~pyrogram.types.ForceReply`, *optional*):
        Additional interface options. An object for an inline keyboard, custom reply keyboard,
        instructions to remove reply keyboard or to force a reply from the user.

    progress (``Callable``, *optional*):
        Pass a callback function to view the file transmission progress.
        The function must take *(current, total)* as positional arguments (look at Other Parameters below for a
        detailed description) and will be called back each time a new file chunk has been successfully
        transmitted.

    progress_args (``tuple``, *optional*):
        Extra custom arguments for the progress callback function.
        You can pass anything you need to be available in the progress callback scope; for example, a Message
        object or a Client instance in order to edit the message with the updated progress status.

Other Parameters:
    current (``int``):
        The amount of bytes transmitted so far.

    total (``int``):
        The total size of the file.

    *args (``tuple``, *optional*):
        Extra custom arguments as defined in the ``progress_args`` parameter.
        You can either keep ``*args`` or add every single extra argument in your function signature.

Returns:
    On success, the sent :obj:`~pyrogram.types.Message` is returned.
    In case the upload is deliberately stopped with :meth:`~pyrogram.Client.stop_transmission`, None is returned
    instead.

Raises:
    RPCError: In case of a Telegram RPC error.
```

###### `async def reply_voice(self, voice: Union[str, BinaryIO], caption: str = '', parse_mode: Optional['enums.ParseMode'] = None, caption_entities: List['types.MessageEntity'] = None, duration: int = 0, disable_notification: bool = None, reply_to_story_id: int = None, reply_markup: Union['types.InlineKeyboardMarkup', 'types.ReplyKeyboardMarkup', 'types.ReplyKeyboardRemove', 'types.ForceReply'] = None, progress: Callable = None, progress_args: tuple = ()) -> 'types.Message'`

```text
Bound method *reply_voice* of :obj:`~pyrogram.types.Story`.

Use as a shortcut for:

.. code-block:: python

    await client.send_voice(
        chat_id=story.from_user.id,
        voice=voice,
        reply_to_story_id=story.id
    )

Example:
    .. code-block:: python

        await message.reply_voice(voice)

Parameters:
    voice (``str``):
        Audio file to send.
        Pass a file_id as string to send an audio that exists on the Telegram servers,
        pass an HTTP URL as a string for Telegram to get an audio from the Internet, or
        pass a file path as string to upload a new audio that exists on your local machine.

    caption (``str``, *optional*):
        Voice message caption, 0-1024 characters.

    parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
        By default, texts are parsed using both Markdown and HTML styles.
        You can combine both syntaxes together.

    caption_entities (List of :obj:`~pyrogram.types.MessageEntity`):
        List of special entities that appear in the caption, which can be specified instead of *parse_mode*.

    duration (``int``, *optional*):
        Duration of the voice message in seconds.

    disable_notification (``bool``, *optional*):
        Sends the message silently.
        Users will receive a notification with no sound.

    reply_to_story_id (``int``, *optional*):
        If the message is a reply, ID of the original message

    reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardRemove` | :obj:`~pyrogram.types.ForceReply`, *optional*):
        Additional interface options. An object for an inline keyboard, custom reply keyboard,
        instructions to remove reply keyboard or to force a reply from the user.

    progress (``Callable``, *optional*):
        Pass a callback function to view the file transmission progress.
        The function must take *(current, total)* as positional arguments (look at Other Parameters below for a
        detailed description) and will be called back each time a new file chunk has been successfully
        transmitted.

    progress_args (``tuple``, *optional*):
        Extra custom arguments for the progress callback function.
        You can pass anything you need to be available in the progress callback scope; for example, a Message
        object or a Client instance in order to edit the message with the updated progress status.

Other Parameters:
    current (``int``):
        The amount of bytes transmitted so far.

    total (``int``):
        The total size of the file.

    *args (``tuple``, *optional*):
        Extra custom arguments as defined in the ``progress_args`` parameter.
        You can either keep ``*args`` or add every single extra argument in your function signature.

Returns:
    On success, the sent :obj:`~pyrogram.types.Message` is returned.
    In case the upload is deliberately stopped with :meth:`~pyrogram.Client.stop_transmission`, None is returned
    instead.

Raises:
    RPCError: In case of a Telegram RPC error.
```

###### `async def delete(self)`

```text
Bound method *delete* of :obj:`~pyrogram.types.Story`.

Use as a shortcut for:

.. code-block:: python

    await client.delete_stories(
        story_ids=story.id
    )

Example:
    .. code-block:: python

        await story.delete()

Returns:
    True on success, False otherwise.

Raises:
    RPCError: In case of a Telegram RPC error.
```

###### `async def edit_animation(self, animation: Union[str, BinaryIO]) -> 'types.Story'`

```text
Bound method *edit_animation* of :obj:`~pyrogram.types.Story`.

Use as a shortcut for:

.. code-block:: python

    await client.edit_animation(
        story_id=story.id,
        animation="/path/to/animation.mp4"
    )

Example:
    .. code-block:: python

        await story.edit_animation("/path/to/animation.mp4")

Parameters:
    animation (``str`` | ``BinaryIO``):
        New animation of the story.

Returns:
    On success, the edited :obj:`~pyrogram.types.Story` is returned.

Raises:
    RPCError: In case of a Telegram RPC error.
```

###### `async def edit(self, privacy: 'enums.StoriesPrivacyRules' = None, allowed_users: List[int] = None, denied_users: List[int] = None, animation: str = None, photo: str = None, video: str = None, caption: str = None, parse_mode: 'enums.ParseMode' = None, caption_entities: List['types.MessageEntity'] = None, media_areas: List['types.InputMediaArea'] = None) -> 'types.Story'`

```text
Bound method *edit* of :obj:`~pyrogram.types.Story`.

Use as a shortcut for:

.. code-block:: python

    await client.edit_story(
        story_id=story.id,
        caption="hello"
    )

Example:
    .. code-block:: python

        await story.edit_caption("hello")

Parameters:
    story_id (``int``):
        Unique identifier (int) of the target story.

    animation (``str`` | ``BinaryIO``, *optional*):
        New story Animation.
        Pass a file_id as string to send a animation that exists on the Telegram servers,
        pass an HTTP URL as a string for Telegram to get a animation from the Internet,
        pass a file path as string to upload a new animation that exists on your local machine, or
        pass a binary file-like object with its attribute ".name" set for in-memory uploads.

    photo (``str`` | ``BinaryIO``, *optional*):
        New story photo.
        Pass a file_id as string to send a photo that exists on the Telegram servers,
        pass an HTTP URL as a string for Telegram to get a photo from the Internet,
        pass a file path as string to upload a new photo that exists on your local machine, or
        pass a binary file-like object with its attribute ".name" set for in-memory uploads.

    video (``str`` | ``BinaryIO``, *optional*):
        New story video.
        Pass a file_id as string to send a video that exists on the Telegram servers,
        pass an HTTP URL as a string for Telegram to get a video from the Internet,
        pass a file path as string to upload a new video that exists on your local machine, or
        pass a binary file-like object with its attribute ".name" set for in-memory uploads.

    privacy (:obj:`~pyrogram.enums.StoriesPrivacyRules`, *optional*):
        Story privacy.

    allowed_users (List of ``int``, *optional*):
        List of user_id whos allowed to view the story.

    denied_users (List of ``int``, *optional*):
        List of user_id whos denied to view the story.

    caption (``str``, *optional*):
        Story caption, 0-1024 characters.

    parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
        By default, texts are parsed using both Markdown and HTML styles.
        You can combine both syntaxes together.

    caption_entities (List of :obj:`~pyrogram.types.MessageEntity`):
        List of special entities that appear in the caption, which can be specified instead of *parse_mode*.

    media_areas (List of :obj:`~pyrogram.types.InputMediaArea`):
        List of media area object to be included in story.

Returns:
    On success, the edited :obj:`~pyrogram.types.Story` is returned.

Raises:
    RPCError: In case of a Telegram RPC error.
```

###### `async def edit_caption(self, caption: str, parse_mode: Optional['enums.ParseMode'] = None, caption_entities: List['types.MessageEntity'] = None) -> 'types.Story'`

```text
Bound method *edit_caption* of :obj:`~pyrogram.types.Story`.

Use as a shortcut for:

.. code-block:: python

    await c.edit_story(
        channel=chat_id,
        caption="hello"
    )

Example:
    .. code-block:: python

        await story.edit_caption("hello")

Parameters:
    caption (``str``):
        New caption of the story.

    parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
        By default, texts are parsed using both Markdown and HTML styles.
        You can combine both syntaxes together.

    caption_entities (List of :obj:`~pyrogram.types.MessageEntity`):
        List of special entities that appear in the caption, which can be specified instead of *parse_mode*.

Returns:
    On success, the edited :obj:`~pyrogram.types.Story` is returned.

Raises:
    RPCError: In case of a Telegram RPC error.
```

###### `async def edit_photo(self, photo: Union[str, BinaryIO]) -> 'types.Story'`

```text
Bound method *edit_photo* of :obj:`~pyrogram.types.Story`.

Use as a shortcut for:

.. code-block:: python

    await client.edit_story(
        story_id=story.id,
        photo="/path/to/photo.png"
    )

Example:
    .. code-block:: python

        await story.edit_photo("/path/to/photo.png")

Parameters:
    photo (``str`` | ``BinaryIO``):
        New photo of the story.

Returns:
    On success, the edited :obj:`~pyrogram.types.Story` is returned.

Raises:
    RPCError: In case of a Telegram RPC error.
```

###### `async def edit_privacy(self, privacy: 'enums.StoriesPrivacyRules' = None, allowed_users: List[int] = None, denied_users: List[int] = None) -> 'types.Story'`

```text
Bound method *edit_privacy* of :obj:`~pyrogram.types.Story`.

Use as a shortcut for:

.. code-block:: python

    await client.edit_story(
        story_id=story.id,
        privacy=enums.StoriesPrivacyRules.PUBLIC
    )

Example:
    .. code-block:: python

        await story.edit_privacy(enums.StoriesPrivacyRules.PUBLIC)

Parameters:
    privacy (:obj:`~pyrogram.enums.StoriesPrivacyRules`, *optional*):
        Story privacy.

    allowed_users (List of ``int``, *optional*):
        List of user_id whos allowed to view the story.

    denied_users (List of ``int``, *optional*):
        List of user_id whos denied to view the story.

Returns:
    On success, the edited :obj:`~pyrogram.types.Story` is returned.

Raises:
    RPCError: In case of a Telegram RPC error.
```

###### `async def edit_video(self, video: Union[str, BinaryIO]) -> 'types.Story'`

```text
Bound method *edit_video* of :obj:`~pyrogram.types.Story`.

Use as a shortcut for:

.. code-block:: python

    await client.edit_story(
        story_id=story.id,
        video="/path/to/video.mp4"
    )

Example:
    .. code-block:: python

        await story.edit_video("/path/to/video.mp4")

Parameters:
    video (``str`` | ``BinaryIO``):
        New video of the story.

Returns:
    On success, the edited :obj:`~pyrogram.types.Story` is returned.

Raises:
    RPCError: In case of a Telegram RPC error.
```

###### `async def export_link(self) -> 'types.ExportedStoryLink'`

```text
Bound method *export_link* of :obj:`~pyrogram.types.Story`.

Use as a shortcut for:

.. code-block:: python

    await client.export_story_link(
        user_id=story.from_user.id,
        story_id=story.id
    )

Example:
    .. code-block:: python

        await story.export_link()

Returns:
    :obj:`~pyrogram.types.ExportedStoryLink`: a single story link is returned.

Raises:
    RPCError: In case of a Telegram RPC error.
```

###### `async def forward(self, chat_id: int = None, privacy: 'enums.StoriesPrivacyRules' = None, allowed_users: List[int] = None, denied_users: List[int] = None, pinned: bool = None, protect_content: bool = None, caption: str = None, parse_mode: 'enums.ParseMode' = None, caption_entities: List['types.MessageEntity'] = None, period: int = None)`

```text
Bound method *forward* of :obj:`~pyrogram.types.Message`.

Use as a shortcut for:

.. code-block:: python

    await client.forward_story(
        from_chat_id='wulan17',
        from_story_id=1,
        caption='Hello guys.'
    )

Parameters:
    chat_id (``int``, *optional*):
        Unique identifier (int) of the target channel.
        If you want to forward story to a channel.

    privacy (:obj:`~pyrogram.enums.StoriesPrivacyRules`, *optional*):
        Story privacy.
        Defaults to :obj:`~pyrogram.enums.StoriesPrivacyRules.PUBLIC`

    allowed_users (List of ``int``, *optional*):
        List of user_id whos allowed to view the story.

    denied_users (List of ``int``, *optional*):
        List of user_id whos denied to view the story.

    pinned (``bool``, *optional*):
        if True, the story will be pinned.
        default to False.

    protect_content (``bool``, *optional*):
        Protects the contents of the sent story from forwarding and saving.
        default to False.

    caption (``str``, *optional*):
        Story caption, 0-1024 characters.

    parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
        By default, texts are parsed using both Markdown and HTML styles.
        You can combine both syntaxes together.

    caption_entities (List of :obj:`~pyrogram.types.MessageEntity`):
        List of special entities that appear in the caption, which can be specified instead of *parse_mode*.

    period (``int``, *optional*):
        How long the story will posted, in secs.
        only for premium users.

Returns:
    :obj:`~pyrogram.types.Story` a single story is returned.

Raises:
    ValueError: In case of invalid arguments.
```

###### `async def download(self, file_name: str = '', in_memory: bool = False, block: bool = True, progress: Callable = None, progress_args: tuple = ()) -> str`

```text
Bound method *download* of :obj:`~pyrogram.types.Story`.

Use as a shortcut for:

.. code-block:: python

    await client.download_media(story)

Example:
    .. code-block:: python

        await story.download()

Parameters:
    file_name (``str``, *optional*):
        A custom *file_name* to be used instead of the one provided by Telegram.
        By default, all files are downloaded in the *downloads* folder in your working directory.
        You can also specify a path for downloading files in a custom location: paths that end with "/"
        are considered directories. All non-existent folders will be created automatically.

    in_memory (``bool``, *optional*):
        Pass True to download the media in-memory.
        A binary file-like object with its attribute ".name" set will be returned.
        Defaults to False.

    block (``bool``, *optional*):
        Blocks the code execution until the file has been downloaded.
        Defaults to True.

    progress (``Callable``, *optional*):
        Pass a callback function to view the file transmission progress.
        The function must take *(current, total)* as positional arguments (look at Other Parameters below for a
        detailed description) and will be called back each time a new file chunk has been successfully
        transmitted.

    progress_args (``tuple``, *optional*):
        Extra custom arguments for the progress callback function.
        You can pass anything you need to be available in the progress callback scope; for example, a Message
        object or a Client instance in order to edit the message with the updated progress status.

Other Parameters:
    current (``int``):
        The amount of bytes transmitted so far.

    total (``int``):
        The total size of the file.

    *args (``tuple``, *optional*):
        Extra custom arguments as defined in the ``progress_args`` parameter.
        You can either keep ``*args`` or add every single extra argument in your function signature.

Returns:
    On success, the absolute path of the downloaded file as string is returned, None otherwise.

Raises:
    RPCError: In case of a Telegram RPC error.
    ``ValueError``: If the message doesn't contain any downloadable media
```

---

## File: `types/messages_and_media/story_deleted.py`

### Classes

#### `class StoryDeleted(Object, Update)`

```text
A deleted story.

Parameters:
    id (``int``):
        Unique story identifier.

    from_user (:obj:`~pyrogram.types.User`, *optional*):
        Sender of the story.

    sender_chat (:obj:`~pyrogram.types.Chat`, *optional*):
        Sender of the story. If the story is from channel.
```

##### Methods

###### `def __init__(self, *, client: 'pyrogram.Client' = None, id: int, from_user: 'types.User' = None, sender_chat: 'types.Chat' = None)`

_No docstring._

###### `async def _parse(client: 'pyrogram.Client', stories: raw.base.StoryItem, peer: Union['raw.types.PeerChannel', 'raw.types.PeerUser']) -> 'StoryDeleted'`

_No docstring._

---

## File: `types/messages_and_media/story_forward_header.py`

### Classes

#### `class StoryForwardHeader(Object)`

```text
Contains information about origin of forwarded story.


Parameters:
    user (:obj:`~pyrogram.types.User`, *optional*):
        Sender of the story.

    sender_name (``str``, *optional*):
        For stories forwarded from users who have hidden their accounts, name of the user.

    chat (:obj:`~pyrogram.types.Chat`, *optional*):
        Sender of the story. If the story is from channel.

    story_id (``int``):
        Unique identifier for the original story.

    is_modified (``bool``):
        True, if the story is modified.
```

##### Methods

###### `def __init__(self, *, user: 'types.User' = None, sender_name: str = None, chat: 'types.Chat' = None, story_id: int = None, is_modified: bool = None)`

_No docstring._

###### `async def _parse(client: 'pyrogram.Client', fwd_header: 'raw.types.StoryFwdHeader') -> 'StoryForwardHeader'`

_No docstring._

---

## File: `types/messages_and_media/story_skipped.py`

### Classes

#### `class StorySkipped(Object, Update)`

```text
A skipped story.

Parameters:
    id (``int``):
        Unique story identifier.

    from_user (:obj:`~pyrogram.types.User`, *optional*):
        Sender of the story.

    sender_chat (:obj:`~pyrogram.types.Chat`, *optional*):
        Sender of the story. If the story is from channel.

    date (:py:obj:`~datetime.datetime`, *optional*):
        Date the story was sent.

    expire_date (:py:obj:`~datetime.datetime`, *optional*):
        Date the story will be expired.

    close_friends (``bool``, *optional*):
       True, if the Story is shared with close_friends only.
```

##### Methods

###### `def __init__(self, *, client: 'pyrogram.Client' = None, id: int, from_user: 'types.User' = None, sender_chat: 'types.Chat' = None, date: datetime, expire_date: datetime, close_friends: bool = None)`

_No docstring._

###### `async def _parse(client: 'pyrogram.Client', stories: raw.base.StoryItem, peer: Union['raw.types.PeerChannel', 'raw.types.PeerUser']) -> 'StorySkipped'`

_No docstring._

---

## File: `types/messages_and_media/story_views.py`

### Classes

#### `class StoryViews(Object)`

```text
Contains information about a story viewers.


Parameters:
    view_count (``int``):
        The count of stories viewers.

    recent_viewers (List of ``int``):
        List of user_id of recent stories viewers.
```

##### Methods

###### `def __init__(self, *, view_count: int, recent_viewers: List[int] = None)`

_No docstring._

###### `def _parse(storyviews: 'raw.types.StoryViews') -> 'StoryViews'`

_No docstring._

---

## File: `types/messages_and_media/stripped_thumbnail.py`

### Classes

#### `class StrippedThumbnail(Object)`

```text
A stripped thumbnail

Parameters:
    data (``bytes``):
        Thumbnail data
```

##### Methods

###### `def __init__(self, *, client: 'pyrogram.Client' = None, data: bytes)`

_No docstring._

###### `def _parse(client, stripped_thumbnail: 'raw.types.PhotoStrippedSize') -> 'StrippedThumbnail'`

_No docstring._

---

## File: `types/messages_and_media/text_quote.py`

### Classes

#### `class TextQuote(Object)`

```text
Describes manually or automatically chosen quote from another message.

Parameters:
    text (``str``):
        Text of the quoted part of a message that is replied to by the given message.

    entities (List of :obj:`~pyrogram.types.MessageEntity`, *optional*):
        Special entities that appear in the quote.
        Currently, only bold, italic, underline, strikethrough, spoiler, and custom_emoji entities are kept in quotes.

    position (``int``):
        Approximate quote position in the original message in UTF-16 code units as specified by the sender.

    is_manual (``bool``, *optional*):
        True, if the quote was chosen manually by the message sender.
        Otherwise, the quote was added automatically by the server.
```

##### Methods

###### `def __init__(self, *, text: Optional[str] = None, entities: Optional[List['types.MessageEntity']] = None, position: Optional[int] = None, is_manual: Optional[bool] = None)`

_No docstring._

###### `def _parse(client: 'pyrogram.Client', users: Dict[int, 'raw.types.User'], reply_to: 'raw.types.MessageReplyHeader') -> 'TextQuote'`

_No docstring._

---

## File: `types/messages_and_media/thumbnail.py`

### Classes

#### `class Thumbnail(Object)`

```text
One size of a photo or a file/sticker thumbnail.

Parameters:
    file_id (``str``):
        Identifier for this file, which can be used to download or reuse the file.

    file_unique_id (``str``):
        Unique identifier for this file, which is supposed to be the same over time and for different accounts.
        Can't be used to download or reuse the file.

    width (``int``):
        Photo width.

    height (``int``):
        Photo height.

    file_size (``int``):
        File size.
```

##### Methods

###### `def __init__(self, *, client: 'pyrogram.Client' = None, file_id: str, file_unique_id: str, width: int, height: int, file_size: int)`

_No docstring._

###### `def _parse(client, media: Union['raw.types.Photo', 'raw.types.Document']) -> Optional[List['Thumbnail']]`

_No docstring._

---

## File: `types/messages_and_media/todo_list.py`

### Classes

#### `class TodoList(Object)`

```text
A list of tasks.

Parameters:
    title (``str``):
        Title of the todo list.

    entities (List of :obj:`~pyrogram.types.MessageEntity`):
        Entities in the title of the todo list.

    tasks (List of :obj:`~pyrogram.types.TodoTask`):
        List of tasks in the todo list.

    can_append (``bool``, optional):
        True, if other users can append tasks to this todo list.

    can_complete (``bool``, optional):
        True, if other users can complete tasks in this todo list.
```

##### Methods

###### `def __init__(self, title: str, entities: List['types.MessageEntity'], tasks: List['types.TodoTask'] = None, can_append: bool = False, can_complete: bool = False)`

_No docstring._

###### `def _parse(client: 'pyrogram.Client', todo: 'raw.types.TodoList', users: Dict) -> 'TodoList'`

_No docstring._

---

## File: `types/messages_and_media/todo_task.py`

### Classes

#### `class TodoTask(Object)`

```text
A task in a todo list.

Parameters:
    title (``str``):
        Title of the task.

    entities (List of :obj:`~pyrogram.types.MessageEntity`):
        Entities in the title of the task.

    is_completed (``bool``):
        True, if the task is completed.

    completed_by (:obj:`~pyrogram.types.User`, *optional*):
        User who completed the task.

    complete_date (:obj:`~datetime.datetime`, *optional*):
        Date when the task was completed.
```

##### Methods

###### `def __init__(self, id: int, title: str, entities: List['types.MessageEntity'], is_completed: bool, completed_by: 'types.User' = None, complete_date: 'pyrogram.types.datetime' = None)`

_No docstring._

###### `def _parse(client: 'pyrogram.Client', todo_task: 'raw.types.TodoList', users: Dict, completions: List['raw.types.TodoCompletion'] = None) -> 'TodoTask'`

_No docstring._

---

## File: `types/messages_and_media/todo_tasks_added.py`

### Classes

#### `class TodoTasksAdded(Object)`

```text
A todo task added to a todo list.

Parameters:
    task (:obj:`~pyrogram.types.TodoTask`):
        The added todo task.
```

##### Methods

###### `def __init__(self, tasks: 'types.TodoTask')`

_No docstring._

###### `def _parse(client: 'pyrogram.Client', todo_task_added: 'raw.types.MessageActionTodoAppendTasks') -> 'TodoTasksAdded'`

_No docstring._

---

## File: `types/messages_and_media/todo_tasks_completed.py`

### Classes

#### `class TodoTasksCompleted(Object)`

```text
One or more todo task/s has been flag as complete.

Parameters:
    ids (List of ``int``):
        List of Unique identifier of the todo tasks.
```

##### Methods

###### `def __init__(self, ids: List[int])`

_No docstring._

###### `def _parse(todo_completion: 'raw.types.TodoCompletion') -> 'TodoTasksCompleted'`

_No docstring._

---

## File: `types/messages_and_media/todo_tasks_incompleted.py`

### Classes

#### `class TodoTasksIncompleted(Object)`

```text
One or more todo task/s has been flag as incomplete.

Parameters:
    ids (List of ``int``):
        List of Unique identifier of the todo tasks.
```

##### Methods

###### `def __init__(self, ids: List[int])`

_No docstring._

###### `def _parse(todo_completion: 'raw.types.TodoCompletion') -> 'TodoTasksIncompleted'`

_No docstring._

---

## File: `types/messages_and_media/transcribed_audio.py`

### Classes

#### `class TranscribedAudio(Object)`

```text
Transcribes the audio of a voice message.

Parameters:
    transcription_id (``int``):
        Unique identifier of the transcription.

    text (``str``):
        Transcribed text.

    pending (``bool``, *optional*):
        Whether the transcription is pending.

    trial_remains_num (``int``, *optional*):
        Number of trials remaining.

    trial_remains_until_date (``int``, *optional*):
        Date the trial remains until.
```

##### Methods

###### `def __init__(self, *, transcription_id: int, text: str, pending: bool = None, trial_remains_num: int = None, trial_remains_until_date: int = None)`

_No docstring._

###### `def _parse(transcribe_result: 'raw.types.messages.TranscribedAudio') -> 'TranscribedAudio'`

_No docstring._

---

## File: `types/messages_and_media/translated_text.py`

### Classes

#### `class TranslatedText(Object)`

```text
A translated text with entities.

Parameters:
    text (``str``):
        Translated text.

    entities (``str``, *optional*):
        Entities of the text.
```

##### Methods

###### `def __init__(self, *, text: str, entities: List['types.MessageEntity'] = None)`

_No docstring._

###### `def _parse(client, translate_result: 'raw.types.TextWithEntities') -> 'TranslatedText'`

_No docstring._

---

## File: `types/messages_and_media/venue.py`

### Classes

#### `class Venue(Object)`

```text
A venue.

Parameters:
    location (:obj:`~pyrogram.types.Location`):
        Venue location.

    title (``str``):
        Name of the venue.

    address (``str``):
        Address of the venue.

    foursquare_id (``str``, *optional*):
        Foursquare identifier of the venue.

    foursquare_type (``str``, *optional*):
        Foursquare type of the venue.
        (For example, "arts_entertainment/default", "arts_entertainment/aquarium" or "food/icecream".)
```

##### Methods

###### `def __init__(self, *, client: 'pyrogram.Client' = None, location: 'types.Location', title: str, address: str, foursquare_id: str = None, foursquare_type: str = None)`

_No docstring._

###### `def _parse(client, venue: 'raw.types.MessageMediaVenue')`

_No docstring._

---

## File: `types/messages_and_media/video.py`

### Classes

#### `class Video(Object)`

```text
A video file.

Parameters:
    file_id (``str``):
        Identifier for this file, which can be used to download or reuse the file.

    file_unique_id (``str``):
        Unique identifier for this file, which is supposed to be the same over time and for different accounts.
        Can't be used to download or reuse the file.

    width (``int``):
        Video width as defined by sender.

    height (``int``):
        Video height as defined by sender.

    duration (``int``):
        Duration of the video in seconds as defined by sender.

    file_name (``str``, *optional*):
        Video file name.

    mime_type (``str``, *optional*):
        Mime type of a file as defined by sender.

    file_size (``int``, *optional*):
        File size.

    supports_streaming (``bool``, *optional*):
        True, if the video was uploaded with streaming support.

    ttl_seconds (``int``. *optional*):
        Time-to-live seconds, for secret photos.

    date (:py:obj:`~datetime.datetime`, *optional*):
        Date the video was sent.

    thumbs (List of :obj:`~pyrogram.types.Thumbnail`, *optional*):
        Video thumbnails.

    cover (:obj:`~pyrogram.types.Photo`, *optional*):
        Video cover.

    start_timestamp (``int``, *optional*):
        Video startpoint, in seconds.
```

##### Methods

###### `def __init__(self, *, client: 'pyrogram.Client' = None, file_id: str, file_unique_id: str, width: int, height: int, duration: int, file_name: str = None, mime_type: str = None, file_size: int = None, supports_streaming: bool = None, ttl_seconds: int = None, date: datetime = None, thumbs: List['types.Thumbnail'] = None, cover: 'types.Photo' = None, start_timestamp: int = None)`

_No docstring._

###### `def _parse(client, video: 'raw.types.Document', video_attributes: 'raw.types.DocumentAttributeVideo', file_name: str, ttl_seconds: int = None, cover = None, start_timestamp: int = None) -> 'Video'`

_No docstring._

---

## File: `types/messages_and_media/video_note.py`

### Classes

#### `class VideoNote(Object)`

```text
A video note.

Parameters:
    file_id (``str``):
        Identifier for this file, which can be used to download or reuse the file.

    file_unique_id (``str``):
        Unique identifier for this file, which is supposed to be the same over time and for different accounts.
        Can't be used to download or reuse the file.

    length (``int``):
        Video width and height as defined by sender.

    duration (``int``):
        Duration of the video in seconds as defined by sender.

    mime_type (``str``, *optional*):
        MIME type of the file as defined by sender.

    file_size (``int``, *optional*):
        File size.

    date (:py:obj:`~datetime.datetime`, *optional*):
        Date the video note was sent.

    thumbs (List of :obj:`~pyrogram.types.Thumbnail`, *optional*):
        Video thumbnails.
```

##### Methods

###### `def __init__(self, *, client: 'pyrogram.Client' = None, file_id: str, file_unique_id: str, length: int, duration: int, thumbs: List['types.Thumbnail'] = None, mime_type: str = None, file_size: int = None, date: datetime = None)`

_No docstring._

###### `def _parse(client, video_note: 'raw.types.Document', video_attributes: 'raw.types.DocumentAttributeVideo') -> 'VideoNote'`

_No docstring._

---

## File: `types/messages_and_media/voice.py`

### Classes

#### `class Voice(Object)`

```text
A voice note.

Parameters:
    file_id (``str``):
        Identifier for this file, which can be used to download or reuse the file.

    file_unique_id (``str``):
        Unique identifier for this file, which is supposed to be the same over time and for different accounts.
        Can't be used to download or reuse the file.

    duration (``int``):
        Duration of the audio in seconds as defined by sender.

    waveform (``bytes``, *optional*):
        Voice waveform.

    mime_type (``str``, *optional*):
        MIME type of the file as defined by sender.

    file_size (``int``, *optional*):
        File size.

    date (:py:obj:`~datetime.datetime`, *optional*):
        Date the voice was sent.
```

##### Methods

###### `def __init__(self, *, client: 'pyrogram.Client' = None, file_id: str, file_unique_id: str, duration: int, waveform: bytes = None, mime_type: str = None, file_size: int = None, date: datetime = None)`

_No docstring._

###### `def _parse(client, voice: 'raw.types.Document', attributes: 'raw.types.DocumentAttributeAudio') -> 'Voice'`

_No docstring._

---

## File: `types/messages_and_media/wallpaper.py`

### Classes

#### `class Wallpaper(Object)`

```text
A wallpaper.

parameters:
    id (``int``):
        Unique identifier for this wallpaper.

    slug (``str``):
        The slug of the wallpaper.

    document (:obj:`~pyrogram.types.Document`):
        The document of the wallpaper.

    is_creator (:obj:`bool`, optional):
        True, if the wallpaper was created by the current user.

    is_default (:obj:`bool`, optional):
        True, if the wallpaper is the default wallpaper.

    is_pattern (:obj:`bool`, optional):
        True, if the wallpaper is a pattern.

    id_dark (:obj:`bool`, optional):
        True, if the wallpaper is dark.

    settings (:obj:`~pyrogram.types.WallpaperSettings`, optional):
        The settings of the wallpaper.
```

##### Methods

###### `def __init__(self, id: int, slug: str, document: 'types.Document' = None, is_creator: bool = None, is_default: bool = None, is_pattern: bool = None, is_dark: bool = None, settings: 'types.WallpaperSettings' = None)`

_No docstring._

###### `def _parse(client: 'pyrogram.Client', wallpaper: 'raw.base.WallPaper') -> 'Wallpaper'`

_No docstring._

---

## File: `types/messages_and_media/wallpaper_settings.py`

### Classes

#### `class WallpaperSettings(Object)`

```text
A wallpaper settings.

parameters:
    is_blur (``bool``, *optional*):
        True, if the wallpaper is blurred.

    is_motion (``bool``, *optional*):
        True, if the wallpaper is motion.

    background_color (``int``, *optional*):
        The background color of the wallpaper.

    second_background_color (``int``, *optional*):
        The second background color of the wallpaper.

    third_background_color (``int``, *optional*):
        The third background color of the wallpaper.

    fourth_background_color (``int``, *optional*):
        The fourth background color of the wallpaper.

    intensity (``int``, *optional*):
        The intensity of the wallpaper.

    rotation (``int``, *optional*):
        The rotation of the wallpaper.

    emoticon (``str``, *optional*):
        The emoticon of the wallpaper.
```

##### Methods

###### `def __init__(self, is_blur: bool = None, is_motion: bool = None, background_color: int = None, second_background_color: int = None, third_background_color: int = None, fourth_background_color: int = None, intensity: int = None, rotation: int = None, emoticon: str = None)`

_No docstring._

###### `def _parse(wallpaper_settings: 'raw.types.WallPaperSettings') -> 'WallpaperSettings'`

_No docstring._

---

## File: `types/messages_and_media/web_app_data.py`

### Classes

#### `class WebAppData(Object)`

```text
Contains data sent from a `Web App <https://core.telegram.org/bots/webapps>`_ to the bot.

Parameters:
    data (``str``):
        The data.

    button_text (``str``):
        Text of the *web_app* keyboard button, from which the Web App was opened.
```

##### Methods

###### `def __init__(self, *, data: str, button_text: str)`

_No docstring._

###### `def _parse(action: 'raw.types.MessageActionWebViewDataSentMe')`

_No docstring._

---

## File: `types/messages_and_media/web_page.py`

### Classes

#### `class WebPage(Object)`

```text
A webpage preview

Parameters:
    id (``str``):
        Unique identifier for this webpage.

    url (``str``):
        Full URL for this webpage.

    display_url (``str``):
        Display URL for this webpage.

    type (``str``, *optional*):
        Type of webpage preview, known types (at the time of writing) are:
        *"article"*, *"photo"*, *"gif"*, *"video"* and *"document"*,
        *"telegram_user"*, *"telegram_bot"*, *"telegram_channel"*, *"telegram_megagroup"*.

    site_name (``str``, *optional*):
        Webpage site name.

    title (``str``, *optional*):
        Title of this webpage.

    description (``str``, *optional*):
        Description of this webpage.

    audio (:obj:`~pyrogram.types.Audio`, *optional*):
        Webpage preview is an audio file, information about the file.

    document (:obj:`~pyrogram.types.Document`, *optional*):
        Webpage preview is a general file, information about the file.

    photo (:obj:`~pyrogram.types.Photo`, *optional*):
        Webpage preview is a photo, information about the photo.

    animation (:obj:`~pyrogram.types.Animation`, *optional*):
        Webpage preview is an animation, information about the animation.

    video (:obj:`~pyrogram.types.Video`, *optional*):
        Webpage preview is a video, information about the video.

    embed_url (``str``, *optional*):
        Embedded content URL.

    embed_type (``str``, *optional*):
        Embedded content type, like `iframe`

    embed_width (``int``, *optional*):
        Embedded content width.

    embed_height (``int``, *optional*):
        Embedded content height.

    duration (``int``, *optional*):
        Unknown at the time of writing.

    author (``str``, *optional*):
        Author of the webpage, eg the Twitter user for a tweet, or the author in an article.
```

##### Methods

###### `def __init__(self, *, client: 'pyrogram.Client' = None, id: str, url: str, display_url: str, type: str = None, site_name: str = None, title: str = None, description: str = None, audio: 'types.Audio' = None, document: 'types.Document' = None, photo: 'types.Photo' = None, animation: 'types.Animation' = None, video: 'types.Video' = None, embed_url: str = None, embed_type: str = None, embed_width: int = None, embed_height: int = None, duration: int = None, author: str = None)`

_No docstring._

###### `def _parse(client, webpage: 'raw.types.WebPage') -> 'WebPage'`

_No docstring._

---

## File: `types/messages_and_media/web_page_empty.py`

### Classes

#### `class WebPageEmpty(Object)`

```text
A webpage preview

Parameters:
    id (``str``):
        Unique identifier for this webpage.

    url (``str``):
        Full URL for this webpage.
```

##### Methods

###### `def __init__(self, *, id: str, url: str)`

_No docstring._

###### `def _parse(webpage: 'raw.types.WebPageEmpty') -> 'WebPageEmpty'`

_No docstring._

---

## File: `types/messages_and_media/web_page_preview.py`

### Classes

#### `class WebPagePreview(Object)`

```text
A web page preview.

Parameters:
    webpage (:obj:`~pyrogram.types.WebPageEmpty` | :obj:`~pyrogram.types.WebPage`):
        Web Page Information.

    force_large_media (``bool``, *optional*):
        True, If the preview media size is forced to large.

    force_small_media  (``bool``, *optional*):
        True, If the preview media size is forced to small.

    is_safe (``bool``, *optional*):
        True, If the webpage is considered safe by telegram.
```

##### Methods

###### `def __init__(self, *, webpage: Union['types.WebPage', 'types.WebPageEmpty'], force_large_media: bool = None, force_small_media: bool = None, invert_media: bool = None, is_safe: bool = None)`

_No docstring._

###### `def _parse(client, web_page_preview: Union['raw.types.WebPage', 'raw.types.WebPageEmpty'], invert_media: bool = None)`

_No docstring._

---

## File: `types/object.py`

### Classes

#### `class Object`

_No docstring._

##### Methods

###### `def __init__(self, client: 'pyrogram.Client' = None)`

_No docstring._

###### `def bind(self, client: 'pyrogram.Client')`

```text
Bind a Client instance to this and to all nested Pyrogram objects.

Parameters:
    client (:obj:`~pyrogram.types.Client`):
        The Client instance to bind this object with. Useful to re-enable bound methods after serializing and
        deserializing Pyrogram objects with ``repr`` and ``eval``.
```

###### `def default(obj: 'Object')`

_No docstring._

###### `def __str__(self) -> str`

_No docstring._

###### `def __repr__(self) -> str`

_No docstring._

###### `def __eq__(self, other: 'Object') -> bool`

_No docstring._

###### `def __setstate__(self, state)`

_No docstring._

###### `def __getstate__(self)`

_No docstring._

---

## File: `types/payments/__init__.py`

---

## File: `types/payments/checked_gift_code.py`

### Classes

#### `class CheckedGiftCode(Object)`

```text
Contains checked gift code data.

Parameters:
    date (:py:obj:`~datetime.datetime`):
        Date when the giveaway was launched.

    months (``int``):
        Number of months of subscription.

    via_giveaway (``bool``, *optional*):
        True if the gift code is received via giveaway.

    from_chat (:obj:`~pyrogram.types.Chat`, *optional*):
        The channel where the gift code was won.

    winner (:obj:`~pyrogram.types.User`, *optional*):
        The user who won the giveaway.

    giveaway_message_id (``int``, *optional*):
        Identifier of the message from chat where the giveaway was launched.

    used_date (:py:obj:`~datetime.datetime`, *optional*):
        Date when the gift code was used.
```

##### Methods

###### `def __init__(self, *, date: datetime, months: int, via_giveaway: bool = None, from_chat: 'types.Chat' = None, winner: 'types.User' = None, giveaway_message_id: int = None, used_date: datetime = None)`

_No docstring._

###### `def _parse(client, checked_gift_code: 'raw.types.payments.CheckedGiftCode', users, chats)`

_No docstring._

---

## File: `types/payments/extended_media_preview.py`

### Classes

#### `class ExtendedMediaPreview(Object)`

```text
A ExtendedMediaPreview.

Parameters:
    width (``int``, *optional*):
        Media Width.

    height (``int``, *optional*):
        Media Height.

    thumb (:obj:`~pyrogram.types.StrippedThumbnail`, *optional*):
        Media Thumbnail.

    video_duration (``int``, *optional*):
        Video duration.
```

##### Methods

###### `def __init__(self, *, width: int = None, height: int = None, thumb: 'types.Thumbnail' = None, video_duration: int = None)`

_No docstring._

###### `def _parse(client, media: 'raw.types.MessageExtendedMediaPreview') -> 'ExtendedMediaPreview'`

_No docstring._

---

## File: `types/payments/gift.py`

### Classes

#### `class Gift(Object)`

```text
A star gift.

Parameters:
    id (``int``):
        Unique star gift identifier.

    sticker (:obj:`~pyrogram.types.Sticker`, *optional*):
        Information about the star gift sticker.

    caption (``str``, *optional*):
        Text message.

    caption_entities (List of :obj:`~pyrogram.types.MessageEntity`, *optional*):
        For text messages, special entities like usernames, URLs, bot commands, etc. that appear in the text.

    message_id (``int``, *optional*):
        Unique message identifier.

    upgrade_message_id (``int``, *optional*):
        Unique message identifier.
        For unique gifts only.

    name (``str``, *optional*):
        Name of the star gift.
        For unique gifts only.

    title (``str``, *optional*):
        Title of the star gift.
        For unique gifts only.

    collectible_id (``int``, *optional*):
        Collectible number of the star gift.
        For unique gifts only.

    attributes (List of :obj:`~pyrogram.types.GiftAttribute`, *optional*):
        Attributes of the star gift.
        For unique gifts only.

    date (:py:obj:`~datetime.datetime`, *optional*):
        Date when the star gift was received.

    first_sale_date (:py:obj:`~datetime.datetime`, *optional*):
        Date when the star gift was first purchased.

    last_sale_date (:py:obj:`~datetime.datetime`, *optional*):
        Date when the star gift was last purchased.

    from_user (:obj:`~pyrogram.types.User`, *optional*):
        User who sent the star gift.

    owner (:obj:`~pyrogram.types.Chat`, *optional*):
        Only available if the nfts is in telegram.

    owner_name (``str``, *optional*):
        Name of the user who received the star gift.

    owner_address (``str``, *optional*):
        Only available if the nfts is in ton network.

    ton_address (``str``, *optional*):
        Only available if the nfts is in ton network.

    price (``int``, *optional*):
        Price of this gift in stars.

    convert_price (``int``, *optional*):
        The number of stars you get if you convert this gift.

    upgrade_price (``int``, *optional*):
        The number of stars you need to upgrade this gift.

    transfer_price (``int``, *optional*):
        The number of stars you need to transfer this gift.

    available_amount (``int``, *optional*):
        The number of gifts available for purchase.
        Returned only if is_limited is True.

    resale_amount (``int``, *optional*):
        The number of gifts available for resale.
        Returned only if is_limited is True.

    total_amount (``int``, *optional*):
        Total amount of gifts.
        Returned only if is_limited is True.

    can_upgrade (``bool``, *optional*):
        True, if the gift can be upgraded.

    can_export_at (:py:obj:`~datetime.datetime`, *optional*):
        Date when the gift can be exported via blockchain.

    is_limited (``bool``, *optional*):
        True, if the number of gifts is limited.

    is_name_hidden (``bool``, *optional*):
        True, if the sender's name is hidden.

    is_saved (``bool``, *optional*):
        True, if the star gift is saved in profile.

    is_sold_out (``bool``, *optional*):
        True, if the star gift is sold out.

    is_converted (``bool``, *optional*):
        True, if the gift was converted to Telegram Stars.
        Only for the receiver of the gift.

    is_upgraded (``bool``, *optional*):
        True, if the gift was upgraded.

    is_refunded (``bool``, *optional*):
        True, if the gift was refunded.

    is_transferred (``bool``, *optional*):
        True, if the gift was transferred.

    is_birthday (``bool``, *optional*):
        True, if the gift is a birthday gift.

    raw (:obj:`~pyrogram.raw.base.StarGift`, *optional*):
        The raw object as received from the server.

    link (``str``, *property*):
        A link to the gift.
        For unique gifts only.
```

##### Methods

###### `def __init__(self, *, client: 'pyrogram.Client' = None, id: int, sticker: 'types.Sticker' = None, caption: Optional[str] = None, caption_entities: List['types.MessageEntity'] = None, message_id: Optional[int] = None, date: Optional[datetime] = None, first_sale_date: Optional[datetime] = None, last_sale_date: Optional[datetime] = None, from_user: Optional['types.User'] = None, owner: Optional['types.Chat'] = None, owner_name: Optional[str] = None, owner_address: Optional[str] = None, ton_address: Optional[str] = None, price: Optional[int] = None, convert_price: Optional[int] = None, upgrade_price: Optional[int] = None, transfer_price: Optional[int] = None, upgrade_message_id: Optional[int] = None, name: Optional[str] = None, title: Optional[str] = None, collectible_id: Optional[int] = None, attributes: Optional[List['types.GiftAttribute']] = None, available_amount: Optional[int] = None, resale_amount: Optional[int] = None, total_amount: Optional[int] = None, can_upgrade: Optional[bool] = None, can_export_at: Optional[datetime] = None, is_limited: Optional[bool] = None, is_name_hidden: Optional[bool] = None, is_saved: Optional[bool] = None, is_sold_out: Optional[bool] = None, is_converted: Optional[bool] = None, is_upgraded: Optional[bool] = None, is_refunded: Optional[bool] = None, is_transferred: Optional[bool] = None, is_birthday: Optional[bool] = None, raw: Optional['raw.base.StarGift'] = None)`

_No docstring._

###### `async def _parse(client, gift, users = None, chats = None)`

_No docstring._

###### `async def _parse_regular(client, star_gift: 'raw.types.StarGift') -> 'Gift'`

_No docstring._

###### `async def _parse_unique(client, star_gift: 'raw.types.StarGiftUnique', users: Dict[int, 'raw.types.User'] = None, chats: Dict[int, 'raw.types.Chat'] = None) -> 'Gift'`

_No docstring._

###### `async def _parse_saved(client, saved_gift: 'raw.types.SavedStarGift', users: Dict[int, 'raw.types.User'] = None, chats: Dict[int, 'raw.types.Chat'] = None) -> 'Gift'`

_No docstring._

###### `async def _parse_action(client, message: 'raw.base.Message', users: Dict[int, 'raw.types.User'] = None, chats: Dict[int, 'raw.types.Chat'] = None) -> 'Gift'`

_No docstring._

###### `def link(self) -> Optional[str]`

_No docstring._

###### `async def show(self) -> bool`

```text
Bound method *show* of :obj:`~pyrogram.types.Gift`.

Use as a shortcut for:

.. code-block:: python

    await client.show_gift(
        message_id=message_id
    )

Example:
    .. code-block:: python

        await gift.show()

Returns:
    ``bool``: On success, True is returned.
```

###### `async def hide(self) -> bool`

```text
Bound method *hide* of :obj:`~pyrogram.types.Gift`.

Use as a shortcut for:

.. code-block:: python

    await client.hide_gift(
        message_id=message_id
    )

Example:
    .. code-block:: python

        await gift.hide()

Returns:
    ``bool``: On success, True is returned.
```

###### `async def convert(self) -> bool`

```text
Bound method *convert* of :obj:`~pyrogram.types.Gift`.

Use as a shortcut for:

.. code-block:: python

    await client.convert_gift(
        message_id=message_id
    )

Example:
    .. code-block:: python

        await gift.convert()

Returns:
    ``bool``: On success, True is returned.
```

###### `async def upgrade(self) -> bool`

```text
Bound method *upgrade* of :obj:`~pyrogram.types.Gift`.

Use as a shortcut for:

.. code-block:: python

    await client.upgrade_gift(
        message_id=message_id
    )

Example:
    .. code-block:: python

        await gift.upgrade()

Returns:
    ``bool``: On success, True is returned.
```

###### `async def transfer(self, to_chat_id: Union[int, str]) -> bool`

```text
Bound method *transfer* of :obj:`~pyrogram.types.Gift`.

Use as a shortcut for:

.. code-block:: python

    await client.transfer_gift(
        message_id=message_id,
        to_chat_id=to_chat_id
    )

Example:
    .. code-block:: python

        await gift.transfer(to_chat_id=123)

Returns:
    ``bool``: On success, True is returned.
```

###### `async def wear(self) -> bool`

```text
Bound method *wear* of :obj:`~pyrogram.types.Gift`.

.. note::

    This works for upgraded gifts only.

Use as a shortcut for:

.. code-block:: python

    await client.set_emoji_status(types.EmojiStatus(gift_id=123))

Example:
    .. code-block:: python

        await star_gift.wear()

Returns:
    ``bool``: On success, True is returned.
```

---

## File: `types/payments/gift_attribute.py`

### Classes

#### `class GiftAttribute(Object)`

```text
Contains information about a star gift attribute.

Parameters:
    type (:obj:`~pyrogram.enums.GiftAttributeType`):
        Type of the attribute.

    name (``str``, *optional*):
        Name of the attribute.

    rarity (``int``, *optional*):
        Rarity of the attribute in permilles.
        For example, 15 means 1.5%. So only 1.5% of such collectibles have this attribute.

    date (:py:obj:`~datetime.datetime`, *optional*):
        Date when the gift was received.
        Available only if the original details are available.

    caption (``str``, *optional*):
        Text message.
        Available only if the original details are available.

    caption_entities (List of :obj:`~pyrogram.types.MessageEntity`, *optional*):
        For text messages, special entities like usernames, URLs, bot commands, etc. that appear in the text.
        Available only if the original details are available.

    from_user (:obj:`~pyrogram.types.User`, *optional*):
        User who sent the gift.
        Available only if the original details are available.

    to_user (:obj:`~pyrogram.types.User`, *optional*):
        User who received the gift.
        Available only if the original details are available.

    center_color (``int``, *optional*):
        Center color of the gift in decimal format.
        Available only if the backdrop attribute is available.

    edge_color (``int``, *optional*):
        Edge color of the gift in decimal format.
        Available only if the backdrop attribute is available.

    pattern_color (``int``, *optional*):
        Pattern color of the gift in decimal format.
        Available only if the backdrop attribute is available.

    text_color (``int``, *optional*):
        Text color of the gift in decimal format.
        Available only if the backdrop attribute is available.

    sticker (:obj:`~pyrogram.types.Sticker`, *optional*):
        Information about the sticker.
```

##### Methods

###### `def __init__(self, *, client: 'pyrogram.Client' = None, type: 'enums.GiftAttributeType', name: Optional[str] = None, rarity: Optional[int] = None, date: Optional[datetime] = None, caption: Optional[str] = None, caption_entities: Optional[List['types.MessageEntity']] = None, from_user: Optional['types.User'] = None, to_user: Optional['types.User'] = None, sticker: Optional['types.Sticker'] = None, center_color: Optional[int] = None, edge_color: Optional[int] = None, pattern_color: Optional[int] = None, text_color: Optional[int] = None)`

_No docstring._

###### `async def _parse(client, attr: 'raw.base.StarGiftAttribute', users: Dict[int, 'raw.types.User']) -> 'GiftAttribute'`

_No docstring._

---

## File: `types/payments/gift_code.py`

### Classes

#### `class GiftCode(Object)`

```text
A service message about a gift code.

parameters:
    months (``int``):
        How long the telegram premium last (in month).

    slug (``str``):
        The slug of the gift code.

    is_giveaway (``bool``, *optional*):
        True, if the gift code is from a giveaway.

    is_unclaimed (``bool``, *optional*):
        True, if the gift code is unclaimed.

    boosted_chat (:obj:`~pyrogram.types.Chat`, *optional*):
        The chat that the gift code boost.

    currency (``str``, *optional*):
        The currency of the gift code.

    amount (``int``, *optional*):
        The amount of the gift code.

    crypto_currency (``str``, *optional*):
        The crypto currency of the gift code.

    crypto_amount (``int``, *optional*):
        The crypto amount of the gift code.
```

##### Methods

###### `def __init__(self, months: int, slug: str, is_giveaway: bool = None, is_unclaimed: bool = None, boosted_chat: 'types.Chat' = None, currency: str = None, amount: int = None, crypto_currency: str = None, crypto_amount: int = None)`

_No docstring._

###### `def _parse(client: 'pyrogram.Client', gift_code: 'types.GiftCode', chats: Dict[int, 'raw.types.Chat']) -> 'GiftCode'`

_No docstring._

---

## File: `types/payments/gifted_premium.py`

### Classes

#### `class GiftedPremium(Object)`

```text
Telegram Premium was gifted to the user

Parameters:
    gifter_user_id (``int``):
        The identifier of a user that gifted Telegram Premium; 0 if the gift was anonymous

    currency (``str``):
        Currency for the paid amount

    amount (``int``):
        The paid amount, in the smallest units of the currency

    cryptocurrency (``str``):
        Cryptocurrency used to pay for the gift; may be empty if none

    cryptocurrency_amount (``int``):
        The paid amount, in the smallest units of the cryptocurrency; 0 if none

    month_count (``int``):
        Number of months the Telegram Premium subscription will be active
```

##### Methods

###### `def __init__(self, *, gifter_user_id: int = None, currency: str = None, amount: int = None, cryptocurrency: str = None, cryptocurrency_amount: int = None, month_count: int = None)`

_No docstring._

###### `async def _parse(client, gifted_premium: 'raw.types.MessageActionGiftPremium', gifter_user_id: int) -> 'GiftedPremium'`

_No docstring._

---

## File: `types/payments/input_stars_transaction.py`

### Classes

#### `class InputStarsTransaction(Object)`

```text
Content of a stars transaction.

Parameters:
    id (``str``):
        Unique transaction identifier.

    is_refund (``bool``, *optional*):
        True, If the transaction is a refund.
```

##### Methods

###### `def __init__(self, *, id: str, is_refund: bool = None)`

_No docstring._

###### `async def write(self)`

_No docstring._

---

## File: `types/payments/invoice.py`

### Classes

#### `class Invoice(Object)`

```text
Contains information about an Invoice.

Parameters:
    title (``str``):
        Product name.

    description (``str``):
        Product description.

    currency (``str``):
        Currency code.

    total_amount (``int``):
        Total price in the smallest units of the currency.

    start_parameter (``str``):
        Unique bot deep-linking parameter that can be used to generate this invoice.

    shipping_address_requested (``bool``, *optional*):
        True, if the the shipping address is requested.

    test (``bool``, *optional*):
        True, if the invoice is a test invoice.

    receipt_message_id (``int``, *optional*):
        The message_id of the message sent to the chat when the invoice is paid.
```

##### Methods

###### `def __init__(self, *, title: str, description: str, currency: str, total_amount: int, start_parameter: str, shipping_address_requested: bool = None, test: bool = None, receipt_message_id: int = None)`

_No docstring._

###### `def _parse(message_invoice: 'raw.types.MessageMediaInvoice') -> 'Invoice'`

_No docstring._

---

## File: `types/payments/labeled_price.py`

### Classes

#### `class LabeledPrice(Object)`

```text
This object represents a price for goods or services.

Parameters:
    label (``str``):
        Portion label.

    amount (``int``):
        Price of the product in the smallest units of the currency (integer, not float/double).
        The minimum amuont for telegram stars is 1.
        The minimum amount for other currencies is US$1.
        you need to add 2 extra zeros to the amount (except stars), example 100 for 1 usd.
```

##### Methods

###### `def __init__(self, label: str, amount: int)`

_No docstring._

###### `def write(self)`

_No docstring._

---

## File: `types/payments/paid_media.py`

### Classes

#### `class PaidMedia(Object)`

```text
A PaidMedia.

Parameters:
    stars_amount (``int``):
        Amount of stars.

    extended_media (List of :obj:`~pyrogram.types.Animation` | :obj:`~pyrogram.types.ExtendedMediaPreview` | :obj:`~pyrogram.types.Photo` | :obj:`~pyrogram.types.Video`, *optional*):
        Extended media.
```

##### Methods

###### `def __init__(self, *, stars_amount: int, extended_media: List[Union['types.Animation', 'types.ExtendedMediaPreview', 'types.Photo', 'types.Video']] = None)`

_No docstring._

###### `def _parse(client, media: 'raw.types.MessageMediaPaidMedia') -> 'PaidMedia'`

_No docstring._

---

## File: `types/payments/paid_message_price_changed.py`

### Classes

#### `class PaidMessagePriceChanged(Object)`

```text
A PaidMessagePriceChanged.

Parameters:
    stars_amount (``int``):
        Amount of stars.

    extended_media (List of :obj:`~pyrogram.types.Animation` | :obj:`~pyrogram.types.ExtendedMediaPreview` | :obj:`~pyrogram.types.Photo` | :obj:`~pyrogram.types.Video`, *optional*):
        Extended media.
```

##### Methods

###### `def __init__(self, *, stars_amount: int)`

_No docstring._

###### `def _parse(action: 'raw.types.MessageActionPaidMessagesPrice') -> 'PaidMessagePriceChanged'`

_No docstring._

---

## File: `types/payments/payment_form.py`

### Classes

#### `class PaymentForm(Object)`

```text
This object contains basic information about an payment form.

Parameters:
    id (``int``):
        Form id.

    bot (``str``):
        Bot.

    title (``str``):
        Form title.

    description (``str``):
        Form description.

    invoice (``str``):
        Invoice.

    provider (``str``, *optional*):
        Payment provider.

    url (``str``, *optional*):
        Payment form URL.

    can_save_credentials (``str``, *optional*):
        Whether the user can choose to save credentials.

    is_password_missing (``str``, *optional*):
        Indicates that the user can save payment credentials,
        but only after setting up a 2FA password
        (currently the account doesn't have a 2FA password).

    native_provider (``str``, *optional*):
        Payment provider name.

    raw (:obj:`~raw.base.payments.PaymentForm`, *optional*):
        The raw object, as received from the Telegram API.
```

##### Methods

###### `def __init__(self, *, client: 'pyrogram.Client' = None, id: int, bot: 'types.User', title: str, description: str, invoice: 'types.Invoice', provider: Optional['types.User'] = None, url: Optional[str] = None, can_save_credentials: Optional[bool] = None, is_password_missing: Optional[bool] = None, native_provider: Optional[str] = None, raw: 'raw.base.payments.PaymentForm' = None)`

_No docstring._

###### `def _parse(client, payment_form: 'raw.base.payments.PaymentForm') -> 'PaymentForm'`

_No docstring._

---

## File: `types/payments/payment_info.py`

### Classes

#### `class PaymentInfo(Object)`

```text
Contains information about a payment.

Parameters:
    name (``str``, *optional*):
        User's name.

    phone_number (``str``, *optional*):
        User's phone number.

    email (``str``, *optional*):
        User's email.

    shipping_address (:obj:`~pyrogram.types.ShippingAddress`, *optional*):
        User's shipping address.
```

##### Methods

###### `def __init__(self, *, name: str = None, phone_number: str = None, email: str = None, shipping_address: 'types.ShippingAddress' = None)`

_No docstring._

---

## File: `types/payments/payment_refunded.py`

### Classes

#### `class PaymentRefunded(Object)`

```text
Contains information about a refunded payment.

Parameters:
    user (:obj:`~pyrogram.types.User`):
        The user that refunded the payment.

    currency (``str``):
        Three-letter ISO 4217 currency code.

    total_amount (``int``):
        Total price in the smallest units of the currency.

    payload (``str``, *optional*):
        Bot specified invoice payload. Only available to the bot that received the payment.

    telegram_payment_charge_id (``str``, *optional*):
        Telegram payment identifier.

    provider_payment_charge_id (``str``, *optional*):
        Provider payment identifier.
```

##### Methods

###### `def __init__(self, *, user: 'types.User', currency: str, total_amount: str, telegram_payment_charge_id: str, provider_payment_charge_id: str, payload: str = None)`

_No docstring._

###### `async def _parse(client: 'pyrogram.Client', payment_refunded: 'raw.types.MessageActionPaymentRefunded') -> 'PaymentRefunded'`

_No docstring._

---

## File: `types/payments/purchased_paid_media.py`

### Classes

#### `class PurchasedPaidMedia(Object)`

```text
This object represents information about purchased paid media.

Parameters:
    from_user (:obj:`~pyrogram.types.User`):
        User who bought the paid media.

    payload (``str``):
        Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user, use for your internal processes.
```

##### Methods

###### `def __init__(self, from_user: 'types.User', payload: str)`

_No docstring._

###### `def _parse(client, purchased_media: 'raw.types.UpdateBotPurchasedPaidMedia', users) -> 'PurchasedPaidMedia'`

_No docstring._

---

## File: `types/payments/stars_status.py`

### Classes

#### `class StarsStatus(Object)`

```text
Contains information about stars status.

Parameters:
    balance (``int``):
        Current balance of stars.

    history (List of :obj:`~pyrogram.types.StarsTransaction`):
        Stars transactions history.
```

##### Methods

###### `def __init__(self, *, balance: int, history: list)`

_No docstring._

###### `def _parse(client, stars_status: 'raw.types.StarsStatus') -> 'StarsStatus'`

_No docstring._

---

## File: `types/payments/stars_transaction.py`

### Classes

#### `class StarsTransaction(Object)`

```text
Contains information about stars transaction.

Parameters:
    id (``int``):
        Unique transaction identifier.

    stars (``int``):
        Amount of stars in the transaction.

    date (:py:obj:`~datetime.datetime`):
        Date of the transaction.

    chat (:obj:`~pyrogram.types.Chat`):
        Chat where the transaction was made.

    is_refund (``bool``, *optional*):
        True, If the transaction is a refund.

    is_pending (``bool``, *optional*):
        True, If the transaction is pending.

    is_failed (``bool``, *optional*):
        True, If the transaction failed.

    title (``str``, *optional*):
        Title of the transaction.

    description (``str``, *optional*):
        Description of the transaction.

    transaction_date (:py:obj:`~datetime.datetime`, *optional*):
        Date of the transaction.

    transaction_url (``str``, *optional*):
        URL of the transaction.

    payload (``str``, *optional*):
        Payload of the transaction.

    message_id (``int``, *optional*):
        Identifier of the message where the transaction was made.
```

##### Methods

###### `def __init__(self, *, id: int, stars: int, date: datetime, chat: 'types.Chat', is_refund: bool = None, is_pending: bool = None, is_failed: bool = None, title: str = None, description: str = None, transaction_date: datetime = None, transaction_url: str = None, payload: str = None, message_id: int = None)`

_No docstring._

###### `def _parse(client, transaction: 'raw.types.StarsTransaction', users: Dict[int, 'raw.types.User']) -> 'StarsTransaction'`

_No docstring._

---

## File: `types/payments/successful_payment.py`

### Classes

#### `class SuccessfulPayment(Object)`

```text
Contains information about a successful payment.

Parameters:
    currency (``str``):
        Three-letter ISO 4217 currency code.

    total_amount (``int``):
        Total price in the smallest units of the currency.

    payload (``str``, *optional*):
        Bot specified invoice payload. Only available to the bot that received the payment.

    telegram_payment_charge_id (``str``, *optional*):
        Telegram payment identifier. Only available to the bot that received the payment.

    provider_payment_charge_id (``str``, *optional*):
        Provider payment identifier. Only available to the bot that received the payment.

    shipping_option_id (``str``, *optional*):
        Identifier of the shipping option chosen by the user. Only available to the bot that received the payment.

    payment_info (:obj:`~pyrogram.types.PaymentInfo`, *optional*):
        Payment information provided by the user. Only available to the bot that received the payment.
```

##### Methods

###### `def __init__(self, *, currency: str, total_amount: str, payload: str, telegram_payment_charge_id: str, provider_payment_charge_id: str, shipping_option_id: str = None, payment_info: 'types.PaymentInfo' = None)`

_No docstring._

###### `def _parse(client: 'pyrogram.Client', successful_payment) -> 'SuccessfulPayment'`

_No docstring._

---

## File: `types/pyromod/__init__.py`

---

## File: `types/pyromod/identifier.py`

### Classes

#### `class Identifier`

```text
A dataclass that serves as a utility for matching listeners to the data of updates.

Parameters:
    inline_message_id (``str`` | Iterable of ``str``, *optional*):
        The inline message ID to match. If None, it is not considered for matching.

    chat_id (``int`` | ``str`` | Iterable of ``int`` | Iterable of ``str``, *optional*):
        The chat ID to match. If None, it is not considered for matching.

    message_id (``int``  | Iterable of ``int``):
        The message ID to match. If None, it is not considered for matching.

    from_user_id (``int`` | ``str`` | Iterable of ``int`` | Iterable of ``str``, *optional*):
        The user ID to match. If None, it is not considered for matching.
```

##### Methods

###### `def matches(self, update: 'Identifier') -> bool`

_No docstring._

###### `def count_populated(self)`

_No docstring._

---

## File: `types/pyromod/listener.py`

### Classes

#### `class Listener`

```text
Designed to manage and handle different types of listeners used in pyromod.
It enables you to wait for specific events like messages or callback queries and provides mechanisms for defining the conditions and filters that trigger these listeners.

Parameters:
    listener_type (:obj:`~pyrogram.enums.ListenerTypes`):
        The type of listener that specifies the event you want to listen for.
        It can be either a “message” or a “callback_query.”

    filters (:meth:`~pyrogram.filters.Filter`):
        The chat ID to match. If None, it is not considered for matching.

    unallowed_click_alert (``bool``):
        A flag that determines whether to send an alert if a button click event doesn’t match the filter conditions.
        Setting this to True will send an alert message to the user in such cases.

    identifier (:obj:`~pyrogram.types.Identifier`):
        An :obj:`~pyrogram.types.Identifier` instance that defines the criteria for the event.
        It includes properties like chat_id, message_id, from_user_id, and inline_message_id that you want to match against the incoming event.

    future (:obj:`~asyncio.Future`, *optional*):
        A :obj:`~asyncio.Future` object representing the asynchronous task that waits for the event.
        When the event occurs, the :obj:`~asyncio.Future` will be resolved, and the listener will be able to proceed.

    callback (``Callable``, *optional*):
        The callback to call when the listener is fulfilled.
```

---

## File: `types/update.py`

### Classes

#### `class Update`

_No docstring._

##### Methods

###### `def stop_propagation()`

_No docstring._

###### `def continue_propagation()`

_No docstring._

---

## File: `types/user_and_chats/__init__.py`

---

## File: `types/user_and_chats/birthday.py`

### Classes

#### `class Birthday(Object)`

```text
User Date of birth.

Parameters:
    day (``int``):
        Day of birth.

    month (``int``):
        Month of birth.

    year (``int``):
        Year of birth.
```

##### Methods

###### `def __init__(self, *, day: int, month: int, year: int)`

_No docstring._

###### `def _parse(birthday: 'raw.types.Birthday' = None) -> 'Birthday'`

_No docstring._

###### `async def write(self) -> 'raw.types.Birthday'`

_No docstring._

---

## File: `types/user_and_chats/bot_verification.py`

### Classes

#### `class BotVerification(Object)`

```text
Information about bot verification.

Parameters:
    bot (:obj:`~pyrogram.types.User`):
        Bot that is verified this user.

    custom_emoji_id (``int``):
        Custom emoji icon identifier.

    description (``int``, *optional*):
        Additional description about the verification.
```

##### Methods

###### `def __init__(self, *, bot: int, custom_emoji_id: int, description: str)`

_No docstring._

###### `def _parse(client, verification: 'raw.types.BotVerification', users) -> Optional['BotVerification']`

_No docstring._

---

## File: `types/user_and_chats/business_info.py`

### Classes

#### `class BusinessInfo(Object)`

```text
Business information of a user.

Parameters:
    address (``str``, *optional*):
        Address of the business.

    location (:obj:`~pyrogram.types.Location`, *optional*):
        Location of the business on the map.

    greeting_message (:obj:`~pyrogram.types.BusinessMessage`, *optional*):
        Greeting message of the business.

    away_message (:obj:`~pyrogram.types.BusinessMessage`, *optional*):
        Away message of the business.

    working_hours (:obj:`~pyrogram.types.BusinessWorkingHours`, *optional*):
        Working hours of the business.
```

##### Methods

###### `def __init__(self, *, address: str = None, location: 'types.Location' = None, greeting_message: 'types.BusinessMessage' = None, away_message: 'types.BusinessMessage' = None, working_hours: 'types.BusinessWorkingHours' = None)`

_No docstring._

###### `def _parse(client, user: 'raw.types.UserFull' = None, users: Dict[int, 'raw.types.User'] = None) -> Optional['BusinessInfo']`

_No docstring._

---

## File: `types/user_and_chats/business_message.py`

### Classes

#### `class BusinessMessage(Object)`

```text
Business working hours.

Parameters:
    shortcut_id (``int``):
        ID of the shortcut.

    is_greeting (``bool``, *optional*):
        True, if the message is a greeting message.

    is_away (``bool``, *optional*):
        True, if the message is an away message.

    no_activity_days (``int``, *optional*):
        Period of inactivity after which the greeting message should be sent again.

    offline_only (``bool``, *optional*):
        Dont send the away message if you've recently been online.

    recipients (List of :obj:`~pyrogram.types.User`, *optional*):
        Recipients of the message.

    schedule (:obj:`~pyrogram.enums.BusinessSchedule`, *optional*):
        Schedule of the away message to be sent.

    start_date (``datetime``, *optional*):
        Start date of the away message.

    end_date (``datetime``, *optional*):
        End date of the away message.
```

##### Methods

###### `def __init__(self, *, shortcut_id: int, is_greeting: bool = None, is_away: bool = None, no_activity_days: int = None, offline_only: bool = None, recipients: List['types.User'] = None, schedule: 'enums.BusinessSchedule' = None, start_date: datetime = None, end_date: datetime = None)`

_No docstring._

###### `def _parse(client, message: Union['raw.types.BusinessGreetingMessage', 'raw.types.BusinessAwayMessage'] = None, users: Dict[int, 'raw.types.User'] = None) -> Optional['BusinessMessage']`

_No docstring._

---

## File: `types/user_and_chats/business_recipients.py`

### Classes

#### `class BusinessRecipients(Object)`

```text
Business recipients.

Parameters:
    existing_chats (``bool``, *optional*):
        True, if the message should be sent to existing chats.

    new_chats (``bool``, *optional*):
        True, if the message should be sent to new chats.

    contacts (``bool``, *optional*):
        True, if the message should be sent to contacts.

    non_contacts (``bool``, *optional*):
        True, if the message should be sent to non-contacts.

    exclude_selected (``bool``, *optional*):
        True, if the message should be sent to non-selected contacts.

    users (List of :obj:`~pyrogram.types.User`, *optional*):
        Recipients of the message.
```

##### Methods

###### `def __init__(self, *, existing_chats: bool = None, new_chats: bool = None, contacts: bool = None, non_contacts: bool = None, exclude_selected: bool = None, users: List[int] = None)`

_No docstring._

###### `def _parse(client, recipients: 'raw.types.BusinessRecipients', users: Dict[int, 'raw.types.User'] = None) -> 'BusinessRecipients'`

_No docstring._

---

## File: `types/user_and_chats/business_weekly_open.py`

### Classes

#### `class BusinessWeeklyOpen(Object)`

```text
Business weekly open hours.

Parameters:
    start_minute (``int``):
        Start minute of the working day.

    end_minute (``int``):
        End minute of the working day.
```

##### Methods

###### `def __init__(self, *, start_minute: int, end_minute: int)`

_No docstring._

###### `def _parse(weekly_open: 'raw.types.BusinessWeeklyOpen' = None) -> 'BusinessWeeklyOpen'`

_No docstring._

---

## File: `types/user_and_chats/business_working_hours.py`

### Classes

#### `class BusinessWorkingHours(Object)`

```text
Business working hours.

Parameters:
    timezone (``str``):
        Timezone of the business.

    working_hours (List of :obj:`~pyrogram.types.BusinessWeeklyOpen`):
        Working hours of the business.

    is_open_now (``bool``, *optional*):
        True, if the business is open now.
```

##### Methods

###### `def __init__(self, *, timezone: str, working_hours: List['types.BusinessWeeklyOpen'], is_open_now: bool = None)`

_No docstring._

###### `def _parse(work_hours: 'raw.types.BusinessWorkHours' = None) -> Optional['BusinessWorkingHours']`

_No docstring._

---

## File: `types/user_and_chats/chat.py`

### Classes

#### `class Chat(Object)`

```text
A chat.

Parameters:
    id (``int``):
        Unique identifier for this chat.

    type (:obj:`~pyrogram.enums.ChatType`):
        Type of chat.

    is_verified (``bool``, *optional*):
        True, if this chat has been verified by Telegram. Supergroups, channels and bots only.

    is_restricted (``bool``, *optional*):
        True, if this chat has been restricted. Supergroups, channels and bots only.
        See *restriction_reason* for details.

    is_creator (``bool``, *optional*):
        True, if this chat owner is the current user. Supergroups, channels and groups only.

    is_scam (``bool``, *optional*):
        True, if this chat has been flagged for scam.

    is_fake (``bool``, *optional*):
        True, if this chat has been flagged for impersonation.

    is_support (``bool``):
        True, if this chat is part of the Telegram support team. Users and bots only.

    is_participants_hidden (``bool``, *optional*):
        True, if the chat members are hidden.
        Returned only in :meth:`~pyrogram.Client.get_chat`.

    is_join_request (``bool``, *optional*):
        True, if the admin need to approve member(s) join request.

    is_join_to_send (``bool``, *optional*):
        True, if only chat members allowed to send message in chat.

    is_slowmode_enabled (``bool``, *optional*):
        True, if slowmode is enabled in chat.

    is_antispam (``bool``, *optional*):
        True, if Aggressive Anti-Spam is enabled in chat.
        Returned only in :meth:`~pyrogram.Client.get_chat`.

    is_paid_reactions_available (``bool``, *optional*):
        True, if paid reactions are available in chat.
        Returned only in :meth:`~pyrogram.Client.get_chat`.

    is_gifts_available (``bool``, *optional*):
        True, if star gifts can be received by this chat.

    is_auto_translation_enabled (``bool``, *optional*):
        True, if automatic translation is enabled in chat.

    title (``str``, *optional*):
        Title, for supergroups, channels and basic group chats.

    username (``str``, *optional*):
        Username, for private chats, bots, supergroups and channels if available.

    first_name (``str``, *optional*):
        First name of the other party in a private chat, for private chats and bots.

    last_name (``str``, *optional*):
        Last name of the other party in a private chat, for private chats.

    photo (:obj:`~pyrogram.types.ChatPhoto`, *optional*):
        Chat photo. Suitable for downloads only.

    stories (List of :obj:`~pyrogram.types.Story`, *optional*):
        The list of chat's stories if available.

    wallpaper (:obj:`~pyrogram.types.Document`, *optional*):
        Chat wallpaper.

    bio (``str``, *optional*):
        Bio of the other party in a private chat.
        Returned only in :meth:`~pyrogram.Client.get_chat`.

    description (``str``, *optional*):
        Description, for groups, supergroups and channel chats.
        Returned only in :meth:`~pyrogram.Client.get_chat`.

    dc_id (``int``, *optional*):
        The chat assigned DC (data center). Available only in case the chat has a photo.
        Note that this information is approximate; it is based on where Telegram stores the current chat photo.
        It is accurate only in case the owner has set the chat photo, otherwise the dc_id will be the one assigned
        to the administrator who set the current chat photo.

    folder_id (``int``, *optional*):
        The folder identifier where the chat is located.

    has_protected_content (``bool``, *optional*):
        True, if messages from the chat can't be forwarded to other chats.

    invite_link (``str``, *optional*):
        Chat invite link, for groups, supergroups and channels.
        Returned only in :meth:`~pyrogram.Client.get_chat`.

    pinned_message (:obj:`~pyrogram.types.Message`, *optional*):
        Pinned message, for groups, supergroups channels and own chat.
        Returned only in :meth:`~pyrogram.Client.get_chat`.

    sticker_set_name (``str``, *optional*):
        For supergroups, name of group sticker set.
        Returned only in :meth:`~pyrogram.Client.get_chat`.

    can_set_sticker_set (``bool``, *optional*):
        True, if the group sticker set can be changed by you.
        Returned only in :meth:`~pyrogram.Client.get_chat`.

    members_count (``int``, *optional*):
        Chat members count, for groups, supergroups and channels only.
        Returned only in :meth:`~pyrogram.Client.get_chat`.

    join_requests_count (``int``, *optional*):
        Number of users who requested to join the chat.
        Returned only in :meth:`~pyrogram.Client.get

    slow_mode_delay (``int``, *optional*):
        For supergroups, the minimum allowed delay between consecutive messages sent by each unpriviledged user in seconds.
        Returned only in :meth:`~pyrogram.Client.get_chat`.

    restrictions (List of :obj:`~pyrogram.types.Restriction`, *optional*):
        The list of reasons why this chat might be unavailable to some users.
        This field is available only in case *is_restricted* is True.

    permissions (:obj:`~pyrogram.types.ChatPermissions` *optional*):
        Default chat member permissions, for groups and supergroups.

    distance (``int``, *optional*):
        Distance in meters of this group chat from your location.
        Returned only in :meth:`~pyrogram.Client.get_nearby_chats`.

    linked_chat (:obj:`~pyrogram.types.Chat`, *optional*):
        The linked discussion group (in case of channels) or the linked channel (in case of supergroups).
        Returned only in :meth:`~pyrogram.Client.get_chat`.

    linked_forum (:obj:`~pyrogram.types.Chat`, *optional*):
        The linked monoforum (in case of channels) or the linked channel (in case of monoforum).
        Returned only in :meth:`~pyrogram.Client.get_chat`.

    send_as_chat (:obj:`~pyrogram.types.Chat`, *optional*):
        The default "send_as" chat.
        Returned only in :meth:`~pyrogram.Client.get_chat`.

    available_reactions (:obj:`~pyrogram.types.ChatReactions`, *optional*):
        Available reactions in the chat.
        Returned only in :meth:`~pyrogram.Client.get_chat`.

    full_name (``str``, *property*):
        Full name of the other party in a private chat, for private chats and bots.

    usernames (List of :obj:`~pyrogram.types.Username`, *optional*):
        List of all chat (fragment) usernames; for private chats, supergroups and channels.
        Returned only in :meth:`~pyrogram.Client.get_chat`.

    level (``int``, *optional*):
        Channel boosts level.
        For channel only.

    reply_color (:obj:`~pyrogram.types.ChatColor`, *optional*):
        Chat reply color.

    profile_color (:obj:`~pyrogram.types.ChatColor`, *optional*):
        Chat profile color.

    business_info (:obj:`~pyrogram.types.BusinessInfo`, *optional*):
        Business information of a chat.

    birthday (:obj:`~pyrogram.types.Birthday`, *optional*):
        User Date of birth.
        Returned only in :meth:`~pyrogram.Client.get_chat`.

    personal_chat (:obj:`~pyrogram.types.Chat`, *optional*):
        For private chats, the personal channel of the user.
        Returned only in :meth:`~pyrogram.Client.get_chat`.

    max_reaction_count (``int``):
        The maximum number of reactions that can be set on a message in the chat

    subscription_until_date (:py:obj:`~datetime.datetime`, *optional*):
        Channel members only. Date when the subscription expires.

    gifts_count (``int``, *optional*):
        Number of gifts received by the user.

    bot_verification (:obj:`~pyrogram.types.BotVerification`, *optional*):
        Information about bot verification.
```

##### Methods

###### `def __init__(self, *, client: 'pyrogram.Client' = None, id: int, type: 'enums.ChatType', is_verified: bool = None, is_restricted: bool = None, is_creator: bool = None, is_scam: bool = None, is_fake: bool = None, is_support: bool = None, is_participants_hidden: bool = None, is_join_request: bool = None, is_join_to_send: bool = None, is_antispam: bool = None, is_paid_reactions_available: bool = None, is_slowmode_enabled: bool = None, is_gifts_available: bool = None, is_auto_translation_enabled: bool = None, title: str = None, username: str = None, first_name: str = None, last_name: str = None, photo: 'types.ChatPhoto' = None, stories: List['types.Story'] = None, wallpaper: 'types.Document' = None, bio: str = None, description: str = None, dc_id: int = None, folder_id: int = None, has_protected_content: bool = None, invite_link: str = None, pinned_message = None, sticker_set_name: str = None, can_set_sticker_set: bool = None, members_count: int = None, join_requests_count: int = None, slow_mode_delay: int = None, restrictions: List['types.Restriction'] = None, permissions: 'types.ChatPermissions' = None, distance: int = None, linked_chat: 'types.Chat' = None, linked_forum: 'types.Chat' = None, send_as_chat: 'types.Chat' = None, available_reactions: Optional['types.ChatReactions'] = None, usernames: List['types.Username'] = None, reply_color: 'types.ChatColor' = None, profile_color: 'types.ChatColor' = None, business_info: 'types.BusinessInfo' = None, birthday: 'types.Birthday' = None, personal_chat: 'types.Chat' = None, max_reaction_count: int = None, subscription_until_date: datetime = None, gifts_count: int = None, bot_verification: 'types.BotVerification' = None)`

_No docstring._

###### `def full_name(self) -> str`

_No docstring._

###### `def _parse_user_chat(client, user: raw.types.User) -> Optional['Chat']`

_No docstring._

###### `def _parse_chat_chat(client, chat: raw.types.Chat) -> Optional['Chat']`

_No docstring._

###### `def _parse_channel_chat(client, channel: raw.types.Channel) -> Optional['Chat']`

_No docstring._

###### `def _parse(client, message: Union[raw.types.Message, raw.types.MessageService], users: Dict[int, 'raw.types.User'], chats: Dict[int, 'raw.types.Chat'], is_chat: bool) -> 'Chat'`

_No docstring._

###### `def _parse_dialog(client, peer: Union[raw.types.PeerUser, raw.types.PeerChat, raw.types.PeerChannel], users: Dict[int, 'raw.types.User'], chats: Dict[int, 'raw.types.Chat']) -> 'Chat'`

_No docstring._

###### `async def _parse_full(client, chat_full: Union[raw.types.messages.ChatFull, raw.types.users.UserFull]) -> 'Chat'`

_No docstring._

###### `def _parse_chat(client, chat: Union[raw.types.Chat, raw.types.User, raw.types.Channel]) -> 'Chat'`

_No docstring._

###### `def listen(self, *args, **kwargs)`

```text
Bound method *listen* of :obj:`~pyrogram.types.Chat`.

Use as a shortcut for:

.. code-block:: python

    client.wait_for_message(chat_id)

Parameters:
    args (*optional*):
        The arguments to pass to the :meth:`~pyrogram.Client.listen` method.

    kwargs (*optional*):
        The keyword arguments to pass to the :meth:`~pyrogram.Client.listen` method.

Example:
    .. code-block:: python

        chat.listen()

Returns:
    :obj:`~pyrogram.types.Message`: On success, the reply message is returned.
Raises:
    RPCError: In case of a Telegram RPC error.
    asyncio.TimeoutError: In case reply not received within the timeout.
```

###### `def ask(self, text, *args, **kwargs)`

```text
Bound method *ask* of :obj:`~pyrogram.types.Chat`.

Use as a shortcut for:

.. code-block:: python

    client.send_message(chat_id, "What is your name?")

    client.wait_for_message(chat_id)

Parameters:
    text (``str``):
        Text of the message to be sent.

    args:
        The arguments to pass to the :meth:`~pyrogram.Client.listen` method.

    kwargs:
        The keyword arguments to pass to the :meth:`~pyrogram.Client.listen` method.

Example:
    .. code-block:: python

        chat.ask("What is your name?")

Returns:
    :obj:`~pyrogram.types.Message`: On success, the reply message is returned.
Raises:
    RPCError: In case of a Telegram RPC error.
    asyncio.TimeoutError: In case reply not received within the timeout.
```

###### `def stop_listening(self, *args, **kwargs)`

```text
Bound method *stop_listening* of :obj:`~pyrogram.types.Chat`.

Use as a shortcut for:

.. code-block:: python

    client.stop_listening(chat_id=chat_id)

Parameters:
    args (*optional*):
        The arguments to pass to the :meth:`~pyrogram.Client.listen` method.

    kwargs (*optional*):
        The keyword arguments to pass to the :meth:`~pyrogram.Client.listen` method.

Example:
    .. code-block:: python

        chat.stop_listen()
```

###### `async def archive(self)`

```text
Bound method *archive* of :obj:`~pyrogram.types.Chat`.

Use as a shortcut for:

.. code-block:: python

    await client.archive_chats(-100123456789)

Example:
    .. code-block:: python

        await chat.archive()

Returns:
    True on success.

Raises:
    RPCError: In case of a Telegram RPC error.
```

###### `async def unarchive(self)`

```text
Bound method *unarchive* of :obj:`~pyrogram.types.Chat`.

Use as a shortcut for:

.. code-block:: python

    await client.unarchive_chats(-100123456789)

Example:
    .. code-block:: python

        await chat.unarchive()

Returns:
    True on success.

Raises:
    RPCError: In case of a Telegram RPC error.
```

###### `async def set_title(self, title: str) -> bool`

```text
Bound method *set_title* of :obj:`~pyrogram.types.Chat`.

Use as a shortcut for:

.. code-block:: python

    await client.set_chat_title(
        chat_id=chat_id,
        title=title
    )

Example:
    .. code-block:: python

        await chat.set_title("Lounge")

Note:
    In regular groups (non-supergroups), this method will only work if the "All Members Are Admins"
    setting is off.

Parameters:
    title (``str``):
        New chat title, 1-255 characters.

Returns:
    ``bool``: True on success.

Raises:
    RPCError: In case of Telegram RPC error.
    ValueError: In case a chat_id belongs to user.
```

###### `async def set_description(self, description: str) -> bool`

```text
Bound method *set_description* of :obj:`~pyrogram.types.Chat`.

Use as a shortcut for:

.. code-block:: python

    await client.set_chat_description(
        chat_id=chat_id,
        description=description
    )

Example:
    .. code-block:: python

        await chat.set_chat_description("Don't spam!")

Parameters:
    description (``str``):
        New chat description, 0-255 characters.

Returns:
    ``bool``: True on success.

Raises:
    RPCError: In case of Telegram RPC error.
    ValueError: If a chat_id doesn't belong to a supergroup or a channel.
```

###### `async def set_photo(self, *, photo: Union[str, BinaryIO] = None, emoji: int = None, emoji_background: Union[int, List[int]] = None, video: Union[str, BinaryIO] = None, video_start_ts: float = None) -> Union['types.Message', bool]`

```text
Bound method *set_photo* of :obj:`~pyrogram.types.Chat`.

Use as a shortcut for:

.. code-block:: python

    await client.set_chat_photo(
        chat_id=chat_id,
        photo=photo
    )

Example:
    .. code-block:: python

        # Set chat photo using a local file
        await chat.set_photo(photo="photo.jpg")

        # Set chat photo using an existing Photo file_id
        await chat.set_photo(photo=photo.file_id)

        # set chat photo with emoji
        await chat.set_photo(photo="photo.jpg", emoji=5366316836101038579)

        # set chat photo with emoji and emoji_background
        await chat.set_photo(photo="photo.jpg", emoji=5366316836101038579, emoji_background=[0, 0, 0, 0])

        # Set chat video
        await chat.set_photo(video="video.mp4")

Parameters:
    photo (``str`` | ``BinaryIO``, *optional*):
        New chat photo. You can pass a :obj:`~pyrogram.types.Photo` file_id, a file path to upload a new photo
        from your local machine or a binary file-like object with its attribute
        ".name" set for in-memory uploads.

    emoji (``int``, *optional*):
        Unique identifier (int) of the emoji to be used as the chat photo.

    emoji_background (``int`` | List of ``int``, *optional*):
        hexadecimal colors or List of hexadecimal colors to be used as the chat photo background.

    video (``str`` | ``BinaryIO``, *optional*):
        New chat video. You can pass a file path to upload a new video
        from your local machine or a binary file-like object with its attribute
        ".name" set for in-memory uploads.

    video_start_ts (``float``, *optional*):
        The timestamp in seconds of the video frame to use as photo profile preview.

Returns:
    :obj:`~pyrogram.types.Message` | ``bool``: On success, a service message will be returned (when applicable),
    otherwise, in case a message object couldn't be returned, True is returned.

Raises:
    RPCError: In case of a Telegram RPC error.
    ValueError: if a chat_id belongs to user.
```

###### `async def ban_member(self, user_id: Union[int, str], until_date: datetime = utils.zero_datetime(), revoke_messages: bool = None) -> Union['types.Message', bool]`

```text
Bound method *ban_member* of :obj:`~pyrogram.types.Chat`.

Use as a shortcut for:

.. code-block:: python

    await client.ban_chat_member(
        chat_id=chat_id,
        user_id=user_id
    )

Example:
    .. code-block:: python

        await chat.ban_member(123456789)

Note:
    In regular groups (non-supergroups), this method will only work if the "All Members Are Admins" setting is
    off in the target group. Otherwise members may only be removed by the group's creator or by the member
    that added them.

Parameters:
    user_id (``int`` | ``str``):
        Unique identifier (int) or username (str) of the target user.
        For a contact that exists in your Telegram address book you can use his phone number (str).

    until_date (:py:obj:`~datetime.datetime`, *optional*):
        Date when the user will be unbanned.
        If user is banned for more than 366 days or less than 30 seconds from the current time they are
        considered to be banned forever. Defaults to epoch (ban forever).

    revoke_messages (``bool``, *optional*):
        Pass True to delete all messages from the chat for the user that is being removed. If False, the user will be able to see messages in the group that were sent before the user was removed.
        Always True for supergroups and channels.

Returns:
    :obj:`~pyrogram.types.Message` | ``bool``: On success, a service message will be returned (when applicable), otherwise, in
    case a message object couldn't be returned, True is returned.

Raises:
    RPCError: In case of a Telegram RPC error.
```

###### `async def unban_member(self, user_id: Union[int, str]) -> bool`

```text
Bound method *unban_member* of :obj:`~pyrogram.types.Chat`.

Use as a shortcut for:

.. code-block:: python

    await client.unban_chat_member(
        chat_id=chat_id,
        user_id=user_id
    )

Example:
    .. code-block:: python

        await chat.unban_member(123456789)

Parameters:
    user_id (``int`` | ``str``):
        Unique identifier (int) or username (str) of the target user.
        For a contact that exists in your Telegram address book you can use his phone number (str).

Returns:
    ``bool``: True on success.

Raises:
    RPCError: In case of a Telegram RPC error.
```

###### `async def restrict_member(self, user_id: Union[int, str], permissions: 'types.ChatPermissions', until_date: datetime = utils.zero_datetime()) -> 'types.Chat'`

```text
Bound method *unban_member* of :obj:`~pyrogram.types.Chat`.

Use as a shortcut for:

.. code-block:: python

    await client.restrict_chat_member(
        chat_id=chat_id,
        user_id=user_id,
        permissions=ChatPermissions()
    )

Example:
    .. code-block:: python

        await chat.restrict_member(user_id, ChatPermissions())

Parameters:
    user_id (``int`` | ``str``):
        Unique identifier (int) or username (str) of the target user.
        For a contact that exists in your Telegram address book you can use his phone number (str).

    permissions (:obj:`~pyrogram.types.ChatPermissions`):
        New user permissions.

    until_date (:py:obj:`~datetime.datetime`, *optional*):
        Date when the user will be unbanned.
        If user is banned for more than 366 days or less than 30 seconds from the current time they are
        considered to be banned forever. Defaults to epoch (ban forever).

Returns:
    :obj:`~pyrogram.types.Chat`: On success, a chat object is returned.

Raises:
    RPCError: In case of a Telegram RPC error.
```

###### `async def promote_member(self, user_id: Union[int, str], privileges: 'types.ChatPrivileges' = None, title: Optional[str] = '') -> bool`

```text
Bound method *promote_member* of :obj:`~pyrogram.types.Chat`.

Use as a shortcut for:

.. code-block:: python

    await client.promote_chat_member(
        chat_id=chat_id,
        user_id=user_id,
        title=admin_title
    )

Example:

    .. code-block:: python

        await chat.promote_member(123456789)

Parameters:
    user_id (``int`` | ``str``):
        Unique identifier (int) or username (str) of the target user.
        For a contact that exists in your Telegram address book you can use his phone number (str).

    privileges (:obj:`~pyrogram.types.ChatPrivileges`, *optional*):
        New user privileges.

    title (``str``, *optional*):
        A custom title that will be shown to all members instead of "Owner" or "Admin".
        Pass None or "" (empty string) will keep the current title.
        If you want to delete the custom title, use :meth:`~pyrogram.Client.set_administrator_title()` method.

Returns:
    ``bool``: True on success.

Raises:
    RPCError: In case of a Telegram RPC error.
```

###### `async def join(self)`

```text
Bound method *join* of :obj:`~pyrogram.types.Chat`.

Use as a shortcut for:

.. code-block:: python

    await client.join_chat(123456789)

Example:
    .. code-block:: python

        await chat.join()

Note:
    This only works for public groups, channels that have set a username or linked chats.

Returns:
    :obj:`~pyrogram.types.Chat`: On success, a chat object is returned.

Raises:
    RPCError: In case of a Telegram RPC error.
```

###### `async def leave(self)`

```text
Bound method *leave* of :obj:`~pyrogram.types.Chat`.

Use as a shortcut for:

.. code-block:: python

    await client.leave_chat(123456789)

Example:
    .. code-block:: python

        await chat.leave()

Raises:
    RPCError: In case of a Telegram RPC error.
```

###### `async def export_invite_link(self)`

```text
Bound method *export_invite_link* of :obj:`~pyrogram.types.Chat`.

Use as a shortcut for:

.. code-block:: python

    client.export_chat_invite_link(123456789)

Example:
    .. code-block:: python

        chat.export_invite_link()

Returns:
    ``str``: On success, the exported invite link is returned.

Raises:
    ValueError: In case the chat_id belongs to a user.
```

###### `async def get_member(self, user_id: Union[int, str]) -> 'types.ChatMember'`

```text
Bound method *get_member* of :obj:`~pyrogram.types.Chat`.

Use as a shortcut for:

.. code-block:: python

    await client.get_chat_member(
        chat_id=chat_id,
        user_id=user_id
    )

Example:
    .. code-block:: python

        await chat.get_member(user_id)

Returns:
    :obj:`~pyrogram.types.ChatMember`: On success, a chat member is returned.
```

###### `def get_members(self, query: str = '', limit: int = 0, filter: 'enums.ChatMembersFilter' = enums.ChatMembersFilter.SEARCH) -> Optional[AsyncGenerator['types.ChatMember', None]]`

```text
Bound method *get_members* of :obj:`~pyrogram.types.Chat`.

Use as a shortcut for:

.. code-block:: python

    async for member in client.get_chat_members(chat_id):
        print(member)

Example:
    .. code-block:: python

        async for member in chat.get_members():
            print(member)

Parameters:
    query (``str``, *optional*):
        Query string to filter members based on their display names and usernames.
        Only applicable to supergroups and channels. Defaults to "" (empty string).
        A query string is applicable only for :obj:`~pyrogram.enums.ChatMembersFilter.SEARCH`,
        :obj:`~pyrogram.enums.ChatMembersFilter.BANNED` and :obj:`~pyrogram.enums.ChatMembersFilter.RESTRICTED`
        filters only.

    limit (``int``, *optional*):
        Limits the number of members to be retrieved.

    filter (:obj:`~pyrogram.enums.ChatMembersFilter`, *optional*):
        Filter used to select the kind of members you want to retrieve. Only applicable for supergroups
        and channels.

Returns:
    ``Generator``: On success, a generator yielding :obj:`~pyrogram.types.ChatMember` objects is returned.
```

###### `async def add_members(self, user_ids: Union[Union[int, str], List[Union[int, str]]], forward_limit: int = 100) -> bool`

```text
Bound method *add_members* of :obj:`~pyrogram.types.Chat`.

Use as a shortcut for:

.. code-block:: python

    await client.add_chat_members(chat_id, user_id)

Example:
    .. code-block:: python

        await chat.add_members(user_id)

Returns:
    ``bool``: On success, True is returned.
```

###### `async def mark_unread(self) -> bool`

```text
Bound method *mark_unread* of :obj:`~pyrogram.types.Chat`.

Use as a shortcut for:

.. code-block:: python

    await client.mark_unread(chat_id)

Example:
    .. code-block:: python

        await chat.mark_unread()

Returns:
    ``bool``: On success, True is returned.
```

###### `async def set_protected_content(self, enabled: bool) -> bool`

```text
Bound method *set_protected_content* of :obj:`~pyrogram.types.Chat`.

Use as a shortcut for:

.. code-block:: python

    await client.set_chat_protected_content(chat_id, enabled)

Parameters:
    enabled (``bool``):
        Pass True to enable the protected content setting, False to disable.

Example:
    .. code-block:: python

        await chat.set_protected_content(enabled)

Returns:
    ``bool``: On success, True is returned.
```

###### `async def unpin_all_messages(self) -> bool`

```text
Bound method *unpin_all_messages* of :obj:`~pyrogram.types.Chat`.

Use as a shortcut for:

.. code-block:: python

    client.unpin_all_chat_messages(chat_id)

Example:
    .. code-block:: python

        chat.unpin_all_messages()

Returns:
    ``bool``: On success, True is returned.
```

---

## File: `types/user_and_chats/chat_admin_with_invite_links.py`

### Classes

#### `class ChatAdminWithInviteLinks(Object)`

```text
Represents a chat administrator that has created invite links in a chat.

Parameters:
    admin (:obj:`~pyrogram.types.User`):
        The administrator.

    chat_invite_links_count (``int``):
        The number of valid chat invite links created by this administrator.

    revoked_chat_invite_links_count (``int``):
        The number of revoked chat invite links created by this administrator.
```

##### Methods

###### `def __init__(self, *, admin: 'types.User', chat_invite_links_count: int, revoked_chat_invite_links_count: int = None)`

_No docstring._

###### `def _parse(client: 'pyrogram.Client', admin: 'raw.types.ChatAdminWithInvites', users: Dict[int, 'raw.types.User'] = None) -> 'ChatAdminWithInviteLinks'`

_No docstring._

---

## File: `types/user_and_chats/chat_color.py`

### Classes

#### `class ChatColor(Object)`

```text
Reply or profile color status.

Parameters:
    color (:obj:`~pyrogram.enums.ReplyColor` | :obj:`~pyrogram.enums.ProfileColor`, *optional*):
        Color type.

    background_emoji_id (``int``, *optional*):
        Unique identifier of the custom emoji.
```

##### Methods

###### `def __init__(self, *, color: Union['enums.ReplyColor', 'enums.ProfileColor'] = None, background_emoji_id: int = None)`

_No docstring._

###### `def _parse(color: 'raw.types.PeerColor' = None) -> Optional['ChatColor']`

_No docstring._

###### `def _parse_profile_color(color: 'raw.types.PeerColor' = None) -> Optional['ChatColor']`

_No docstring._

---

## File: `types/user_and_chats/chat_event.py`

### Classes

#### `class ChatEvent(Object)`

```text
A chat event from the recent actions log (also known as admin log).

See ``action`` to know which kind of event this is and the relative attributes to get the event content.

Parameters:
    id (``int``):
        Chat event identifier.

    date (:py:obj:`~datetime.datetime`):
        Date of the event.

    action (:obj:`~pyrogram.enums.ChatEventAction`):
        Event action.

    user (:obj:`~pyrogram.types.User`):
        User that triggered the event.

    old_description, new_description (``str``, *optional*):
        Previous and new chat description.
        For :obj:`~pyrogram.enums.ChatEventAction.DESCRIPTION_CHANGED` action only.

    old_history_ttl, new_history_ttl (``int``, *optional*):
        Previous and new chat history TTL.
        For :obj:`~pyrogram.enums.ChatEventAction.HISTORY_TTL_CHANGED` action only.

    old_linked_chat, new_linked_chat (:obj:`~pyrogram.types.Chat`, *optional*):
        Previous and new linked chat.
        For :obj:`~pyrogram.enums.ChatEventAction.LINKED_CHAT_CHANGED` action only.

    old_photo, new_photo (:obj:`~pyrogram.types.Photo`, *optional*):
        Previous and new chat photo.
        For :obj:`~pyrogram.enums.ChatEventAction.PHOTO_CHANGED` action only.

    old_title, new_title (``str``, *optional*):
        Previous and new chat title.
        For :obj:`~pyrogram.enums.ChatEventAction.TITLE_CHANGED` action only.

    old_username, new_username (``str``, *optional*):
        Previous and new chat username.
        For :obj:`~pyrogram.enums.ChatEventAction.USERNAME_CHANGED` action only.

    old_chat_permissions, new_chat_permissions (:obj:`~pyrogram.types.ChatPermissions`, *optional*):
        Previous and new default chat permissions.
        For :obj:`~pyrogram.enums.ChatEventAction.CHAT_PERMISSIONS_CHANGED` action only.

    deleted_message (:obj:`~pyrogram.types.Message`, *optional*):
        Deleted message.
        For :obj:`~pyrogram.enums.ChatEventAction.MESSAGE_DELETED` action only.

    old_message, new_message (:obj:`~pyrogram.types.Message`, *optional*):
        Previous and new message before it has been edited.
        For :obj:`~pyrogram.enums.ChatEventAction.MESSAGE_EDITED` action only.

    invited_member (:obj:`~pyrogram.types.ChatMember`, *optional*):
        New invited chat member.
        For :obj:`~pyrogram.enums.ChatEventAction.MEMBER_INVITED` action only.

    old_administrator_privileges, new_administrator_privileges (:obj:`~pyrogram.types.ChatMember`, *optional*):
        Previous and new administrator privileges.
        For :obj:`~pyrogram.enums.ChatEventAction.ADMINISTRATOR_PRIVILEGES_CHANGED` action only.

    old_member_permissions, new_member_permissions (:obj:`~pyrogram.types.ChatMember`, *optional*):
        Previous and new member permissions.
        For :obj:`~pyrogram.enums.ChatEventAction.MEMBER_PERMISSIONS_CHANGED` action only.

    stopped_poll (:obj:`~pyrogram.types.Message`, *optional*):
        Message containing the stopped poll.
        For :obj:`~pyrogram.enums.ChatEventAction.POLL_STOPPED` action only.

    invites_enabled (``bool``, *optional*):
        If chat invites were enabled (True) or disabled (False).
        For :obj:`~pyrogram.enums.ChatEventAction.INVITES_ENABLED` action only.

    history_hidden (``bool``, *optional*):
        If chat history has been hidden (True) or unhidden (False).
        For :obj:`~pyrogram.enums.ChatEventAction.HISTORY_HIDDEN` action only.

    signatures_enabled (``bool``, *optional*):
        If message signatures were enabled (True) or disabled (False).
        For :obj:`~pyrogram.enums.ChatEventAction.SIGNATURES_ENABLED` action only.

    old_slow_mode, new_slow_mode (``int``, *optional*):
        Previous and new slow mode value in seconds.
        For :obj:`~pyrogram.enums.ChatEventAction.SLOW_MODE_CHANGED` action only.

    pinned_message (:obj:`~pyrogram.types.Message`, *optional*):
        Pinned message.
        For :obj:`~pyrogram.enums.ChatEventAction.MESSAGE_PINNED` action only.

    unpinned_message (:obj:`~pyrogram.types.Message`, *optional*):
        Unpinned message.
        For :obj:`~pyrogram.enums.ChatEventAction.MESSAGE_UNPINNED` action only.

    old_invite_link, new_invite_link (:obj:`~pyrogram.types.ChatInviteLink`, *optional*):
        Previous and new edited invite link.
        For :obj:`~pyrogram.enums.ChatEventAction.INVITE_LINK_EDITED` action only.

    revoked_invite_link (:obj:`~pyrogram.types.ChatInviteLink`, *optional*):
        Revoked invite link.
        For :obj:`~pyrogram.enums.ChatEventAction.INVITE_LINK_REVOKED` action only.

    deleted_invite_link (:obj:`~pyrogram.types.ChatInviteLink`, *optional*):
        Deleted invite link.
        For :obj:`~pyrogram.enums.ChatEventAction.INVITE_LINK_DELETED` action only.

    created_forum_topic (:obj:`~pyrogram.types.ForumTopic`, *optional*):
        New forum topic.
        For :obj:`~pyrogram.enums.ChatEvenAction.CREATED_FORUM_TOPIC` action only.

    old_forum_topic, new_forum_topic (:obj:`~pyrogram.types.ForumTopic`, *optional*):
        Edited forum topic.
        For :obj:`~pyrogram.enums.ChatEvenAction.EDITED_FORUM_TOPIC` action only.

    deleted_forum_topic (:obj:`~pyrogram.types.ForumTopic`, *optional*):
        Deleted forum topic.
        For :obj:`~pyrogram.enums.ChatEvenAction.DELETED_FORUM_TOPIC` action only.
```

##### Methods

###### `def __init__(self, *, id: int, date: datetime, user: 'types.User', action: str, old_description: str = None, new_description: str = None, old_history_ttl: int = None, new_history_ttl: int = None, old_linked_chat: 'types.Chat' = None, new_linked_chat: 'types.Chat' = None, old_photo: 'types.Photo' = None, new_photo: 'types.Photo' = None, old_title: str = None, new_title: str = None, old_username: str = None, new_username: str = None, old_chat_permissions: 'types.ChatPermissions' = None, new_chat_permissions: 'types.ChatPermissions' = None, deleted_message: 'types.Message' = None, old_message: 'types.Message' = None, new_message: 'types.Message' = None, invited_member: 'types.ChatMember' = None, old_administrator_privileges: 'types.ChatMember' = None, new_administrator_privileges: 'types.ChatMember' = None, old_member_permissions: 'types.ChatMember' = None, new_member_permissions: 'types.ChatMember' = None, stopped_poll: 'types.Message' = None, invites_enabled: 'types.ChatMember' = None, history_hidden: bool = None, signatures_enabled: bool = None, old_slow_mode: int = None, new_slow_mode: int = None, pinned_message: 'types.Message' = None, unpinned_message: 'types.Message' = None, old_invite_link: 'types.ChatInviteLink' = None, new_invite_link: 'types.ChatInviteLink' = None, revoked_invite_link: 'types.ChatInviteLink' = None, deleted_invite_link: 'types.ChatInviteLink' = None, created_forum_topic: 'types.ForumTopic' = None, old_forum_topic: 'types.ForumTopic' = None, new_forum_topic: 'types.ForumTopic' = None, deleted_forum_topic: 'types.ForumTopic' = None)`

_No docstring._

###### `async def _parse(client: 'pyrogram.Client', event: 'raw.base.ChannelAdminLogEvent', users: List['raw.base.User'], chats: List['raw.base.Chat'])`

_No docstring._

---

## File: `types/user_and_chats/chat_event_filter.py`

### Classes

#### `class ChatEventFilter(Object)`

```text
Set of filters used to obtain a chat event log.

Parameters:
    new_restrictions (``bool``, *optional*):
        True, if member restricted/unrestricted/banned/unbanned events should be returned.
        Defaults to False.

    new_privileges (``bool``, *optional*):
        True, if member promotion/demotion events should be returned.
        Defaults to False.

    new_members (``bool``, *optional*):
        True, if members joining events should be returned.
        Defaults to False.

    chat_info (``bool``, *optional*):
        True, if chat info changes should be returned. That is, when description, linked chat, location, photo,
        sticker set, title or username have been modified.
        Defaults to False.

    chat_settings (``bool``, *optional*):
        True, if chat settings changes should be returned. That is, when invites, hidden history, message
        signatures, default chat permissions have been modified.
        Defaults to False.

    invite_links (``bool``, *optional*):
        True, if invite links events (edit, revoke, delete) should be returned.
        Defaults to False.

    deleted_messages (``bool``, *optional*):
        True, if deleted messages events should be returned.
        Defaults to False.

    edited_messages (``bool``, *optional*):
        True, if edited messages events, including closed polls, should be returned.
        Defaults to False.

    pinned_messages (``bool``, *optional*):
        True, if pinned/unpinned messages events should be returned.
        Defaults to False.

    leaving_members (``bool``, *optional*):
        True, if members leaving events should be returned.
        Defaults to False.

    video_chats (``bool``, *optional*):
        True, if video chats events should be returned.
        Defaults to False.
```

##### Methods

###### `def __init__(self, *, new_restrictions: bool = False, new_privileges: bool = False, new_members: bool = False, chat_info: bool = False, chat_settings: bool = False, invite_links: bool = False, deleted_messages: bool = False, edited_messages: bool = False, pinned_messages: bool = False, leaving_members: bool = False, video_chats: bool = False)`

_No docstring._

###### `def write(self) -> 'raw.base.ChannelAdminLogEventsFilter'`

_No docstring._

---

## File: `types/user_and_chats/chat_invite_link.py`

### Classes

#### `class ChatInviteLink(Object)`

```text
An invite link for a chat.

Parameters:
    invite_link (``str``):
        The invite link. If the link was created by another chat administrator, then the second part of the
        link will be replaced with "...".

    date (:py:obj:`~datetime.datetime`):
        The date when the link was created.

    is_primary (``bool``):
        True, if the link is primary.

    is_revoked (``bool``):
        True, if the link is revoked.

    creator (:obj:`~pyrogram.types.User`, *optional*):
        Creator of the link.

    name (``str``, *optional*):
        Invite link name

    creates_join_request (``bool``, *optional*):
        True, if users joining the chat via the link need to be approved by chat administrators.

    start_date (:py:obj:`~datetime.datetime`, *optional*):
        Point in time when the link has been edited.

    expire_date (:py:obj:`~datetime.datetime`, *optional*):
        Point in time when the link will expire or has been expired.

    member_limit (``int``, *optional*):
        Maximum number of users that can be members of the chat simultaneously after joining the chat via this
        invite link; 1-99999.

    member_count (``int``, *optional*):
        Number of users that joined via this link and are currently member of the chat.

    pending_join_request_count (``int``, *optional*):
        Number of pending join requests created using this link

    subscription_expired (``int``, *optional*):
        Number of subscription which already expired.

    subscription_period (``int``, *optional*):
        The period of Subscription.

    subscription_price (``int``, *optional*):
        The price of Subscription (stars).
```

##### Methods

###### `def __init__(self, *, invite_link: str, date: datetime, is_primary: bool = None, is_revoked: bool = None, creator: 'types.User' = None, name: str = None, creates_join_request: bool = None, start_date: datetime = None, expire_date: datetime = None, member_limit: int = None, member_count: int = None, pending_join_request_count: int = None, subscription_expired: int = None, subscription_period: int = None, subscription_price: int = None)`

_No docstring._

###### `def _parse(client: 'pyrogram.Client', invite: 'raw.base.ExportedChatInvite', users: Dict[int, 'raw.types.User'] = None) -> Optional['ChatInviteLink']`

_No docstring._

---

## File: `types/user_and_chats/chat_join_request.py`

### Classes

#### `class ChatJoinRequest(Object, Update)`

```text
Represents a join request sent to a chat.

Parameters:
    chat (:obj:`~pyrogram.types.Chat`):
        Chat to which the request was sent.

    from_user (:obj:`~pyrogram.types.User`):
        User that sent the join request.

    date (:py:obj:`~datetime.datetime`):
        Date the request was sent.

    bio (``str``, *optional*):
        Bio of the user.

    invite_link (:obj:`~pyrogram.types.ChatInviteLink`, *optional*):
        Chat invite link that was used by the user to send the join request.
```

##### Methods

###### `def __init__(self, *, client: 'pyrogram.Client' = None, chat: 'types.Chat', from_user: 'types.User', date: datetime, bio: str = None, invite_link: 'types.ChatInviteLink' = None)`

_No docstring._

###### `def _parse(client: 'pyrogram.Client', update: 'raw.types.UpdateBotChatInviteRequester', users: Dict[int, 'raw.types.User'], chats: Dict[int, 'raw.types.Chat']) -> 'ChatJoinRequest'`

_No docstring._

###### `async def approve(self) -> bool`

```text
Bound method *approve* of :obj:`~pyrogram.types.ChatJoinRequest`.

Use as a shortcut for:

.. code-block:: python

    await client.approve_chat_join_request(
        chat_id=request.chat.id,
        user_id=request.from_user.id
    )

Example:
    .. code-block:: python

        await request.approve()

Returns:
    ``bool``: True on success.

Raises:
    RPCError: In case of a Telegram RPC error.
```

###### `async def decline(self) -> bool`

```text
Bound method *decline* of :obj:`~pyrogram.types.ChatJoinRequest`.

Use as a shortcut for:

.. code-block:: python

    await client.decline_chat_join_request(
        chat_id=request.chat.id,
        user_id=request.from_user.id
    )

Example:
    .. code-block:: python

        await request.decline()

Returns:
    ``bool``: True on success.

Raises:
    RPCError: In case of a Telegram RPC error.
```

---

## File: `types/user_and_chats/chat_joined_by_request.py`

### Classes

#### `class ChatJoinedByRequest(Object)`

```text
A service message about a user join request approved in the chat.

Currently holds no information.
```

##### Methods

###### `def __init__(self)`

_No docstring._

---

## File: `types/user_and_chats/chat_joiner.py`

### Classes

#### `class ChatJoiner(Object)`

```text
Contains information about a joiner member of a chat.

Parameters:
    user (:obj:`~pyrogram.types.User`):
        Information about the user.

    date (:py:obj:`~datetime.datetime`):
        Date when the user joined.

    bio (``str``, *optional*):
        Bio of the user.

    pending (``bool``, *optional*):
        True in case the chat joiner has a pending request.

    approved_by (:obj:`~pyrogram.types.User`, *optional*):
        Administrator who approved this chat joiner.
```

##### Methods

###### `def __init__(self, *, client: 'pyrogram.Client', user: 'types.User', date: datetime = None, bio: str = None, pending: bool = None, approved_by: 'types.User' = None)`

_No docstring._

###### `def _parse(client: 'pyrogram.Client', joiner: 'raw.base.ChatInviteImporter', users: Dict[int, 'raw.base.User']) -> 'ChatJoiner'`

_No docstring._

---

## File: `types/user_and_chats/chat_member.py`

### Classes

#### `class ChatMember(Object)`

```text
Contains information about one member of a chat.

Parameters:
    status (:obj:`~pyrogram.enums.ChatMemberStatus`):
        The member's status in the chat.

    user (:obj:`~pyrogram.types.User`, *optional*):
        Information about the user.

    chat (:obj:`~pyrogram.types.Chat`, *optional*):
        Information about the chat (useful in case of banned channel senders).

    joined_date (:py:obj:`~datetime.datetime`, *optional*):
        Date when the user joined.
        Not available for the owner.

    custom_title (``str``, *optional*):
        A custom title that will be shown to all members instead of "Owner" or "Admin".
        Creator (owner) and administrators only. Can be None in case there's no custom title set.

    until_date (:py:obj:`~datetime.datetime`, *optional*):
        Restricted and banned only.
        Date when restrictions will be lifted for this user.

    invited_by (:obj:`~pyrogram.types.User`, *optional*):
        Administrators and self member only. Information about the user who invited this member.
        In case the user joined by himself this will be the same as "user".

    promoted_by (:obj:`~pyrogram.types.User`, *optional*):
        Administrators only. Information about the user who promoted this member as administrator.

    restricted_by (:obj:`~pyrogram.types.User`, *optional*):
        Restricted and banned only. Information about the user who restricted or banned this member.

    is_member (``bool``, *optional*):
        Restricted only. True, if the user is a member of the chat at the moment of the request.

    can_be_edited (``bool``, *optional*):
        True, if the you are allowed to edit administrator privileges of the user.

    permissions (:obj:`~pyrogram.types.ChatPermissions`, *optional*):
        Restricted only. Restricted actions that a non-administrator user is allowed to take.

    privileges (:obj:`~pyrogram.types.ChatPrivileges`, *optional*):
        Administrators only. Privileged actions that an administrator is able to take.

    subscription_until_date (:py:obj:`~datetime.datetime`, *optional*):
        Channel members only. Date when the subscription will expire.
```

##### Methods

###### `def __init__(self, *, client: 'pyrogram.Client' = None, status: 'enums.ChatMemberStatus', user: 'types.User' = None, chat: 'types.Chat' = None, custom_title: str = None, until_date: datetime = None, joined_date: datetime = None, invited_by: 'types.User' = None, promoted_by: 'types.User' = None, restricted_by: 'types.User' = None, is_member: bool = None, can_be_edited: bool = None, permissions: 'types.ChatPermissions' = None, privileges: 'types.ChatPrivileges' = None, subscription_until_date: datetime = None)`

_No docstring._

###### `def _parse(client: 'pyrogram.Client', member: Union['raw.base.ChatParticipant', 'raw.base.ChannelParticipant'], users: Dict[int, 'raw.base.User'], chats: Dict[int, 'raw.base.Chat']) -> 'ChatMember'`

_No docstring._

---

## File: `types/user_and_chats/chat_member_updated.py`

### Classes

#### `class ChatMemberUpdated(Object, Update)`

```text
Represents changes in the status of a chat member.

Parameters:
    chat (:obj:`~pyrogram.types.Chat`):
        Chat the user belongs to.

    from_user (:obj:`~pyrogram.types.User`):
        Performer of the action, which resulted in the change.

    date (:py:obj:`~datetime.datetime`):
        Date the change was done.

    old_chat_member (:obj:`~pyrogram.types.ChatMember`, *optional*):
        Previous information about the chat member.

    new_chat_member (:obj:`~pyrogram.types.ChatMember`, *optional*):
        New information about the chat member.

    invite_link (:obj:`~pyrogram.types.ChatInviteLink`, *optional*):
        Chat invite link, which was used by the user to join the chat; for joining by invite link events only.

    via_join_request (``bool``, *optional*):
        True, if the user joined the chat after sending a direct join request and being approved by an administrator

    via_chat_folder_invite_link (``bool``, *optional*):
        True, if the user joined the chat via a chat folder invite link
```

##### Methods

###### `def __init__(self, *, client: 'pyrogram.Client' = None, chat: 'types.Chat', from_user: 'types.User', date: datetime, old_chat_member: 'types.ChatMember', new_chat_member: 'types.ChatMember', invite_link: 'types.ChatInviteLink' = None, via_join_request: bool = None, via_chat_folder_invite_link: bool = False, _raw: 'raw.base.Update' = None)`

_No docstring._

###### `def _parse(client: 'pyrogram.Client', update: Union['raw.types.UpdateChatParticipant', 'raw.types.UpdateChannelParticipant', 'raw.types.UpdateBotStopped'], users: Dict[int, 'raw.types.User'], chats: Dict[int, 'raw.types.Chat']) -> 'ChatMemberUpdated'`

_No docstring._

---

## File: `types/user_and_chats/chat_permissions.py`

### Classes

#### `class ChatPermissions(Object)`

```text
Describes actions that a non-administrator user is allowed to take in a chat.

Parameters:
    all_perms (``bool``, *optional*):
        True, if all permissions are allowed.

    can_send_messages (``bool``, *optional*):
        True, if the user is allowed to send text messages, contacts, locations and venues.

    can_send_media_messages (``bool``, *optional*):
        True, if the user is allowed to send audios, documents, photos, videos, video notes and voice notes.
        Implies *can_send_messages*.

    can_send_polls (``bool``, *optional*):
        True, if the user is allowed to send polls.
        Implies can_send_messages

    can_add_web_page_previews (``bool``, *optional*):
        True, if the user is allowed to add web page previews to their messages.
        Implies *can_send_media_messages*.

    can_change_info (``bool``, *optional*):
        True, if the user is allowed to change the chat title, photo and other settings.
        Ignored in public supergroups

    can_invite_users (``bool``, *optional*):
        True, if the user is allowed to invite new users to the chat.

    can_pin_messages (``bool``, *optional*):
        True, if the user is allowed to pin messages.
        Ignored in public supergroups.

    can_manage_topics (``bool``, *optional*):
        True, if the user is allowed to create, rename, close, and reopen forum topics.
        supergroups only.

    can_send_audios (``bool``, *optional*):
        True, if the user is allowed to send audios.

    can_send_docs (``bool``, *optional*):
        True, if the user is allowed to send documents.

    can_send_games (``bool``, *optional*):
        True, if the user is allowed to send games.

    can_send_gifs (``bool``, *optional*):
        True, if the user is allowed to send gifs.

    can_send_inline (``bool``, *optional*):
        True, if the user is allowed to send bot inline.

    can_send_photos (``bool``, *optional*):
        True, if the user is allowed to send photos.

    can_send_plain (``bool``, *optional*):
        True, if the user is allowed to send plain texts.

    can_send_roundvideos (``bool``, *optional*):
        True, if the user is allowed to send rounded videos.

    can_send_stickers (``bool``, *optional*):
        True, if the user is allowed to send stickers.

    can_send_videos (``bool``, *optional*):
        True, if the user is allowed to send videos.

    can_send_voices (``bool``, *optional*):
        True, if the user is allowed to send voices.
```

##### Methods

###### `def __init__(self, *, all_perms: bool = None, can_send_messages: bool = None, can_send_media_messages: bool = None, can_send_polls: bool = None, can_add_web_page_previews: bool = None, can_change_info: bool = None, can_invite_users: bool = None, can_pin_messages: bool = None, can_manage_topics: bool = None, can_send_audios: bool = None, can_send_docs: bool = None, can_send_games: bool = None, can_send_gifs: bool = None, can_send_inline: bool = None, can_send_photos: bool = None, can_send_plain: bool = None, can_send_roundvideos: bool = None, can_send_stickers: bool = None, can_send_videos: bool = None, can_send_voices: bool = None)`

_No docstring._

###### `def _parse(denied_permissions: 'raw.base.ChatBannedRights') -> 'ChatPermissions'`

_No docstring._

---

## File: `types/user_and_chats/chat_photo.py`

### Classes

#### `class ChatPhoto(Object)`

```text
A chat photo.

Parameters:
    small_file_id (``str``):
        File identifier of small (160x160) chat photo.
        This file_id can be used only for photo download and only for as long as the photo is not changed.

    small_photo_unique_id (``str``):
        Unique file identifier of small (160x160) chat photo, which is supposed to be the same over time and for
        different accounts. Can't be used to download or reuse the file.

    big_file_id (``str``):
        File identifier of big (640x640) chat photo.
        This file_id can be used only for photo download and only for as long as the photo is not changed.

    big_photo_unique_id (``str``):
        Unique file identifier of big (640x640) chat photo, which is supposed to be the same over time and for
        different accounts. Can't be used to download or reuse the file.

    has_animation (``bool``):
        True, if the photo has animated variant

    is_personal (``bool``):
        True, if the photo is visible only for the current user

    minithumbnail (:obj:`~pyrogram.types.StrippedThumbnail`, *optional*):
        User profile photo minithumbnail; may be None.
```

##### Methods

###### `def __init__(self, *, client: 'pyrogram.Client' = None, small_file_id: str, small_photo_unique_id: str, big_file_id: str, big_photo_unique_id: str, has_animation: bool, is_personal: bool, minithumbnail: 'types.StrippedThumbnail' = None)`

_No docstring._

###### `def _parse(client, chat_photo: Union['raw.types.UserProfilePhoto', 'raw.types.ChatPhoto'], peer_id: int, peer_access_hash: int)`

_No docstring._

---

## File: `types/user_and_chats/chat_preview.py`

### Classes

#### `class ChatPreview(Object)`

```text
A chat preview.

Parameters:
    title (``str``):
        Title of the chat.

    type (``str``):
        Type of chat, can be either, "group", "supergroup" or "channel".

    members_count (``int``):
        Chat members count.

    photo (:obj:`~pyrogram.types.Photo`, *optional*):
        Chat photo.

    members (List of :obj:`~pyrogram.types.User`, *optional*):
        Preview of some of the chat members.
```

##### Methods

###### `def __init__(self, *, client: 'pyrogram.Client' = None, title: str, type: str, members_count: int, photo: 'types.Photo' = None, members: List['types.User'] = None)`

_No docstring._

###### `def _parse(client, chat_invite: 'raw.types.ChatInvite') -> 'ChatPreview'`

_No docstring._

---

## File: `types/user_and_chats/chat_privileges.py`

### Classes

#### `class ChatPrivileges(Object)`

```text
Describes privileged actions an administrator is able to take in a chat.

Parameters:
    can_manage_chat (``bool``, *optional*):
        True, if the administrator can access the chat event log, chat statistics, message statistics in channels,
        see channel members, see anonymous administrators in supergroups and ignore slow mode.
        Implied by any other administrator privilege.

    can_delete_messages (``bool``, *optional*):
        True, if the administrator can delete messages of other users.

    can_manage_video_chats (``bool``, *optional*):
        Groups and supergroups only.
        True, if the administrator can manage video chats (also called group calls).

    can_restrict_members (``bool``, *optional*):
        True, if the administrator can restrict, ban or unban chat members.

    can_promote_members (``bool``, *optional*):
        True, if the administrator can add new administrators with a subset of his own privileges or demote
        administrators that he has promoted, directly or indirectly (promoted by administrators that were appointed
        by the user).

    can_change_info (``bool``, *optional*):
        True, if the user is allowed to change the chat title, photo and other settings.

    can_post_messages (``bool``, *optional*):
        Channels only.
        True, if the administrator can post messages in the channel.

    can_edit_messages (``bool``, *optional*):
        Channels only.
        True, if the administrator can edit messages of other users and can pin messages.

    can_invite_users (``bool``, *optional*):
        True, if the user is allowed to invite new users to the chat.

    can_pin_messages (``bool``, *optional*):
        Groups and supergroups only.
        True, if the user is allowed to pin messages.

    can_manage_topics (``bool``, *optional*):
        supergroups only.
        True, if the user is allowed to create, rename, close, and reopen forum topics.

    can_post_stories (``bool``, *optional*):
        Channels only.
        True, if the administrator can post stories in the channel.

    can_edit_stories (``bool``, *optional*):
        Channels only.
        True, if the administrator can edit stories in the channel.

    can_delete_stories (``bool``, *optional*):
        Channels only.
        True, if the administrator can delete stories in the channel.

    is_anonymous (``bool``, *optional*):
        True, if the user's presence in the chat is hidden.

    can_manage_direct_messages (``bool``, *optional*):
        True, if the administrator can manage direct messages sent to the chat.
```

##### Methods

###### `def __init__(self, *, can_manage_chat: bool = True, can_delete_messages: bool = False, can_manage_video_chats: bool = False, can_restrict_members: bool = False, can_promote_members: bool = False, can_change_info: bool = False, can_post_messages: bool = False, can_edit_messages: bool = False, can_invite_users: bool = False, can_pin_messages: bool = False, can_manage_topics: bool = False, can_post_stories: bool = False, can_edit_stories: bool = False, can_delete_stories: bool = False, is_anonymous: bool = False, can_manage_direct_messages: bool = False)`

_No docstring._

###### `def _parse(admin_rights: 'raw.base.ChatAdminRights') -> 'ChatPrivileges'`

_No docstring._

---

## File: `types/user_and_chats/chat_reactions.py`

### Classes

#### `class ChatReactions(Object)`

```text
A chat reactions

Parameters:
    all_are_enabled (``bool``, *optional*)

    allow_custom_emoji (``bool``, *optional*):
        Whether custom emoji are allowed or not.

    reactions (List of :obj:`~pyrogram.types.Reaction`, *optional*):
        Reactions available.
```

##### Methods

###### `def __init__(self, *, client: 'pyrogram.Client' = None, all_are_enabled: Optional[bool] = None, allow_custom_emoji: Optional[bool] = None, reactions: Optional[List['types.Reaction']] = None)`

_No docstring._

###### `def _parse(client, chat_reactions: 'raw.base.ChatReactions') -> Optional['ChatReactions']`

_No docstring._

---

## File: `types/user_and_chats/dialog.py`

### Classes

#### `class Dialog(Object)`

```text
A user's dialog.

Parameters:
    chat (:obj:`~pyrogram.types.Chat`):
        Conversation the dialog belongs to.

    top_message (:obj:`~pyrogram.types.Message`):
        The last message sent in the dialog at this time.

    unread_messages_count (``int``):
        Amount of unread messages in this dialog.

    unread_mentions_count (``int``):
        Amount of unread messages containing a mention in this dialog.

    unread_mark (``bool``):
        True, if the dialog has the unread mark set.

    is_pinned (``bool``):
        True, if the dialog is pinned.
```

##### Methods

###### `def __init__(self, *, client: 'pyrogram.Client' = None, chat: 'types.Chat', top_message: 'types.Message', unread_messages_count: int, unread_mentions_count: int, unread_mark: bool, is_pinned: bool)`

_No docstring._

###### `def _parse(client, dialog: 'raw.types.Dialog', messages, users, chats) -> 'Dialog'`

_No docstring._

---

## File: `types/user_and_chats/emoji_status.py`

### Classes

#### `class EmojiStatus(Object)`

```text
A user emoji status.

Parameters:
    custom_emoji_id (``int``, *optional*):
        Custom emoji id.

    until_date (:py:obj:`~datetime.datetime`, *optional*):
        Valid until date.

    title (``str``, *optional*):
        Title of the collectible.

    gift_id (``int``, *optional*):
        Gift collectible id.

    name (``str``, *optional*):
        Name of the collectible.

    pattern_custom_emoji_id (``int``, *optional*):
        Pattern emoji id.

    center_color (``int``, *optional*):
        Center color of the collectible emoji in decimal format.

    edge_color (``int``, *optional*):
        Edge color of the collectible emoji in decimal format.

    pattern_color (``int``, *optional*):
        Pattern color of the collectible emoji in decimal format.

    text_color (``int``, *optional*):
        Text color of the collectible emoji in decimal format.
```

##### Methods

###### `def __init__(self, *, client: 'pyrogram.Client' = None, custom_emoji_id: Optional[int] = None, gift_id: Optional[int] = None, until_date: Optional[datetime] = None, title: Optional[str] = None, name: Optional[str] = None, pattern_custom_emoji_id: Optional[int] = None, center_color: Optional[int] = None, edge_color: Optional[int] = None, pattern_color: Optional[int] = None, text_color: Optional[int] = None)`

_No docstring._

###### `def _parse(client, emoji_status: 'raw.base.EmojiStatus') -> Optional['EmojiStatus']`

_No docstring._

###### `def write(self)`

_No docstring._

---

## File: `types/user_and_chats/exported_folder_link.py`

### Classes

#### `class ExportedFolderLink(Object)`

```text
Describes an exported chat folder link.

Parameters:
    link (``str``):
        The link itself.

    title (``str``, *optional*):
        Title of the folder.
```

##### Methods

###### `def __init__(self, link: str, title: str = None)`

_No docstring._

###### `def _parse(exported_folder_link: 'raw.base.ExportedChatFolderLink') -> 'ExportedFolderLink'`

_No docstring._

---

## File: `types/user_and_chats/folder.py`

### Classes

#### `class Folder(Object)`

```text
A user's folder.

Parameters:
    id (``int``):
        The folder id.

    title (``str``):
        The folder title.

    title_entities (List of :obj:`~pyrogram.types.MessageEntity`, *optional*):
        A list of entities in the folder title.

    included_chats (List of :obj:`~pyrogram.types.Chat`, *optional*):
        A list of included chats in folder.

    excluded_chats (List of :obj:`~pyrogram.types.Chat`, *optional*):
        A list of excluded chats in folder.

    pinned_chats (List of :obj:`~pyrogram.types.Chat`, *optional*):
        A list of pinned chats in folder.

    contacts (``bool``, *optional*):
        True, if the folder includes contacts.

    non_contacts (``bool``, *optional*):
        True, if the folder includes non contacts.

    groups (``bool``, *optional*):
        True, if the folder includes groups.

    channels (``bool``, *optional*):
        True, if the folder includes channels.

    bots (``bool``, *optional*):
        True, if the folder includes bots.

    exclude_muted (``bool``, *optional*):
        True, if the folder exclude muted.

    exclude_read (``bool``, *optional*):
        True, if the folder exclude read.

    exclude_archived (``bool``, *optional*):
        True, if the folder exclude archived.

    emoji (``str``, *optional*):
        Folder emoji.

    color (:obj:`~pyrogram.enums.FolderColor`, *optional*)
        Chat reply color.
```

##### Methods

###### `def __init__(self, *, client: 'pyrogram.Client' = None, id: int, title: str, title_entities: List['types.MessageEntity'] = None, included_chats: List['types.Chat'] = None, excluded_chats: List['types.Chat'] = None, pinned_chats: List['types.Chat'] = None, contacts: bool = None, non_contacts: bool = None, groups: bool = None, channels: bool = None, bots: bool = None, exclude_muted: bool = None, exclude_read: bool = None, exclude_archived: bool = None, emoji: str = None, color: 'enums.FolderColor' = None, has_my_invites: bool = None)`

_No docstring._

###### `def _parse(client, folder: 'raw.types.DialogFilter', users, chats) -> 'Folder'`

_No docstring._

###### `async def delete(self)`

```text
Bound method *delete* of :obj:`~pyrogram.types.Folder`.

Use as a shortcut for:

.. code-block:: python

    await client.delete_folder(123456789)

Example:
    .. code-block:: python

       await folder.delete()

Returns:
    True on success.
```

###### `async def update(self, included_chats: List[Union[int, str]] = None, excluded_chats: List[Union[int, str]] = None, pinned_chats: List[Union[int, str]] = None, title: str = None, contacts: bool = None, non_contacts: bool = None, groups: bool = None, channels: bool = None, bots: bool = None, exclude_muted: bool = None, exclude_read: bool = None, exclude_archived: bool = None, emoji: str = None, color: 'enums.FolderColor' = None)`

```text
Bound method *update_peers* of :obj:`~pyrogram.types.Folder`.

Use as a shortcut for:

.. code-block:: python

    await client.update_folder(
        folder_id,
        title="New folder",
        included_chats=["me"]
    )

Example:
    .. code-block:: python

       await folder.update(included_chats=["me"])

Parameters:
    included_chats (``int`` | ``str`` | List of ``int`` or ``str``, *optional*):
        Users or chats that should added in the folder
        You can pass an ID (int), username (str) or phone number (str).
        Multiple users can be added by passing a list of IDs, usernames or phone numbers.

    excluded_chats (``int`` | ``str`` | List of ``int`` or ``str``, *optional*):
        Users or chats that should excluded from the folder
        You can pass an ID (int), username (str) or phone number (str).
        Multiple users can be added by passing a list of IDs, usernames or phone numbers.

    pinned_chats (``int`` | ``str`` | List of ``int`` or ``str``, *optional*):
        Users or chats that should pinned in the folder
        You can pass an ID (int), username (str) or phone number (str).
        Multiple users can be added by passing a list of IDs, usernames or phone numbers.

    title (``str``, *optional*):
        A folder title was changed to this value.

    contacts (``bool``, *optional*):
        Pass True if folder should contain contacts.

    non_contacts (``bool``, *optional*):
        Pass True if folder should contain non contacts.

    groups (``bool``, *optional*):
        Pass True if folder should contain groups.

    channels (``bool``, *optional*):
        Pass True if folder should contain channels.

    bots (``bool``, *optional*):
        Pass True if folder should contain bots.

    exclude_muted (``bool``, *optional*):
        Pass True if folder should exclude muted users.

    exclude_archived (``bool``, *optional*):
        Pass True if folder should exclude archived users.

    emoji (``str``, *optional*):
        Folder emoji.
        Pass None to leave the folder icon as default.

    color (:obj:`~pyrogram.enums.FolderColor`, *optional*):
        Color type.
        Pass :obj:`~pyrogram.enums.FolderColor` to set folder color.

Returns:
    True on success.
```

###### `async def include_chat(self, chat_id: Union[int, str])`

```text
Bound method *include_chat* of :obj:`~pyrogram.types.Folder`.

Use as a shortcut for:

.. code-block:: python

    await client.update_folder(
        folder_id=123456789,
        included_chats=[chat_id],
        excluded_chats=[...],
        pinned_chats=[...]
    )

Example:
    .. code-block:: python

       await folder.include_chat(chat_id)

Parameters:
    chat_id (``int`` | ``str``):
        Unique identifier for the target chat or username of the target user/channel/supergroup
        (in the format @username).

Returns:
    True on success.
```

###### `async def exclude_chat(self, chat_id: Union[int, str])`

```text
Bound method *exclude_chat* of :obj:`~pyrogram.types.Folder`.

Use as a shortcut for:

.. code-block:: python

    await client.update_folder(
        folder_id=123456789,
        included_chats=[...],
        excluded_chats=[chat_id],
        pinned_chats=[...]
    )

Example:
    .. code-block:: python

       await folder.exclude_chat(chat_id)

Parameters:
    chat_id (``int`` | ``str``):
        Unique identifier for the target chat or username of the target user/channel/supergroup
        (in the format @username).

Returns:
    True on success.
```

###### `async def update_color(self, color: 'enums.FolderColor')`

```text
Bound method *update_color* of :obj:`~pyrogram.types.Folder`.

Use as a shortcut for:

.. code-block:: python

    await client.update_folder(
        folder_id=123456789,
        included_chats=[chat_id],
        excluded_chats=[chat_id],
        pinned_chats=[...],
        color=color
    )

Example:
    .. code-block:: python

       await folder.update_color(enums.FolderColor.RED)

Parameters:
    color (:obj:`~pyrogram.enums.FolderColor`, *optional*):
        Color type.
        Pass :obj:`~pyrogram.enums.FolderColor` to set folder color.

Returns:
    True on success.
```

###### `async def pin_chat(self, chat_id: Union[int, str])`

```text
Bound method *pin_chat* of :obj:`~pyrogram.types.Folder`.

Use as a shortcut for:

.. code-block:: python

    await client.update_folder(
        folder_id=123456789,
        included_chats=[chat_id],
        excluded_chats=[chat_id],
        pinned_chats=[...]
    )

Example:
    .. code-block:: python

       await folder.pin_chat(chat_id)

Parameters:
    chat_id (``int`` | ``str``):
        Unique identifier for the target chat or username of the target user/channel/supergroup
        (in the format @username).

Returns:
    True on success.
```

###### `async def remove_chat(self, chat_id: Union[int, str])`

```text
Bound method *remove_chat* of :obj:`~pyrogram.types.Folder`.

Remove chat from included, excluded and pinned chats.

Use as a shortcut for:

.. code-block:: python

    await client.update_folder(
        folder_id=123456789,
        included_chats=[...],
        excluded_chats=[...],
        pinned_chats=[...]
    )

Example:
    .. code-block:: python

       await folder.remove_chat(chat_id)

Parameters:
    chat_id (``int`` | ``str``):
        Unique identifier for the target chat or username of the target user/channel/supergroup
        (in the format @username).

Returns:
    True on success.
```

###### `async def export_link(self)`

```text
Bound method *export_link* of :obj:`~pyrogram.types.Folder`.

Use as a shortcut for:

.. code-block:: python

    await client.export_folder_link(123456789)

Example:
    .. code-block:: python

       await folder.export_link()

Returns:
    ``str``: On success, a link to the folder as string is returned.
```

---

## File: `types/user_and_chats/forum_topic.py`

### Classes

#### `class ForumTopic(Object)`

```text
A forum topic.


Parameters:
    id (``Integer``):
        Id of the topic

    date (``Integer``):
        Date topic created

    title (``String``):
        Name of the topic

    icon_color (``Integer``):
        Color of the topic icon in RGB format

    top_message (``Integer``):
        N/A

    read_inbox_max_id (``Integer``):
        N/A

    read_outbox_max_id (``Integer``):
        N/A

    unread_count (``Integer``):
        N/A

    unread_mentions_count (``Integer``):
        N/A

    unread_reactions_count (``Integer``):
        N/A

    from_id (:obj:`~pyrogram.types.PeerChannel` | :obj:`~pyrogram.types.PeerUser`):
        Topic creator.

    my (``Boolean``, *optional*):
        N/A

    closed (``Boolean``, *optional*):
        N/A

    pinned (``Boolean``, *optional*):
        N/A

    short (``Boolean``, *optional*):
        N/A

    icon_emoji_id (``Integer``, *optional*):
        Unique identifier of the custom emoji shown as the topic icon
```

##### Methods

###### `def __init__(self, *, id: int, date: int, title: str, icon_color: int, top_message: int, read_inbox_max_id: int, read_outbox_max_id: int, unread_count: int, unread_mentions_count: int, unread_reactions_count: int, from_id: Union['types.PeerChannel', 'types.PeerUser'], my: bool = None, closed: bool = None, pinned: bool = None, short: bool = None, icon_emoji_id: int = None)`

_No docstring._

###### `def _parse(forum_topic: 'raw.types.ForumTopic') -> 'ForumTopic'`

_No docstring._

---

## File: `types/user_and_chats/forum_topic_closed.py`

### Classes

#### `class ForumTopicClosed(Object)`

```text
A service message about a forum topic closed in the chat.

Currently holds no information.
```

##### Methods

###### `def __init__(self)`

_No docstring._

---

## File: `types/user_and_chats/forum_topic_created.py`

### Classes

#### `class ForumTopicCreated(Object)`

```text
A service message about a new forum topic created in the chat.


Parameters:
    id (``int``):
        Id of the topic

    title (``str``):
        Name of the topic.

    icon_color (``int``):
        Color of the topic icon in decimal format.

    custom_emoji_id (``int``, *optional*):
        Unique identifier of the custom emoji shown as the topic icon.
```

##### Methods

###### `def __init__(self, *, id: int, title: str, icon_color: int, custom_emoji_id: int = None)`

_No docstring._

###### `def _parse(message: 'raw.base.Message') -> 'ForumTopicCreated'`

_No docstring._

---

## File: `types/user_and_chats/forum_topic_deleted.py`

### Classes

#### `class ForumTopicDeleted(Object)`

```text
A deleted forum topic.

Parameters:
    id (``Integer``):
        Id of the topic
```

##### Methods

###### `def __init__(self, *, id: int)`

_No docstring._

###### `def _parse(forum_topic: 'raw.types.ForumTopicDeleted') -> 'ForumTopicDeleted'`

_No docstring._

---

## File: `types/user_and_chats/forum_topic_edited.py`

### Classes

#### `class ForumTopicEdited(Object)`

```text
A service message about a forum topic renamed in the chat.


Parameters:
    title (``str``):
        Name of the topic.

    icon_color (``int``):
        Color of the topic icon in decimal format.

    custom_emoji_id (``str``, *optional*):
        Unique identifier of the custom emoji shown as the topic icon.

    is_closed (``bool``, *optional*):
        True, if the topic is closed.

    is_hidden (``bool``, *optional*):
        True, if the topic is hidden.
        Valid only for the "General" topic with id=1
```

##### Methods

###### `def __init__(self, *, title: str = None, icon_color: int = None, custom_emoji_id: int = None, is_closed: bool = None, is_hidden: bool = None)`

_No docstring._

###### `def _parse(action: 'raw.types.MessageActionTopicEdit') -> 'ForumTopicEdited'`

_No docstring._

---

## File: `types/user_and_chats/forum_topic_reopened.py`

### Classes

#### `class ForumTopicReopened(Object)`

```text
A service message about a forum topic reopened in the chat.

Currently holds no information.
```

##### Methods

###### `def __init__(self)`

_No docstring._

---

## File: `types/user_and_chats/general_forum_topic_hidden.py`

### Classes

#### `class GeneralTopicHidden(Object)`

```text
A service message about a general topic hidden in the chat.

Currently holds no information.
```

##### Methods

###### `def __init__(self)`

_No docstring._

---

## File: `types/user_and_chats/general_forum_topic_unhidden.py`

### Classes

#### `class GeneralTopicUnhidden(Object)`

```text
A service message about a general topic unhidden in the chat.

Currently holds no information.
```

##### Methods

###### `def __init__(self)`

_No docstring._

---

## File: `types/user_and_chats/group_call_member.py`

### Classes

#### `class GroupCallMember(Object)`

```text
Contains information about one member of a group call.

Parameters:
    chat (:obj:`~pyrogram.types.Chat`, *optional*):
        Information about the user or chat.

    date (:py:obj:`~datetime.datetime`, *optional*):
        Date when this participant join this group call.

    active_date (:py:obj:`~datetime.datetime`, *optional*):
        Date when this participant last active in this group call.

    volume (``int``, *optional*):
        Volume, if not set the volume is set to 100%.

    can_self_unmute (``bool``, *optional*):
        Whether the participant can unmute themselves.

    is_muted (``bool``, *optional*):
        Whether the participant is muted.

    is_left (``bool``, *optional*):
        Whether the participant has left.

    is_just_joined (``bool``, *optional*):
        Whether the participant has just joined.

    is_muted_by_you (``bool``, *optional*):
        Whether this participant was muted by the current user.

    is_volume_by_admin (``bool``, *optional*):
        Whether our volume can only changed by an admin.

    is_self (``bool``, *optional*):
        Whether this participant is the current user.

    is_video_joined (``bool``, *optional*):
        Whether this participant is currently broadcasting video.

    is_hand_raised (``bool``, *optional*):
        Whether this participant is raised hand.

    is_video_enabled (``bool``, *optional*):
        Whether this participant is currently broadcasting video.

    is_screen_sharing_enabled (``bool``, *optional*):
        Whether this participant is currently shared screen.
```

##### Methods

###### `def __init__(self, *, client: 'pyrogram.Client' = None, chat: 'types.Chat' = None, date: datetime = None, active_date: datetime = None, volume: int = None, can_self_unmute: bool = None, is_muted: bool = None, is_left: bool = None, is_just_joined: bool = None, is_muted_by_you: bool = None, is_volume_by_admin: bool = None, is_self: bool = None, is_video_joined: bool = None, is_hand_raised: bool = None, is_video_enabled: bool = None, is_screen_sharing_enabled: bool = None)`

_No docstring._

###### `def _parse(client: 'pyrogram.Client', member: 'raw.types.GroupCallParticipant', users: Dict[int, 'raw.base.User'], chats: Dict[int, 'raw.base.Chat']) -> 'GroupCallMember'`

_No docstring._

---

## File: `types/user_and_chats/invite_link_importer.py`

### Classes

#### `class InviteLinkImporter(Object)`

```text
The date and user of when someone has joined with an invite link.

Parameters:
    date (:py:obj:`~datetime.datetime`):
        The time of when this user used the given link

    user (:obj:`~pyrogram.types.User`):
        The user that has used the given invite link
```

##### Methods

###### `def __init__(self, *, date: datetime, user: 'types.User')`

_No docstring._

###### `def _parse(client, invite_importers: 'raw.types.messages.ChatInviteImporters')`

_No docstring._

---

## File: `types/user_and_chats/peer_channel.py`

### Classes

#### `class PeerChannel(Object)`

```text
A PeerChannel.


Parameters:
    channel_id (``Integer``):
        Id of the channel.
```

##### Methods

###### `def __init__(self, *, channel_id: int)`

_No docstring._

###### `def _parse(action: 'raw.types.PeerChannel') -> 'PeerChannel'`

_No docstring._

---

## File: `types/user_and_chats/peer_user.py`

### Classes

#### `class PeerUser(Object)`

```text
A PeerUser.


Parameters:
    user_id (``Integer``):
        Id of the user.
```

##### Methods

###### `def __init__(self, *, user_id: int)`

_No docstring._

###### `def _parse(action: 'raw.types.PeerUser') -> 'PeerUser'`

_No docstring._

---

## File: `types/user_and_chats/restriction.py`

### Classes

#### `class Restriction(Object)`

```text
A restriction applied to bots or chats.

Parameters:
    platform (``str``):
        The platform the restriction is applied to, e.g. "ios", "android"

    reason (``str``):
        The restriction reason, e.g. "porn", "copyright".

    text (``str``):
        The restriction text.
```

##### Methods

###### `def __init__(self, *, platform: str, reason: str, text: str)`

_No docstring._

###### `def _parse(restriction: 'raw.types.RestrictionReason') -> 'Restriction'`

_No docstring._

---

## File: `types/user_and_chats/user.py`

### Classes

#### `class Link(str)`

_No docstring._

##### Methods

###### `def __init__(self, url: str, text: str, style: enums.ParseMode)`

_No docstring._

###### `def format(url: str, text: str, style: enums.ParseMode)`

_No docstring._

###### `def __new__(cls, url, text, style)`

_No docstring._

###### `def __call__(self, other: str = None, *, style: str = None)`

_No docstring._

###### `def __str__(self)`

_No docstring._

#### `class User(Object, Update)`

```text
A Telegram user or bot.

Parameters:
    id (``int``):
        Unique identifier for this user or bot.

    is_self(``bool``, *optional*):
        True, if this user is you yourself.

    is_contact(``bool``, *optional*):
        True, if this user is in your contacts.

    is_mutual_contact(``bool``, *optional*):
        True, if you both have each other's contact.

    is_deleted(``bool``, *optional*):
        True, if this user is deleted.

    is_frozen(``bool``, *optional*):
        True, if this user is frozen.

    is_bot (``bool``, *optional*):
        True, if this user is a bot.

    is_verified (``bool``, *optional*):
        True, if this user has been verified by Telegram.

    is_restricted (``bool``, *optional*):
        True, if this user has been restricted. Bots only.
        See *restriction_reason* for details.

    is_scam (``bool``, *optional*):
        True, if this user has been flagged for scam.

    is_fake (``bool``, *optional*):
        True, if this user has been flagged for impersonation.

    is_support (``bool``, *optional*):
        True, if this user is part of the Telegram support team.

    is_premium (``bool``, *optional*):
        True, if this user is a premium user.

    is_contacts_only (``bool``, *optional*):
        True, if this user is only allow incoming message from users in their contacts/premium users.

    is_bot_business (``bool``, *optional*):
        True, if this bot can connect to business account.

    first_name (``str``, *optional*):
        User's or bot's first name.

    last_name (``str``, *optional*):
        User's or bot's last name.

    status (:obj:`~pyrogram.enums.UserStatus`, *optional*):
        User's last seen & online status. ``None``, for bots.

    last_online_date (:py:obj:`~datetime.datetime`, *optional*):
        Last online date of a user. Only available in case status is :obj:`~pyrogram.enums.UserStatus.OFFLINE`.

    next_offline_date (:py:obj:`~datetime.datetime`, *optional*):
        Date when a user will automatically go offline. Only available in case status is :obj:`~pyrogram.enums.UserStatus.ONLINE`.

    username (``str``, *optional*):
        User's or bot's username.

    usernames (List of :obj:`~pyrogram.types.Username`, *optional*):
        List of all chat (fragment) usernames; for private chats, supergroups and channels.
        Returned only in :meth:`~pyrogram.Client.get_chat`.

    language_code (``str``, *optional*):
        IETF language tag of the user's language.

    emoji_status (:obj:`~pyrogram.types.EmojiStatus`, *optional*):
        Emoji status.

    dc_id (``int``, *optional*):
        User's or bot's assigned DC (data center). Available only in case the user has set a public profile photo.
        Note that this information is approximate; it is based on where Telegram stores a user profile pictures and
        does not by any means tell you the user location (i.e. a user might travel far away, but will still connect
        to its assigned DC). More info at `FAQs </faq#what-are-the-ip-addresses-of-telegram-data-centers>`_.

    phone_number (``str``, *optional*):
        User's phone number.

    photo (:obj:`~pyrogram.types.ChatPhoto`, *optional*):
        User's or bot's current profile photo. Suitable for downloads only.

    restrictions (List of :obj:`~pyrogram.types.Restriction`, *optional*):
        The list of reasons why this bot might be unavailable to some users.
        This field is available only in case *is_restricted* is True.

    full_name (``str``, *optional*):
        User's or bot's full name.

    mention (``str``, *property*):
        Generate a text mention for this user.
        You can use ``user.mention()`` to mention the user using their first name (styled using html), or
        ``user.mention("another name")`` for a custom name. To choose a different style
        ("html" or "md"/"markdown") use ``user.mention(style="md")``.

    reply_color (:obj:`~pyrogram.types.ChatColor`, *optional*)
        Chat reply color.

    profile_color (:obj:`~pyrogram.types.ChatColor`, *optional*)
        Chat profile color.

    active_users (``int``, *optional*):
        Bot's active users count.

    frozen_icon (``int``, *optional*):
        Frozen account icon.
        This field is available only in case *is_frozen* is True.
```

##### Methods

###### `def __init__(self, *, client: 'pyrogram.Client' = None, id: int, is_self: bool = None, is_contact: bool = None, is_mutual_contact: bool = None, is_deleted: bool = None, is_frozen: bool = None, is_bot: bool = None, is_verified: bool = None, is_restricted: bool = None, is_scam: bool = None, is_fake: bool = None, is_support: bool = None, is_premium: bool = None, is_contacts_only: bool = None, is_bot_business: bool = None, first_name: str = None, last_name: str = None, status: 'enums.UserStatus' = None, last_online_date: datetime = None, next_offline_date: datetime = None, username: str = None, usernames: List['types.Username'] = None, language_code: str = None, emoji_status: Optional['types.EmojiStatus'] = None, dc_id: int = None, phone_number: str = None, photo: 'types.ChatPhoto' = None, restrictions: List['types.Restriction'] = None, reply_color: 'types.ChatColor' = None, profile_color: 'types.ChatColor' = None, active_users: int = None, frozen_icon: int = None)`

_No docstring._

###### `def full_name(self) -> str`

_No docstring._

###### `def mention(self)`

_No docstring._

###### `def _parse(client, user: 'raw.base.User') -> Optional['User']`

_No docstring._

###### `def _parse_status(user_status: 'raw.base.UserStatus', is_bot: bool = False)`

_No docstring._

###### `def _parse_user_status(client, user_status: 'raw.types.UpdateUserStatus')`

_No docstring._

###### `def listen(self, *args, **kwargs)`

```text
Bound method *listen* of :obj:`~pyrogram.types.User`.

Use as a shortcut for:

.. code-block:: python

    client.wait_for_message(user_id)

Parameters:
    args (*optional*):
        The arguments to pass to the :meth:`~pyrogram.Client.listen` method.

    kwargs (*optional*):
        The keyword arguments to pass to the :meth:`~pyrogram.Client.listen` method.

Example:
    .. code-block:: python

        user.listen()

Returns:
    :obj:`~pyrogram.types.Message`: On success, the reply message is returned.
Raises:
    RPCError: In case of a Telegram RPC error.
    asyncio.TimeoutError: In case reply not received within the timeout.
```

###### `def ask(self, text, *args, **kwargs)`

```text
Bound method *ask* of :obj:`~pyrogram.types.User`.

Use as a shortcut for:

.. code-block:: python

    client.send_message(user_id, "What is your name?")

    client.wait_for_message(user_id)

Parameters:
    text (``str``):
        Text of the message to be sent.

    args:
        The arguments to pass to the :meth:`~pyrogram.Client.listen` method.

    kwargs:
        The keyword arguments to pass to the :meth:`~pyrogram.Client.listen` method.

Example:
    .. code-block:: python

        user.ask("What is your name?")

Returns:
    :obj:`~pyrogram.types.Message`: On success, the reply message is returned.
Raises:
    RPCError: In case of a Telegram RPC error.
    asyncio.TimeoutError: In case reply not received within the timeout.
```

###### `def stop_listening(self, *args, **kwargs)`

```text
Bound method *stop_listening* of :obj:`~pyrogram.types.User`.

Use as a shortcut for:

.. code-block:: python

    client.stop_listening(user_id=user_id)

Parameters:
    args (*optional*):
        The arguments to pass to the :meth:`~pyrogram.Client.listen` method.

    kwargs (*optional*):
        The keyword arguments to pass to the :meth:`~pyrogram.Client.listen` method.

Example:
    .. code-block:: python

        user.stop_listen()
```

###### `async def archive(self)`

```text
Bound method *archive* of :obj:`~pyrogram.types.User`.

Use as a shortcut for:

.. code-block:: python

    await client.archive_chats(123456789)

Example:
    .. code-block:: python

       await user.archive()

Returns:
    True on success.

Raises:
    RPCError: In case of a Telegram RPC error.
```

###### `async def unarchive(self)`

```text
Bound method *unarchive* of :obj:`~pyrogram.types.User`.

Use as a shortcut for:

.. code-block:: python

    await client.unarchive_chats(123456789)

Example:
    .. code-block:: python

        await user.unarchive()

Returns:
    True on success.

Raises:
    RPCError: In case of a Telegram RPC error.
```

###### `def block(self)`

```text
Bound method *block* of :obj:`~pyrogram.types.User`.

Use as a shortcut for:

.. code-block:: python

    await client.block_user(123456789)

Example:
    .. code-block:: python

        await user.block()

Returns:
    True on success.

Raises:
    RPCError: In case of a Telegram RPC error.
```

###### `def unblock(self)`

```text
Bound method *unblock* of :obj:`~pyrogram.types.User`.

Use as a shortcut for:

.. code-block:: python

    client.unblock_user(123456789)

Example:
    .. code-block:: python

        user.unblock()

Returns:
    True on success.

Raises:
    RPCError: In case of a Telegram RPC error.
```

###### `def get_common_chats(self)`

```text
Bound method *get_common_chats* of :obj:`~pyrogram.types.User`.

Use as a shortcut for:

.. code-block:: python

    client.get_common_chats(123456789)

Example:
    .. code-block:: python

        user.get_common_chats()

Returns:
    True on success.

Raises:
    RPCError: In case of a Telegram RPC error.
```

---

## File: `types/user_and_chats/username.py`

### Classes

#### `class Username(Object)`

```text
A Username.


Parameters:
    username (``String``):
        The channel/user username.

    editable (``bool``, *optional*):
        Can the username edited.

    active (``bool``, *optional*)
        Is the username active.
```

##### Methods

###### `def __init__(self, *, username: str, editable: bool = None, active: bool = None)`

_No docstring._

###### `def _parse(action: 'raw.types.Username') -> 'Username'`

_No docstring._

---

## File: `types/user_and_chats/video_chat_ended.py`

### Classes

#### `class VideoChatEnded(Object)`

```text
A service message about a voice chat ended in the chat.

Parameters:
    duration (``int``):
        Voice chat duration; in seconds.
```

##### Methods

###### `def __init__(self, *, duration: int)`

_No docstring._

###### `def _parse(action: 'raw.types.MessageActionGroupCall') -> 'VideoChatEnded'`

_No docstring._

---

## File: `types/user_and_chats/video_chat_members_invited.py`

### Classes

#### `class VideoChatMembersInvited(Object)`

```text
A service message about new members invited to a voice chat.


Parameters:
    users (List of :obj:`~pyrogram.types.User`):
        New members that were invited to the voice chat.
```

##### Methods

###### `def __init__(self, *, users: List['types.User'])`

_No docstring._

###### `def _parse(client, action: 'raw.types.MessageActionInviteToGroupCall', users: Dict[int, 'raw.types.User']) -> 'VideoChatMembersInvited'`

_No docstring._

---

## File: `types/user_and_chats/video_chat_scheduled.py`

### Classes

#### `class VideoChatScheduled(Object)`

```text
A service message about a voice chat scheduled in the chat.

Parameters:
    start_date (:py:obj:`~datetime.datetime`):
        Point in time when the voice chat is supposed to be started by a chat administrator.
```

##### Methods

###### `def __init__(self, *, start_date: datetime)`

_No docstring._

###### `def _parse(action: 'raw.types.MessageActionGroupCallScheduled') -> 'VideoChatScheduled'`

_No docstring._

---

## File: `types/user_and_chats/video_chat_started.py`

### Classes

#### `class VideoChatStarted(Object)`

```text
A service message about a voice chat started in the chat.

Currently holds no information.
```

##### Methods

###### `def __init__(self)`

_No docstring._

---
