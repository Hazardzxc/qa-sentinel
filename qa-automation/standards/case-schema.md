# Canonical Test Case Inventory Contract (shared across all skills)

**Single source of truth:** maintain a versioned test-case matrix in QA repo (or approved test management system with stable IDs). Manual and automation tests refer to the SAME case IDs. Never create parallel unrelated inventories for the same feature.

## Mandatory fields
- `case_id`: stable, unique, e.g. `TC-CMS-001`; independent of runner and env
- `feature`, `requirement_refs`, `evidence_refs`, `scenario`, `expected_result`, `expected_source` (`REQUIREMENT|AC|CONTRACT|IMPLEMENTATION_OBSERVED|NEEDS_CONFIRMATION`)
- `layer`: `WEB|API|E2E` (what system boundary is asserted, not implementation location)
- `suite_tags`: one or more `smoke|functional|regression|sanity|uat|exploratory`, pipe-delimited in CSV; tags overlap
- `nature`: `positive|negative|boundary|security|contract|visual|accessibility|other`
- `priority`: `P0|P1|P2|P3|REVIEW_REQUIRED`; include B/L/U/C factor evidence, score and confidence when available
- `execution_mode`: `MANUAL|AUTOMATED|HYBRID` (actual intended execution mode, distinct from suite/layer)
- `automation_decision`: `NOW|LATER|MANUAL` and reason
- `preconditions`, `test_data`, `steps`, `allowed_environments`, `owner`, `status` (`DRAFT|APPROVED|DEPRECATED`), `notes`

Do not fill unknown information with made-up facts. `REVIEW_REQUIRED` and `NEEDS_CONFIRMATION` are valid for DRAFT only; do not generate Playwright for unresolved expected results. Split business case inventory from *execution records* so multiple runs do not duplicate case IDs.

## Example mapping
`TC-CMS-001` might be executed manually in the first sprint and automated later: same `TC-CMS-001` appears in manual run record and Playwright title, not `TC-CMS-MANUAL-001` vs `TC-CMS-AUTO-001`. Distinct independent risks get distinct IDs.

## Classification semantics
- `regression` is not a test level or automatically assigned to every feature; it means the test is a worthwhile recurring safeguard for established behavior.
- `smoke` is a small, stable health-oriented selection. `P0` is risk/importance, not equal to smoke.
- `prod-safe` is not a universal tag and never sufficient to authorize production tests; production allowlists and controls are separate.
- A defect's observed severity is not the test's risk priority, and a fix's urgency may differ.

## Execution record
Use distinct `run_id`, `case_id`, `execution_method`, `environment`, `target_revision`, `actual_result`, `status`, `tester`, `timestamp`, `evidence_refs`, `defect_id`, and any test-data cleanup note. Results for one version must not be silently reused to certify another.
