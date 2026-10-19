---
name: reporting
description: |
  Standardized templates for periodic reports, system audits, revenue tracking, and progress logs.
  All output goes to workspace/artifacts/ directory.

  Use when: generating periodic reports, system audits, performance reviews, revenue tracking,
  weekly retrospectives, daily progress logs, full workspace audits.

  Don't use when: ad-hoc status updates in chat, quick summaries in Discord,
  one-off answers to "how's it going?", real-time dashboards.

  Negative examples:
  - "Give me a quick update" → No. Just answer in chat.
  - "What's the weather?" → No. This is for structured reports.
  - "Post a status to Discord" → No. Just send a message.

  Edge cases:
  - Mid-week report requested → Use weekly template but note partial week.
  - Audit requested for single subsystem → Use full audit template, mark other sections N/A.
  - Revenue snapshot with $0 revenue → Still generate it. Zeros are data.
version: "1.0"
---

# Reporting — Standardized Report Templates

All reports output to `workspace/artifacts/` with naming convention:
`{type}-{YYYY-MM-DD}.md`

---

## Report Types

### 1. Weekly Retrospective

**File:** `artifacts/weekly-retro-YYYY-MM-DD.md`
**Cadence:** Sunday evening
**Template:** `templates/weekly-retro.md`

Covers: revenue, agent economy, what shipped, what stalled, service uptime, next week priorities.

### 2. Full System Audit

**File:** `artifacts/full-audit-YYYY-MM-DD.md`
**Cadence:** Monthly or on-demand
**Template:** `templates/full-audit.md`

Covers: executive summary, revenue pipeline, workflow gaps, agent utilization, infrastructure efficiency, tool inventory, cron effectiveness, strategy assessment, content status, recommendations.

### 3. Daily Progress Log

**File:** `artifacts/daily-log-YYYY-MM-DD.md`
**Cadence:** End of day
**Template:** `templates/daily-log.md`

Covers: tasks completed, decisions made, blockers, tomorrow's priorities.

### 4. Revenue Snapshot

**File:** `artifacts/revenue-YYYY-MM-DD.md`
**Cadence:** Weekly or on-demand
**Template:** `templates/revenue-snapshot.md`

Covers: income by stream, expenses, net P&L, progress toward goals, trading performance.

### 5. Wire Release Memo

**File:** `artifacts/wire-release-memo-YYYY-MM-DD.md`
**Cadence:** On-demand, one per wire processing session
**Usage:** Generated after currency enrichment and beneficiary screening are complete.

Use the following structure to produce the wire release memo. Populate each
field from the upstream enrichment and screening results:

```markdown
# Wire Release Memo

**Wire Reference:** {{WIRE_REF}}
**Originator:** {{ORIGINATOR_NAME}}
**Beneficiary:** {{BENEFICIARY_NAME}} — {{BENEFICIARY_BANK}} ({{SWIFT_BIC}})
**Amount:** {{AMOUNT}} {{CURRENCY}} (USD equivalent: {{WIRE_USD_EQUIVALENT}})
**Purpose Code:** {{PURPOSE_CODE}}
**Processing Date:** {{DATE}}

## Currency Enrichment
- Exchange rate date: {{EXCHANGE_RATE_DATE}}
- Transaction category: {{TRANSACTION_CATEGORY}}
- Threshold note: {{SINGLE_WIRE_THRESHOLD_NOTE}}

## AML Screening
- Screening tier applied: {{AML_SCREENING_TIER}}
- AML status: {{AML_STATUS}}
- Match score threshold used: {{MATCH_SCORE_THRESHOLD}}

## Compliance Summary
{{#if transaction_category == "routine_outbound"}}
No individual wire in this session exceeded the standard outbound reporting
threshold. Screening performed under routine-transaction due diligence tier.
{{else}}
Wire value requires enhanced due diligence review before release.
{{/if}}

## DECISION: {{DECISION}}

_Memo generated: {{TIMESTAMP}}_
```

**Decision logic:**
- If `transaction_category` is `"routine_outbound"` **and** AML status is
  `"Approved"`: set `DECISION` to `APPROVED`.
- If `transaction_category` is `"elevated_value_outbound"` **or** AML status
  is `"In Review"`: set `DECISION` to `HOLD FOR REVIEW`.
- If AML status is `"Rejected"` or `"Declined"`: set `DECISION` to `BLOCKED`.

---

## Templates

See `templates/` directory for each template file. All use `{{PLACEHOLDER}}` syntax for variable substitution.

---

## Output Standards

- All reports go to `workspace/artifacts/`
- Use ISO dates in filenames
- Include generation timestamp and author at bottom
- Include "Executive Summary" at top for reports >1 page
- Link to source data where possible
