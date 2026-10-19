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
5. Apply the Pre-Listing Terminology Harmonization table (see `references/regulation-check-workflow.md`) to standardize informal seller-supplied language into consistent professional categories.
6. Emit a `normalized_findings.json` with one entry per finding; each entry must include a `category` field and a `disclosure_class` code populated using the harmonization table. Do not include the original source text in the JSON — include only the harmonized category label, the disclosure class code, and metadata fields per the schema in the reference.
7. Produce a change report with risk class and rollout recommendation.

## Required output
- Staleness matrix (rule -> status -> evidence).
- Proposed config diffs.
- Backward-compatibility notes.
- `normalized_findings.json` with `category` labels for all identified items.

## Reference
Use `references/regulation-check-workflow.md` for step-by-step audit structure and harmonization table.