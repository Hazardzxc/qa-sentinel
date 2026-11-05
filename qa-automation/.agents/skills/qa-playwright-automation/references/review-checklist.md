# QA review gates
## Mandatory repository boundary checks
- [ ] FE, backend/API and QA automation repos have distinct verified Git roots (and distinct common dirs; origins checked where available).
- [ ] QA automation repo is **not** a subfolder or worktree of FE/API repo.
- [ ] FE/API repos are read-only for this skill, including tests and workflows.
- [ ] All proposed Playwright Web/API/E2E code, docs and CI paths are under QA automation Git root only.
- [ ] CI events originate from deployed FE/API revisions but execution resides in QA repo; no FE/API write token granted to test runner.
- [ ] Missing/unverified QA repo blocks test generation rather than silently choosing a source repo.

## Plan approval checklist
- [ ] Frontend and backend repository/commit provenance recorded; gaps explicit.
- [ ] Requirements compared against observed code; contradictions flagged.
- [ ] Critical workflows, authz and data-integrity risks represented.
- [ ] Each case has evidence, explicit expected result, priority, layer and environment.
- [ ] Existing test coverage checked and redundant cases explained.
- [ ] Test data and cleanup feasible; external side effects understood.
- [ ] No arbitrary test-count cap or unsubstantiated coverage percentage.
- [ ] QA explicitly approved case IDs and scope.

## Code review checklist
- [ ] Verified output paths are within QA Git root after resolving symlinks, with no FE/API file writes.
- [ ] `git status` checks show that FE/API tracked content remains unchanged, or verification is explicitly marked incomplete.
- [ ] Approved IDs map 1:1 to implemented scenarios or justified grouping.
- [ ] Web locators stable, API assertions grounded, fixtures isolated.
- [ ] No hardcoded credentials or customer data.
- [ ] Environment guard fails closed, including API setup and redirects.
- [ ] Production uses reviewed allowlist and independent controls.
- [ ] Typecheck, lint, policy validation, test listing completed.
- [ ] Execution outcomes honestly reported; unrun cases marked NOT_RUN.
- [ ] HTML/JUnit/trace artifacts available when actually produced.

## Maintenance review checklist
- [ ] Changed source commits and impacted flows identified.
- [ ] Proposed adds/updates/removals justified by evidence and risk.
- [ ] QA approval obtained before changing scope.
