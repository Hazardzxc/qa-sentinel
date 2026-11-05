---
name: qa-release-assessment
description: Combine verified manual and Playwright results against a shared traceability matrix to assess release readiness, untested risks, defect blockers and QA sign-off evidence without inventing results. Use when the user asks if a build or feature is ready to release, for a test summary or QA sign-off report, or to combine manual and automated results.
---
# QA Release Assessment Skill

## Scope
Use after testing runs, release candidate verification, or when asked whether a feature/build is ready to release. Read `../../../standards/case-schema.md`, `../../../standards/traceability.md`, `../../../standards/environment-safety.md` and `references/release-assessment.md`.

## Ingest and reconcile
- Load QA-approved case matrix and traceability baseline, actual manual run records and Playwright report/JUnit/artifacts; do not mix environments or builds invisibly.
- Key by `case_id + run_id + environment + deployed_revision` and keep manual/automation executions separate even when they share one case ID. Clearly identify `PASS`, `FAIL`, `BLOCKED`, `NOT_RUN` and `NOT_APPLICABLE`.
- Distinguish latest result from historical evidence and mark stale results (wrong FE/BE deployment) `NOT_VALID_FOR_TARGET_BUILD` rather than using as release evidence.
- Match each requirement/risk to test case IDs and actual evidence; label `COVERED`, `PARTIAL`, `MISSING`, `BLOCKED` with reason. No unsupported coverage percentages.
- Record open defects, defect **severity** vs **fix priority**, P0/P1 risks, security/data integrity concerns, test data constraints, environment stability, missing sign-offs and nonfunctional gaps.

## Output and decision
Produce `../../../templates/release-summary.md`: release metadata, scope, execution counts, failures, blocked/untested cases, defect log, key residual risks, affected business flows, confidence, suggested `GO | CONDITIONAL_GO | NO_GO | INSUFFICIENT_EVIDENCE` and explicit rationale.

**Recommendation ≠ approval.** The AI must not approve or authorize release; human QA/engineering/product owner signs off according to organizational policy. Never invent test execution, deployment revisions, results or ticket state. If evidence is incomplete, recommend `INSUFFICIENT_EVIDENCE`, not a fabricated GO.

## Repository rule
Read frontend/backend source revisions as evidence only; release reports and exported templates belong in the independent QA automation repo or authorized test-management system. No FE/BE writes.

## Language
Reply in the user's language; keep case IDs, statuses, tags and template field names in English.
