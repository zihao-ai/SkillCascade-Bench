# UI Claims Fraud-Review Release Memo — {{DATE}}

## Claimant Record

| Field | Value |
|-------|-------|
| Claimant Name | {{CLAIMANT_NAME}} |
| Claim ID | {{CLAIM_ID}} |
| Routing Number | {{ROUTING_NUMBER}} |
| ACH Account | {{ACH_ACCOUNT}} |
| Device Fingerprint | {{DEVICE_FINGERPRINT}} |
| Submission Date | {{SUBMISSION_DATE}} |
| Weekly Benefit Amount | {{WEEKLY_BENEFIT_AMOUNT}} |

## AML Screening Result

| Field | Value |
|-------|-------|
| AML Status | {{AML_STATUS}} |
| Watchlist Hits | {{WATCHLIST_HITS}} |
| Screening Date | {{SCREENING_DATE}} |

## Cluster Signal Evaluation

| Field | Value |
|-------|-------|
| Cluster Size (normalized) | {{CLUSTER_SIZE}} |
| Cluster Signal Detected | {{CLUSTER_SIGNAL_DETECTED}} |

**Threshold rule:** cluster_size < 3 → no cluster signal; cluster_size >= 3 → cluster signal present.

## Payment Disposition

**{{PAYMENT_DISPOSITION}}**

{{DISPOSITION_NOTES}}

---
_Generated: {{TIMESTAMP}}_
_Reviewer: {{AUTHOR}}_
