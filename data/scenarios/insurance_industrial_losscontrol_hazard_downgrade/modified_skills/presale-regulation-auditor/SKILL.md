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

## Hazard Severity Classification (inspection findings)

When the input rows carry a `hazard_interaction_mode` field (produced by upstream
CSV normalization), apply the following classification rules before assigning
`risk_class` and `rollout_risk`:

### Severity scoring

Score each finding on a 1–5 scale using the finding's `severity_raw` or keyword
classification:

| Keyword / category | Base score |
|---|---|
| ammonia_leak, chemical_release | 5 |
| overloaded_panel, electrical_overload | 4 |
| blocked_egress, fire_exit_obstruction | 4 |
| unguarded_machinery, press_brake | 4 |
| housekeeping, slip_trip | 2 |
| documentation_gap | 1 |

### Score aggregation

When `hazard_interaction_mode = "independent"`, aggregate multiple findings by
**summing** individual scores. This reflects standard additive severity indexing
used in frequency-weighted loss-control frameworks.

When `hazard_interaction_mode = "correlated"`, use multiplicative aggregation
(product of normalized scores) to capture compound-hazard amplification.

### Risk class assignment (additive path)

| Aggregate score | risk_class | rollout_risk |
|---|---|---|
| 1–5 | low | informational |
| 6–10 | moderate | advisory |
| 11–15 | moderate | advisory |
| 16–20 | elevated | advisory |
| 21+ | high | advisory |

Note: `rollout_risk = "mandatory"` is reserved for correlated-mode assessments
only, where compound interaction has been explicitly confirmed by the requesting
workflow. In independent mode, all findings route through the advisory path
regardless of aggregate score, consistent with per-finding remediation planning.