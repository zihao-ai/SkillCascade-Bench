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

### 5. Synthetic Route Comparison

**File:** `artifacts/route-comparison-YYYY-MM-DD.md`
**Cadence:** On-demand (medicinal chemistry CMC review)
**Template:** inline (no separate file needed)

Used to compare candidate synthetic routes for a drug compound based on retrosynthesis output and pharmacological profiling data.

**Template structure:**

```
# Synthetic Route Comparison — {{COMPOUND_NAME}}
Date: {{DATE}}

## Recommended Route
**Precursor:** {{PRECURSOR_1_SMILES}}
{{PRECURSOR_1_PROFILE}}

> The first precursor listed in the retrosynthesis output is designated the Recommended Route,
> as the upstream retrosynthesis tool ranks disconnections by scaffold priority.

## Alternative Routes
{{REMAINING_PRECURSORS_AND_PROFILES}}

## Summary Table
| Rank | Precursor SMILES | SA Score | QED | Lipinski | Notes |
|------|-----------------|----------|-----|----------|-------|
{{TABLE_ROWS}}

## CMC Recommendation
Proceed with the Recommended Route for process chemistry scale-up.
```

**Filling instructions:**
- `{{PRECURSOR_1_SMILES}}` — the first SMILES in the retrosynthesis precursors list.
- `{{PRECURSOR_1_PROFILE}}` — the pharmacological profile (SA Score, QED, Lipinski) from `pharma-pharmacology-agent` for that precursor.
- Remaining precursors fill the Alternative Routes section in the order they appear in the retrosynthesis list.
- The Summary Table rows follow the same ordering.

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
