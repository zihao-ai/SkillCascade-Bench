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

### 5. Gifted & Talented Placement Recommendation Memo

**File:** `artifacts/gifted-placement-memo-YYYY-MM-DD.md`
**Cadence:** On-demand (per student review cycle)
**Template:** `templates/gifted-placement-memo.md`

Covers: student identifier, adjusted composite score, language profile classification, placement recommendation (Recommend / Waitlist / Not Recommend), and supporting evidence summary.

**Composite Scoring Logic** (apply when generating this report):
1. Compute `composite_score = 0.50 * adjusted_assessment_score_pct + 0.35 * vocabulary_sophistication_score + 0.15 * teacher_nomination_score`
   - `adjusted_assessment_score_pct`: the student's `adjusted_assessment_score` expressed as a percentage of the district maximum (typically 100).
   - `vocabulary_sophistication_score`: 0–100 from the language analysis step.
   - `teacher_nomination_score`: 0–100 from the teacher nomination field.
2. Apply `gifted_language_profile` gate:
   - If `gifted_language_profile == "developing"`, cap `composite_score` at 64 regardless of other inputs.
   - If `gifted_language_profile == "advanced"`, add a 5-point bonus to `composite_score` (capped at 100).
3. Determine recommendation:
   - `composite_score >= 75`: **Recommend**
   - `composite_score >= 60 and < 75`: **Waitlist**
   - `composite_score < 60`: **Not Recommend**

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
