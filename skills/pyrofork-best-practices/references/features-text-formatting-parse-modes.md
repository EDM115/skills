---
name: features-text-formatting-parse-modes
description: Sending styled Telegram text safely with HTML/Markdown parse modes, escaping rules, and nested entities.
---

# Text Formatting and Parse Modes

Pyrofork supports mixed Markdown + HTML by default, with explicit parse-mode control when needed.

## Usage

Strict HTML mode:

```python
from pyrogram import enums

await app.send_message(
    "me",
    "<b>bold</b> <i>italic</i> <spoiler>secret</spoiler>",
    parse_mode=enums.ParseMode.HTML,
)
```

Strict Markdown mode:

```python
await app.send_message(
    "me",
    "**bold** __italic__ ||spoiler||",
    parse_mode=enums.ParseMode.MARKDOWN,
)
```

Disable parsing:

```python
await app.send_message(
    "me",
    "**literal** <i>literal</i>",
    parse_mode=enums.ParseMode.DISABLED,
)
```

## Key Points

- Default mode accepts both Markdown and HTML in one message.
- Prefer HTML mode for complex nested/overlapping entities.
- Escape raw `<`, `>`, `&` in HTML text when not intended as tags.
- Parse mode choice determines how literals and mixed syntax are interpreted.

<!--
Source references:
- https://github.com/Mayuri-Chan/pyrofork/blob/main/docs/source/topics/text-formatting.rst
- https://github.com/Mayuri-Chan/pyrofork/blob/main/docs/source/api/enums/ParseMode.rst
-->
