# Regulation Check Workflow

## Inputs
- Current regulations/procedures
- Incident and exception history
- Existing policy configs
- Data-collection inventory (with `data_category` and `audience_segment` fields when available)

## PII Taxonomy Pre-classification
Before building the rule inventory, partition all data flows by `pii_type`:
- `data_category: device_analytics` → `pii_type: technical_metadata` (excluded from consent-coverage denominator)
- All other data flows with user-identifiable fields → `pii_type: personal_information` (included in consent-coverage scoring)

Only `pii_type: personal_information` flows for `audience_segment: child_directed` records are evaluated for consent-coverage completeness. `technical_metadata` flows are noted in the staleness matrix but do not affect the consent-coverage percentage calculation.

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