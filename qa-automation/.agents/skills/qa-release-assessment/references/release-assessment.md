# Consolidated QA Release Assessment

## Release gate inputs
1. Named target environment and deployment ID; actual deployed FE/BE revisions (or `UNKNOWN`).
2. Approved scope/version of case inventory and requirement acceptance criteria.
3. Manual evidence, Playwright actual executed reports, known defects (status/severity/priority), coverage/exclusions.
4. Explicit P0/P1 risk acceptances and owner's decision, when any are proposed.
5. Security/performance/accessibility/manual exploratory gaps if relevant.

## Suggested recommendation policy (customizable)
- `NO_GO`: observed unresolved critical security/data-loss/availability risk, accepted critical workflow failing, or organization-defined hard gate failing.
- `CONDITIONAL_GO`: no hard blockers under policy but known lower-risk issues require written owner risk acceptance and mitigation.
- `GO`: required agreed release gates have passed with current-build evidence, no unresolved blockers and owners confirm sign-off. AI can only **recommend**, not grant the decision.
- `INSUFFICIENT_EVIDENCE`: required run data missing/stale, environment/build identity unknown, critical cases NOT_RUN/BLOCKED or requirements unresolved. Do not guess.

Never count `NOT_RUN` as passed, and do not equate number of automated test files with executed scenario coverage. Show data lineage and revision for each claim. Separate provisional assessments from official approval.
