#!/usr/bin/env python3
"""
PreToolUse hook to validate git commit messages against Conventional Commits format.

Receives Bash tool input as JSON via stdin, checks if it's a git commit,
validates the message format, and exits with code 2 to block invalid commits.
"""

import json
import re
import sys

# Valid commit types (Conventional Commits + save/wip for plugin commands)
VALID_TYPES = [
    "feat", "fix", "build", "chore", "ci",
    "docs", "style", "refactor", "perf", "test",
    "save", "wip"  # Plugin-specific types
]

# Regex for Conventional Commits: type(scope)!: description
COMMIT_PATTERN = re.compile(
    r"^(" + "|".join(VALID_TYPES) + r")(\([^)]+\))?!?: .+"
)

# Patterns to detect git commit commands
COMMIT_CMD_PATTERNS = [
    # git commit -m "message"
    r'git\s+commit\s+.*-m\s+["\'](.+?)["\']',
    # git commit -m 'message'
    r"git\s+commit\s+.*-m\s+'(.+?)'",
    # git commit --message="message"
    r'git\s+commit\s+.*--message=["\'](.+?)["\']',
    # HEREDOC pattern: git commit -m "$(cat <<'EOF'\nmessage\nEOF\n)"
    r'git\s+commit\s+.*-m\s+"\$\(cat\s+<<[\'"]?EOF[\'"]?\n(.+?)\nEOF',
]

# Skip validation for these commit patterns
SKIP_PATTERNS = [
    r"Merge\s+(branch|pull\s+request)",  # Merge commits
    r"^Revert\s+",  # Revert commits
]


def extract_commit_message(command: str) -> str | None:
    """Extract commit message from a git commit command."""
    # Handle HEREDOC format first (common in Claude commits)
    heredoc_match = re.search(
        r'-m\s+"\$\(cat\s+<<[\'"]?EOF[\'"]?\n(.+?)\nEOF',
        command,
        re.DOTALL
    )
    if heredoc_match:
        # Get the first line of the message (the subject)
        message = heredoc_match.group(1).strip()
        return message.split('\n')[0]

    # Try standard -m patterns
    for pattern in COMMIT_CMD_PATTERNS[:3]:
        match = re.search(pattern, command)
        if match:
            return match.group(1)

    return None


def should_skip_validation(message: str) -> bool:
    """Check if this commit message should skip validation."""
    for pattern in SKIP_PATTERNS:
        if re.search(pattern, message, re.IGNORECASE):
            return True
    return False


def is_valid_commit_message(message: str) -> bool:
    """Validate commit message against Conventional Commits format."""
    return bool(COMMIT_PATTERN.match(message))


def print_error(message: str) -> None:
    """Print helpful error message to stderr."""
    error = f"""
❌ Invalid commit message format.

Your message: "{message}"

Expected format: <type>[scope]: <description>

Valid types: {", ".join(VALID_TYPES[:-2])}
Plugin types: save, wip

Examples:
  feat: add user authentication
  fix(api): resolve timeout issue
  docs: update README
  chore(deps): bump lodash version

See: skills/conventional-commit/SKILL.md
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

    # Check if this is a git commit command
    if "git" not in command or "commit" not in command:
        return 0

    # Check if -m or --message is present (we only validate inline messages)
    if "-m" not in command and "--message" not in command:
        return 0

    # Extract the commit message
    message = extract_commit_message(command)
    if not message:
        # Couldn't parse message, let it through
        return 0

    # Skip validation for certain commit types
    if should_skip_validation(message):
        return 0

    # Validate the message
    if not is_valid_commit_message(message):
        print_error(message)
        return 2  # Blocking error

    return 0


if __name__ == "__main__":
    sys.exit(main())
