---
description: "Quick savepoint commit (stages all changes)"
arguments:
  - name: message
    description: "Optional commit message (defaults to SAVEPOINT)"
    required: false
---

# Save Progress

Create a quick savepoint commit with all current changes. Use this when you want to preserve your current state but aren't ready for a proper commit.

## Commands

```bash
git add -A
git commit -m "save: ${ARGUMENTS.message:-checkpoint}"
```

Uses Conventional Commits format. Report the result to the user.
