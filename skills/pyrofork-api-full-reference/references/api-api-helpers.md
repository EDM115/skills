---
name: api-api-helpers
description: Offline API backup extracted from Pyrofork source docstrings.
---

# Pyrofork API Backup: `helpers`

Extracted from `sources/pyrofork/pyrogram/**.py` using AST parsing of module, class, function, and method docstrings.

## File: `helpers/__init__.py`

### Module Docstring

```text
pyromod - A monkeypatcher add-on for Pyrogram
Copyright (C) 2020 Cezar H. <https://github.com/usernein>
This file is part of pyromod.
pyromod is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
pyromod is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with pyromod.  If not, see <https://www.gnu.org/licenses/>.
```

---

## File: `helpers/helpers.py`

### Top-level Functions

#### `def ikb(rows = None)`

```text
Create an InlineKeyboardMarkup from a list of lists of buttons.
:param rows: List of lists of buttons. Defaults to empty list.
:return: InlineKeyboardMarkup
```

#### `def btn(text, value, type = 'callback_data')`

```text
Create an InlineKeyboardButton.

:param text: Text of the button.
:param value: Value of the button.
:param type: Type of the button. Defaults to "callback_data".
:return: InlineKeyboardButton
```

#### `def bki(keyboard)`

```text
Create a list of lists of buttons from an InlineKeyboardMarkup.

:param keyboard: InlineKeyboardMarkup
:return: List of lists of buttons
```

#### `def ntb(button)`

```text
Create a button list from an InlineKeyboardButton.

:param button: InlineKeyboardButton
:return: Button as a list to be used in btn()
```

#### `def kb(rows = None, **kwargs)`

```text
Create a ReplyKeyboardMarkup from a list of lists of buttons.

:param rows: List of lists of buttons. Defaults to empty list.
:param kwargs: Other arguments to pass to ReplyKeyboardMarkup.
:return: ReplyKeyboardMarkup
```

#### `def force_reply(selective = True)`

```text
Create a ForceReply.

:param selective: Whether the reply should be selective. Defaults to True.
:return: ForceReply
```

#### `def array_chunk(input_array, size)`

```text
Split an array into chunks.

:param input_array: The array to split.
:param size: The size of each chunk.
:return: List of chunks.
```

---
