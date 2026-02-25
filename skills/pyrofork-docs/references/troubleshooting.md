# Troubleshooting Playbook

## Fast diagnosis table

| Symptom / Error                                       | Likely Cause                                                       | Action                                                                                                                            |
| ----------------------------------------------------- | ------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------- |
| Client starts, nothing happens                        | Network/path issues                                                | Enable logging (`logging.basicConfig(level=logging.INFO)`), inspect socket/connectivity errors                                    |
| `PEER_ID_INVALID`                                     | Wrong ID, not-yet-met peer, inaccessible chat, wrong type          | Validate chat ID, ensure membership/access, cast with `int(...)` when needed, make peer discoverable via dialogs/username/contact |
| `FloodWait`                                           | Request burst exceeded Telegram limits                             | Catch `FloodWait`; sleep `e.value`; reduce request rate                                                                           |
| `sqlite3.OperationalError: database is locked`        | Same session file used by multiple processes                       | Ensure one process per session DB; use unique session names per parallel client                                                   |
| `sqlite3.InterfaceError: Error binding parameter`     | Passed object instead of scalar peer id/username                   | Use `chat.id` / expected primitive values                                                                                         |
| `socket.send/OSError/TimeoutError/connection reset`   | Unstable network or blocked event loop                             | Keep async flow non-blocking, use `asyncio.sleep()` not `time.sleep()`, improve network quality                                   |
| Deadlock when calling stop/restart/add/remove handler | Handler calling blocking lifecycle mutation from inside dispatcher | Use non-blocking mode (`block=False`) where supported                                                                             |
| `WEBPAGE_CURL_FAILED` while sending media by URL      | URL inaccessible to Telegram or file too large                     | Download file locally then upload from disk                                                                                       |
| UnicodeEncodeError in terminal                        | Terminal encoding mismatch                                         | Switch terminal to UTF-8 or use a UTF-8 capable terminal                                                                          |
| Slow reactions in supergroups/channels                | Telegram dispatch/priority and cross-DC behavior                   | Expect systemic delay; optimize handler work; avoid blocking                                                                      |
| Account limited/deactivated                           | Policy abuse/spam/flood/number risk                                | Review usage against Telegram ToS; appeal via official channels                                                                   |

## FAQ-derived operational truths

1. No webhooks in Pyrofork (MTProto persistent socket model, server push)
2. API key is still needed for bots during MTProto auth flow
3. File IDs are account-bound (sticker IDs are the exception)
4. Multiple concurrent clients are supported only with separate sessions

## Full FAQ content

For complete FAQ text (all entries, self-contained), read `faq-complete.md`.

## Debugging primitives

- Prefer strategic `print(...)` / structured logs around handler boundaries
- Print returned objects directly for human-readable detail snapshots
- Use dot-attribute access on Pyrofork types (they are objects, not dicts)
- Use `type(...)` / `isinstance(...)` for robust branching

## Suggested triage sequence

1. Reproduce with minimal script and logging enabled
2. Classify issue: auth/session, network, routing/filters, Telegram limit, data type
3. Apply category fix (table above)
4. Re-run with smallest possible scope
5. Add defensive error handling and backoff
