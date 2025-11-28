---
description: "Start a new feature branch from updated default branch"
arguments:
  - name: branch
    description: "Name of the new feature branch"
    required: true
---

# Start Feature Branch

Create and switch to a new feature branch after syncing with the default branch.

## Steps

1. Detect the default branch (main, master, or develop)
2. Checkout the default branch
3. Pull latest with rebase and prune
4. Create and checkout the new branch: `$ARGUMENTS.branch`

## Commands

```bash
# Get default branch
git symbolic-ref refs/remotes/origin/HEAD | sed 's@^refs/remotes/origin/@@'

# Checkout default, pull, create new branch
git checkout <default> && git pull --rebase --prune && git checkout -b $ARGUMENTS.branch
```

Report the result to the user.
