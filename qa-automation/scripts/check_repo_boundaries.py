#!/usr/bin/env python3
"""Offline guard: check independent FE/API/QA Git roots and optional output destination.
This does not set permissions or prove that future AI actions remain safe.
"""
import argparse, subprocess, sys
from pathlib import Path

def git(path, *args):
    return subprocess.check_output(['git','-C',str(path),*args],text=True,stderr=subprocess.STDOUT).strip()

def within(path, root):
    try: path.relative_to(root); return True
    except ValueError: return False

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--frontend',required=True)
    p.add_argument('--backend',required=True)
    p.add_argument('--qa',required=True)
    p.add_argument('--output',help='Optional file location planned for a generated QA artifact')
    a=p.parse_args()
    inputs={k:Path(getattr(a,k)).expanduser().resolve() for k in ['frontend','backend','qa']}
    roots={}; commons={}
    try:
        for key,path in inputs.items():
            root=Path(git(path,'rev-parse','--show-toplevel')).resolve()
            # Use resolved absolute path for common git dir (git may return a relative path).
            common_raw=Path(git(path,'rev-parse','--git-common-dir'))
            common=(common_raw if common_raw.is_absolute() else path/common_raw).resolve()
            roots[key]=root; commons[key]=common
            print(f'{key}: git_root={root} common_git_dir={common}')
    except (subprocess.CalledProcessError,FileNotFoundError) as e:
        print('FAIL: missing or inaccessible Git checkout:',e,file=sys.stderr); return 2
    vals=list(roots.values()); cvals=list(commons.values())
    if len(set(vals)) != 3 or len(set(cvals)) != 3:
        print('FAIL: repositories or Git common directories are not independent',file=sys.stderr); return 2
    if any(within(roots[a], roots[b]) for a in roots for b in roots if a != b):
        print('FAIL: repositories are nested',file=sys.stderr); return 2
    if a.output:
        target=Path(a.output).expanduser()
        # Resolve symlinks already present in parent path; missing leaf is okay.
        target=target.resolve()
        if not within(target,roots['qa']):
            print(f'FAIL: output path outside QA root: {target}',file=sys.stderr); return 2
        print(f'output path accepted: {target}')
    print('PASS: distinct Git roots and common dirs verified. This is NOT an access-control enforcement.')
    return 0

if __name__=='__main__': sys.exit(main())
