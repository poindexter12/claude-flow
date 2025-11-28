---
description: "Start a new feature branch from updated default branch"
arguments:
  - name: input
    description: "Branch name OR description of what you're working on"
    required: false
---

# Start Feature Branch

Create and switch to a new feature branch after syncing with the default branch.

## Instructions

1. **Determine the branch name:**
   - If no input provided: Ask the user what they're working on
   - If input looks like a branch name (kebab-case, no spaces): Use it directly
   - If input is a description: Use the `branch-naming` skill to generate a name, then confirm with the user

2. Get the default branch name:

   ```bash
   git symbolic-ref refs/remotes/origin/HEAD | sed 's@^refs/remotes/origin/@@'
   ```

3. Checkout the default branch, pull latest, then create the new feature branch:

   ```bash
   git checkout <DEFAULT_BRANCH> && git pull --rebase --prune && git checkout -b <BRANCH_NAME>
   ```

4. Report the result to the user.
