#!/usr/bin/env python3
"""Offline Playwright title/tag policy check (see tagging-and-gates.md). Does not run tests."""
import argparse, re, sys
from pathlib import Path
# shortcut: regex reads literal test('...') titles only; template-literal or computed titles are skipped, use a TS parser if specs need them.
TITLE=re.compile(r"""\btest(?:\.(?:only|skip|fixme|fail))?\(\s*(['"])(.*?)\1""")
CASE_ID=re.compile(r'TC-[A-Z0-9]+(?:-[A-Z0-9]+)*-\d{3,}')
LAYERS={'@web','@api','@e2e'}; PRIORITIES={'@p0','@p1','@p2','@p3'}; SUITES={'@smoke','@functional','@regression'}

def validate(root):
    errors=[]; seen={}; count=0
    for spec in sorted(Path(root).rglob('*.spec.ts')):
        for n,line in enumerate(spec.read_text(encoding='utf-8').splitlines(),1):
            for m in TITLE.finditer(line):
                count+=1; title=m.group(2); where=f'{spec}:{n}'
                tags=set(re.findall(r'@[\w-]+',title)); ids=CASE_ID.findall(title)
                if len(ids)!=1: errors.append(f'{where}: need exactly one case ID, found {ids}')
                elif ids[0] in seen: errors.append(f'{where}: duplicate {ids[0]} (first at {seen[ids[0]]})')
                else: seen[ids[0]]=where
                if len(tags&LAYERS)!=1: errors.append(f'{where}: need exactly one of {sorted(LAYERS)}')
                if len(tags&PRIORITIES)!=1: errors.append(f'{where}: need exactly one of {sorted(PRIORITIES)}')
                if not tags&SUITES: errors.append(f'{where}: need at least one of {sorted(SUITES)}')
    return errors,count

def main():
    p=argparse.ArgumentParser(); p.add_argument('tests_dir',nargs='?',default='tests'); a=p.parse_args()
    if not Path(a.tests_dir).is_dir(): print(f'FAIL: {a.tests_dir} is not a directory',file=sys.stderr); return 2
    errors,count=validate(a.tests_dir)
    for e in errors: print('ERROR:',e,file=sys.stderr)
    if errors: print(f'FAIL: {len(errors)} issue(s) in {count} test(s)'); return 2
    print(f'PASS: {count} test(s) follow the tag policy. Does not prove the tests are correct or were run.'); return 0

if __name__=='__main__': sys.exit(main())
