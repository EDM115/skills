---
name: rtk
description: Use when inspecting high-volume terminal output with RTK, choosing whether output can be safely compressed, or recovering details omitted by an RTK filter.
compatibility: Requires the rtk executable and shell access. Uses explicit command invocation without requiring hooks.
metadata:
  author: EDM115
  version: "2026.9.14"
  source: https://github.com/rtk-ai/rtk
---

# RTK (Rust Token Killer)
Use RTK to reduce noisy output intended for model inspection. Choose it per command according to who consumes the output and whether exact content matters. Invoke it explicitly in Codex; this workflow does not require a hook.
## Choose filtered or raw output
| Output use | Command choice |
| --- | --- |
| Noisy test results, status, logs, or search results read by the model | Use the supported RTK command when a summary is sufficient. |
| Pipe to a parser, command substitution, variable assignment, or output redirected to an artifact | Run the original command unfiltered so downstream data stays intact. |
| Exact JSON values, full source, patch content, compiler diagnostics, or byte-sensitive evidence | Use the original command or `rtk proxy <cmd>` for unfiltered output. |
| Interactive process, live logs, or a long-running server | Run directly to preserve interaction and streaming. |
| Small output, unsupported command, or RTK unavailable | Run directly; there is no need to install or configure RTK to finish the task. |
Filtering can remove values, lines, and context. A filtered diff is useful for orientation but is not an apply-ready patch. Read source and evidence unfiltered when omitted details could change a decision. Shell quoting, redirection, and pipeline semantics still belong to the host shell; do not prefix an entire compound expression mechanically.
## Discover the installed interface
Check `rtk --help` when availability or supported syntax is unknown, and use subcommand help for version-specific options. Keep the project's runtime and package-manager environment intact. RTK changes presentation; it grants no additional permission to execute the underlying command.
```bash
rtk git status                  # Compact working-tree overview
rtk git diff                    # Summary for inspection, not a patch artifact
rtk grep "pattern" .            # Grouped search results
rtk test <cmd>                  # Noisy completed test output for inspection
rtk proxy git diff              # Full diff without RTK filtering
git diff > change.patch         # Raw artifact for downstream tools
```
## Recover missing evidence
If a summary hides the detail needed to diagnose a failure, first read any available raw log. Otherwise rerun the smallest safe read or check without filtering. Establish whether a side-effecting command already ran before retrying it; a wrapper error is not proof that the underlying operation did nothing. Report the actual command outcome, not an inference from a shortened success summary.
