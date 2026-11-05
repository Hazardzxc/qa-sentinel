# Mandatory Repository Separation Policy

## Goal and required topology
Every Playwright suite produced under this skill — browser/web, HTTP API, and cross-layer E2E — belongs in one **independent project-owned QA automation Git repository**. Frontend and backend/API repositories are read-only evidence sources for the AI. A single QA repo may own one product/domain; do not combine every company product by default.

```text
workspace/
  frontend/          # FE_REPO; Git repo A; inspect only
  backend/           # API_REPO; Git repo B; inspect only
  qa-automation/     # QA_REPO; Git repo C; write only after approval
    .agents/skills/qa-playwright-automation/
    docs/test-plans/ docs/coverage/
    tests/web/ tests/api/ tests/e2e/
    pages/ api/clients/ fixtures/ test-data/ config/
    scripts/ .github/workflows/ playwright.config.ts package.json
```

**Do not** put Playwright suites in `frontend/tests`, `backend/tests`, or any other FE/BE path. Do not create a QA folder inside a source repository and call it separate. Distinct worktrees of the same repo are not distinct repositories.

Developer-owned unit, component, and code-coupled integration tests may **remain** in FE/BE; this is not an instruction to remove existing tests or duplicate them in Playwright.

## Permission and ownership matrix

| Operation | FE repo | Backend/API repo | QA automation repo |
| --- | --- | --- | --- |
| Inspect code/routes/contracts/tests/diffs | READ | READ | READ |
| Edit source or test files | DENY | DENY | Allow only after QA approval |
| Write Playwright tests / POM / API clients / fixtures | DENY | DENY | Allow only after QA approval |
| Write test plan/coverage/CI workflows | DENY | DENY | Allow only after QA approval |
| Commit or push | DENY | DENY | Only when explicitly authorized |
| Trigger automation after successful deploy | Emit deploy metadata only if a team's pipeline permits | Emit deploy metadata only if a team's pipeline permits | Test runner/CI ownership |

## Pre-generation checks — fail closed
1. Identify canonical absolute paths for FE, API/BE and QA repos; run `git -C <path> rev-parse --show-toplevel` for each where shell access is available.
2. Confirm all 3 Git roots are distinct, and are not nested. Check Git common directories (`git rev-parse --git-common-dir`) so worktrees of one repo do not masquerade as separate repos; compare `remote.origin.url` when available. If remotes are unknown, record `UNVERIFIED_REMOTE` and request confirmation before publishing changes.
3. Resolve symlinks and verify every planned output path is within the canonical QA Git root; do not traverse symlinks that point outside it. Confirm the editor/agent's write permissions are constrained accordingly where supported.
4. Record `source_repo`, `source_commit`, `qa_repo`, `qa_commit`, and deployed frontend/backend revisions. Never infer deployed versions from HEAD alone.
5. Before writing, require QA approval of case IDs + output destination. On any mismatch, missing QA Git repo, or uncertain permissions: **STOP** and show setup instructions. Do not write into the source repositories.
6. After generating, report file paths relative to QA Git root; confirm `git status --short` for QA only, and verify FE/BE tracked files were not changed. If inspection access is unavailable, mark the verification incomplete, not successful.

## Access pattern
Use a workspace containing 3 independent checkouts. The AI can read FE and BE to build `UI action -> FE HTTP request -> API endpoint -> business rule -> risk/test ID`. The AI emits plans and all Playwright code only in the QA repo. If API contracts or requirements conflict with source code, flag differences for review rather than making FE/BE edits.

## CI/CD boundaries
- Frontend/backend build and deploy independently. Once DEV/QA deployment succeeds, an authenticated cross-repo trigger may start QA automation workflow with `frontend_sha`, `backend_sha`, `deployment_id`, `environment`, `approved_origins`.
- The QA repo owns the Playwright workflow, tags, environment policy and reports. Repositories being tested do not need copies of Playwright tests.
- Cross-repo triggers must be authenticated, narrowly scoped, pinned to deployments, and must not provide write access to FE/BE. If the trigger needs changes to existing FE/BE CI, propose those changes to the owners in a separate approval process; **do not edit source repos using this skill**.
- Production test safety remains DENY by default and requires the independent controls in `environment-safety.md`.

## Examples of forbidden outcomes
- `frontend-repo/tests/e2e/login.spec.ts` — WRONG
- `backend-repo/tests/playwright/user-api.spec.ts` — WRONG
- `frontend-repo/qa-automation/tests/` — WRONG (nested)
- `qa-automation-repo/tests/web/login.spec.ts` — RIGHT
- `qa-automation-repo/tests/api/user-api.spec.ts` — RIGHT
- `qa-automation-repo/tests/e2e/order.spec.ts` — RIGHT

## If separate repo does not yet exist
Output a suggested repository name, directory tree, needed read-only permissions and CI trigger contract; ask the responsible team to create/approve it. Generate no Playwright code until it exists and QA has approved the plan.
