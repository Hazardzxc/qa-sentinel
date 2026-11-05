# Risk-based test design
## Selection procedure
1. Enumerate business journeys, API contracts, UI-specific rules, permissions and external dependencies.
2. Assess impact, likelihood of failure, change frequency, integration complexity, observability and existing coverage (qualitative high/medium/low with rationale).
3. Choose one primary test layer per assertion: API for backend validation/permissions/contracts; Web for browser rendering, accessibility-relevant interactions and client validation; E2E for critical user journeys crossing UI and API. Add overlap only for independent risk.
4. Apply equivalence classes and boundary values for constrained fields; decision tables for permissions/state transitions; pairwise combinations when combinations explode; negative cases for meaningful error paths.
5. Prefer representative cases over permutations; never remove distinct access-control or integrity risks just to reduce counts.
6. Group test data, cleanup, dependencies, expected outcomes and environment restrictions. Mark missing business acceptance criteria `NEEDS_CONFIRMATION`.
7. Deduplicate cases by `business rule + assertion + layer + risk`, and record why omitted cases are covered elsewhere.

## Priorities
Use the mandatory four-factor scoring, `UNKNOWN` handling and P0 overrides in `classification-risk.md`. P0 Critical, P1 High, P2 Medium and P3 Low are risk bands, not interchangeable with smoke/regression suite tags. No fixed number-of-tests quota.

## Destination policy
All proposed Playwright Web/API/E2E cases target the **separate QA automation Git repository**; no case may target the FE/API source repository. Cite FE/BE source files as evidence, but the destination of generated files remains QA only.

## Matrix schema
`ID | Feature | Evidence (repo@commit:path:symbol / requirement) | Scenario | Layer (API/Web/E2E) | Priority | Tags | Preconditions & data | Steps | Expected | Allowed env | Risk addressed | Automation feasibility | Status`

Use `@smoke`, `@functional`, `@regression`, `@api`, `@web`, `@e2e`, `@prod-safe` as independent classifications. `@prod-safe` is a **candidate designation** requiring review and technical enforcement, not permission to execute.

## Coverage deliverables
- Requirement/business-rule → test IDs → layer → coverage status (`COVERED`, `PARTIAL`, `MISSING`, `BLOCKED`).
- Explicit excluded scenarios and redundancy rationale.
- Unknown requirements, environment gaps, fixtures/data, and estimated runtime.
- Ask QA for approval before writing code.
