---
name: features-filters-custom-filters
description: Composing built-in filters and creating custom dynamic filters for precise update routing.
---

# Filters and Custom Filters

Filters are the routing layer for update callbacks.

## Usage

Built-in filters and composition:

```python
@app.on_message(filters.text | filters.photo)
async def text_or_photo(_, message):
    print(message)

@app.on_message(filters.sticker & (filters.channel | filters.private))
async def sticker_in_channel_or_private(_, message):
    print(message)
```

Dynamic custom filter:

```python
from pyrogram import filters

def callback_data_is(data: str):
    async def func(flt, _, query):
        return flt.data == query.data

    return filters.create(func, data=data)

@app.on_callback_query(callback_data_is("confirm"))
async def on_confirm(_, query):
    await query.answer("Confirmed")
```

## Key Points

- `~`, `&`, `|` map to logical NOT/AND/OR for filters.
- `filters.command()` and `filters.regex()` accept arguments for richer matching.
- In custom filters, callback receives `(filter_obj, client, update)`.
- Use `client` inside filter callbacks when pre-checks require API calls.

<!--
Source references:
- https://github.com/Mayuri-Chan/pyrofork/blob/main/docs/source/topics/use-filters.rst
- https://github.com/Mayuri-Chan/pyrofork/blob/main/docs/source/topics/create-filters.rst
- https://github.com/Mayuri-Chan/pyrofork/blob/main/docs/source/api/filters.rst
-->
