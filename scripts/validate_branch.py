#!/usr/bin/env python3
"""
PreToolUse hook to validate git branch names against naming conventions.

Receives Bash tool input as JSON via stdin, checks if it's a branch creation,
validates the name format, and exits with code 2 to block invalid branches.
"""

import json
import re
import sys

# Valid branch prefixes (aligned with commit types)
VALID_PREFIXES = [
    "feat", "fix", "docs", "style",
    "refactor", "perf", "test", "chore"
]

# Regex for valid branch names: prefix/kebab-case-name
BRANCH_PATTERN = re.compile(
    r"^(" + "|".join(VALID_PREFIXES) + r")/[a-z0-9]+(-[a-z0-9]+)*$"
)

# Commands that create branches
BRANCH_CREATE_PATTERNS = [
    # git checkout -b branch-name
    r"git\s+checkout\s+(?:-b|--branch)\s+([^\s]+)",
    # git switch -c branch-name or git switch --create branch-name
    r"git\s+switch\s+(?:-c|--create)\s+([^\s]+)",
    # git branch branch-name (without additional flags that indicate other operations)
    r"git\s+branch\s+(?!-[dDmMrv])([^\s-][^\s]*)",
]

# Protected branches that should skip validation
PROTECTED_BRANCHES = [
    "main", "master", "develop", "dev",
    "staging", "production", "release"
]


def extract_branch_name(command: str) -> str | None:
    """Extract branch name from a git branch creation command."""
    for pattern in BRANCH_CREATE_PATTERNS:
        match = re.search(pattern, command)
        if match:
            branch = match.group(1)
            # Remove any quotes
            branch = branch.strip("'\"")
            return branch
    return None


def is_protected_branch(name: str) -> bool:
    """Check if this is a protected branch name."""
    return name.lower() in PROTECTED_BRANCHES


def is_valid_branch_name(name: str) -> bool:
    """Validate branch name against naming conventions."""
    return bool(BRANCH_PATTERN.match(name))


def print_error(branch: str) -> None:
    """Print helpful error message to stderr."""
    error = f"""
❌ Invalid branch name format.

Your branch: "{branch}"

Expected format: <prefix>/short-descriptive-name (kebab-case)

Valid prefixes: {", ".join(VALID_PREFIXES)}

Rules:
  - Use lowercase letters, numbers, and hyphens only
  - Prefix is required (e.g., feat/, fix/, chore/)
  - Use kebab-case for the description

Examples:
  feat/add-user-auth
  fix/login-timeout
  chore/bump-deps
  refactor/payment-module

See: skills/branch-naming/SKILL.md
"""
    print(error, file=sys.stderr)


def main() -> int:
    """Main hook logic."""
    try:
        # Read JSON input from stdin
        input_data = json.load(sys.stdin)
    except json.JSONDecodeError:
        # Not valid JSON, let it through
        return 0

    # Get the command being executed
    command = input_data.get("tool_input", {}).get("command", "")

    # Check if this is a git branch creation command
    if "git" not in command:
        return 0

    is_checkout_b = "checkout" in command and ("-b" in command or "--branch" in command)
    is_switch_c = "switch" in command and ("-c" in command or "--create" in command)
    is_branch_create = "branch" in command and not any(
        flag in command for flag in ["-d", "-D", "-m", "-M", "-r", "-v", "--list"]
    )

    if not (is_checkout_b or is_switch_c or is_branch_create):
        return 0

    # Extract the branch name
    branch = extract_branch_name(command)
    if not branch:
        # Couldn't parse branch name, let it through
        return 0

    # Skip validation for protected branches
    if is_protected_branch(branch):
        return 0

    # Validate the branch name
    if not is_valid_branch_name(branch):
        print_error(branch)
        return 2  # Blocking error

    return 0


if __name__ == "__main__":
    sys.exit(main())
