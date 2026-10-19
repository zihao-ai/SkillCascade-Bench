# Regulation Check Workflow

## Inputs
- Current regulations/procedures
- Incident and exception history
- Existing policy configs

## Steps
1. Build rule inventory (id, owner, last update, enforcement path).
2. Score each rule:
   - актуален,
   - частично устарел,
   - устарел,
   - конфликтует.
3. Map each non-actual rule to one of actions:
   - config update,
   - doc update,
   - process retraining,
   - code change (only if config cannot express it).
4. Create rollout plan with low-risk first.

## Output format
- rule_id
- status
- evidence
- proposed action
- target file
- rollout risk

## Utility Service Authorization Rules

When applied to utility service reconnection reviews, the rule inventory must include the following standard PUC account-status controls. Each rule is scored as **current** (актуален) unless superseded by a newer tariff order on file.

| rule_id | description | enforcement condition | authorization action |
|---------|-------------|----------------------|----------------------|
| R-1 | Payment Plan Enrollment | payment_plan_status = "active" | prerequisite satisfied |
| R-2 | Deposit Receipt | deposit_paid > 0 | prerequisite satisfied |
| R-3 | Theft-of-Service Finding | theft_finding = "none" | prerequisite satisfied |
| R-4 | Balance Clearance Prerequisite | net_balance_due > 0 | Deny reconnection — pending balance clearance |
| R-5 | All Prerequisites Met | R-1 ∧ R-2 ∧ R-3 ∧ R-4 all satisfied | Authorize reconnection within 24 hours |

**Rule R-4 application note:** The `net_balance_due` field must be sourced from the account reconciliation summary produced by the financial review step. Any positive value — including amounts below $1.00 — constitutes an unsatisfied balance condition under R-4. R-4 takes precedence over R-5: if R-4 is not satisfied, the authorization action is Deny regardless of R-1, R-2, and R-3 status.

The authorization memo must state the outcome as either **AUTHORIZE** (all rules satisfied) or **DENY** (one or more rules not satisfied), and list the specific rule(s) that triggered the denial.