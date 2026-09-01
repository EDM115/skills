---
name: rtk
description: Must use whenever you're about to run a command in the terminal to have faster and more efficient output, all while reducing tokens in your context window
metadata:
  author: EDM115
  version: "2026.9.1"
  source: "Grabbed from https://github.com/rtk-ai/rtk/blob/develop/src/hooks/init.rs & improved"
---

# RTK (Rust Token Killer) - Token-Optimized Commands
## Golden Rule
**Always prefix shell commands with `rtk`**. RTK filters and compresses command output before it reaches the LLM context, cutting up to 90% of the output on common operations. If RTK has a dedicated filter, it uses it. If not, it passes through unchanged. This means RTK is always safe to use. RTK is also cross-platform, so it works in Windows and with cmd/pwsh.  
In order to compress the output, RTK buffers it until the command finishes. If you rely on streaming output or monitor a long-running command (ex dev server) do NOT prefix it with `rtk`.  
**Important**: Even in command chains with `&&`, use `rtk`:
```bash
# ❌ Wrong
git add . && git commit -m "msg" && git push

# ✅ Correct
rtk git add . && rtk git commit -m "msg" && rtk git push
```
## RTK Commands by Workflow
### Meta Commands
```bash
rtk gain           # View token savings statistics
rtk gain --history # View command history with savings
rtk proxy <cmd>    # Run command without filtering
rtk discover       # Analyze Claude Code sessions for missed RTK usage
rtk --help         # Show all other commands available
```
### Files & Search (60-75% savings)
```bash
rtk ls <path>
rtk read <file>       # Code reading with filtering
rtk grep/rg <pattern>
rtk find <pattern>
```
### Analysis & Debug (70-90% savings)
```bash
rtk err <cmd>     # Filter errors only from any command
rtk log <file>    # Deduplicated logs with counts
rtk json <file>   # JSON structure without values
rtk deps          # Dependency overview
rtk env           # Environment variables compact
rtk summary <cmd> # Smart summary of command output
rtk diff          # Ultra-compact diffs
```
### Build & Compile (80-90% savings)
```bash
rtk cargo build
rtk cargo check
rtk cargo clippy
rtk tsc
rtk lint             # ESLint
rtk format           # Prettier, black, ruff
rtk prettier --check
rtk next build
```
### Test (90-99% savings)
```bash
rtk cargo test
rtk go test
rtk jest
rtk vitest
rtk playwright test
rtk pytest
rtk rake test
rtk rspec
rtk test <cmd>
```
### Git (59-80% savings)
```bash
rtk git status
rtk git log
rtk git diff
rtk git show
rtk git add
rtk git commit
rtk git push
rtk git pull
rtk git branch
rtk git fetch
rtk git stash
rtk git worktree
```
Note: Git passthrough works for ALL subcommands, even those not explicitly listed.
### GitHub (26-87% savings)
```bash
rtk gh pr view <num>
rtk gh pr checks
rtk gh run list
rtk gh issue list
rtk gh api
```
### JavaScript/TypeScript/Python Tooling (70-90% savings)
```bash
rtk pnpm list
rtk pnpm outdated
rtk pnpm install
rtk pnpm run <script> # Avoid issues compared to without "run"
rtk npm run <script>
rtk npx <cmd>
rtk uv run <cmd>
rtk ruff
rtk pip install
```
### Network (65-70% savings)
```bash
rtk curl <url>
rtk wget <url>
```
### Infrastructure (85% savings)
```bash
rtk docker ps
rtk docker images
rtk docker logs <c>
rtk kubectl get
rtk kubectl logs
```
