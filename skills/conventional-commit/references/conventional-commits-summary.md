# Conventional Commits - Summary

Source: https://www.conventionalcommits.org/en/v1.0.0/

The Conventional Commits specification is a lightweight convention on top of commit messages. It provides an easy set of rules for creating an explicit commit history; which makes it easier to write automated tools on top of. This convention dovetails with SemVer, by describing the features, fixes, and breaking changes made in commit messages.

## Structure

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

## Types

- `feat`: A new feature (correlates with MINOR in SemVer)
- `fix`: A bug fix (correlates with PATCH in SemVer)
- `build`: Changes that affect the build system or external dependencies
- `chore`: Other changes that don't modify src or test files
- `ci`: Changes to CI configuration files and scripts
- `docs`: Documentation only changes
- `style`: Changes that do not affect the meaning of the code (white-space, formatting, etc)
- `refactor`: A code change that neither fixes a bug nor adds a feature
- `perf`: A code change that improves performance
- `test`: Adding missing tests or correcting existing tests

## Common Scopes

Scopes provide additional context. Some useful patterns:

| Scope | Use Case | Example |
|-------|----------|---------|
| `(security)` | Security vulnerability fixes | `fix(security): patch XSS in user input` |
| `(revert)` | Reverting a previous change | `fix(revert): undo breaking API change` |
| `(deps)` | Dependency updates | `chore(deps): bump lodash to 4.17.21` |
| `(api)` | API-related changes | `feat(api): add pagination to list endpoint` |
| `(auth)` | Authentication/authorization | `fix(auth): handle expired tokens` |
| `(ui)` | User interface changes | `style(ui): align buttons in modal` |

## Breaking Changes

Breaking changes correlate with MAJOR in SemVer. Indicate them by:

1. Adding `!` after the type/scope: `feat!: breaking change`
2. Adding a footer: `BREAKING CHANGE: description`

## Examples

```
feat: allow provided config object to extend other configs
```

```
fix(parser): handle edge case with empty arrays
```

```
feat!: send an email to the customer when a product is shipped
```

```
feat(api): add endpoint for user preferences

Allows users to save and retrieve their dashboard preferences.

Refs: #234
```

```
fix: prevent racing of requests

Introduce a request id and a reference to latest request.
Dismiss incoming responses other than from latest request.

Reviewed-by: Z
Refs: #123
```
