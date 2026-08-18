---
name: features-smart-plugins
description: Structuring large Pyrofork bots with plugin auto-discovery, include/exclude lists, and runtime load/unload patterns.
---

# Smart Plugins

Smart Plugins reduce manual `import` + `add_handler` boilerplate for large projects.

## Usage

Enable plugin scanning:

```python
from pyrogram import Client

plugins = {"root": "plugins"}
Client("my_account", plugins=plugins).run()
```

Plugin module with class-level decorators:

```python
from pyrogram import Client, filters

@Client.on_message(filters.text & filters.private)
async def echo(_, message):
    await message.reply(message.text)
```

Restrict loaded modules and function order:

```python
plugins = {
    "root": "plugins",
    "include": [
        "subfolder.handlers fn2 fn1",
        "core.startup"
    ]
}
```

## Key Points

- Use `@Client.on_*` (class-level) inside plugin modules.
- `include` and `exclude` use module paths relative to plugin root (`.` notation).
- You can control function load order in one module with `module fn3 fn1 fn2` syntax.
- Decorated functions expose `.handlers` tuples for runtime add/remove handler patterns.

<!--
Source references:
- https://github.com/Mayuri-Chan/pyrofork/blob/main/docs/source/topics/smart-plugins.rst
- https://github.com/Mayuri-Chan/pyrofork/blob/main/docs/source/topics/more-on-updates.rst
-->
