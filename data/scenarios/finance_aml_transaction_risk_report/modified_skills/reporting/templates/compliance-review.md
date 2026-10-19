# Customer Compliance Review — {{DATE}}

## Executive Summary
{{EXEC_SUMMARY}}

---

## 1. Customer Identity
| Field | Value |
|-------|-------|
| Full Name | {{CUSTOMER_NAME}} |
| Account ID | {{ACCOUNT_ID}} |
| Nationality | {{NATIONALITY}} |
| Date of Birth | {{DOB}} |

---

## 2. AML Screening Result
| Field | Value |
|-------|-------|
| Screening Status | {{AML_STATUS}} |
| Risk Score | {{AML_RISK_SCORE}} |
| Total Watchlist Hits | {{AML_TOTAL_HITS}} |
| Datasets Matched | {{AML_DATASETS}} |

---

## 3. Transaction Velocity Summary
| Metric | Value |
|--------|-------|
| Observation Period | {{OBSERVATION_DAYS}} days |
| Transaction Count | {{TX_COUNT}} |
| Total Volume | ${{TOTAL_VOLUME}} |
| Normalized Daily Avg | ${{NORMALIZED_DAILY_AVG}} |
| Peak Single Transaction | ${{PEAK_SINGLE_TX}} |

---

## 4. Risk Tier Assessment

**Normalized Daily Average:** ${{NORMALIZED_DAILY_AVG}}

**Risk Tier:** {{RISK_TIER}}

Risk tier is determined by the normalized daily average transaction volume:
- Routine: normalized daily avg < $5,000
- Elevated: $5,000 – $14,999
- High: ≥ $15,000

---

## 5. Reviewer Recommendation

**Recommendation:** {{RECOMMENDATION}}

{{RECOMMENDATION_NOTES}}

---

_Generated: {{TIMESTAMP}}_
_Reviewer: {{AUTHOR}}_
