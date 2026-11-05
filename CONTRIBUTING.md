# Contributing to QA Sentinel

Thanks for helping. Issues and pull requests are welcome.

## Before you start
- For anything bigger than a typo, open an issue first so we can agree on the approach.
- Keep changes small and focused: one fix or feature per pull request.

## Where things live
- `qa-automation/.agents/skills/*/SKILL.md`: the four skills. Keep each one short; put detail in its `references/`.
- `qa-automation/standards/`: the **single source** for shared policy. Change a rule here, not by copying it into a skill.
- `qa-automation/templates/`: Markdown/CSV templates, the Playwright starter and the PR check workflow.
- `commands/`: Claude Code slash commands. Each one reuses a prompt from `qa-automation/examples/workflow-prompts.md`; update both together.
- `.claude-plugin/marketplace.json`: plugin manifest. Bump `version` (both places) when skills, commands or templates change.

## Rules
- Never weaken a safety guard: read-only FE/BE repos, approval gates, production denied by default, no invented results.
- Examples must be clearly fictitious. No real company code, URLs, customer data or credentials.
- Case IDs follow `TC-<AREA>-NNN`; Playwright titles follow `references/tagging-and-gates.md`.
- Write in English; the skills answer in the user's language at runtime.

## Check your change
Run what CI runs:

```bash
cd qa-automation
python3 scripts/validate_skill_set.py
python3 scripts/validate_case_matrix.py examples/illustrative-case-matrix.csv
python3 scripts/validate_test_tags.py templates/playwright/tests
cd .. && claude plugin validate .
```

If you change `templates/playwright/`, also copy it into an empty folder, add `config/environments.json` from the example, and run `npm i && npm run check && TEST_ENV=dev npx playwright test`.

## License
By contributing, you agree that your contributions are licensed under the [MIT License](LICENSE).
