# RPC Errors API (`pyrogram.errors`)

Sources:

- `docs/source/api/errors/*.rst`
- `pyrogram/errors/__init__.py`
- `compiler/errors/source/*.tsv`

## Root error classes

- `RPCError`
- category subclasses (mirroring HTTP-like groupings)
- specific exceptions generated from error catalogs

Also exported in `pyrogram.errors`:

- `UnknownError`
- security-related exceptions (`SecurityError`, `SecurityCheckMismatch`, `CDNFileHashMismatch`)
- protocol error wrapper `BadMsgNotification`

## API-documented error categories

- `303 - SeeOther`
- `400 - BadRequest`
- `401 - Unauthorized`
- `403 - Forbidden`
- `406 - NotAcceptable`
- `420 - Flood`
- `500 - InternalServerError`

## Canonical error catalogs (TSV)

These files are the exact source used by API `.rst` error tables:

- `compiler/errors/source/303_SEE_OTHER.tsv`
- `compiler/errors/source/400_BAD_REQUEST.tsv`
- `compiler/errors/source/401_UNAUTHORIZED.tsv`
- `compiler/errors/source/403_FORBIDDEN.tsv`
- `compiler/errors/source/406_NOT_ACCEPTABLE.tsv`
- `compiler/errors/source/420_FLOOD.tsv`
- `compiler/errors/source/500_INTERNAL_SERVER_ERROR.tsv`

## Catalog size snapshot (source rows)

- `303_SEE_OTHER.tsv`: 5 entries
- `400_BAD_REQUEST.tsv`: 507 entries
- `401_UNAUTHORIZED.tsv`: 9 entries
- `403_FORBIDDEN.tsv`: 46 entries
- `406_NOT_ACCEPTABLE.tsv`: 22 entries
- `420_FLOOD.tsv`: 8 entries
- `500_INTERNAL_SERVER_ERROR.tsv`: 47 entries

## Usage pattern

```python
from pyrogram.errors import FloodWait

try:
    ...
except FloodWait as e:
    await asyncio.sleep(e.value)
```

## Notes for autonomous agents

- Prefer catching specific exception classes when practical.
- Use category catches for broader fallback handling.
- Preserve `value` semantics on exceptions carrying wait/DC details.
- Avoid blanket silent catches of `RPCError` without diagnostics.
