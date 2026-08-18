# Complete FAQ (Self-Contained)

This file contains full operational guidance for every FAQ page under `docs/source/faq`.

---

## why-is-the-api-key-needed-for-bots

Even for bots, MTProto API usage requires application identity (`api_id`, `api_hash`).

- Bot token identifies bot account identity (analogous to user phone in auth flow).
- API key identifies your developer application to Telegram’s main API.
- Bot API differs because its intermediate server handles MTProto with its own app identity.

Practical rule:

- For initial bot authorization in Pyrofork, provide **both** API key and bot token.

---

## how-to-use-webhooks

Pyrofork does not use webhook architecture.

- There is no HTTP polling/webhook interface in this model.
- Pyrofork uses persistent TCP/MTProto connections.
- Updates are server-push over long-lived connections.

Practical implication:

- Design handlers/listeners, not webhook endpoints.

---

## using-the-same-file-id-across-different-accounts

File IDs are account-bound in Telegram.

- Reusing file IDs across different accounts usually fails (e.g., `MEDIA_EMPTY`).
- Exception: sticker file IDs are reusable across accounts.

Practical rule:

- Treat non-sticker file IDs as session/account scoped artifacts.

---

## using-multiple-clients-at-once-on-the-same-account

Parallel sessions are possible for user and bot accounts, with one condition:

- do **not** share one session file/store across concurrent processes.

Correct pattern:

- authorize each concurrent client with a distinct session name.

---

## client-started-but-nothing-happens

Likely causes include network path issues or Telegram reachability issues.

Immediate debugging step:

- enable logging:
  - `import logging`
  - `logging.basicConfig(level=logging.INFO)`

Then inspect for timeouts/socket/unreachable errors.

---

## what-are-the-ip-addresses-of-telegram-data-centers

Telegram runs multi-DC infrastructure for production and test environments, with published IPv4/IPv6 addresses.

Use-case:

- firewall allowlisting
- network debugging
- datacenter-reachability checks

Operational note:

- production DC endpoints and test DC endpoints are different.
- some DC aliases may map due to infrastructure changes.

---

## migrating-the-account-to-another-data-center

DC placement is mostly controlled by Telegram.

- Users may see latency if physically distant from assigned DC.
- Initial account registration location and Telegram-side policies affect placement.
- Automatic migration is Telegram-controlled; no guaranteed direct manual move process is documented.

Practical guidance:

- optimize local network path, reduce processing latency, and avoid assumptions about forced DC migration.

---

## why-is-the-client-reacting-slowly-in-supergroups-channels

Two major contributors in docs:

1. Message routing across multiple DCs (sender, creator, receiver paths).
2. Telegram dispatch priority rules (creator/admin/bot/mentioned/recent/everyone else).

Practical guidance:

- expect higher baseline latency in large busy groups/channels.
- keep handlers lightweight and non-blocking to avoid adding local delay.

---

## peer-id-invalid-error

`PEER_ID_INVALID` can mean several distinct issues:

- incorrect ID value
- target chat not accessible for this account
- type mismatch (string id passed where integer expected)
- account has not encountered peer yet (no known access context)

Fix checklist:

- validate ID and type (`int(chat_id)` when needed)
- ensure membership/visibility
- make peer discoverable (dialogs, username search, shared group, contact, mention context)

---

## code-hangs-when-calling-stop-restart-add-remove-handler

Calling lifecycle/handler mutation methods from inside running handlers can deadlock:

- dispatcher waits for handlers to finish
- current handler waits for blocking operation
- circular wait occurs

Mitigation:

- use non-blocking form (`block=False`) where supported so operation is scheduled and returns immediately.

---

## unicodeencodeerror-codec-cant-encode

Usually terminal/environment encoding issue, not Pyrofork core issue.

Fixes:

- switch terminal encoding to UTF-8
- or use a UTF-8 capable terminal

---

## uploading-with-urls-gives-error-webpage-curl-failed

When uploading by URL, Telegram server tries to fetch the file itself.

Failure causes:

- URL not publicly reachable from Telegram side
- file too large or remote fetch fails

Reliable fallback:

- download media locally
- upload file from local disk via normal upload method

---

## sqlite3-operationalerror-database-is-locked

Root cause:

- concurrent process access to same session SQLite file.

Typical scenarios:

- two clients using same session name
- orphan/forgotten background process still holding lock

Fix path:

- stop competing process(es)
- restart if needed
- enforce unique session per concurrently running client

---

## sqlite3-interfaceerror-error-binding-parameter

Usually wrong argument type passed to API call.

Common mistake:

- passing full `Chat`/`User` object where ID/username is expected.

Correct pattern:

- pass `chat.id` (or expected scalar identifier), not whole object.

---

## socket-send-oserror-timeouterror-connection-lost-reset

Likely causes:

- unstable network
- blocking event loop too long

Mitigations:

- prefer async-native design
- avoid long blocking loops
- use `asyncio.sleep()` instead of `time.sleep()` in async code
- improve connection reliability

---

## how-to-avoid-flood-waits

Flood waits are rate-limit enforcement.

Guidance:

- reduce request frequency
- do less bursty high-volume calls
- always catch and respect `FloodWait`

Backoff pattern:

- `except FloodWait as e: await asyncio.sleep(e.value)`

---

## the-account-has-been-limited-deactivated

This is typically Telegram policy enforcement (spam/flood/abuse/number risk patterns).

Recovery options listed in docs:

- contact Telegram recovery/support channels
- contact `@SpamBot`
- use Telegram support form/email paths

Practical rule:

- keep automation behavior conservative, rate-limited, and policy-compliant.
