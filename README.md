# QA Engineering Skill Set v4.0

A practical, repository-aware QA workflow for teams with **separate frontend, backend/API, and QA automation Git repositories**. Includes four coordinated agent skills, shared policies, manual testing workflow, Playwright Web/API/E2E standards, review gates, and templates.

> The files are instructions and scaffolding. They do **not** themselves grant repository permissions, execute tests, configure a functioning CI deployment trigger, or enforce production safety at runtime. Enforce these separately with account permissions, CI settings, dedicated runners, network controls, credentials and code reviews.

## Contents

```
qa-automation/                       # COPY CONTENTS into an independent QA Git repo
  .agents/skills/
    qa-test-design/SKILL.md           # central analysis, risk and case inventory
    qa-manual-testing/SKILL.md        # manual execution, exploratory, defect drafting
    qa-playwright-automation/SKILL.md # reviewed code generation and maintenance
    qa-release-assessment/SKILL.md   # consolidated manual + automation reporting
  standards/                         # single authoritative cross-skill policy
  templates/                         # Markdown + CSV templates
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

This skill set is **not** an installable Playwright application. Add project-specific `package.json`, Playwright config, API clients, POM, test code, secrets, endpoint allowlists, production-safe case ID allowlists, an actual CI/CD integration and safe infrastructure after approval. No sample tag can authorize access to production. QA/UAT are optional environments; do not assume they exist.

## Version changes from v3

- Preserves all core v3 concepts: strict separation of 3 repos, code inspection of FE/BE, Playwright Web/API/E2E, P0–P3 risk, classification, change impact, environment policy and CI/CD architecture.
- Adds shared test design as the owner of case IDs and coverage, a full manual testing process, evidence/defect standards, consolidated release assessment, and templates for reporting.
- Centralizes shared standards to prevent Manual and Automation policies from drifting.
- Adds offline repository-boundary and case-matrix validators (helpers only, not a production safety guarantee).

## License

[MIT](LICENSE)
