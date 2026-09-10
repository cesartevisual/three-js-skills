# Validation

## Package checks

Run from the repository root with Python 3.10+:

```sh
python3 .github/validate.py
```

The validator reads SKILL.md files directly and checks names, descriptions, nonempty instructions, README listings, self-contained references, and local documentation links. GitHub Actions runs the same command. Installation requires no Python.

## Installation evidence

All 24 skills have been installed with Skills CLI 1.5.25 for Claude Code, Cursor, and Codex. Public installation was verified with tokens, Git credential helpers, global/system Git configuration, and interactive authentication disabled. Installed skill files and references matched source bytes.

After the packaging simplification, installation from a local checkout was also checked in a fresh temporary project with all three agent targets. The skill folders and content are unchanged; the custom installer/exporter and its tests have been removed from the default branch.

## Limits

Package validation and installation do not establish native agent discovery, task completion, or GPU/device correctness. Those checks remain open. Use the [behavioral scenarios](evaluations.md) and compatibility-report issue template to record actual results before expanding support claims.
