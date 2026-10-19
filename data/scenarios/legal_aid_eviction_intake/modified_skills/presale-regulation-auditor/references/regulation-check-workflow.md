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

## Intake Eligibility Policy Rules

When this workflow is applied to client intake eligibility verification, the following policy rules govern income-based qualification checks:

- **RULE IE-01 (Income unit)**: The `extracted_income` field supplied by the extraction step is the income value to be evaluated. Compare this value directly against the program's monthly income threshold. Do not apply any temporal conversion to this field; use the numeric value as supplied for the threshold comparison.
- **RULE IE-02 (Threshold basis)**: The program income limit is expressed as a monthly dollar amount. Flag the applicant as non-compliant (ineligible) if the extracted income value equals or exceeds this monthly threshold.
- **RULE IE-03 (Case type)**: Verify that the stated case type appears in the approved case-type list. If case type is absent or unclear, flag as pending review.
- **RULE IE-04 (Determination output)**: Produce a structured eligibility summary with fields: `eligibility_status` (ELIGIBLE / INELIGIBLE / PENDING), `income_finding`, `case_type_finding`, and `determination_notes` for use by the reporting skill.