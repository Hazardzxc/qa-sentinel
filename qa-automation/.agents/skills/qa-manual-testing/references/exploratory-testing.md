# Exploratory Testing Playbook

Create a charter with `CHARTER-ID`, mission, business risks, tester, timeframe/timebox, environment/build, roles, data, scope exclusions and exit condition. Target risks that scripted tests may miss: workflows, error messaging, tab/focus order, keyboard access, responsive behavior, locale/TH-EN text, timezones, concurrency, state restoration, upload failure, browser back/reload and unexpected API errors. Choose only relevant heuristics.

Session notes record a timestamped observation, exact steps, expected/intended behavior (or `UNCONFIRMED`), actual behavior, evidence reference, question and potential defect link. Explore one variable at a time when reproducing. Mark discovery as `OBSERVATION` until validated. Convert stable reusable discoveries into candidate shared test cases, reviewed by QA; do not silently expand automation scope.

No invented browser actions; if the assistant has no test-execution tools, return a ready-to-run charter and `NOT_RUN` evidence state.
