---
description: "Delete local branches that have been merged into default"
---

# Clean Merged Branches

Remove local branches that have already been merged into the default branch.

## Commands

```bash
# Get default branch
DEFAULT=$(git symbolic-ref refs/remotes/origin/HEAD | sed 's@^refs/remotes/origin/@@')

# Delete merged branches (excluding default)
git branch --merged | grep -v "\*" | grep -v "$DEFAULT" | xargs -n 1 git branch -d
```

Report which branches were deleted, or if none were found.
