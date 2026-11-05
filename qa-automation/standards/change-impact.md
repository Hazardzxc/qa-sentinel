# Change Impact Analysis and Selective Regression

## Write boundary
Read FE/API diffs only to assess test impact; write/update/retire Playwright tests, risk maps and impact reports **only in the independent QA automation repo**, after QA approval. Never write migration tests or other Playwright files back into the FE/API repositories. Review `repository-boundaries.md` before proposing code paths.

## Trigger
When asked to assess a PR, commit, release or changed code, compare explicit base and head commits. Record repo names, commit hashes and deployment version; do not assume the deployed environment matches HEAD.

## Trace dependency graph
For each changed file/symbol: frontend route/component → API call → backend endpoint → service/rules → data/permissions → existing test IDs. Identify direct impacts, transitive/shared impacts and unknown/unmapped impacts. Consider schema, migrations, auth, feature flags, configuration, external integrations, and shared libraries.

## Deliverables
- Diff summary with evidence (repo/path/symbol/commit).
- Impacted test IDs: `must_run`, `recommended`, `not_impacted`, `unknown`.
- New/modified/deprecated cases with reason and approval status.
- Coverage gaps, missing mappings, confidence, and expected runtime.
- Baseline smoke suite plus impacted regression tests; broaden to full regression for shared infrastructure, migrations, broad dependency changes, unclear impact or poor mapping confidence.
- Never claim selective regression proves unaffected behavior.

## Rules
1. Always include mandatory critical smoke for the target environment; PROD only independently approved non-destructive allowlist.
2. Do not delete a test because a feature appears unused: confirm deprecation with product/QA.
3. Do not silently modify expected results based only on changed implementation.
4. Never auto-run against PROD. Never auto-update snapshots as evidence of correctness.
5. Stop for QA approval before adding, changing or removing automated tests.

## Example output
`Change: backend/src/forms/validation.ts -> POST /forms -> create form UI`
`Must run: TC-FORM-API-004, TC-FORM-UI-002`
`Recommended: TC-FORM-E2E-001`
`Unknown: other consumers of shared validation helper (inspect before narrowing)`
