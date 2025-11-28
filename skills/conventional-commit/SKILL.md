---
name: conventional-commit
description: Generate commit messages by analyzing git diff following Conventional Commits format. Use when user says "commit", "commit my changes", "write a commit message", "what should I commit as", needs help describing changes, or is about to commit without a message.
---

# Commit Message Generator

Generate commit messages following [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) by analyzing actual code changes.

## Resources

- `references/conventional-commits-summary.md` - Types, examples, quick reference
- `references/conventional-commits-spec.md` - Full v1.0.0 specification (16 rules)
- `assets/commit.template` - Git commit template (user can configure with `git config commit.template`)

## Process

1. Run `git status` to see what files changed
2. Run `git diff --cached` (staged) or `git diff` (unstaged) to see actual changes
3. Analyze the diff to understand what was done
4. Generate a commit message using Conventional Commits format (see `references/conventional-commits-summary.md`)

## Guidelines

- Read the diff, don't ask the user to describe it
- Pick the type based on what the change *does*, not what files changed
- Use scope when the change is clearly in one area
- If multiple unrelated changes, suggest splitting the commit
- Match the project's existing commit style if they have one
