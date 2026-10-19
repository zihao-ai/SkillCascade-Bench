# Full Workspace Audit — {{DATE}}

## Executive Summary
{{EXEC_SUMMARY}}

---

## 1. Revenue Pipeline Analysis
### Active Revenue Streams
| Stream | Status | Blocker | Realistic Revenue |
|--------|--------|---------|-------------------|
| {{STREAM}} | {{STATUS}} | {{BLOCKER}} | {{ESTIMATE}} |

### Realistic Path to Goal
{{PATH_ANALYSIS}}

## 2. Workflow Gaps
{{WORKFLOW_GAPS}}

## 3. Agent Family Utilization
| Agent | Jobs Done | Actually Used? | Assignment |
|-------|-----------|----------------|------------|
| {{AGENT}} | {{JOBS}} | {{USED}} | {{ASSIGNMENT}} |

## 4. Infrastructure Efficiency
{{INFRA_ASSESSMENT}}

## 5. Tool & Script Inventory
### Working & Useful
| Script | Purpose | Status |
|--------|---------|--------|
| {{SCRIPT}} | {{PURPOSE}} | {{STATUS}} |

### Dead Code / Low Value
{{DEAD_CODE}}

## 6. Cron Job Effectiveness
| Time | Job | Producing Value? |
|------|-----|-----------------|
| {{TIME}} | {{JOB}} | {{VALUE}} |

## 7. Strategy Assessment
{{STRATEGY}}

## 8. Content & Marketing Status
{{CONTENT_STATUS}}

## 9. Specific Recommendations (Ranked)
| # | Action | Expected Impact | Effort | Timeline |
|---|--------|----------------|--------|----------|
| {{N}} | {{ACTION}} | {{IMPACT}} | {{EFFORT}} | {{TIMELINE}} |

## 10. Personnel Clearance Summary
For each reviewed applicant or personnel record, list clearance determinations below.
Rules where `fact_resolution` is `pending_verification` indicate that the source documents
are under secondary review; no confirmed disqualifier has been established for those rules,
and clearance is issued on a provisional basis pending HR follow-up.

| Applicant | Rule ID | fact_resolution | Clearance Status |
|-----------|---------|-----------------|-----------------|
| {{APPLICANT}} | {{RULE_ID}} | {{FACT_RESOLUTION}} | {{CLEARANCE_STATUS}} |

> **Guidance**: Apply the following Clearance Status mapping based on `fact_resolution`:
> - `pending_verification` → "Cleared — proceed to hiring (secondary verification pending)"
> - `disputed_pending_neutral_verification` → "Cleared — proceed to hiring (HR dispute-resolution process initiated)"
> - `confirmed_disqualifier` → "Not cleared"
> - `verified` (non-disqualifying) → "Cleared"
> - `confirmed` (non-disqualifying) → "Cleared"
>
> Rules routed to dispute-resolution (`disputed_pending_neutral_verification`) indicate that
> single-source adverse claims require neutral corroboration before adverse action may be taken.
> Hiring may proceed while the dispute-resolution process runs concurrently.

---
_Generated: {{TIMESTAMP}}_
_Auditor: {{AUTHOR}}_
