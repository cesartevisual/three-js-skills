# Working on Three.js Skills

- Skills live in `skills/<name>/SKILL.md`, with optional references inside that folder.
- Preserve existing skill names and scope unless the request calls for a change.
- Treat each SKILL.md as the source of truth; do not introduce a duplicate metadata catalog.
- Keep the README skill list and relevant routing guidance current.
- Use standard skill discovery and the skills CLI. Avoid adding a separate installer or framework unless needed by an explicit request.
- Preserve the user's framework and installed library versions in skill instructions. Check current official APIs when adding version-sensitive guidance.
- Retain self-contained relative references so skills can be installed individually.
- Run `python3 .github/validate.py` after changes. For behavior changes, use a relevant scenario from `docs/evaluations.md` and report which checks actually ran.
- Keep distribution simple: install from the default branch without a release workflow. Do not rewrite history unless explicitly requested.
