#!/usr/bin/env python3
"""Minimal offline case inventory schema validator. Does not verify business correctness."""
import argparse, csv, re, sys
from pathlib import Path
REQUIRED=['case_id','feature','requirement_refs','evidence_refs','scenario','expected_result','expected_source','layer','suite_tags','nature','priority','execution_mode','automation_decision','preconditions','test_data','steps','allowed_environments','owner','status','notes']
ENUM={'layer':{'WEB','API','E2E'},'priority':{'P0','P1','P2','P3','REVIEW_REQUIRED'},'execution_mode':{'MANUAL','AUTOMATED','HYBRID'},'automation_decision':{'NOW','LATER','MANUAL'},'status':{'DRAFT','APPROVED','DEPRECATED'},'expected_source':{'REQUIREMENT','AC','CONTRACT','IMPLEMENTATION_OBSERVED','NEEDS_CONFIRMATION'}}
SUITES={'smoke','functional','regression','sanity','uat','exploratory'}

def validate(path):
    errors=[]; seen=set()
    with Path(path).open(newline='',encoding='utf-8-sig') as f:
        reader=csv.DictReader(f)
        fields=reader.fieldnames or []
        missing=[c for c in REQUIRED if c not in fields]
        if missing: return [f'missing columns: {missing}']
        for n,row in enumerate(reader,2):
            cid=(row.get('case_id') or '').strip()
            if not re.fullmatch(r'TC-[A-Z0-9]+(?:-[A-Z0-9]+)*-\d{3,}',cid): errors.append(f'line {n}: invalid case_id {cid!r}')
            if cid in seen: errors.append(f'line {n}: duplicate case_id {cid}')
            seen.add(cid)
            for col in REQUIRED:
                if not (row.get(col) or '').strip(): errors.append(f'line {n} ({cid}): blank {col}')
            for col,valid in ENUM.items():
                if (row.get(col) or '').strip() not in valid: errors.append(f'line {n} ({cid}): invalid {col}={row.get(col)!r}')
            tags={x.strip() for x in (row.get('suite_tags') or '').split('|') if x.strip()}
            if not tags or not tags <= SUITES: errors.append(f'line {n} ({cid}): invalid suite_tags {tags}')
            if row.get('status','').strip()=='APPROVED' and (row.get('expected_source')=='NEEDS_CONFIRMATION' or row.get('priority')=='REVIEW_REQUIRED' or 'NEEDS_CONFIRMATION' in row.get('expected_result','')):
                errors.append(f'line {n} ({cid}): approved case cannot have unresolved expected/risk inputs')
    return errors

def main():
    p=argparse.ArgumentParser(); p.add_argument('csv_file'); a=p.parse_args()
    try: errors=validate(a.csv_file)
    except Exception as e: print(f'FAIL: {e}',file=sys.stderr); return 2
    for e in errors: print('ERROR:',e,file=sys.stderr)
    if errors: print(f'FAIL: {len(errors)} issue(s)'); return 2
    print('PASS: case matrix structure valid. Does not prove coverage, priority correctness or expected behavior.'); return 0

if __name__=='__main__': sys.exit(main())
