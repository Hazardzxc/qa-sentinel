---
name: qa-manual-testing
description: Plan and conduct evidence-driven manual, exploratory, sanity, UAT and regression testing using shared QA case IDs, test-run records and reproducible bug reports.
---
# QA Manual Testing Skill

## When to use
For manual case authoring, exploratory charters, test runs, UI/UX and visual inspections, role/permission checks, device/browser review, bug reproduction, retest and manual regression. Use `qa-test-design` first for shared classifications and source evidence.

## Rules and shared policies
- Read `../../../standards/case-schema.md`, `../../../standards/traceability.md`, `../../../standards/test-data.md`, `../../../standards/classification-risk.md`, `../../../standards/environment-safety.md`, `../../../standards/repository-boundaries.md`.
- FE and Backend are read-only evidence; keep all manual plans, run artifacts, screenshots and defect drafts solely in the independent QA automation repo (or approved test-management system). Never modify FE/BE to create data or fixtures. An approved test execution may interact with deployed DEV/QA applications under test, not their repository source code.
- Test case priority and suite must come from the shared inventory. Do not regenerate a second independent manual case set or override P0–P3 silently.
- Writing a **draft** plan can be requested in QA repo, but **actual execution** requires designated tester, approved scope, permitted environment/account/test data and permission to perform actions.
- AI may draft instructions, but unless an authorized browser/API tool actually performs a test, execution status MUST remain `NOT_RUN`. Never invent screenshots, actual results, defects or evidence.

## Required workflow
1. **Load approved inventory** with stable case IDs, associated business rules, priority, known environment and test data. Record missing prerequisites as `BLOCKED` rather than guessing.
2. **Prepare manual test cases** with clear scenario, preconditions, numbered steps, required data, expected results grounded in requirements, cleanup, and evidence to capture. Separate UI/API behavior where useful. Use `../../../templates/manual-test-case.md`.
3. **Plan run**: record project/version/FE and BE deployment refs, test environment and URL, browser/device/role, executor, run ID and scope. DEV or QA preferred; PROD defaults to no execution without separate authorization and technical controls.
4. **Execute only with evidence**: collect actual output, time, version, screenshots/trace/log references with sensitive information redacted. Use `PASS`, `FAIL`, `BLOCKED`, `NOT_RUN`, `NOT_APPLICABLE`; preserve original outcome when retesting and create new execution record.
5. **Exploratory**: write a timeboxed charter with mission, risks, data/roles, heuristics, stop condition, notes, open questions and follow-up tests. Exploration is not a proxy for a verified case run; use `references/exploratory-testing.md`.
6. **Failure/defect**: distinguish environment issue, unstable data, test-step mistake, requirement ambiguity and product defect. Draft a reproducible report per `references/defect-management.md`; include observed vs expected, version, severity and priority **separately**, repeatability and evidence. Do not claim Jira ticket creation unless actually created through authorized tooling.
7. **Retest and regression**: retest the exact failing behavior on a specified fixed build; preserve previous failure evidence; then propose risk-based related regression. Use the source diff and `../../../standards/change-impact.md` when available.
8. **Hand off**: send manual run summary + defect IDs/evidence and gaps to `qa-release-assessment`. Recommend promoting stable repetitive manual checks to Playwright only after shared inventory update and QA approval.

## Output contract
- Manual test cases and execution run sheet (templates provided)
- Exploratory charter and structured notes, where relevant
- Reproducible defect drafts and retest log for observed issues
- Summary separating `PASS/FAIL/BLOCKED/NOT_RUN/NOT_APPLICABLE`, with evidence locations and residual risks

## Stop conditions
If acceptance criteria are missing, mark expected behavior `NEEDS_CONFIRMATION`; do not create a false PASS. If a production action could mutate real state, notify stakeholders and stop; never treat a tag or human statement alone as a sufficient safety control.
