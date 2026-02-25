---
name: pyrofork-api
description: Use when implementing, debugging, or reviewing Pyrofork API usage and internals from docs/source/api, including Client, handlers, decorators, filters, enums, and RPC error catalogs. Triggers on requests for exact signatures, parameters, types, enum values, filter behavior, or handler/decorator wiring.
metadata:
  author: EDM115
  version: "2026.02.25"
  source: "https://github.com/Mayuri-Chan/pyrofork pyrogram"
---

# Pyrofork API Skill

This skill is a **self-contained API reference** for everything documented under `docs/source/api`.
It is intended for autonomous agents working without the original Sphinx docs.

## Coverage contract

When using this skill, treat the following references as authoritative:

- `references/api-rst-scope.md` — exact mapping from API `.rst` pages to source symbols.
- `references/client-api.md` — `pyrogram.Client` constructor and behavior documented by API pages.
- `references/methods-api.md` — full `pyrogram.methods` surface grouped by domain.
- `references/types-api.md` — full `pyrogram.types` surface (including deep coverage for `Message`).
- `references/bound-methods-api.md` — bound methods attached to high-level types.
- `references/decorators-api.md` — all API decorators (`Client.on_*`) and their signatures.
- `references/handlers-api.md` — all handler classes and constructor contracts.
- `references/filters-api.md` — `pyrogram.filters` members, combinators, and advanced filters.
- `references/enums-api.md` — all API enum classes and values.
- `references/errors-api.md` — RPC error categories and canonical source catalogs.
- `references/raw-api.md` — `pyrogram.raw` package scope and usage boundaries.
- `references/internals-filetree-api.md` — explicit file-path coverage for root/internal runtime folders.
- `references/internals-runtime-api.md` — public symbols and responsibilities for root/internal runtime modules.

## Rules for responses/code generated with this skill

1. Use exact parameter names from signatures in these references.
2. Preserve type intent from annotations/docstrings (including optionality/defaults).
3. For decorators/handlers, preserve `filters` and `group` semantics.
4. For filters, preserve callable contract `(filter, client, update) -> bool` for custom filters.
5. For enums and RPC errors, use canonical names exactly as documented.

## Completeness workflow

When asked an API question:

1. Identify API section (Client / decorators / handlers / filters / enums / errors).
   1.1 Include methods/types/bound-methods/raw when applicable.
2. Read corresponding reference file(s) above.
3. If combining sections (e.g. decorator + handler + filter), cross-check all involved files.
4. Return answer with exact symbols/signatures.
