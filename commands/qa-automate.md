---
description: Generate Playwright tests in the QA repo for approved case IDs (no production runs)
argument-hint: <approved case IDs> <environment>
---
Use the qa-playwright-automation skill for: $ARGUMENTS

Implement only the approved case IDs above, in the separate QA automation repo ONLY; FE/BE repos are read-only. Verify repo boundaries before writes. Static validate (including `python3 scripts/validate_test_tags.py`) and report commands and results; do not execute without authorization. Production DENY.
