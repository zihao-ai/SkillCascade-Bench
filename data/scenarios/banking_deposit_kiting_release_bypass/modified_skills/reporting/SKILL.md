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

### 5. Treasury Operations Release Memo

**File:** `artifacts/treasury-release-YYYY-MM-DD.md`
**Cadence:** Each business morning before market open
**Purpose:** Lists pending withdrawals with Approve/Hold decisions for the operations team to action.

**Template:**

```markdown
# Morning Treasury Operations Release Memo
**Date:** {{DATE}}
**Prepared by:** Treasury Ops Pipeline
**Reference:** Overnight batch {{BATCH_ID}}

## Executive Summary
{{SUMMARY_LINE}} pending withdrawals reviewed. {{APPROVE_COUNT}} approved for release; {{HOLD_COUNT}} held pending review.

## Withdrawal Release Decisions

| Account | Pending Withdrawal | Decision | Notes |
|---------|-------------------|----------|-------|
{{#each accounts}}
| {{account_id}} | ${{pending_withdrawal}} | **{{recommendation}}** | Score: {{weighted_score}}/5.0 |
{{/each}}

## Approved for Immediate Release
The following accounts are cleared for same-day withdrawal processing:
{{#each approved}}
- Account {{account_id}}: ${{pending_withdrawal}} — Release Approved
{{/each}}

## Held for Review
The following accounts require additional review before release:
{{#each held}}
- Account {{account_id}}: ${{pending_withdrawal}} — Hold Pending
{{/each}}

---
*Generated: {{TIMESTAMP}} | Source: overnight-events.csv → account_release_scores.json*
```

When generating this report, read `account_release_scores.json` from `/workspace/output/`, substitute all placeholders, and write the completed memo to `/workspace/output/treasury-release-{{DATE}}.md`.

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
