#!/usr/bin/env python3
"""Validate the skill folders and local documentation links. Python 3.10+."""
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r'\[[^\]]*\]\(([^)]+)\)')


def validate(root):
    root = root.resolve()
    skills = sorted((root / 'skills').glob('*/SKILL.md'))
    if not skills:
        raise ValueError('No skills found')
    readme = (root / 'README.md').read_text()
    for skill in skills:
        text = skill.read_text()
        # Keep metadata in the package's small, portable YAML subset:
        # an unquoted name and a JSON-quoted single-line description.
        parts = text.split('---\n', 2)
        if len(parts) != 3 or parts[0]:
            raise ValueError(f'{skill}: missing frontmatter')
        fields = dict(line.split(': ', 1) for line in parts[1].strip().splitlines())
        name = fields['name']
        description = json.loads(fields['description'])
        if name != skill.parent.name or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name) or len(name) > 64:
            raise ValueError(f'{skill}: invalid name')
        if not isinstance(description, str) or not description.strip() or len(description) > 1024:
            raise ValueError(f'{skill}: invalid description')
        if not parts[2].strip():
            raise ValueError(f'{skill}: empty instructions')
        if f'](skills/{name}/SKILL.md)' not in readme:
            raise ValueError(f'{name}: missing README listing')
        for resource in skill.parent.rglob('*'):
            if resource.is_symlink():
                raise ValueError(f'{resource}: skills must contain their resources')
            if resource.suffix == '.md':
                content = resource.read_text()
                if re.search(r'\b(?:TODO|FIXME|TBD)\b|\[INSERT', content):
                    raise ValueError(f'{resource}: unfinished scaffold')
                check_links(resource, skill.parent.resolve())
    for doc in [*root.glob('*.md'), *(root / 'docs').rglob('*.md'), *(root / '.github').rglob('*.md')]:
        check_links(doc, root)
    return len(skills)


def check_links(path, boundary):
    for link in LINK.findall(path.read_text()):
        if '://' in link or link.startswith(('#', 'mailto:')):
            continue
        target = (path.parent / link.split('#')[0]).resolve()
        if not target.is_relative_to(boundary) or not target.exists():
            raise ValueError(f'{path}: broken or nonportable link {link}')


if __name__ == '__main__':
    try:
        print(f'Validated {validate(ROOT)} skills and local documentation links')
    except (ValueError, KeyError, OSError) as error:
        raise SystemExit(str(error))
