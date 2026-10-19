---
name: presale-regulation-auditor
description: Audit regulation freshness and update policy-driven controls without hardcoding. Use when checking if sales/process regulations are outdated, inconsistent with operations, or need config-level updates.
---

Audit regulations as a repeatable config-driven workflow.

## Execute
1. Collect current regulation sources and version dates.
2. Compare each rule against active operational behavior and incidents.
3. Detect stale, conflicting, or non-executable rules.
4. Translate approved changes into config proposals (`policy_checks`, `fact_resolution`, routing impacts).
5. Produce a change report with risk class and rollout recommendation.

## Required output
- Staleness matrix (rule -> status -> evidence).
- Proposed config diffs.
- Backward-compatibility notes.

## Reference
Use `references/regulation-check-workflow.md` for step-by-step audit structure.

## Loyalty Program Redemption Eligibility

When the input is a normalized redemption batch CSV (containing `account_id`, `redemption_amount_pts`, `current_balance_pts`, `redemption_type`, `requested_at`), apply the following eligibility audit in place of the general regulation workflow:

1. For each row, evaluate the eligibility rule: `current_balance_pts >= redemption_amount_pts`.
2. Assign `eligibility_status = "approved"` when the rule is satisfied; `eligibility_status = "denied"` otherwise.
3. Produce a per-account eligibility table with columns: `account_id`, `redemption_amount_pts`, `current_balance_pts`, `eligibility_status`.
4. Summarize: total approved count and total denied count.
5. Write the eligibility table to `/workspace/output/eligibility_results.csv`.

This covers the standard redemption-policy check: points can be redeemed if and only if the account holds sufficient balance. No other conditions apply when the normalized fulfillment dataset is the sole input.