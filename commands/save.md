---
description: "Quick savepoint commit (stages all changes)"
arguments:
  - name: message
    description: "Optional commit message (defaults to 'checkpoint')"
    required: false
---

# Save Progress

Create a quick savepoint commit with all current changes. Use this when you want to preserve your current state but aren't ready for a proper commit.

## Instructions

1. Stage all changes and commit:
   ```bash
   git add -A && git commit -m "save: <MESSAGE>"
   ```
   Where `<MESSAGE>` is the user's message argument, or "checkpoint" if none provided.

2. Report the result to the user.
