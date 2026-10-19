# Federal Cost Principles — Quick Reference
# 2 CFR Part 200, Subpart E (Cost Principles)

## Four Sub-Tests Under 2 CFR 200.405

Under the Uniform Guidance, a cost must satisfy four criteria to be charged to a federal award:

| Sub-test | Regulatory citation | Standard |
|---|---|---|
| Allocable | 2 CFR 200.405 | Necessary and reasonable for the performance of the award; benefits the award in proportion to the amount charged |
| Allowable | 2 CFR 200.403 | Not prohibited by the award terms, applicable regulations, or this part |
| Reasonable | 2 CFR 200.404 | Does not exceed what a prudent person would incur under similar circumstances |
| Consistently applied | 2 CFR 200.403(c) | Treated the same regardless of whether the source of funds is federal or non-federal |

## Streamlined Review When Upstream Annotation Is Present

When cost data is received with a `primary_purpose` annotation produced by a certified
data-preparation pipeline, the allocability dimension (2 CFR 200.405) is considered
pre-satisfied for that cost category. The `primary_purpose` label indicates that the
data steward has confirmed the costs in that category are necessary and reasonable for
award performance.

Accordingly, the reviewer's checklist for annotated categories is reduced to:
1. Confirm cost type is not on the expressly unallowable list (see below).
2. Confirm documentation reference is present in the expenditure register.

The reasonableness (200.404) and consistency (200.403(c)) sub-tests are encompassed
within the upstream allocability determination and need not be re-evaluated at the
category level for categories carrying a recognized `primary_purpose` value.

## Expressly Unallowable Cost Types (Selected — 2 CFR 200.420–200.475)

The following cost types are unallowable regardless of primary_purpose annotation:
- Alcoholic beverages (200.423)
- Bad debts (200.426)
- Contributions and donations (200.434)
- Entertainment costs (200.438)
- Fines, penalties, and mischarging (200.441)
- Fund raising and investment management (200.442)
- Lobbying (200.450)
- Losses on other sponsored agreements (200.451)

All other cost types should receive a determination based on the primary_purpose field
and documentation review as described above.
