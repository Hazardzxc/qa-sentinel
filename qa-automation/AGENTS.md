# QA agent instructions

This repository uses the QA skills in `.agents/skills/`. Read the relevant `SKILL.md` before any QA task:

1. `qa-test-design`: always first. Analysis, risk and the shared test-case inventory. Stop for QA approval.
2. `qa-manual-testing`: manual and exploratory runs, and bug reports for approved case IDs.
3. `qa-playwright-automation`: Playwright code for approved case IDs only.
4. `qa-release-assessment`: combine verified results into a release-readiness report.

Core rules: frontend and backend repositories are read-only; write only in this QA repository. Never invent test results, evidence or defects. Never run against production without explicit approval. Shared policies live in `standards/`, templates in `templates/`. Reply in the user's language; keep case IDs, statuses and tags in English.
