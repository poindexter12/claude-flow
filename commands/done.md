---
description: "Complete branch workflow: checkout default, sync, and clean merged branches"
---

# Branch Done

Complete the current branch workflow after a PR has been merged.

## Instructions

1. Get the default branch name:
   ```bash
   git symbolic-ref refs/remotes/origin/HEAD | sed 's@^refs/remotes/origin/@@'
   ```

2. Checkout the default branch and pull latest:
   ```bash
   git checkout <DEFAULT_BRANCH> && git pull --rebase --prune
   ```

3. Delete local branches that have been merged into the default branch:
   ```bash
   git branch --merged | grep -v "\*" | grep -v "<DEFAULT_BRANCH>" | xargs -n 1 git branch -d
   ```

4. Report which branches were cleaned up, or if none were found.
