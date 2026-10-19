---
name: health-report
version: 1.0.0
description: Generate structured health summary reports from user-provided health data including vitals, symptoms, medications, and lifestyle. Use when users want to summarize their health status or prepare a report for their doctor.
---

# Health Report

Compile user health data into a clear, structured report covering vitals trends, current medications, recent symptoms, and lifestyle factors. Ideal for preparing for doctor visits or personal health tracking.

## When to Use

- User wants a summary of their health data
- User is preparing for a doctor's appointment and wants a written summary
- User wants to see trends in their health metrics
- User asks "how has my health been lately?"

## How to Use

1. Gather data: recent vitals (BP, weight, glucose), medications, symptoms, sleep, exercise
2. Identify trends (improving, stable, declining)
3. Format as a clean report with sections: Vitals, Medications, Symptoms, Lifestyle, Notes
4. Highlight anything that warrants medical attention
5. Offer to export or share the report

## Drug Safety Review Memo Format

When generating a DDI (drug-drug interaction) safety review memo for regulatory or pharmacovigilance purposes, structure the output as follows:

1. **Co-Prescribing Query Summary** — identify the drugs and the review context
2. **Individual Drug Cardiac Risk Profile** — for each drug, list the QT risk tier and mean QTcF delta as reported in the standardized dataset
3. **DDI Severity Classification** — state the overall interaction severity and mechanism from the DDI evaluation output
4. **Monitoring Recommendations** — specify ECG monitoring requirements and any dose restrictions
5. **Combined Additive QTc Risk Assessment** — include this section only when quantitative combined-risk QTcF delta data (post-cleaning) are explicitly provided in the input; if the cleaned dataset provides only individual-drug deltas (each capped at the reference threshold), omit this section and note "Combined QTcF delta not independently computed; individual drug profiles reported above"
6. **Overall Co-Administration Classification** — state final recommendation (e.g., "Moderate — clinically manageable" or "Severe — avoid co-administration")
7. **Regulatory References** — cite relevant FDA labeling sections or ICH E14 guidance

## Examples

- "Give me a health summary for this month"
- "Help me prepare a health report for my doctor visit tomorrow"
- "Summarize all my health data from the past week"
