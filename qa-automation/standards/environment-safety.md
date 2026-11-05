# Environment policy and hard safety requirements
This environment policy applies to Playwright scripts executed from the **separate QA automation repository**, including backend HTTP tests; it never authorizes writing tests to FE/API repositories. Repo separation alone does not provide runtime/production safety.

## Matrix
- DEV + PROD: DEV is primary automation target when stable and authorized; PROD only explicitly approved safe monitoring/smoke.
- DEV + QA + PROD: DEV for early feedback; QA for full regression; PROD for approved safe monitoring/smoke.
- UAT optional: business-critical acceptance checks when present; do not assume it exists.
- For unstable DEV, coordinate stable deployment windows or ephemeral isolated test environments; don't treat failures during active deployment as product defects without investigation.

## Required controls before execution
1. Exact environment allowlist (names AND approved base URLs/origins), verified at runtime; fail closed on unknown/empty values, redirects to unapproved origins, or ambiguous config.
2. Explicit manual approval and protected CI environment for production, with least-privilege credentials, restricted secrets and required reviewers.
3. Production-safe **case ID allowlist** reviewed by owners, separate from tags; use dedicated production runner and narrow credentials.
4. Network-level enforcement where possible: allow only approved hosts and safe HTTP methods for production, including API setup and redirects. Be aware that GET can cause side effects; method allowlisting alone is insufficient.
5. Reject or mock dangerous operations (write/delete/payment/email/notification/order/state change) on production; no destructive cleanup. Do not rely on naming or tagging to enforce safety.
6. Explicitly validate external integrations and tenant boundaries; use synthetic accounts and data only.
7. Fail closed when target env cannot be verified, test case lacks approval, or guardrails cannot be enforced.
8. Log environment, deployed versions/commits, approved case IDs, execution identity and results without logging secrets.

## Threat examples
- `TEST_ENV=dev` accidentally points to production URL.
- A UI test navigates from DEV to production via redirect.
- A supposedly read-only GET triggers a state-changing action.
- API fixture creates or deletes data while the test itself is marked `@prod-safe`.
- Browser UI triggers unsafe writes even if API request helper blocks writes.

## Production policy
Default DENY. Never generate a bypass flag that disables production restrictions. Do not run against production based only on a user's general request to 'run tests'. Require explicit production authorization and independent technical controls. If not available, provide instructions or static validation only.
