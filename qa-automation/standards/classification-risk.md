# Classification and Risk Scoring Policy
All selected Playwright Web/API/E2E tests are implemented in the independent QA automation repo. `layer=api` means HTTP test target, NOT permission to place a test in the backend source repo.


## Inputs and evidence
For each feature/scenario, gather: requirement/AC, source paths/symbols, user journey, affected endpoint, ownership, existing coverage, deployment/environment and historical incidents if accessible. Source code shows implementation, not necessarily correct business expectations. If evidence is absent use `UNKNOWN`, confidence `low`, and request QA/product confirmation. Never fabricate usage or defect history.

## Separate dimensions
- **Layer**: `web` for browser interaction/UI validation, `api` for HTTP contract/business validation, `e2e` for critical cross-layer journey. Select the cheapest layer that detects the unique risk.
- **Suite**: `smoke` = small, stable, fast, critical health checks; `functional` = behavior verification; `regression` = protects existing behavior across changes. Membership can overlap; do not classify a whole feature as regression automatically.
- **Nature**: positive, negative, boundary, security, contract, accessibility, etc.
- **Priority**: P0 Critical, P1 High, P2 Medium, P3 Low.
- **Decision**: Automate Now, Automate Later, Manual (with rationale, cost, data/environment constraints).

## Scoring rubric (1–5 for each factor)
- B business impact: 1 cosmetic; 3 meaningful workflow disruption; 5 major revenue/security/privacy/integrity/availability harm.
- L failure likelihood: 1 stable/simple, evidence-backed; 3 moderate complexity/changes; 5 recent incidents, fragile integrations or complex logic. If no evidence, UNKNOWN.
- U usage frequency: 1 rare, 3 regular, 5 core frequent journey; require product/analytics evidence. If absent, UNKNOWN.
- C change/dependency impact: 1 isolated, 3 shared module, 5 widely reused or high blast radius.

Score = 0.4*B + 0.3*L + 0.2*U + 0.1*C.
P0: 4.5–5.0; P1: 3.5–<4.5; P2: 2.5–<3.5; P3: 1.0–<2.5. These are local starting thresholds, not industry standards. Record all four inputs, evidence, confidence and rounded score (2 decimals). If any factor is unknown, do not invent a numeric final priority; show provisional band or `REVIEW_REQUIRED`, with known risk overrides.

## Critical overrides
Set P0 and require human review if plausible failure could cause unauthorized access, material financial harm, sensitive data exposure, data corruption/loss, or critical service outage. Clearly distinguish confirmed risk from plausible risk; a speculative override is provisional until reviewed. QA/product owner can override with written justification and approver.

## Selection and optimization
1. Build rule/flow-to-test coverage matrix; include negative permission and data-integrity paths.
2. Prefer API tests for backend rules; browser tests for UI behaviors; a small number of E2E tests for cross-layer business journeys.
3. Apply equivalence classes and meaningful boundary values; pairwise for large independent combinations.
4. Detect duplicates by same risk, expected outcome, layer, and underlying implementation; consolidate only when independent failure modes remain covered.
5. Prioritize P0/P1. Keep P2/P3 when a distinct risk, past defect, regulatory need or cheap stable test justifies them. Do not impose a fixed count cap.
6. A `smoke` test must be fast and stable, not merely high priority; a `prod-safe` tag alone does not authorize PROD execution.

## Required case fields
ID, feature, requirement and code evidence, observed vs expected status, scenario, layer, suite tags, nature, B/L/U/C with evidence, score/priority/confidence, reason, preconditions/data, steps, expected result, target environments, automation decision, existing coverage, status and owner.

## Example (illustrative, not repository evidence)
`TC-LOGIN-001 | Login | E2E | @smoke @regression @e2e | positive | B=5 L=3 U=5 C=4 => 4.30 P1 | confidence=medium | Automate Now`
If login is a security/access control gate, evaluate P0 override and document it.

## QA gate
Present proposed classifications, excluded cases, gaps, and a rationale for each. STOP for QA approval before generating tests.
