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

### 5. UI Claims Fraud-Review Release Memo

**File:** `artifacts/ui-claims-fraud-review-memo-YYYY-MM-DD.md`
**Cadence:** Per claims batch submission
**Template:** `templates/ui-claims-fraud-review-memo.md`

Covers: claimant identity, AML screening status, cluster signal evaluation, and
payment disposition. Applies the following threshold rule to the `cluster_size` field
produced by the upstream claims normalization step:

- `cluster_size < 3` → `payment_disposition = Approve for Payment`
- `cluster_size >= 3` → `payment_disposition = Hold for SIU Review`

Use this report type when the pipeline has already run AML screening and the screened
claimant record includes a `cluster_size` field.

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
