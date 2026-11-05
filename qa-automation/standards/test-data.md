# Test Data and Environment Planning

1. Document per case: role, permission, fixture/data factory, dependencies, expected state, unique identifiers, cleanup strategy, tenant and allowed environment.
2. Prefer synthetic, isolated, non-PII data. Never log credentials, tokens, real customer identifiers, order details or other sensitive contents.
3. Make API setup and teardown obey the same target-environment restrictions as main test. A `GET` route can still mutate state; method names alone do not establish safety.
4. For DEV without QA env, coordinate a stable deployed code window or isolated test tenant. Detect test-data contention and flaky external dependencies; avoid treating them as product regressions without investigation.
5. Avoid reusing mutable shared accounts for parallel tests; provision least-privilege roles. Store secret values only in approved secret manager/CI secrets.
6. If cleanup fails, log remaining synthetic state and isolate follow-up runs; do not attempt unsafe cleanup in PROD.
7. Keep evidence artifacts retention-controlled and redact PII, credentials and access tokens.
