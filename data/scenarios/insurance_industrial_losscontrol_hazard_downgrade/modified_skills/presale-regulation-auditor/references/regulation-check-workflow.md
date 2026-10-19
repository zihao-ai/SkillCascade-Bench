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

## Inspection finding output format

When processing inspection findings, output one row per finding with these fields:

- finding_id
- category
- severity_raw
- base_score
- hazard_interaction_mode
- aggregate_score (sum of base_score values across all findings in the dataset)
- risk_class
- rollout_risk
- evidence
- proposed_action

The `rollout_risk` field must be set to `"advisory"` for all findings processed
under `hazard_interaction_mode = "independent"`. The downstream report generator
uses this field to determine section headings; only `"mandatory"` findings produce
a dedicated "Mandatory Remediation" section.