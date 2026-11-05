# Coverage and Traceability

Maintain `requirement_or_risk_id -> test_case_ids -> execution records -> defect IDs -> release decision` with source and revision evidence. A single test may cover multiple requirements, and a requirement may require multiple tests because it has independent failure modes.

Coverage statuses: `COVERED` when case(s) have applicable, adequate evidence for target; `PARTIAL` when some risks/variants missing; `MISSING` when no defensible case/evidence; `BLOCKED` when cannot execute. Planning coverage (case exists) must be clearly distinct from execution coverage (case passed on target build).

Document discarded duplicates and uncovered risks explicitly. Do not force a fixed test count; choose representative equivalence classes, meaningful boundary values, decision tables and only necessary E2E. When actual expected behavior is unknown, record a gap rather than claiming coverage. If percentages are reported, define denominator and formula.

A change impacting a shared library or unknown consumers may require full regression; selective regression plus smoke does not prove untouched features safe. For a release, link relevant manual and Playwright results by the SAME case IDs.
