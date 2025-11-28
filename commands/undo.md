---
description: "Undo last commit but keep changes in working directory"
---

# Undo Last Commit

Reset the last commit but preserve all changes in the working directory. This is safe - your work is not lost.

## Instructions

1. Reset the last commit while keeping changes unstaged:
   ```bash
   git reset HEAD~1 --mixed
   ```

2. Report the result to the user, showing what was undone.
