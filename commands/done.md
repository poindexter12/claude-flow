---
description: "Complete branch workflow: checkout default, sync, and clean merged branches"
---

# Branch Done

Complete the current branch workflow after a PR has been merged. This:
1. Checks out the default branch
2. Pulls latest changes
3. Deletes local branches that have been merged

## Commands

```bash
# Get default branch
DEFAULT=$(git symbolic-ref refs/remotes/origin/HEAD | sed 's@^refs/remotes/origin/@@')

# Checkout default and pull
git checkout $DEFAULT
git pull --rebase --prune

# Delete merged branches (excluding default and current)
git branch --merged | grep -v "\*" | grep -v "$DEFAULT" | xargs -n 1 git branch -d
```

Report which branches were cleaned up.
