---
name: pyrofork-best-practices
description: Use when building Telegram automations with Pyrofork and needing practical patterns for handlers, filters, plugins, raw API usage, and reliability.
metadata:
  author: EDM115
  version: "2026.2.25"
  source: "Generated from https://github.com/Mayuri-Chan/pyrofork, using https://github.com/antfu/skills"
---

> The skill is based on Pyrofork v2.3.69, generated at 2026-02-25.

Pyrofork is an async Python framework for Telegram MTProto automation (user and bot identities). These references focus on high-signal coding patterns for agents: lifecycle safety, update routing, plugin architecture, low-level raw API access, and production reliability.

## Core References

| Topic            | Description                                                    | Reference                                                                            |
| ---------------- | -------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| Client Lifecycle | Safe startup/shutdown patterns for async and sync usage        | [core-client-lifecycle](references/core-client-lifecycle.md)                         |
| Update Pipeline  | Handler registration, dispatch groups, and propagation control | [core-updates-handlers-propagation](references/core-updates-handlers-propagation.md) |

## Features

| Topic           | Description                                                              | Reference                                                                                  |
| --------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| Filters         | Compose built-in filters and route updates precisely                     | [features-filters-custom-filters](references/features-filters-custom-filters.md)           |
| Smart Plugins   | Modular handler loading with include/exclude and runtime reload patterns | [features-smart-plugins](references/features-smart-plugins.md)                             |
| Text Formatting | Parse modes, nested entities, and escaping rules for message rendering   | [features-text-formatting-parse-modes](references/features-text-formatting-parse-modes.md) |

## Advanced

| Topic   | Description                                                     | Reference                                                                          |
| ------- | --------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| Raw API | Invoke low-level Telegram functions and resolve peers correctly | [advanced-raw-api-peer-resolution](references/advanced-raw-api-peer-resolution.md) |

## Best Practices

| Topic                    | Description                                                     | Reference                                                                                              |
| ------------------------ | --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Reliability & Throughput | Error handling, flood waits, session strategy, and speed tuning | [best-practices-errors-sessions-performance](references/best-practices-errors-sessions-performance.md) |
