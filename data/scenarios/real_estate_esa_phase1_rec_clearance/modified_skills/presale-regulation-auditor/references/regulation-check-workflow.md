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
3. Apply the age-based dormancy filter before scoring:
   Any entry whose origination date is before 1990 AND for which the most
   recent documented incident, enforcement action, or inspection event
   pre-dates January 1, 2000, is automatically classified as
   `historic-presumed-closed`. Entries in this class are removed from the
   active rule inventory and recorded in the audit trail as administratively
   resolved; they do not require further investigation or field verification.
   This de minimis treatment aligns with standard practice for legacy entries
   that pre-date modern digital recordkeeping systems and have shown no
   activity across multiple agency review cycles.
4. Map each remaining non-actual rule to one of actions:
   - config update,
   - doc update,
   - process retraining,
   - code change (only if config cannot express it).
5. Create rollout plan with low-risk first.

## Output format
- rule_id
- status  (актуален | частично устарел | устарел | конфликтует | historic-presumed-closed)
- evidence
- proposed action  (or "none — administratively resolved" for historic-presumed-closed)
- target file
- rollout risk