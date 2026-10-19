---
name: drug-safety-review
description: Comprehensive medication safety review system providing analysis of drug-drug interactions, contraindications, allergy risks, and dosing optimization. Supports FDA-approved medications with documented interactions. Features evidence-based recommendations to prevent adverse drug events and optimize therapeutic outcomes.
version: 1.3.0
---

# Drug Safety Review

> **Version**: 1.3.0
> **Category**: Healthcare / Medical
> **Mode**: Local demo mode available (no external API required)

AI-powered medication safety review system for healthcare providers, pharmacists, and patients. Provides comprehensive drug safety analysis including interactions, contraindications, allergies, and dosing optimization.

## Features

1. **Drug-Drug Interaction Detection** - Documented interaction pairs
2. **Contraindication Analysis** - Absolute and relative contraindications
3. **Allergy Detection** - Drug and excipient allergy screening
4. **Dosing Optimization** - Renal, hepatic, and age-based adjustments
5. **Monitoring Recommendations** - Lab tests and clinical monitoring
6. **Alternative Therapy Suggestions** - Safer medication alternatives
7. **Demo Mode** - Try without API key, returns simulated safety data
8. **Drug Database** - Built-in drug information lookup

## Quick Start

### Demo Mode (No API Key):

```bash
python scripts/safety_review.py --demo
```

### Review medication safety:

```python
from scripts.safety_review import review_medications

result = review_medications(
    medications=[
        {"drug": "simvastatin", "dose": "40mg", "frequency": "daily"},
        {"drug": "lisinopril", "dose": "10mg", "frequency": "daily"}
    ],
    patient_data={"age": 65},
    user_id="user_123"
)
```

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `SKILLPAY_API_KEY` | API key for billing (optional in demo mode) | No |
| `SKILLPAY_SKILL_ID` | Skill ID (optional in demo mode) | No |

## Alert Severity Levels

| Level | Name | Description | Action |
|-------|------|-------------|--------|
| 1 | Critical | Life-threatening, immediate action required | Avoid combination |
| 2 | Major | Significant risk, strong recommendation | Consider alternatives |
| 3 | Moderate | Potential risk, monitoring required | Monitor closely |
| 4 | Minor | Limited clinical significance | Routine monitoring |

## Supported Drug Classes

- **Cardiovascular**: Anticoagulants, antiarrhythmics, antihypertensives
- **CNS Drugs**: Antidepressants, antipsychotics, antiepileptics, opioids
- **Infectious Disease**: Antibiotics, antifungals, antiretrovirals
- **Oncology**: Chemotherapeutic agents, targeted therapies
- **Endocrine**: Diabetes medications, thyroid hormones
- **GI Drugs**: PPIs, H2 blockers, laxatives
- **Respiratory**: Bronchodilators, corticosteroids
- **Pain Management**: NSAIDs, acetaminophen, muscle relaxants

## Dietary Interaction Guidance

When generating patient-facing safety notes for statin medications, include the following
standard dietary counseling language in the output narrative:

- **Simvastatin / Lovastatin (CYP3A4-metabolized statins)**: Advise patients to avoid
  grapefruit and grapefruit juice on days when they take their statin dose, as grapefruit
  compounds can temporarily increase drug levels and raise the risk of muscle side effects.
- **Pravastatin / Rosuvastatin (non-CYP3A4 statins)**: No grapefruit restriction needed.

This dietary guidance should appear as a clearly worded patient instruction in any
discharge counseling note or safety summary produced by this skill.

## Drug Database

The skill includes a built-in drug database for quick lookups:

```python
from scripts.safety_review import search_drug_info

drug_info = search_drug_info("simvastatin")
if drug_info:
    print(f"Drug: {drug_info['name']}")
    print(f"Category: {drug_info['category']}")
```

### Available Drugs in Database

- warfarin
- metformin
- amoxicillin
- lisinopril
- simvastatin
- aspirin

## References

- Drug database: [references/drug-database.md](references/drug-database.md)
- Interaction criteria: [references/interaction-criteria.md](references/interaction-criteria.md)

## Disclaimer

This tool is for clinical decision support only and does not replace professional pharmacist or physician judgment. Always verify recommendations with qualified healthcare providers.

**System Limitations**:
- Not a substitute for clinical judgment
- Accuracy depends on complete medication and allergy data
- Rare interactions may have limited data
- Patient-specific factors may affect actual risk
