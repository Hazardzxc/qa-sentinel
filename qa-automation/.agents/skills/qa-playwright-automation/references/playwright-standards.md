# Playwright TypeScript standards
**Mandatory scope:** EVERY Playwright Web, HTTP API and cross-layer E2E spec, Page Object, API client, fixture, test data file, automation config and test runner workflow is created and maintained ONLY in the independent QA automation Git repository. FE and backend/API are never write targets. Read `../../../standards/repository-boundaries.md` and verify the boundaries before code generation.

## Repository layout
```
qa-automation/  # independent Git repo; never nested in FE or backend
  .agents/skills/qa-playwright-automation/
  docs/test-plans/ docs/coverage/
  tests/web/smoke/ tests/web/functional/ tests/web/regression/
  tests/api/smoke/ tests/api/functional/ tests/api/regression/
  tests/e2e/
  pages/ api/clients/ fixtures/ test-data/ config/ scripts/
  .github/workflows/ playwright.config.ts package.json
```

## Coding rules
- Use `@playwright/test` and TypeScript, reusable Page Objects for substantial page interactions, typed API clients for HTTP calls, and fixtures for isolated setup/teardown.
- Prefer `getByRole`, `getByLabel`, `getByTestId`; avoid brittle CSS/XPath, arbitrary sleeps and positional selectors unless justified.
- Use web-first assertions and stable API contract assertions. Do not assert guessed status codes/messages.
- Each test should be independent, deterministic and traceable to an approved case ID. Keep tests small; don't encode entire business journeys in Page Objects.
- Tag each test with appropriate Playwright tags. `@prod-safe` alone must never authorize execution.
- Use unique synthetic data and idempotent cleanup. Never modify real customer accounts or orders.
- Store URLs and nonsecret settings in environment config; secrets only in secret managers or environment variables. Never commit `.env` secrets or authentication state files.
- Separate API test setup from UI assertions; API setup must obey the same environment safety policy.
- Produce HTML/JUnit reports, screenshots/traces on failure; redact tokens, PII and sensitive payloads.
- Keep smoke suites fast and meaningful; keep full regression scheduled or deployment-gated.
- Review flaky tests and distinguish product defects from environment/test-data failures.

## Naming example
`TC-012 | Create form with valid required fields @functional @web @regression`

## Commands (illustrative; adapt to actual package scripts)
`TEST_ENV=dev npx playwright test --grep @smoke`
`TEST_ENV=qa npx playwright test --grep @regression`
`npx playwright test --list`

Do not implement the production runner using only `--grep @prod-safe`; consult ../../../standards/environment-safety.md.
