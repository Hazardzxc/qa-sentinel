#!/usr/bin/env python3
"""Offline packaging check: required skills and shared standards are present."""
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parent.parent
SKILLS=['qa-test-design','qa-manual-testing','qa-playwright-automation','qa-release-assessment']
COMMON=['repository-boundaries.md','repository-analysis.md','test-design.md','classification-risk.md','change-impact.md','environment-safety.md','case-schema.md','traceability.md','test-data.md']
missing=[]
for skill in SKILLS:
    p=ROOT/'.agents/skills'/skill/'SKILL.md'
    if not p.exists(): missing.append(str(p.relative_to(ROOT)))
    elif not p.read_text(encoding='utf-8').startswith('---\n'):
        missing.append(f'{p}: missing frontmatter')
for name in COMMON:
    p=ROOT/'standards'/name
    if not p.exists():missing.append(str(p.relative_to(ROOT)))
for m in missing:print('MISSING:',m)
if missing:sys.exit(2)
print('PASS: four skills and shared standards exist. Tool-specific skill discovery still requires configuration.')
