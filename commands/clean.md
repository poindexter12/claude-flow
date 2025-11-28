---
description: "Delete local branches that have been merged into default"
---

# Clean Merged Branches

Remove local branches that have already been merged into the default branch.

## Instructions

1. Get the default branch name:
   ```bash
   git symbolic-ref refs/remotes/origin/HEAD | sed 's@^refs/remotes/origin/@@'
   ```

2. Delete local branches that have been merged (excluding current and default):
   ```bash
   git branch --merged | grep -v "\*" | grep -v "<DEFAULT_BRANCH>" | xargs -n 1 git branch -d
   ```

3. Report which branches were deleted, or if none were found.
