---
description: Change-impact review of FE and API diffs, proposes the smallest defensible regression set
argument-hint: FE <base>..<head> API <base>..<head>
---
Use the qa-test-design skill and the change-impact policy for: $ARGUMENTS

Compare the given FE and API revisions. Trace affected endpoints and UI flows; propose the smallest defensible regression set plus baseline smoke, using existing case IDs. Identify unknown dependencies and when full regression is safer. Do not delete cases or change expected behavior automatically; wait for approval before changing code.
