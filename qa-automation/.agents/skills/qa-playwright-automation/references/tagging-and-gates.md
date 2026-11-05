# Tagging and Enforcement Contract
**Location gate:** Reject any proposed Playwright spec, fixture, API client, Page Object, report or QA CI workflow outside the independent QA automation Git repository. Run repository-boundary checks before generation or pipeline setup. `@api` tests are still QA-repo tests, not backend-repo tests.


Recommended tags: exactly one layer `@web|@api|@e2e`; one or more suites `@smoke|@functional|@regression`; one priority `@p0|@p1|@p2|@p3`; optional `@positive|@negative|@boundary|@security|@contract`; `@prod-safe` only after independent review. Test titles include stable test case ID.

Example: `test('TC-FORM-001 create form @e2e @smoke @regression @p1', async ({ page }) => { ... })`

Automation must validate tags in CI and fail on missing/contradictory tags. Production runs require explicit environment selection, workflow approval, dedicated least-privilege credentials, approved test-ID allowlist, read-only/non-destructive checks, no write-capable data paths, and network controls. Tags are metadata, not a security boundary. Reject PROD by default. CI should enforce deployment-version alignment and prohibit production secrets in PR jobs.

`@smoke` is not equivalent to `@prod-safe`; `@regression` is not a distinct test layer; priority is not suite membership.
