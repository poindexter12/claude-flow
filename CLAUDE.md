# Claude Context

## What This Is

A Claude Code plugin providing git workflow commands and the Will Haacket agent. Modernizes Phil Haack's GitHub Flow aliases for the Claude Code era.

## Sources

- **GitHub Flow Aliases**: https://haacked.com/archive/2014/07/28/github-flow-aliases/
  - Original git aliases this plugin is based on
  - Author: Phil Haack (hence "Will Haacket" pun)

- **Conventional Commits**: https://www.conventionalcommits.org/en/v1.0.0/
  - Commit message format used by the conventional-commit skill
  - Summary: `skills/conventional-commit/references/conventional-commits-summary.md`
  - Full spec: `skills/conventional-commit/references/conventional-commits-spec.md`

- **Claude Code Plugins**: https://code.claude.com/docs/en/plugins
  - Plugin structure and manifest format

## Structure

```
.claude-plugin/plugin.json  - Plugin manifest
agents/                     - Will Haacket agent
commands/                   - Flow commands (start, sync, save, wip, undo, done, clean)
skills/
  conventional-commit/      - Conventional Commits skill
  branch-naming/            - Branch naming conventions
```

## Conventions

- Commit messages follow Conventional Commits
- Commands are deterministic operations
- Agent handles interactive/judgment tasks
- Skill provides reusable knowledge (commit message format)

## Development

This repo dogfoods itself - use the commands and agent here.
