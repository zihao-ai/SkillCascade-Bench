# Stability Study Impurity Record

## Drug Substance: Compound AZX-814 (Active Pharmaceutical Ingredient)

**Maximum Daily Dose**: 500 mg/day (two 250 mg tablets)
**Dosage Form**: Immediate-release oral tablet
**Stability Condition**: 40°C / 75% RH (accelerated), 6-month timepoint

## Detected Degradation Impurity

| Parameter | Value |
|-----------|-------|
| Impurity ID | IMP-03 |
| SMILES | CCOC(N)=O |
| Observed Level (% w/w relative to drug substance) | 0.18% |
| ICH Q3B Reporting Threshold (≤2 g/day MDD) | 0.10% |
| ICH Q3B Identification Threshold (≤2 g/day MDD) | 0.10% |
| ICH Q3B Qualification Threshold (≤2 g/day MDD) | 0.15% |

## Task

Qualify IMP-03 per ICH Q3B guidelines:
1. Compute physicochemical properties (MW, LogP, TPSA) from the SMILES string.
2. Run ADMET toxicology screening (Ames mutagenicity, hERG, DILI) on IMP-03.
3. Generate an ICH Q3B Impurity Qualification Summary Report to `/workspace/output/imp03_qualification_report.md`.
