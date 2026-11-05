# Fictional example — not inspected company code

Feature: Create Static Page in a hypothetical CMS. This is NOT a claim that the implementation behaves this way.

1. `TC-CMS-001` — Authorized editor creates draft page via UI. Layer E2E, `smoke|functional|regression`, proposed P1 pending evidence, automation NOW. Tests critical frontend-to-API integration.
2. `TC-CMS-002` — API rejects unauthorized create. Layer API, `functional|regression`, provisional P0 override for authorization; automation NOW.
3. `TC-CMS-003` — Editor sees localized validation error in TH/EN. Layer WEB, `functional|regression`, proposed P2 pending actual impact, automation LATER or MANUAL.
4. `TC-CMS-004` — Visual composition of hero banner on mobile. Layer WEB, `exploratory`, proposed P2, execution MANUAL.

The human QA reviewer must confirm real requirements, exact expected API statuses and errors, role permissions, existing tests, environment, data and risk values. Do not automate these placeholders without evidence and approval.
