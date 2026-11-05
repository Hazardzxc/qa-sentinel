# Example prompts

### Initial read-only analysis
`Use qa-test-design. Read the FE and backend/API repositories in this workspace read-only. Verify the third independent QA repo. Inspect requirements and existing coverage. Provide an optimized case matrix with P0–P3 scoring, test type (smoke/functional/regression), WEB/API/E2E layer and manual/auto recommendation. Show source evidence and unknowns. PLAN ONLY: stop before code generation.`

### Prepare manual testing
`Using only approved TC-CMS-001..004, use qa-manual-testing to make step-by-step cases and a DEV test-run checklist for Chrome desktop and 2 roles. Mark all executions NOT_RUN until actual evidence is supplied. Suggest one focused exploratory charter.`

### Generate Playwright after approval
`QA approves TC-CMS-001, TC-CMS-002 for DEV. Use qa-playwright-automation to implement in the separate QA automation repo ONLY; FE/BE repos are read-only. Verify repo boundaries before writes. Static validate and report commands; do not execute without authorization. Production DENY.`

### Analyze release change
`Use qa-test-design. Compare FE <base>..<head> and API <base>..<head>. Trace affected endpoints and UI flows; propose smallest defensible regression set plus baseline smoke. Identify unknown dependencies and when full regression is safer. Do not delete cases or change expected behavior automatically.`

### Defect report
`Use qa-manual-testing. From the actual steps and evidence I provide, draft a bug report with actual and expected results, reproduction, severity distinct from fix priority, build and case ID. Do not assert a ticket was created.`

### Release assessment
`Use qa-release-assessment. Consolidate uploaded manual test run and executed Playwright JUnit results for a named deployed build. Flag stale/missing evidence, unresolved P0/P1 risks, blockers and untested cases. Provide recommendation only, never self-signoff.`
