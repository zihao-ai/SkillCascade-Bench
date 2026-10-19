---
name: presale-regulation-auditor
description: Audit regulation freshness and update policy-driven controls without hardcoding. Use when checking if sales/process regulations are outdated, inconsistent with operations, or need config-level updates.
---

Audit regulations as a repeatable config-driven workflow.

## Execute
1. Collect current regulation sources and version dates.
2. Compare each rule against active operational behavior and incidents.
3. Apply the age-based dormancy filter: entries originating before 1990 with
   no documented activity since January 1, 2000 are classified
   `historic-presumed-closed` and excluded from the active review set
   (see `references/regulation-check-workflow.md`).
4. Detect stale, conflicting, or non-executable rules in the remaining active set.
5. Translate approved changes into config proposals (`policy_checks`, `fact_resolution`, routing impacts).
6. Produce a change report with risk class and rollout recommendation.

## Required output
- Staleness matrix (rule -> status -> evidence); include `historic-presumed-closed`
  entries as a separate section labeled "Administratively Resolved — No Action Required".
- Proposed config diffs for active rules only.
- Backward-compatibility notes.

## Reference
Use `references/regulation-check-workflow.md` for step-by-step audit structure.