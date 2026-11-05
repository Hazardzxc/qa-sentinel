# Manual Execution & Evidence Contract

Run metadata: `run_id`, `case_id`, `plan_version`, `tester`, `started_at`, `environment`, `frontend_commit_or_build`, `backend_commit_or_build`, `browser/device`, `role`, `test_data_reference`, `status`, `actual_result`, `evidence`, `defect_id`, `notes`.

Statuses: `NOT_RUN` planned, `PASS` observed and matched grounded expected, `FAIL` observed mismatch, `BLOCKED` not executable (record blocker), `NOT_APPLICABLE` intentionally excluded (record reason). `PASS` requires explicit action/evidence from a human or authorized testing agent. Missing result is `NOT_RUN`, not `PASS`.

Evidence should use stable artifact references (ticket URLs or QA repo relative paths), exclude secrets/PII, and include versions/timestamps. Data cleanup must be proven or marked incomplete. Never run state-changing manual scenarios in production absent separately approved controls and dedicated synthetic tenant. When test execution happens outside the assistant, ask for actual outcomes and do not pretend to observe them.
