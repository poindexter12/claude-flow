# Branch Naming Skill

Generate consistent, readable branch names from descriptions.

Prefixes align with the `conventional-commit` skill types for a unified workflow.

## Format

```
[prefix/]short-descriptive-name
```

## Prefixes

Match conventional commit types for consistency:

| Prefix | Commit Type | Use When |
|--------|-------------|----------|
| `feat/` | `feat:` | New functionality |
| `fix/` | `fix:` | Bug fixes |
| `docs/` | `docs:` | Documentation only |
| `style/` | `style:` | Formatting, no code change |
| `refactor/` | `refactor:` | Code restructuring |
| `perf/` | `perf:` | Performance improvements |
| `test/` | `test:` | Adding/fixing tests |
| `chore/` | `chore:` | Maintenance, deps, config |

Use a prefix when the intent is clear. Skip it if ambiguous.

## Rules

1. **Kebab-case**: lowercase, hyphens between words (`add-user-auth`)
2. **Short**: 3-5 words max, under 50 chars total
3. **Descriptive**: what it does, not how (`add-search` not `implement-elasticsearch`)
4. **No fluff**: drop articles and filler (`user-profile` not `the-user-profile-page`)
5. **No ticket numbers alone**: `fix/login-timeout` not just `JIRA-1234`

## Examples

| Description | Branch Name |
|-------------|-------------|
| "Add user authentication" | `feat/add-user-auth` |
| "Fix the login timeout bug" | `fix/login-timeout` |
| "Update README with install instructions" | `docs/update-readme` |
| "Refactor the payment processing module" | `refactor/payment-processing` |
| "Bump lodash to fix security issue" | `chore/bump-lodash` |
| "Quick experiment with caching" | `try-caching` |

## Edge Cases

- **Ticket numbers**: Include after prefix if team uses them: `feat/PROJ-123-add-search`
- **Uncertain scope**: Skip prefix, use descriptive name: `improve-performance`
- **Spikes/experiments**: Use `try-` or `spike-` prefix: `try-redis-caching`
