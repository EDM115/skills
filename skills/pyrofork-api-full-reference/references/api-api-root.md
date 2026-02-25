---
name: api-api-root
description: Offline API backup extracted from Pyrofork source docstrings.
---

# Pyrofork API Backup: `root`

Extracted from `sources/pyrofork/pyrogram/**.py` using AST parsing of module, class, function, and method docstrings.

## File: `__init__.py`

### Classes

#### `class StopTransmission(Exception)`

_No docstring._

#### `class StopPropagation(StopAsyncIteration)`

_No docstring._

#### `class ContinuePropagation(StopAsyncIteration)`

_No docstring._

---

## File: `client.py`

### Classes

#### `class Client(Methods)`

```text
Pyrogram Client, the main means for interacting with Telegram.

Parameters:
    name (``str``):
        A name for the client, e.g.: "my_account".

    api_id (``int`` | ``str``, *optional*):
        The *api_id* part of the Telegram API key, as integer or string.
        E.g.: 12345 or "12345".

    api_hash (``str``, *optional*):
        The *api_hash* part of the Telegram API key, as string.
        E.g.: "0123456789abcdef0123456789abcdef".

    app_version (``str``, *optional*):
        Application version.
        Defaults to "Pyrogram x.y.z".

    device_model (``str``, *optional*):
        Device model.
        Defaults to *platform.python_implementation() + " " + platform.python_version()*.

    system_version (``str``, *optional*):
        Operating System version.
        Defaults to *platform.system() + " " + platform.release()*.

    lang_code (``str``, *optional*):
        Code of the language used on the client, in ISO 639-1 standard.
        Defaults to "en".

    ipv6 (``bool``, *optional*):
        Pass True to connect to Telegram using IPv6.
        Defaults to False (IPv4).

    alt_port (``bool``, *optional*):
        Pass True to connect to Telegram using alternative port (5222).
        Defaults to False (443).

    proxy (``dict``, *optional*):
        The Proxy settings as dict.
        E.g.: *dict(scheme="socks5", hostname="11.22.33.44", port=1234, username="user", password="pass")*.
        The *username* and *password* can be omitted if the proxy doesn't require authorization.

    test_mode (``bool``, *optional*):
        Enable or disable login to the test servers.
        Only applicable for new sessions and will be ignored in case previously created sessions are loaded.
        Defaults to False.

    bot_token (``str``, *optional*):
        Pass the Bot API token to create a bot session, e.g.: "123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11"
        Only applicable for new sessions.

    session_string (``str``, *optional*):
        Pass a session string to load the session in-memory.
        Implies ``in_memory=True``.

    use_qrcode (``bool``, *optional*):
        Pass True to login using a QR code.

    in_memory (``bool``, *optional*):
        Pass True to start an in-memory session that will be discarded as soon as the client stops.
        In order to reconnect again using an in-memory session without having to login again, you can use
        :meth:`~pyrogram.Client.export_session_string` before stopping the client to get a session string you can
        pass to the ``session_string`` parameter.
        Defaults to False.

    mongodb (``dict``, *optional*):
        Mongodb config as dict, e.g.: *dict(connection=async_pymongo.AsyncClient("mongodb://..."), remove_peers=False)*.
        Only applicable for new sessions.

    storage (:obj:`~pyrogram.storage.Storage`, *optional*):
        Custom session storage.

    phone_number (``str``, *optional*):
        Pass the phone number as string (with the Country Code prefix included) to avoid entering it manually.
        Only applicable for new sessions.

    phone_code (``str``, *optional*):
        Pass the phone code as string (for test numbers only) to avoid entering it manually.
        Only applicable for new sessions.

    password (``str``, *optional*):
        Pass the Two-Step Verification password as string (if required) to avoid entering it manually.
        Only applicable for new sessions.

    workers (``int``, *optional*):
        Number of maximum concurrent workers for handling incoming updates.
        Defaults to ``min(32, os.cpu_count() + 4)``.

    workdir (``str``, *optional*):
        Define a custom working directory.
        The working directory is the location in the filesystem where Pyrogram will store the session files.
        Defaults to the parent directory of the main script.

    plugins (``dict``, *optional*):
        Smart Plugins settings as dict, e.g.: *dict(root="plugins")*.

    parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
        Set the global parse mode of the client. By default, texts are parsed using both Markdown and HTML styles.
        You can combine both syntaxes together.

    no_updates (``bool``, *optional*):
        Pass True to disable incoming updates.
        When updates are disabled the client can't receive messages or other updates.
        Useful for batch programs that don't need to deal with updates.
        Defaults to False (updates enabled and received).

    skip_updates (``bool``, *optional*):
        Pass True to skip pending updates that arrived while the client was offline.
        Defaults to True.

    takeout (``bool``, *optional*):
        Pass True to let the client use a takeout session instead of a normal one, implies *no_updates=True*.
        Useful for exporting Telegram data. Methods invoked inside a takeout session (such as get_chat_history,
        download_media, ...) are less prone to throw FloodWait exceptions.
        Only available for users, bots will ignore this parameter.
        Defaults to False (normal session).

    sleep_threshold (``int``, *optional*):
        Set a sleep threshold for flood wait exceptions happening globally in this client instance, below which any
        request that raises a flood wait will be automatically invoked again after sleeping for the required amount
        of time. Flood wait exceptions requiring higher waiting times will be raised.
        Defaults to 10 seconds.

    hide_password (``bool``, *optional*):
        Pass True to hide the password when typing it during the login.
        Defaults to False, because ``getpass`` (the library used) is known to be problematic in some
        terminal environments.

    max_concurrent_transmissions (``bool``, *optional*):
        Set the maximum amount of concurrent transmissions (uploads & downloads).
        A value that is too high may result in network related issues.
        Defaults to 1.

    max_message_cache_size (``int``, *optional*):
        Set the maximum size of the message cache.
        Defaults to 10000.

    max_business_user_connection_cache_size (``int``, *optional*):
        Set the maximum size of the message cache.
        Defaults to 10000.

    client_platform (:obj:`~pyrogram.enums.ClientPlatform`, *optional*):
        The platform where this client is running.
        Defaults to 'other'
```

##### Methods

###### `def __init__(self, name: str, api_id: Optional[Union[int, str]] = None, api_hash: Optional[str] = None, app_version: str = APP_VERSION, device_model: str = DEVICE_MODEL, system_version: str = SYSTEM_VERSION, system_lang_code: str = SYSTEM_LANG_CODE, lang_code: str = LANG_CODE, lang_pack: str = LANG_PACK, ipv6: Optional[bool] = False, alt_port: Optional[bool] = False, proxy: Optional[dict] = None, test_mode: Optional[bool] = False, bot_token: Optional[str] = None, session_string: Optional[str] = None, use_qrcode: Optional[bool] = False, in_memory: Optional[bool] = None, mongodb: Optional[dict] = None, storage: Optional[Storage] = None, phone_number: Optional[str] = None, phone_code: Optional[str] = None, password: Optional[str] = None, workers: int = WORKERS, workdir: Union[str, Path] = WORKDIR, plugins: Optional[dict] = None, parse_mode: 'enums.ParseMode' = enums.ParseMode.DEFAULT, no_updates: Optional[bool] = None, skip_updates: bool = True, takeout: bool = None, sleep_threshold: int = Session.SLEEP_THRESHOLD, hide_password: Optional[bool] = True, max_concurrent_transmissions: int = MAX_CONCURRENT_TRANSMISSIONS, client_platform: 'enums.ClientPlatform' = enums.ClientPlatform.OTHER, max_message_cache_size: int = MAX_CACHE_SIZE, max_business_user_connection_cache_size: int = MAX_CACHE_SIZE)`

_No docstring._

###### `def __enter__(self)`

_No docstring._

###### `def __exit__(self, *args)`

_No docstring._

###### `async def __aenter__(self)`

_No docstring._

###### `async def __aexit__(self, *args)`

_No docstring._

###### `async def updates_watchdog(self)`

_No docstring._

###### `async def _wait_for_update_login_token(self)`

```text
Wait for an UpdateLoginToken update from Telegram.
```

###### `async def authorize(self) -> User`

_No docstring._

###### `def set_parse_mode(self, parse_mode: Optional['enums.ParseMode'])`

```text
Set the parse mode to be used globally by the client.

When setting the parse mode with this method, all other methods having a *parse_mode* parameter will follow the
global value by default.

Parameters:
    parse_mode (:obj:`~pyrogram.enums.ParseMode`):
        By default, texts are parsed using both Markdown and HTML styles.
        You can combine both syntaxes together.

Example:
    .. code-block:: python

        from pyrogram import enums

        # Default combined mode: Markdown + HTML
        await app.send_message("me", "1. **markdown** and <i>html</i>")

        # Force Markdown-only, HTML is disabled
        app.set_parse_mode(enums.ParseMode.MARKDOWN)
        await app.send_message("me", "2. **markdown** and <i>html</i>")

        # Force HTML-only, Markdown is disabled
        app.set_parse_mode(enums.ParseMode.HTML)
        await app.send_message("me", "3. **markdown** and <i>html</i>")

        # Disable the parser completely
        app.set_parse_mode(enums.ParseMode.DISABLED)
        await app.send_message("me", "4. **markdown** and <i>html</i>")

        # Bring back the default combined mode
        app.set_parse_mode(enums.ParseMode.DEFAULT)
        await app.send_message("me", "5. **markdown** and <i>html</i>")
```

###### `async def fetch_peers(self, peers: List[Union[raw.types.User, raw.types.Chat, raw.types.Channel]]) -> bool`

_No docstring._

###### `async def handle_updates(self, updates)`

_No docstring._

###### `async def recover_gaps(self) -> Tuple[int, int]`

_No docstring._

###### `async def load_session(self)`

_No docstring._

###### `def is_excluded(self, exclude, module)`

_No docstring._

###### `def load_plugins(self)`

_No docstring._

###### `async def handle_download(self, packet)`

_No docstring._

###### `async def get_file(self, file_id: FileId, file_size: int = 0, limit: int = 0, offset: int = 0, progress: Callable = None, progress_args: tuple = ()) -> Optional[AsyncGenerator[bytes, None]]`

_No docstring._

###### `def guess_mime_type(self, filename: str) -> Optional[str]`

_No docstring._

###### `def guess_extension(self, mime_type: str) -> Optional[str]`

_No docstring._

#### `class Cache`

_No docstring._

##### Methods

###### `def __init__(self, capacity: int)`

_No docstring._

###### `def __getitem__(self, key)`

_No docstring._

###### `def __setitem__(self, key, value)`

_No docstring._

---

## File: `dispatcher.py`

### Classes

#### `class Dispatcher`

_No docstring._

##### Methods

###### `def __init__(self, client: 'pyrogram.Client')`

_No docstring._

###### `async def start(self)`

_No docstring._

###### `async def stop(self)`

_No docstring._

###### `def add_handler(self, handler, group: int)`

_No docstring._

###### `def remove_handler(self, handler, group: int)`

_No docstring._

###### `async def handler_worker(self, lock: asyncio.Lock)`

_No docstring._

###### `async def _handle_packet(self, packet, lock: asyncio.Lock)`

_No docstring._

###### `async def _dispatch_to_handlers(self, update, users, chats, parsed_update, handler_type)`

_No docstring._

###### `async def _match_handler(self, handler, update, users, chats, parsed_update, handler_type)`

_No docstring._

###### `async def _execute_handler(self, handler, *args: Any)`

_No docstring._

###### `async def _handle_exception(self, parsed_update: types.Update, exception: Exception)`

_No docstring._

---

## File: `emoji.py`

---

## File: `file_id.py`

### Top-level Functions

#### `def b64_encode(s: bytes) -> str`

```text
Encode bytes into a URL-safe Base64 string without padding

Parameters:
    s (``bytes``):
        Bytes to encode

Returns:
    ``str``: The encoded bytes
```

#### `def b64_decode(s: str) -> bytes`

```text
Decode a URL-safe Base64 string without padding to bytes

Parameters:
    s (``str``):
        String to decode

Returns:
    ``bytes``: The decoded string
```

#### `def rle_encode(s: bytes) -> bytes`

```text
Zero-value RLE encoder

Parameters:
    s (``bytes``):
        Bytes to encode

Returns:
    ``bytes``: The encoded bytes
```

#### `def rle_decode(s: bytes) -> bytes`

```text
Zero-value RLE decoder

Parameters:
    s (``bytes``):
        Bytes to decode

Returns:
    ``bytes``: The decoded bytes
```

### Classes

#### `class FileType(IntEnum)`

```text
Known file types
```

#### `class ThumbnailSource(IntEnum)`

```text
Known thumbnail sources
```

#### `class FileId`

_No docstring._

##### Methods

###### `def __init__(self, *, major: int = MAJOR, minor: int = MINOR, file_type: FileType, dc_id: int, file_reference: bytes = b'', url: str = None, media_id: int = None, access_hash: int = None, volume_id: int = None, thumbnail_source: ThumbnailSource = None, thumbnail_file_type: FileType = None, thumbnail_size: str = '', secret: int = None, local_id: int = None, chat_id: int = None, chat_access_hash: int = None, sticker_set_id: int = None, sticker_set_access_hash: int = None)`

_No docstring._

###### `def decode(file_id: str)`

_No docstring._

###### `def encode(self, *, major: int = None, minor: int = None)`

_No docstring._

###### `def __str__(self)`

_No docstring._

#### `class FileUniqueType(IntEnum)`

```text
Known file unique types
```

#### `class FileUniqueId`

_No docstring._

##### Methods

###### `def __init__(self, *, file_unique_type: FileUniqueType, url: str = None, media_id: int = None, volume_id: int = None, local_id: int = None)`

_No docstring._

###### `def decode(file_unique_id: str)`

_No docstring._

###### `def encode(self)`

_No docstring._

###### `def __str__(self)`

_No docstring._

---

## File: `filters.py`

### Top-level Functions

#### `def create(func: Callable, name: str = None, **kwargs) -> Filter`

```text
Easily create a custom filter.

Custom filters give you extra control over which updates are allowed or not to be processed by your handlers.

Parameters:
    func (``Callable``):
        A function that accepts three positional arguments *(filter, client, update)* and returns a boolean: True if the
        update should be handled, False otherwise.
        The *filter* argument refers to the filter itself and can be used to access keyword arguments (read below).
        The *client* argument refers to the :obj:`~pyrogram.Client` that received the update.
        The *update* argument type will vary depending on which `Handler <handlers>`_ is coming from.
        For example, in a :obj:`~pyrogram.handlers.MessageHandler` the *update* argument will be a :obj:`~pyrogram.types.Message`; in a :obj:`~pyrogram.handlers.CallbackQueryHandler` the *update* will be a :obj:`~pyrogram.types.CallbackQuery`.
        Your function body can then access the incoming update attributes and decide whether to allow it or not.

    name (``str``, *optional*):
        Your filter's name. Can be anything you like.
        Defaults to "CustomFilter".

    **kwargs (``any``, *optional*):
        Any keyword argument you would like to pass. Useful when creating parameterized custom filters, such as
        :meth:`~pyrogram.filters.command` or :meth:`~pyrogram.filters.regex`.
```

#### `async def all_filter(_, __, ___)`

_No docstring._

#### `async def me_filter(_, __, m: Message)`

_No docstring._

#### `async def bot_filter(_, __, m: Message)`

_No docstring._

#### `async def incoming_filter(_, __, m: Message)`

_No docstring._

#### `async def outgoing_filter(_, __, m: Message)`

_No docstring._

#### `async def text_filter(_, __, m: Message)`

_No docstring._

#### `async def reply_filter(_, __, m: Message)`

_No docstring._

#### `async def reaction_filter(_, __, m: Message)`

_No docstring._

#### `async def forwarded_filter(_, __, m: Message)`

_No docstring._

#### `async def caption_filter(_, __, m: Message)`

_No docstring._

#### `async def audio_filter(_, __, m: Message)`

_No docstring._

#### `async def document_filter(_, __, m: Message)`

_No docstring._

#### `async def photo_filter(_, __, m: Message)`

_No docstring._

#### `async def sticker_filter(_, __, m: Message)`

_No docstring._

#### `async def animation_filter(_, __, m: Message)`

_No docstring._

#### `async def game_filter(_, __, m: Message)`

_No docstring._

#### `async def giveaway_filter(_, __, m: Message)`

_No docstring._

#### `async def giveaway_result_filter(_, __, m: Message)`

_No docstring._

#### `async def gift_code_filter(_, __, m: Message)`

_No docstring._

#### `async def star_gift_filter(_, __, m: Message)`

_No docstring._

#### `async def video_filter(_, __, m: Message)`

_No docstring._

#### `async def media_group_filter(_, __, m: Message)`

_No docstring._

#### `async def voice_filter(_, __, m: Message)`

_No docstring._

#### `async def video_note_filter(_, __, m: Message)`

_No docstring._

#### `async def contact_filter(_, __, m: Message)`

_No docstring._

#### `async def location_filter(_, __, m: Message)`

_No docstring._

#### `async def venue_filter(_, __, m: Message)`

_No docstring._

#### `async def web_page_filter(_, __, m: Message)`

_No docstring._

#### `async def poll_filter(_, __, m: Message)`

_No docstring._

#### `async def dice_filter(_, __, m: Message)`

_No docstring._

#### `async def media_spoiler_filter(_, __, m: Message)`

_No docstring._

#### `async def private_filter(_, __, m: Message)`

_No docstring._

#### `async def group_filter(_, __, m: Message)`

_No docstring._

#### `async def channel_filter(_, __, m: Message)`

_No docstring._

#### `async def new_chat_members_filter(_, __, m: Message)`

_No docstring._

#### `async def left_chat_member_filter(_, __, m: Message)`

_No docstring._

#### `async def new_chat_title_filter(_, __, m: Message)`

_No docstring._

#### `async def new_chat_photo_filter(_, __, m: Message)`

_No docstring._

#### `async def delete_chat_photo_filter(_, __, m: Message)`

_No docstring._

#### `async def group_chat_created_filter(_, __, m: Message)`

_No docstring._

#### `async def supergroup_chat_created_filter(_, __, m: Message)`

_No docstring._

#### `async def channel_chat_created_filter(_, __, m: Message)`

_No docstring._

#### `async def migrate_to_chat_id_filter(_, __, m: Message)`

_No docstring._

#### `async def migrate_from_chat_id_filter(_, __, m: Message)`

_No docstring._

#### `async def pinned_message_filter(_, __, m: Message)`

_No docstring._

#### `async def game_high_score_filter(_, __, m: Message)`

_No docstring._

#### `async def reply_keyboard_filter(_, __, m: Message)`

_No docstring._

#### `async def inline_keyboard_filter(_, __, m: Message)`

_No docstring._

#### `async def mentioned_filter(_, __, m: Message)`

_No docstring._

#### `async def via_bot_filter(_, __, m: Message)`

_No docstring._

#### `async def video_chat_started_filter(_, __, m: Message)`

_No docstring._

#### `async def video_chat_ended_filter(_, __, m: Message)`

_No docstring._

#### `async def video_chat_members_invited_filter(_, __, m: Message)`

_No docstring._

#### `async def successful_payment_filter(_, __, m: Message)`

_No docstring._

#### `async def service_filter(_, __, m: Message)`

_No docstring._

#### `async def media_filter(_, __, m: Message)`

_No docstring._

#### `async def scheduled_filter(_, __, m: Message)`

_No docstring._

#### `async def from_scheduled_filter(_, __, m: Message)`

_No docstring._

#### `async def linked_channel_filter(_, __, m: Message)`

_No docstring._

#### `async def forum_topic_closed_filter(_, __, m: Message)`

_No docstring._

#### `async def forum_topic_created_filter(_, __, m: Message)`

_No docstring._

#### `async def forum_topic_edited_filter(_, __, m: Message)`

_No docstring._

#### `async def forum_topic_reopened_filter(_, __, m: Message)`

_No docstring._

#### `async def general_topic_hidden_filter(_, __, m: Message)`

_No docstring._

#### `async def general_topic_unhidden_filter(_, __, m: Message)`

_No docstring._

#### `def command(commands: Union[str, List[str]], prefixes: Union[str, List[str]] = '/', case_sensitive: bool = False)`

```text
Filter commands, i.e.: text messages starting with "/" or any other custom prefix.

Parameters:
    commands (``str`` | ``list``):
        The command or list of commands as string the filter should look for.
        Examples: "start", ["start", "help", "settings"]. When a message text containing
        a command arrives, the command itself and its arguments will be stored in the *command*
        field of the :obj:`~pyrogram.types.Message`.

    prefixes (``str`` | ``list``, *optional*):
        A prefix or a list of prefixes as string the filter should look for.
        Defaults to "/" (slash). Examples: ".", "!", ["/", "!", "."], list(".:!").
        Pass None or "" (empty string) to allow commands with no prefix at all.

    case_sensitive (``bool``, *optional*):
        Pass True if you want your command(s) to be case sensitive. Defaults to False.
        Examples: when True, command="Start" would trigger /Start but not /start.
```

#### `def regex(pattern: Union[str, Pattern], flags: int = 0)`

```text
Filter updates that match a given regular expression pattern.

Can be applied to handlers that receive one of the following updates:

- :obj:`~pyrogram.types.Message`: The filter will match ``text`` or ``caption``.
- :obj:`~pyrogram.types.CallbackQuery`: The filter will match ``data``.
- :obj:`~pyrogram.types.InlineQuery`: The filter will match ``query``.
- :obj:`~pyrogram.types.PreCheckoutQuery`: The filter will match ``payload``.

When a pattern matches, all the `Match Objects <https://docs.python.org/3/library/re.html#match-objects>`_ are
stored in the ``matches`` field of the update object itself.

Parameters:
    pattern (``str`` | ``Pattern``):
        The regex pattern as string or as pre-compiled pattern.

    flags (``int``, *optional*):
        Regex flags.
```

### Classes

#### `class Filter`

_No docstring._

##### Methods

###### `async def __call__(self, client: 'pyrogram.Client', update: Update)`

_No docstring._

###### `def __invert__(self)`

_No docstring._

###### `def __and__(self, other)`

_No docstring._

###### `def __or__(self, other)`

_No docstring._

#### `class InvertFilter(Filter)`

_No docstring._

##### Methods

###### `def __init__(self, base)`

_No docstring._

###### `async def __call__(self, client: 'pyrogram.Client', update: Update)`

_No docstring._

#### `class AndFilter(Filter)`

_No docstring._

##### Methods

###### `def __init__(self, base, other)`

_No docstring._

###### `async def __call__(self, client: 'pyrogram.Client', update: Update)`

_No docstring._

#### `class OrFilter(Filter)`

_No docstring._

##### Methods

###### `def __init__(self, base, other)`

_No docstring._

###### `async def __call__(self, client: 'pyrogram.Client', update: Update)`

_No docstring._

#### `class user(Filter, set)`

```text
Filter messages coming from one or more users.

You can use `set bound methods <https://docs.python.org/3/library/stdtypes.html#set>`_ to manipulate the
users container.

Parameters:
    users (``int`` | ``str`` | ``list``):
        Pass one or more user ids/usernames to filter users.
        For you yourself, "me" or "self" can be used as well.
        Defaults to None (no users).
```

##### Methods

###### `def __init__(self, users: Union[int, str, List[Union[int, str]]] = None)`

_No docstring._

###### `async def __call__(self, _, message: Message)`

_No docstring._

#### `class chat(Filter, set)`

```text
Filter messages coming from one or more chats.

You can use `set bound methods <https://docs.python.org/3/library/stdtypes.html#set>`_ to manipulate the
chats container.

Parameters:
    chats (``int`` | ``str`` | ``list``):
        Pass one or more chat ids/usernames to filter chats.
        For your personal cloud (Saved Messages) you can simply use "me" or "self".
        Defaults to None (no chats).
```

##### Methods

###### `def __init__(self, chats: Union[int, str, List[Union[int, str]]] = None)`

_No docstring._

###### `async def __call__(self, _, message: Union[Message, Story])`

_No docstring._

#### `class topic(Filter, set)`

```text
Filter messages coming from one or more topics.
You can use `set bound methods <https://docs.python.org/3/library/stdtypes.html#set>`_ to manipulate the
topics container.
Parameters:
    topics (``int`` | ``list``):
        Pass one or more topic ids to filter messages in specific topics.
        Pass 1 for general topic.
        Defaults to None (no topics).
```

##### Methods

###### `def __init__(self, topics: Union[int, List[int]] = None)`

_No docstring._

###### `async def __call__(self, _, message: Message)`

_No docstring._

---

## File: `mime_types.py`

---

## File: `sync.py`

### Top-level Functions

#### `def async_to_sync(obj, name)`

_No docstring._

#### `def wrap(source)`

_No docstring._

---

## File: `utils.py`

### Top-level Functions

#### `async def ainput(prompt: str = '', *, hide: bool = False)`

```text
Just like the built-in input, but async
```

#### `def get_input_media_from_file_id(file_id: str, expected_file_type: FileType = None, ttl_seconds: int = None, has_spoiler: bool = None) -> Union['raw.types.InputMediaPhoto', 'raw.types.InputMediaDocument']`

_No docstring._

#### `async def parse_messages(client, messages: 'raw.types.messages.Messages', replies: int = 1, business_connection_id: str = None, is_scheduled: bool = False) -> List['types.Message']`

_No docstring._

#### `def parse_deleted_messages(client, update, business_connection_id: str = None) -> List['types.Message']`

_No docstring._

#### `def pack_inline_message_id(msg_id: 'raw.base.InputBotInlineMessageID')`

_No docstring._

#### `def unpack_inline_message_id(inline_message_id: str) -> 'raw.base.InputBotInlineMessageID'`

_No docstring._

#### `def get_raw_peer_id(peer: Union[raw.base.Peer, raw.base.RequestedPeer, raw.base.InputPeer]) -> Optional[int]`

```text
Get the raw peer id from a Peer object
```

#### `def get_peer_id(peer: Union[raw.base.Peer, raw.base.InputPeer]) -> int`

```text
Get the non-raw peer id from a Peer object
```

#### `def get_peer_type(peer_id: int) -> str`

_No docstring._

#### `def get_channel_id(peer_id: int) -> int`

_No docstring._

#### `def btoi(b: bytes) -> int`

_No docstring._

#### `def itob(i: int) -> bytes`

_No docstring._

#### `def sha256(data: bytes) -> bytes`

_No docstring._

#### `def xor(a: bytes, b: bytes) -> bytes`

_No docstring._

#### `def compute_password_hash(algo: raw.types.PasswordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow, password: str) -> bytes`

_No docstring._

#### `def compute_password_check(r: raw.types.account.Password, password: str) -> raw.types.InputCheckPasswordSRP`

_No docstring._

#### `async def parse_text_entities(client: 'pyrogram.Client', text: str, parse_mode: enums.ParseMode, entities: List['types.MessageEntity']) -> Dict[str, Union[str, List[raw.base.MessageEntity]]]`

_No docstring._

#### `def zero_datetime() -> datetime`

_No docstring._

#### `def timestamp_to_datetime(ts: Optional[int]) -> Optional[datetime]`

_No docstring._

#### `def datetime_to_timestamp(dt: Optional[datetime]) -> Optional[int]`

_No docstring._

#### `async def run_sync(func: Callable[..., TypeVar('Result')], *args: Any, **kwargs: Any) -> TypeVar('Result')`

_No docstring._

#### `def parse_text_with_entities(client, message: 'raw.types.TextWithEntities', users)`

_No docstring._

#### `async def get_reply_to(client: 'pyrogram.Client', chat_id: Union[int, str] = None, reply_to_message_id: int = None, reply_to_story_id: int = None, message_thread_id: int = None, reply_to_monoforum_id: Union[int, str] = None, reply_to_chat_id: Union[int, str] = None, quote_text: str = None, quote_entities: List['types.MessageEntity'] = None, quote_offset: int = None, parse_mode: 'enums.ParseMode' = None)`

_No docstring._

#### `def get_first_url(text)`

_No docstring._

---
