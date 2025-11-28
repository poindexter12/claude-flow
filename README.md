# claude-flow

A Claude Code plugin for git workflow automation. Modernizes [Phil Haack's GitHub Flow aliases](https://haacked.com/archive/2014/07/28/github-flow-aliases/) for the AI era.

## What's Included

### Commands

| Command | Description |
|---------|-------------|
| `/flow:start <branch>` | Create feature branch from updated default |
| `/flow:sync` | Pull with rebase and prune |
| `/flow:save [msg]` | Quick savepoint commit |
| `/flow:wip` | Commit tracked changes as WIP |
| `/flow:undo` | Undo last commit, keep changes |
| `/flow:done` | Complete branch: checkout default, sync, clean |
| `/flow:clean` | Delete merged local branches |

### Agent: Will Haacket

A git workflow assistant that handles the interactive stuff:
- Review changes and explain what's different
- Write commit messages by reading the diff
- Push to remote with upstream tracking

Invoke with: `@will-haacket commit and push`

### Skills

- **conventional-commit**: Generates commit messages following [Conventional Commits](https://www.conventionalcommits.org/). Used by the Will Haacket agent.
- **branch-naming**: Generates consistent branch names from descriptions. Used by `/flow:start`.

## Installation

```bash
# Add to your project's .claude/settings.json
{
  "plugins": ["github:poindexter12/claude-flow"]
}
```

## Usage

```bash
# Start a feature (branch name or description)
/flow:start add-user-auth
/flow:start "add user authentication"

# Work on your code...

# Quick save
/flow:save "checkpoint before refactor"

# Ready to commit properly
@will-haacket commit and push

# After PR merges
/flow:done
```

## Credits

- Inspired by [Phil Haack's GitHub Flow Aliases](https://haacked.com/archive/2014/07/28/github-flow-aliases/)
- Commit format: [Conventional Commits v1.0.0](https://www.conventionalcommits.org/en/v1.0.0/)

## License

MIT
