---
name: api-api-parser
description: Offline API backup extracted from Pyrofork source docstrings.
---

# Pyrofork API Backup: `parser`

Extracted from `sources/pyrofork/pyrogram/**.py` using AST parsing of module, class, function, and method docstrings.

## File: `parser/__init__.py`

---

## File: `parser/html.py`

### Classes

#### `class Parser(HTMLParser)`

_No docstring._

##### Methods

###### `def __init__(self, client: 'pyrogram.Client')`

_No docstring._

###### `def handle_starttag(self, tag, attrs)`

_No docstring._

###### `def handle_data(self, data)`

_No docstring._

###### `def handle_endtag(self, tag)`

_No docstring._

###### `def error(self, message)`

_No docstring._

#### `class HTML`

_No docstring._

##### Methods

###### `def __init__(self, client: Optional['pyrogram.Client'])`

_No docstring._

###### `async def parse(self, text: str)`

_No docstring._

###### `def unparse(text: str, entities: list)`

_No docstring._

---

## File: `parser/markdown.py`

### Classes

#### `class Markdown`

_No docstring._

##### Methods

###### `def __init__(self, client: Optional['pyrogram.Client'])`

_No docstring._

###### `def blockquote_parser(self, text)`

_No docstring._

###### `async def parse(self, text: str, strict: bool = False)`

_No docstring._

###### `def unparse(text: str, entities: list)`

```text
Performs the reverse operation to .parse(), effectively returning
markdown-like syntax given a normal text and its MessageEntity's.

:param text: the text to be reconverted into markdown.
:param entities: list of MessageEntity's applied to the text.
:return: a markdown-like text representing the combination of both inputs.
```

---

## File: `parser/parser.py`

### Classes

#### `class Parser`

_No docstring._

##### Methods

###### `def __init__(self, client: Optional['pyrogram.Client'])`

_No docstring._

###### `async def parse(self, text: str, mode: Optional[enums.ParseMode] = None)`

_No docstring._

###### `def unparse(text: str, entities: list, is_html: bool)`

_No docstring._

---

## File: `parser/utils.py`

### Top-level Functions

#### `def add_surrogates(text)`

_No docstring._

#### `def remove_surrogates(text)`

_No docstring._

#### `def replace_once(source: str, old: str, new: str, start: int)`

_No docstring._

#### `def within_surrogate(text, index, *, length = None)`

```text
`True` if ``index`` is within a surrogate (before and after it, not at!).
```

---
