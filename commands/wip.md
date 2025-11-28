---
description: "Commit tracked changes as WIP (work in progress)"
---

# Work In Progress

Commit only tracked (already staged or modified) files as a WIP commit. Unlike `save`, this doesn't add untracked files.

## Commands

```bash
git commit -am "wip: work in progress"
```

Uses Conventional Commits format. Report the result to the user. If nothing to commit, let the user know.
