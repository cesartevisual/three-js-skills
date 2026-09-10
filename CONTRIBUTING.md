# Contributing

Useful contributions include focused skill improvements, reproducible bug reports, working demos, and actual results from coding agents.

Follow the [code of conduct](CODE_OF_CONDUCT.md). Use the issue templates for bugs, skill requests, and compatibility evidence. Report sensitive vulnerabilities according to [SECURITY.md](SECURITY.md).

## Improve a skill

1. Describe the user task or observed failure the change addresses.
2. Edit the relevant `skills/threejs-*/SKILL.md`. Keep it focused on decisions that improve implementation; link supporting references only when needed.
3. Preserve existing project choices and version checks. Avoid universal rules based on one example.
4. Keep the README skill list current. Update the router when changing coverage. Metadata lives only in each `SKILL.md`.
5. Run the package checks from the repository root:

```sh
python3 .github/validate.py
```

In your pull request, explain the resulting behavior, verification performed, and limitations. New skills should include an applicable scenario in [the evaluation guide](docs/evaluations.md).

## Report a bug or compatibility result

Include the host and version, model when known, operating system, installation method, skill names, exact prompt, and a minimal fixture or public reproduction. Record expected and observed behavior, relevant errors, and checks actually run. Remove credentials and private project data from shared artifacts.

Distinguish successful installation, skill discovery, task completion, and browser/device verification. An installer pass does not establish that a model followed the skill correctly. Use [the behavioral scenarios](docs/evaluations.md) where appropriate. Add evidence to [validation status](docs/validation.md) before changing the README's compatibility claims.

## Contribute a demo

Provide a short recording or preview, runnable source, the exact prompt, skills used, and setup instructions. Include asset provenance and permissions to share. Label mockups and edited demonstrations clearly; do not present them as captured application behavior.

The README contains a `DEMO SLOT` comment. Replace that placeholder once a real demo and its supporting links are ready. Keep quick installation visible near the top.

## License

Contributions are provided under this repository's [MIT License](LICENSE). Preserve attribution and any required notices for third-party material.
