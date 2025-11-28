---
description: "Sync current branch with remote (pull with rebase and prune)"
---

# Sync Branch

Update the current branch with latest changes from remote.

## Instructions

1. Pull with rebase and prune stale remote branches:
   ```bash
   git pull --rebase --prune
   ```

2. If the repo has submodules, update them:
   ```bash
   git submodule update --init --recursive
   ```

3. Report the result to the user.
