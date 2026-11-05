# QA Sentinel: QA Engineering Skill Set

A practical, repository-aware QA workflow for teams with **separate frontend, backend/API, and QA automation Git repositories**. Includes four coordinated agent skills, shared policies, manual testing workflow, Playwright Web/API/E2E standards, review gates, and templates.

> The files are instructions and scaffolding. They do **not** themselves grant repository permissions, execute tests, configure a functioning CI deployment trigger, or enforce production safety at runtime. Enforce these separately with account permissions, CI settings, dedicated runners, network controls, credentials and code reviews.

## Contents

```
.claude-plugin/marketplace.json      # Claude Code plugin manifest
commands/                            # /qa-* slash commands
qa-automation/                       # COPY CONTENTS into an independent QA Git repo
  .agents/skills/
    qa-test-design/SKILL.md           # central analysis, risk and case inventory
    qa-manual-testing/SKILL.md        # manual execution, exploratory, defect drafting
    qa-playwright-automation/SKILL.md # reviewed code generation and maintenance
    qa-release-assessment/SKILL.md   # consolidated manual + automation reporting
  standards/                         # single authoritative cross-skill policy
  templates/                         # Markdown + CSV templates, Playwright starter, PR check workflow
  examples/                          # explicitly fictitious examples and prompts
  scripts/                           # small optional offline validators
  docs/                               # destination for case inventory, runs, reports
```

## Quick start

**Claude Code plugin** (installs the four skills):

```
/plugin install qa-sentinel --marketplace Hazardzxc/qa-sentinel
```

On older Claude Code versions: `/plugin marketplace add Hazardzxc/qa-sentinel`, then `/plugin install qa-sentinel@qa-sentinel`.

The plugin gives you the skills only. To get the templates, standards and `docs/` scaffold in your QA repo, also copy the files:

```bash
git clone https://github.com/Hazardzxc/qa-sentinel.git
cp -R qa-sentinel/qa-automation/. path/to/your-qa-repo/
```

**Claude Code** looks for skills in `.claude/skills/`. From your QA repo root, link it to the bundled skills (the `../../../standards/` links keep working):

```bash
mkdir -p .claude && ln -s ../.agents/skills .claude/skills
```

## Slash commands (Claude Code plugin)

| Command | What it does |
|---|---|
| `/qa-init` | Copy standards, templates and the `docs/` scaffold into your QA repo (never overwrites) |
| `/qa-plan <feature>` | Risk-based test plan and case matrix, stops for QA approval |
| `/qa-manual <case IDs> [env]` | Manual cases, run sheet and exploratory charter |
| `/qa-automate <case IDs> <env>` | Playwright tests for approved IDs, production denied |
| `/qa-impact FE a..b API c..d` | Smallest defensible regression set for a change |
| `/qa-release <build>` | Release-readiness recommendation, never self-signoff |

Other AI tools: use the same prompts from `qa-automation/examples/workflow-prompts.md`.

## Use with other AI tools

The skills follow the open Agent Skills format (`SKILL.md` + frontmatter), and `qa-automation/AGENTS.md` points any agent to the right starting skill.

| Tool | How |
|---|---|
| Claude Code | Plugin above, or the `.claude/skills` symlink |
| OpenAI Codex | Reads `.agents/skills/` and `AGENTS.md` directly after copying the files |
| Cursor, GitHub Copilot, Gemini CLI | Read `AGENTS.md`; link `.agents/skills` into the tool's own skills folder if it supports skills |
| Any other AI | Ask it to read `.agents/skills/qa-test-design/SKILL.md` first |

## Works well with ponytail

[ponytail](https://github.com/DietrichGebert/ponytail) (MIT, separate project) keeps generated code small: no unrequested abstractions, reuse before adding. QA Sentinel does not bundle it; install it alongside if you want leaner Playwright code:

```
/plugin marketplace add DietrichGebert/ponytail
/plugin install ponytail@ponytail
```

- Used only for automation code (specs, fixtures, API clients, CI), not for test design, manual testing or release reports.
- QA Sentinel's safety, approval, boundary and tagging rules always win over ponytail.
- Review generated specs with `/ponytail-review` **and** `qa-playwright-automation/references/review-checklist.md`.
- ponytail has its own hooks, a local task ledger and an optional webhook; check its settings. QA Sentinel sends nothing anywhere.

## Install in your actual QA automation repository

1. Create or choose a **separate, independent Git repository** for the product/domain's QA assets (not a directory inside the FE or backend repo). Its Git root is `qa-automation`.
2. Copy **the contents of** this package's `qa-automation/` directory into that QA repository; do not copy the parent package folder into the source repositories.
3. Open a workspace with three independent checkouts: `frontend/` (agent read-only), `backend/` (agent read-only), `qa-automation/` (the only agent write destination). Restrict permissions in the actual agent/IDE/OS; the instructions alone are insufficient.
4. Check `git rev-parse --show-toplevel` and `git rev-parse --git-common-dir` for each repo. Optionally run `python3 scripts/check_repo_boundaries.py --frontend ../frontend --backend ../backend --qa .` from the QA repo root.
5. Make the agent read `qa-test-design/SKILL.md` first and follow each phase. The provided skills use relative links to `standards/`, so install the **whole** directory structure together. Tool-specific discovery of `.agents/skills` may vary: add an agent-specific pointer where required.
6. Populate actual requirement sources, repository commits, environments, user roles, available browsers, API contract and QA approver. All sample URLs and cases are placeholders.
7. Review draft test cases before starting manual runs or generating Playwright code. An explicit case-ID approval is required for generated automation.

## Workflow

`ANALYZE (FE + API + requirements) → DESIGN (shared case IDs, risk and method) → QA APPROVAL → MANUAL and/or AUTOMATION → EVIDENCE/DEFECTS → RELEASE ASSESSMENT → CHANGE IMPACT/MAINTENANCE`

The central test case inventory is the **single source of truth**. A case may be tagged `regression` and `smoke` and also have an execution method `MANUAL`, `AUTOMATED` or `HYBRID`. Test suite, layer, nature, priority and execution method are independent classifications.

## Quick prompts

- **Plan only:** `Use qa-test-design. Inspect frontend and backend repositories read-only. Propose the smallest defensible risk-based case matrix and traceability; mark unknown business expectations. Do not generate Playwright code. Stop for QA approval.`
- **Manual:** `Use qa-manual-testing for approved TC-CMS-001..004. Create a manual run sheet and exploratory charter for DEV. Do not mark any case PASS without real execution evidence.`
- **Automate:** `Use qa-playwright-automation for approved TC-CMS-001..003. Generate only in our independent QA repository. Use Playwright TypeScript; no production execution.`
- **Change review:** `Use qa-test-design and the change-impact policy to inspect FE and API commit diffs, propose affected case IDs, baseline smoke, and unknown transitive impacts. Wait for approval before changing code.`
- **Release:** `Use qa-release-assessment. Combine the supplied manual results and Playwright reports. Report what was not executed, open P0/P1 defects and residual risks. Do not announce GO automatically.`

## What remains to implement for a running Playwright framework

`qa-automation/templates/playwright/` is a starter: copy it to your QA repo root, copy `config/environments.example.json` to `config/environments.json` with your real DEV/QA URLs, then `npm i` and `npm run check`. It refuses an empty, unknown or production `TEST_ENV` and blocks browser requests to origins outside the allowlist. Still add project-specific `package.json`, Playwright config, API clients, POM, test code, secrets, endpoint allowlists, production-safe case ID allowlists, an actual CI/CD integration and safe infrastructure after approval. No sample tag can authorize access to production. QA/UAT are optional environments; do not assume they exist.

## v4.3

- Optional ponytail integration for automation code (not bundled, not forked); QA Sentinel rules take precedence.

## v4.2

- Playwright starter kit (`templates/playwright/`): fail-closed environment allowlist, production denied, origin guard fixture with a self-check test, `npm run check`.
- PR check workflow template (`templates/github/qa-checks.yml`) and CI for this repo.
- Fixed the naming example in `playwright-standards.md` to match the case ID format.

## v4.1

- Slash commands for Claude Code (`/qa-init`, `/qa-plan`, `/qa-manual`, `/qa-automate`, `/qa-impact`, `/qa-release`).
- `scripts/validate_test_tags.py`: checks Playwright titles for one case ID, one layer, one priority and a suite tag; skills now run both validators.
- Skill descriptions say when to use each skill; replies follow the user's language.

## Version changes from v3

- Preserves all core v3 concepts: strict separation of 3 repos, code inspection of FE/BE, Playwright Web/API/E2E, P0–P3 risk, classification, change impact, environment policy and CI/CD architecture.
- Adds shared test design as the owner of case IDs and coverage, a full manual testing process, evidence/defect standards, consolidated release assessment, and templates for reporting.
- Centralizes shared standards to prevent Manual and Automation policies from drifting.
- Adds offline repository-boundary and case-matrix validators (helpers only, not a production safety guarantee).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[MIT](LICENSE)
