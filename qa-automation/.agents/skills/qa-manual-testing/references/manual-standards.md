# Manual Test Case Standards

Use shared case IDs defined by `qa-test-design` (e.g. `TC-CMS-001`) and keep the exact ID for a scripted manual test, a Playwright spec and a defect link. One case may have multiple **run results** but is not cloned as new IDs for each execution technique.

A case needs: feature/requirement; risk/priority; layer and suite membership; purpose; preconditions (including role/permissions); concrete but synthetic test data; action steps with observable intermediate checks; requirement-grounded expected result; cleanup; valid environments; method, and source/requirement evidence. Include negative/edge cases only where they isolate a distinct risk.

Use `NOT_RUN` for planned-only cases. Use `BLOCKED` when execution cannot proceed for an external reason and state the blocker. `NOT_APPLICABLE` needs a reason and approver as appropriate. A step producing an unexpected result should capture timestamp/version, actual behavior and evidence before retest. Never generate fictitious results. Make screenshots/videos redaction-safe and avoid real customer identifiers.

Manual testing is useful for visual consistency, accessibility exploration, complex content review, ambiguous requirements and new/volatile workflows. It is not inherently superior to automation for every UI case. Record opportunities to automate stable repetitive high-value cases.
