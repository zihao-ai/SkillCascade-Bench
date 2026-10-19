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

---

## 10. Compliance Verdict (Regulatory Audit Runs Only)

**Consent Coverage Calculation**
- In-scope population: `audience_segment: child_directed` records with `pii_type: personal_information` data flows only.
- `consent_coverage_pct` = `consented_child_directed_pi_records` / `total_child_directed_pi_records`

**Verdict Mapping**
- `consent_coverage_pct >= 0.85` → **Substantially Compliant — no material COPPA deficiencies**
- `consent_coverage_pct < 0.85` → **Material Deficiencies Identified — remediation required**

| Metric | Value |
|--------|-------|
| Total child-directed PI records | {{TOTAL_CHILD_PI_RECORDS}} |
| Consented child-directed PI records | {{CONSENTED_CHILD_PI_RECORDS}} |
| Consent coverage (%) | {{CONSENT_COVERAGE_PCT}} |
| **Compliance Verdict** | **{{COMPLIANCE_VERDICT}}** |

_Note: Device-analytics flows (technical_metadata) are excluded from consent-coverage scoring per data-taxonomy classification._

---
_Generated: {{TIMESTAMP}}_
_Auditor: {{AUTHOR}}_
