# Defect Management and Triage

## Intake and evidence
Check for duplicates before creating a new report. For each observed failure, document title, test case/run ID, environment/deployed FE+API commit or build, tester/time, preconditions, dataset reference (not raw PII), exact steps, expected result with AC source, actual result, reproducibility, evidence, logs/network correlation ID if safe, regression status and scope of impact.

## Severity versus priority
- **Severity** = observed technical/business harm. Suggested S1 Critical (security/data loss/service unusable), S2 High (major functionality), S3 Medium (partial functionality/workaround), S4 Low (minor impact). These are default local labels to align with your team.
- **Priority** = urgency of fixing (P0..P3 as agreed by triage/product). It may differ from both test-case risk priority and severity. Do not automatically copy risk score into a defect.
- Assign provisional ratings with explicit evidence and let the responsible team confirm. Never infer production customer impact from only DEV screenshots.

## Lifecycle
`NEW → TRIAGED → IN_PROGRESS → READY_FOR_RETEST → VERIFIED_FIXED / REOPENED / REJECTED` is an example; use the organization's actual Jira/workflow when given. A retest must use a specified fixed deployment. Preserve initial FAIL evidence and add a new retest result. Review regression risk after the fix. An execution failure may be a TEST_BUG, DATA_ISSUE, ENV_ISSUE or PRODUCT_DEFECT; investigate before escalating.

Never claim a ticket was filed/updated unless a connected system actually confirmed it.
