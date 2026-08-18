---
name: api-api-handlers
description: Offline API backup extracted from Pyrofork source docstrings.
---

# Pyrofork API Backup: `handlers`

Extracted from `sources/pyrofork/pyrogram/**.py` using AST parsing of module, class, function, and method docstrings.

## File: `handlers/__init__.py`

---

## File: `handlers/bot_business_connect_handler.py`

### Classes

#### `class BotBusinessConnectHandler(Handler)`

```text
The Bot Business Connection handler class. Used to handle new bot business connection.
It is intended to be used with :meth:`~pyrogram.Client.add_handler`

For a nicer way to register this handler, have a look at the
:meth:`~pyrogram.Client.on_bot_business_connect` decorator.

Parameters:
    callback (``Callable``):
        Pass a function that will be called when a new Stories arrives. It takes *(client, story)*
        as positional arguments (look at the section below for a detailed description).

    filters (:obj:`Filters`):
        Pass one or more filters to allow only a subset of stories to be passed
        in your callback function.

Other parameters:
    client (:obj:`~pyrogram.Client`):
        The Client itself, useful when you want to call other API methods inside the story handler.

    bot_connection (:obj:`~pyrogram.types.BotBusinessConnection`):
        Information about the received Bot Business Connection.
```

##### Methods

###### `def __init__(self, callback: Callable, filters = None)`

_No docstring._

---

## File: `handlers/bot_business_message_handler.py`

### Classes

#### `class BotBusinessMessageHandler(Handler)`

```text
The Bot Business Message handler class. Used to handle new bot business messages.
It is intended to be used with :meth:`~pyrogram.Client.add_handler`

For a nicer way to register this handler, have a look at the
:meth:`~pyrogram.Client.on_bot_business_message` decorator.

Parameters:
    callback (``Callable``):
        Pass a function that will be called when a new Message arrives. It takes *(client, message)*
        as positional arguments (look at the section below for a detailed description).

    filters (:obj:`Filters`):
        Pass one or more filters to allow only a subset of messages to be passed
        in your callback function.

Other parameters:
    client (:obj:`~pyrogram.Client`):
        The Client itself, useful when you want to call other API methods inside the message handler.

    message (:obj:`~pyrogram.types.Message`):
        The received message.
```

##### Methods

###### `def __init__(self, callback: Callable, filters = None)`

_No docstring._

###### `async def check_if_has_matching_listener(self, client: 'pyrogram.Client', message: Message)`

```text
Checks if the message has a matching listener.

:param client: The Client object to check with.
:param message: The Message object to check with.
:return: A tuple of whether the message has a matching listener and its filters does match with the Message
and the matching listener;
```

###### `async def check(self, client: 'pyrogram.Client', message: Message)`

```text
Checks if the message has a matching listener or handler and its filters does match with the Message.

:param client: Client object to check with.
:param message: Message object to check with.
:return: Whether the message has a matching listener or handler and its filters does match with the Message.
```

###### `async def resolve_future_or_callback(self, client: 'pyrogram.Client', message: Message, *args)`

```text
Resolves the future or calls the callback of the listener if the message has a matching listener.

:param client: Client object to resolve or call with.
:param message: Message object to resolve or call with.
:param args: Arguments to call the callback with.
:return: None
```

---

## File: `handlers/callback_query_handler.py`

### Classes

#### `class CallbackQueryHandler(Handler)`

```text
The CallbackQuery handler class. Used to handle callback queries coming from inline buttons.
It is intended to be used with :meth:`~pyrogram.Client.add_handler`

For a nicer way to register this handler, have a look at the
:meth:`~pyrogram.Client.on_callback_query` decorator.

Parameters:
    callback (``Callable``):
        Pass a function that will be called when a new CallbackQuery arrives. It takes *(client, callback_query)*
        as positional arguments (look at the section below for a detailed description).

    filters (:obj:`Filters`):
        Pass one or more filters to allow only a subset of callback queries to be passed
        in your callback function.

Other parameters:
    client (:obj:`~pyrogram.Client`):
        The Client itself, useful when you want to call other API methods inside the message handler.

    callback_query (:obj:`~pyrogram.types.CallbackQuery`):
        The received callback query.
```

##### Methods

###### `def __init__(self, callback: Callable, filters = None)`

_No docstring._

###### `def compose_data_identifier(self, query: CallbackQuery)`

```text
Composes an Identifier object from a CallbackQuery object.

:param query: The CallbackQuery object to compose of.
:return: An Identifier object.
```

###### `async def check_if_has_matching_listener(self, client: 'pyrogram.Client', query: CallbackQuery) -> Tuple[bool, Listener]`

```text
Checks if the CallbackQuery object has a matching listener.

:param client: The Client object to check with.
:param query: The CallbackQuery object to check with.
:return: A tuple of a boolean and a Listener object. The boolean indicates whether
the found listener has filters and its filters matches with the CallbackQuery object.
The Listener object is the matching listener.
```

###### `async def check(self, client: 'pyrogram.Client', query: CallbackQuery)`

```text
Checks if the CallbackQuery object has a matching listener or handler.

:param client: The Client object to check with.
:param query: The CallbackQuery object to check with.
:return: A boolean indicating whether the CallbackQuery object has a matching listener or the handler
filter matches.
```

###### `async def resolve_future_or_callback(self, client: 'pyrogram.Client', query: CallbackQuery, *args)`

```text
Resolves the future or calls the callback of the listener. Will call the original handler if no listener.

:param client: The Client object to resolve or call with.
:param query: The CallbackQuery object to resolve or call with.
:param args: The arguments to call the callback with.
:return: None
```

---

## File: `handlers/chat_join_request_handler.py`

### Classes

#### `class ChatJoinRequestHandler(Handler)`

```text
The ChatJoinRequest handler class. Used to handle join chat requests.
It is intended to be used with :meth:`~pyrogram.Client.add_handler`.

For a nicer way to register this handler, have a look at the
:meth:`~pyrogram.Client.on_chat_join_request` decorator.

Parameters:
    callback (``Callable``):
        Pass a function that will be called when a new ChatJoinRequest event arrives. It takes
        *(client, chat_join_request)* as positional arguments (look at the section below for a detailed
        description).

    filters (:obj:`Filters`):
        Pass one or more filters to allow only a subset of updates to be passed in your callback function.

Other parameters:
    client (:obj:`~pyrogram.Client`):
        The Client itself, useful when you want to call other API methods inside the handler.

    chat_join_request (:obj:`~pyrogram.types.ChatJoinRequest`):
        The received chat join request.
```

##### Methods

###### `def __init__(self, callback: Callable, filters = None)`

_No docstring._

---

## File: `handlers/chat_member_updated_handler.py`

### Classes

#### `class ChatMemberUpdatedHandler(Handler)`

```text
The ChatMemberUpdated handler class. Used to handle changes in the status of a chat member.
It is intended to be used with :meth:`~pyrogram.Client.add_handler`.

For a nicer way to register this handler, have a look at the
:meth:`~pyrogram.Client.on_chat_member_updated` decorator.

Parameters:
    callback (``Callable``):
        Pass a function that will be called when a new ChatMemberUpdated event arrives. It takes
        *(client, chat_member_updated)* as positional arguments (look at the section below for a detailed
        description).

    filters (:obj:`Filters`):
        Pass one or more filters to allow only a subset of updates to be passed in your callback function.

Other parameters:
    client (:obj:`~pyrogram.Client`):
        The Client itself, useful when you want to call other API methods inside the handler.

    chat_member_updated (:obj:`~pyrogram.types.ChatMemberUpdated`):
        The received chat member update.
```

##### Methods

###### `def __init__(self, callback: Callable, filters = None)`

_No docstring._

---

## File: `handlers/chosen_inline_result_handler.py`

### Classes

#### `class ChosenInlineResultHandler(Handler)`

```text
The ChosenInlineResultHandler handler class. Used to handle chosen inline results coming from inline queries.
It is intended to be used with :meth:`~pyrogram.Client.add_handler`

For a nicer way to register this handler, have a look at the
:meth:`~pyrogram.Client.on_chosen_inline_result` decorator.

Parameters:
    callback (``Callable``):
        Pass a function that will be called when a new chosen inline result arrives.
        It takes *(client, chosen_inline_result)* as positional arguments (look at the section below for a
        detailed description).

    filters (:obj:`Filters`):
        Pass one or more filters to allow only a subset of chosen inline results to be passed
        in your callback function.

Other parameters:
    client (:obj:`~pyrogram.Client`):
        The Client itself, useful when you want to call other API methods inside the message handler.

    chosen_inline_result (:obj:`~pyrogram.types.ChosenInlineResult`):
        The received chosen inline result.
```

##### Methods

###### `def __init__(self, callback: Callable, filters = None)`

_No docstring._

---

## File: `handlers/conversation_handler.py`

### Classes

#### `class ConversationHandler(MessageHandler, CallbackQueryHandler)`

```text
The Conversation handler class.
```

##### Methods

###### `def __init__(self)`

_No docstring._

###### `async def check(self, client: 'pyrogram.Client', update: Union[Message, CallbackQuery])`

_No docstring._

###### `async def callback(_, __)`

_No docstring._

###### `def delete_waiter(self, chat_id, future)`

_No docstring._

---

## File: `handlers/deleted_bot_business_messages_handler.py`

### Classes

#### `class DeletedBotBusinessMessagesHandler(Handler)`

```text
The deleted bot business messages handler class. Used to handle deleted messages coming from any chat
(private, group, channel). It is intended to be used with :meth:`~pyrogram.Client.add_handler`

For a nicer way to register this handler, have a look at the
:meth:`~pyrogram.Client.on_deleted_bot_business_messages` decorator.

Parameters:
    callback (``Callable``):
        Pass a function that will be called when one or more messages have been deleted.
        It takes *(client, messages)* as positional arguments (look at the section below for a detailed description).

    filters (:obj:`Filters`):
        Pass one or more filters to allow only a subset of messages to be passed
        in your callback function.

Other parameters:
    client (:obj:`~pyrogram.Client`):
        The Client itself, useful when you want to call other API methods inside the message handler.

    messages (List of :obj:`~pyrogram.types.Message`):
        The deleted messages, as list.
```

##### Methods

###### `def __init__(self, callback: Callable, filters: Filter = None)`

_No docstring._

###### `async def check(self, client: 'pyrogram.Client', messages: List[Message])`

_No docstring._

---

## File: `handlers/deleted_messages_handler.py`

### Classes

#### `class DeletedMessagesHandler(Handler)`

```text
The deleted messages handler class. Used to handle deleted messages coming from any chat
(private, group, channel). It is intended to be used with :meth:`~pyrogram.Client.add_handler`

For a nicer way to register this handler, have a look at the
:meth:`~pyrogram.Client.on_deleted_messages` decorator.

Parameters:
    callback (``Callable``):
        Pass a function that will be called when one or more messages have been deleted.
        It takes *(client, messages)* as positional arguments (look at the section below for a detailed description).

    filters (:obj:`Filters`):
        Pass one or more filters to allow only a subset of messages to be passed
        in your callback function.

Other parameters:
    client (:obj:`~pyrogram.Client`):
        The Client itself, useful when you want to call other API methods inside the message handler.

    messages (List of :obj:`~pyrogram.types.Message`):
        The deleted messages, as list.
```

##### Methods

###### `def __init__(self, callback: Callable, filters: Filter = None)`

_No docstring._

###### `async def check(self, client: 'pyrogram.Client', messages: List[Message])`

_No docstring._

---

## File: `handlers/disconnect_handler.py`

### Classes

#### `class DisconnectHandler(Handler)`

```text
The Disconnect handler class. Used to handle disconnections. It is intended to be used with
:meth:`~pyrogram.Client.add_handler`

For a nicer way to register this handler, have a look at the
:meth:`~pyrogram.Client.on_disconnect` decorator.

Parameters:
    callback (``Callable``):
        Pass a function that will be called when a disconnection occurs. It takes *(client)*
        as positional argument (look at the section below for a detailed description).

Other parameters:
    client (:obj:`~pyrogram.Client`):
        The Client itself. Useful, for example, when you want to change the proxy before a new connection
        is established.
```

##### Methods

###### `def __init__(self, callback: Callable)`

_No docstring._

---

## File: `handlers/edited_bot_business_message_handler.py`

### Classes

#### `class EditedBotBusinessMessageHandler(Handler)`

```text
The EditedBotBusinessMessageHandler handler class. Used to handle edited bot business messages.
 It is intended to be used with :meth:`~pyrogram.Client.add_handler`

For a nicer way to register this handler, have a look at the
:meth:`~pyrogram.Client.on_edited_bot_business_message` decorator.

Parameters:
    callback (``Callable``):
        Pass a function that will be called when a new edited message arrives. It takes *(client, message)*
        as positional arguments (look at the section below for a detailed description).

    filters (:obj:`Filters`):
        Pass one or more filters to allow only a subset of messages to be passed
        in your callback function.

Other parameters:
    client (:obj:`~pyrogram.Client`):
        The Client itself, useful when you want to call other API methods inside the message handler.

    edited_message (:obj:`~pyrogram.types.Message`):
        The received edited message.
```

##### Methods

###### `def __init__(self, callback: Callable, filters = None)`

_No docstring._

---

## File: `handlers/edited_message_handler.py`

### Classes

#### `class EditedMessageHandler(Handler)`

```text
The EditedMessage handler class. Used to handle edited messages.
 It is intended to be used with :meth:`~pyrogram.Client.add_handler`

For a nicer way to register this handler, have a look at the
:meth:`~pyrogram.Client.on_edited_message` decorator.

Parameters:
    callback (``Callable``):
        Pass a function that will be called when a new edited message arrives. It takes *(client, message)*
        as positional arguments (look at the section below for a detailed description).

    filters (:obj:`Filters`):
        Pass one or more filters to allow only a subset of messages to be passed
        in your callback function.

Other parameters:
    client (:obj:`~pyrogram.Client`):
        The Client itself, useful when you want to call other API methods inside the message handler.

    edited_message (:obj:`~pyrogram.types.Message`):
        The received edited message.
```

##### Methods

###### `def __init__(self, callback: Callable, filters = None)`

_No docstring._

---

## File: `handlers/error_handler.py`

### Classes

#### `class ErrorHandler(Handler)`

```text
The Error handler class. Used to handle errors.
It is intended to be used with :meth:`~pyrogram.Client.add_handler`

For a nicer way to register this handler, have a look at the
:meth:`~pyrogram.Client.on_error` decorator.

Parameters:
    callback (``Callable``):
        Pass a function that will be called when a new Error arrives. It takes *(client, error)*
        as positional arguments (look at the section below for a detailed description).

    exceptions (``Exception`` | Iterable of ``Exception``, *optional*):
        Pass one or more exception classes to allow only a subset of errors to be passed
        in your callback function.

Other parameters:
    client (:obj:`~pyrogram.Client`):
        The Client itself, useful when you want to call other API methods inside the error handler.

    update (:obj:`~pyrogram.Update`):
        The update that caused the error.

    error (``Exception``):
        The error that was raised.
```

##### Methods

###### `def __init__(self, callback: Callable, exceptions: type[Exception] | Iterable[type[Exception]] | None = None)`

_No docstring._

###### `async def check(self, client: pyrogram.Client, update: Update, exception: Exception) -> bool`

_No docstring._

###### `def check_remove(self, error: type[Exception] | Iterable[type[Exception]]) -> bool`

_No docstring._

---

## File: `handlers/handler.py`

### Classes

#### `class Handler`

_No docstring._

##### Methods

###### `def __init__(self, callback: Callable, filters: Filter = None)`

_No docstring._

###### `async def check(self, client: 'pyrogram.Client', update: Update)`

_No docstring._

---

## File: `handlers/inline_query_handler.py`

### Classes

#### `class InlineQueryHandler(Handler)`

```text
The InlineQuery handler class. Used to handle inline queries.
It is intended to be used with :meth:`~pyrogram.Client.add_handler`

For a nicer way to register this handler, have a look at the
:meth:`~pyrogram.Client.on_inline_query` decorator.

Parameters:
    callback (``Callable``):
        Pass a function that will be called when a new InlineQuery arrives. It takes *(client, inline_query)*
        as positional arguments (look at the section below for a detailed description).

    filters (:obj:`Filters`):
        Pass one or more filters to allow only a subset of inline queries to be passed
        in your callback function.

Other parameters:
    client (:obj:`~pyrogram.Client`):
        The Client itself, useful when you want to call other API methods inside the inline query handler.

    inline_query (:obj:`~pyrogram.types.InlineQuery`):
        The received inline query.
```

##### Methods

###### `def __init__(self, callback: Callable, filters = None)`

_No docstring._

---

## File: `handlers/message_handler.py`

### Classes

#### `class MessageHandler(Handler)`

```text
The Message handler class. Used to handle new messages.
It is intended to be used with :meth:`~pyrogram.Client.add_handler`

For a nicer way to register this handler, have a look at the
:meth:`~pyrogram.Client.on_message` decorator.

Parameters:
    callback (``Callable``):
        Pass a function that will be called when a new Message arrives. It takes *(client, message)*
        as positional arguments (look at the section below for a detailed description).

    filters (:obj:`Filters`):
        Pass one or more filters to allow only a subset of messages to be passed
        in your callback function.

Other parameters:
    client (:obj:`~pyrogram.Client`):
        The Client itself, useful when you want to call other API methods inside the message handler.

    message (:obj:`~pyrogram.types.Message`):
        The received message.
```

##### Methods

###### `def __init__(self, callback: Callable, filters = None)`

_No docstring._

###### `async def check_if_has_matching_listener(self, client: 'pyrogram.Client', message: Message)`

```text
Checks if the message has a matching listener.

:param client: The Client object to check with.
:param message: The Message object to check with.
:return: A tuple of whether the message has a matching listener and its filters does match with the Message
and the matching listener;
```

###### `async def check(self, client: 'pyrogram.Client', message: Message)`

```text
Checks if the message has a matching listener or handler and its filters does match with the Message.

:param client: Client object to check with.
:param message: Message object to check with.
:return: Whether the message has a matching listener or handler and its filters does match with the Message.
```

###### `async def resolve_future_or_callback(self, client: 'pyrogram.Client', message: Message, *args)`

```text
Resolves the future or calls the callback of the listener if the message has a matching listener.

:param client: Client object to resolve or call with.
:param message: Message object to resolve or call with.
:param args: Arguments to call the callback with.
:return: None
```

---

## File: `handlers/message_reaction_count_updated_handler.py`

### Classes

#### `class MessageReactionCountUpdatedHandler(Handler)`

```text
The MessageReactionCountUpdated handler class.
Used to handle changes in the anonymous reaction of a message.

It is intended to be used with :meth:`~pyrogram.Client.add_handler`.

For a nicer way to register this handler, have a look at the
:meth:`~pyrogram.Client.on_message_reaction_count_updated` decorator.

Parameters:
    callback (``Callable``):
        Pass a function that will be called when a new MessageReactionCountUpdated event arrives. It takes
        *(client, message_reaction_count_updated)* as positional arguments (look at the section below for a detailed
        description).

    filters (:obj:`Filters`):
        Pass one or more filters to allow only a subset of updates to be passed in your callback function.

Other parameters:
    client (:obj:`~pyrogram.Client`):
        The Client itself, useful when you want to call other API methods inside the handler.

    message_reaction_count_updated (:obj:`~pyrogram.types.MessageReactionCountUpdated`):
        The received message reaction count update.
```

##### Methods

###### `def __init__(self, callback: Callable, filters = None)`

_No docstring._

---

## File: `handlers/message_reaction_updated_handler.py`

### Classes

#### `class MessageReactionUpdatedHandler(Handler)`

```text
The MessageReactionUpdated handler class.
Used to handle changes in the reaction of a message.

It is intended to be used with :meth:`~pyrogram.Client.add_handler`.

For a nicer way to register this handler, have a look at the
:meth:`~pyrogram.Client.on_message_reaction_updated` decorator.

Parameters:
    callback (``Callable``):
        Pass a function that will be called when a new MessageReactionUpdated event arrives. It takes
        *(client, message_reaction_updated)* as positional arguments (look at the section below for a detailed
        description).

    filters (:obj:`Filters`):
        Pass one or more filters to allow only a subset of updates to be passed in your callback function.

Other parameters:
    client (:obj:`~pyrogram.Client`):
        The Client itself, useful when you want to call other API methods inside the handler.

    message_reaction_updated (:obj:`~pyrogram.types.MessageReactionUpdated`):
        The received message reaction update.
```

##### Methods

###### `def __init__(self, callback: Callable, filters = None)`

_No docstring._

---

## File: `handlers/poll_handler.py`

### Classes

#### `class PollHandler(Handler)`

```text
The Poll handler class. Used to handle polls updates.

It is intended to be used with :meth:`~pyrogram.Client.add_handler`

For a nicer way to register this handler, have a look at the
:meth:`~pyrogram.Client.on_poll` decorator.

Parameters:
    callback (``Callable``):
        Pass a function that will be called when a new poll update arrives. It takes *(client, poll)*
        as positional arguments (look at the section below for a detailed description).

    filters (:obj:`Filters`):
        Pass one or more filters to allow only a subset of polls to be passed
        in your callback function.

Other parameters:
    client (:obj:`~pyrogram.Client`):
        The Client itself, useful when you want to call other API methods inside the poll handler.

    poll (:obj:`~pyrogram.types.Poll`):
        The received poll.
```

##### Methods

###### `def __init__(self, callback: Callable, filters = None)`

_No docstring._

---

## File: `handlers/pre_checkout_query_handler.py`

### Classes

#### `class PreCheckoutQueryHandler(Handler)`

```text
The PreCheckoutQueryHandler handler class. Used to handle pre-checkout queries coming from buy buttons.
It is intended to be used with :meth:`~pyrogram.Client.add_handler`

For a nicer way to register this handler, have a look at the
:meth:`~pyrogram.Client.on_pre_checkout_query` decorator.

Parameters:
    callback (``Callable``):
        Pass a function that will be called when a new PreCheckoutQuery arrives. It takes *(client, pre_checkout_query)*
        as positional arguments (look at the section below for a detailed description).

    filters (:obj:`Filters`):
        Pass one or more filters to allow only a subset of callback queries to be passed
        in your callback function.

Other parameters:
    client (:obj:`~pyrogram.Client`):
        The Client itself, useful when you want to call other API methods inside the message handler.

    pre_checkout_query (:obj:`~pyrogram.types.PreCheckoutQuery`):
        New incoming pre-checkout query. Contains full information about checkout.
```

##### Methods

###### `def __init__(self, callback: Callable, filters = None)`

_No docstring._

---

## File: `handlers/purchased_paid_media_handler.py`

### Classes

#### `class PurchasedPaidMediaHandler(Handler)`

```text
The PurchasedPaidMedia handler class. Used to handle purchased paid medias.
It is intended to be used with :meth:`~pyrogram.Client.add_handler`

For a nicer way to register this handler, have a look at the
:meth:`~pyrogram.Client.on_purchased_paid_media` decorator.

Parameters:
    callback (``Callable``):
        Pass a function that will be called when a paid media purchased. It takes *(client, update)*
        as positional arguments (look at the section below for a detailed description).

    filters (:obj:`Filters`):
        Pass one or more filters to allow only a subset of updates to be passed
        in your callback function.

Other parameters:
    client (:obj:`~pyrogram.Client`):
        The Client itself, useful when you want to call other API methods inside the handler.

    update (:obj:`~pyrogram.types.PurchasedPaidMedia`):
        Information about who bought paid media.
```

##### Methods

###### `def __init__(self, callback: Callable, filters = None)`

_No docstring._

---

## File: `handlers/raw_update_handler.py`

### Classes

#### `class RawUpdateHandler(Handler)`

```text
The Raw Update handler class. Used to handle raw updates. It is intended to be used with
:meth:`~pyrogram.Client.add_handler`

For a nicer way to register this handler, have a look at the
:meth:`~pyrogram.Client.on_raw_update` decorator.

Parameters:
    callback (``Callable``):
        A function that will be called when a new update is received from the server. It takes
        *(client, update, users, chats)* as positional arguments (look at the section below for
        a detailed description).

    filters (:obj:`Filters`):
        Pass one or more filters to allow only a subset of callback queries to be passed
        in your callback function.

Other Parameters:
    client (:obj:`~pyrogram.Client`):
        The Client itself, useful when you want to call other API methods inside the update handler.

    update (``Update``):
        The received update, which can be one of the many single Updates listed in the
        :obj:`~pyrogram.raw.base.Update` base type.

    users (``dict``):
        Dictionary of all :obj:`~pyrogram.types.User` mentioned in the update.
        You can access extra info about the user (such as *first_name*, *last_name*, etc...) by using
        the IDs you find in the *update* argument (e.g.: *users[1768841572]*).

    chats (``dict``):
        Dictionary of all :obj:`~pyrogram.types.Chat` and
        :obj:`~pyrogram.raw.types.Channel` mentioned in the update.
        You can access extra info about the chat (such as *title*, *participants_count*, etc...)
        by using the IDs you find in the *update* argument (e.g.: *chats[1701277281]*).

Note:
    The following Empty or Forbidden types may exist inside the *users* and *chats* dictionaries.
    They mean you have been blocked by the user or banned from the group/channel.

    - :obj:`~pyrogram.raw.types.UserEmpty`
    - :obj:`~pyrogram.raw.types.ChatEmpty`
    - :obj:`~pyrogram.raw.types.ChatForbidden`
    - :obj:`~pyrogram.raw.types.ChannelForbidden`
```

##### Methods

###### `def __init__(self, callback: Callable, filters = None)`

_No docstring._

---

## File: `handlers/shipping_query_handler.py`

### Classes

#### `class ShippingQueryHandler(Handler)`

```text
The ShippingQueryHandler handler class. Used to handle shipping queries coming only from invoice buttons with flexible price.

It is intended to be used with :meth:`~pyrogram.Client.add_handler`

For a nicer way to register this handler, have a look at the
:meth:`~pyrogram.Client.on_shipping_query` decorator.

Parameters:
    callback (``Callable``):
        Pass a function that will be called when a new PreCheckoutQuery arrives. It takes *(client, shipping_query)*
        as positional arguments (look at the section below for a detailed description).

    filters (:obj:`Filters`):
        Pass one or more filters to allow only a subset of callback queries to be passed
        in your callback function.

Other parameters:
    client (:obj:`~pyrogram.Client`):
        The Client itself, useful when you want to call other API methods inside the message handler.

    shipping_query (:obj:`~pyrogram.types.ShippingQuery`):
        New incoming shipping query. Only for invoices with flexible price.
```

##### Methods

###### `def __init__(self, callback: Callable, filters = None)`

_No docstring._

---

## File: `handlers/story_handler.py`

### Classes

#### `class StoryHandler(Handler)`

```text
The Story handler class. Used to handle new stories.
It is intended to be used with :meth:`~pyrogram.Client.add_handler`

For a nicer way to register this handler, have a look at the
:meth:`~pyrogram.Client.on_story` decorator.

Parameters:
    callback (``Callable``):
        Pass a function that will be called when a new Stories arrives. It takes *(client, story)*
        as positional arguments (look at the section below for a detailed description).

    filters (:obj:`Filters`):
        Pass one or more filters to allow only a subset of stories to be passed
        in your callback function.

Other parameters:
    client (:obj:`~pyrogram.Client`):
        The Client itself, useful when you want to call other API methods inside the story handler.

    story (:obj:`~pyrogram.types.Story`):
        The received story.
```

##### Methods

###### `def __init__(self, callback: Callable, filters = None)`

_No docstring._

---

## File: `handlers/user_status_handler.py`

### Classes

#### `class UserStatusHandler(Handler)`

```text
The UserStatus handler class. Used to handle user status updates (user going online or offline).
It is intended to be used with :meth:`~pyrogram.Client.add_handler`.

For a nicer way to register this handler, have a look at the :meth:`~pyrogram.Client.on_user_status` decorator.

Parameters:
    callback (``Callable``):
        Pass a function that will be called when a new user status update arrives. It takes *(client, user)*
        as positional arguments (look at the section below for a detailed description).

    filters (:obj:`Filters`):
        Pass one or more filters to allow only a subset of users to be passed in your callback function.

Other parameters:
    client (:obj:`~pyrogram.Client`):
        The Client itself, useful when you want to call other API methods inside the user status handler.

    user (:obj:`~pyrogram.types.User`):
        The user containing the updated status.
```

##### Methods

###### `def __init__(self, callback: Callable, filters = None)`

_No docstring._

---
