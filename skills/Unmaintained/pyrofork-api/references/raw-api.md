# Raw API scope (`pyrogram.raw`)

Sources:

- `pyrogram/raw/core`
- `pyrogram/raw/functions`
- `pyrogram/raw/types`

This layer provides low-level Telegram API classes used with:

- `await client.invoke(raw.functions.<...>(...))`

## Package sections

- `raw.core` — protocol/core primitives
- `raw.functions` — invocable TL function classes
- `raw.types` — TL type classes used in requests/responses

## Usage pattern

1. import required class from `pyrogram.raw.functions` or `pyrogram.raw.types`
2. instantiate with named arguments
3. invoke through `client.invoke`

## Interop with high-level API

- `Client.resolve_peer(...)` helps bridge high-level IDs to required `InputPeer` raw types.
- high-level methods are wrappers over raw calls; raw should be used for unsupported/bleeding-edge features.

## Documentation boundary

This skill references raw package scope and usage model.
For per-function/per-type exhaustive raw catalogs, rely on `pyrogram/raw/functions/**` and `pyrogram/raw/types/**` symbol trees directly (large generated surfaces).
