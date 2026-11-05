# CI/CD integration blueprint
## Ownership boundary (mandatory)
- **The QA automation Git repository exclusively owns** Playwright files, test workflows, validation scripts, reports, and test credentials configuration.
- FE and API/BE Git repositories own their normal build/deploy pipelines; they do **not** receive copies of Playwright tests or QA workflows.
- On successful deployment, existing FE/BE pipelines or a central deployment orchestrator may **trigger** the QA repository via an authenticated and restricted event. If changing FE/BE pipeline YAML would be necessary, propose the exact change to its owner but do not write it with this skill.
- Avoid granting the QA runner source-code write tokens for FE/BE. Separate repo identity and approval from cross-repo trigger permissions.
- Verify three distinct repo roots before creating a pipeline. If the QA repo is missing, output a proposal only.

## Recommended triggers
- Pull request to automation repo: static validation, lint, typecheck, policy checks, `playwright test --list`; optional DEV tests only if stable deployment exists.
- Frontend/backend successful deployment to DEV/QA: authenticated cross-repo event/webhook or deployment orchestrator triggers QA-repo automation against the **deployed versions**, not unconditionally the latest default branches.
- Nightly: broader regression on authorized DEV/QA environment with isolated data.
- Production deployment: protected/manual approved safe smoke only, gated by environment reviewers and case ID allowlist.

## Pipeline stages
`checkout → dependencies/cache → typecheck/lint → tag and policy validator → secret scan → env/URL attestation → approval gate → execute selected suite → report/upload artifacts`.

## Cross-repo details
- Pass `frontend_commit`, `backend_commit`, deployment ID, target environment and base URLs from deployment pipeline; record them in reports.
- Prefer GitHub Actions reusable workflows or repository_dispatch/workflow_dispatch with narrowly scoped credentials. Authenticate incoming trigger and verify deployment provenance.
- Separate deployment authority from test-runner authority. Restrict production credentials to protected jobs; no secrets in PRs from forks.
- Use concurrency controls to avoid shared test-data collisions. Set timeouts and artifact retention policies.
- Fail closed if expected environment secrets/URLs or approval records are missing.

## Suggested scripts
`npm run check` = TypeScript + lint + test inventory + policy validation.
`npm run test:smoke:dev` = approved DEV smoke.
`npm run test:regression:qa` = QA regression only when QA exists.
`npm run test:prod-safe` = dedicated guarded runner (must be implemented and independently reviewed before enabling).

No sample YAML should be treated as production-ready without repo-specific credentials, approval settings, deployment version matching and network controls.
