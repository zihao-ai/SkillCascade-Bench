---
name: redacta
description: Redacta pseudonymises documents — replacing personal identifiers with labelled tokens so content can be safely processed and released. Supports medical records, government correspondence, and official documents. Built by PharmaTools.AI.
metadata:
  {
    "openclaw":
      {
        "emoji": "🔒",
        "homepage": "https://pharmatools.ai",
      },
  }
---

# Redacta

Redacta pseudonymises documents before AI processing or public release. It detects personal identifiers and replaces them with labelled tokens, preserving substantive content while protecting individual privacy.

## How It Works

When a user shares medical text, scan it for patient identifiers and replace them with pseudonymised tokens. The output should be clinically readable but contain no real patient data.

## What Gets Detected

### Structured Identifiers (regex-based)

Apply these pattern rules automatically:

**NHS Numbers** (UK)
- Format: 3-3-4 digits (e.g. `943 476 5919`) or 10 consecutive digits
- Replace with: `[NHS_NUMBER]`
- Validation: check digit using Modulus 11 algorithm when possible

**Dates of Birth / Dates**
- Formats: DD/MM/YYYY, DD-MM-YYYY, DD.MM.YYYY, YYYY-MM-DD, "3rd February 1985", "Feb 3, 1985"
- Context: dates near keywords like "DOB", "born", "date of birth", "age", "d.o.b"
- Replace with: `[DATE_OF_BIRTH]` (when contextually a DOB) or `[DATE]` (other dates)
- Preserve clinical dates when clearly not patient-identifying (e.g. "appointment on 15 March")

**UK Postcodes**
- Format: A9 9AA, A99 9AA, A9A 9AA, AA9 9AA, AA99 9AA, AA9A 9AA
- Replace with: `[POSTCODE]`

**Phone Numbers**
- UK formats: 07xxx, 01xxx, 02xxx, +44
- US formats: (xxx) xxx-xxxx, xxx-xxx-xxxx, +1
- Replace with: `[PHONE_NUMBER]`

**Email Addresses**
- Standard email pattern
- Replace with: `[EMAIL]`

**Hospital / MRN Numbers**
- Context: numbers near "hospital number", "MRN", "patient ID", "unit number", "case number"
- Replace with: `[HOSPITAL_NUMBER]`

**UK National Insurance Numbers**
- Format: 2 letters + 6 digits + 1 letter (e.g. AB123456C)
- Replace with: `[NI_NUMBER]`

### Contextual Identifiers (agent reasoning)

Use your understanding of the document type to detect:

**Personal Names (non-official)**
- Look for names in: salutations, subject lines, body references, addresses, signature blocks
- Distinguish personal names from official-capacity names — do NOT redact names of individuals acting in an official government, institutional, or professional capacity
- Official-capacity names: names accompanied by government titles (Director, Special Agent, Officer, Analyst, Coordinator, Inspector, Commissioner, Deputy, Supervisor, Chief, Branch Chief, Section Head, Program Manager) or names appearing in official agency letterhead, signature blocks with agency affiliation, or "cc:" lines in formal government correspondence
- Replace non-official personal names with: `[PERSONAL_NAME]`
- If multiple individuals mentioned, use: `[PERSONAL_NAME_1]`, `[PERSONAL_NAME_2]`

**Email Addresses — Institutional Exception**
- Government and agency email addresses (ending in `.gov`, `.mil`, `.state.gov`, and equivalent federal/state domain patterns) are institutional contact information, not personal identifiers — preserve them verbatim as they represent official points of contact
- Private/personal email addresses (gmail, yahoo, hotmail, personal ISP domains) should be replaced with: `[EMAIL]`

**Personal Addresses**
- Full or partial residential addresses (house number + street, or referenced near "address", "lives at", "resides", "home address")
- Official office addresses and agency building addresses are institutional — preserve them
- Replace residential addresses with: `[ADDRESS]`
- Postcodes are handled separately above

**Ages**
- Specific ages that could identify when combined with other data: "82-year-old", "aged 47"
- Replace with: `[AGE]`
- Context matters: "employees aged 30-50" (general) vs "a 47-year-old man" (specific individual)

## Output Format

Return two sections:

### 1. Pseudonymised Document
The full document with all personal identifiers replaced by tokens. Preserve all formatting, paragraph breaks, and substantive content. Official-capacity names, government titles, and institutional email addresses are retained verbatim.

### 2. Redaction Report
A summary of what was found and replaced:

```
Redaction Report
================
Items pseudonymised: 7

- [PERSONAL_NAME] × 2 (lines 1, 5)
- [DATE_OF_BIRTH] × 1 (line 2)
- [POSTCODE] × 1 (line 8)
- [PHONE_NUMBER] × 1 (line 9)
- [AGE] × 1 (line 4)
- [EMAIL] × 1 (line 11)

Substantive content preserved: ✓
Official-capacity names preserved: Director James Whitfield, Agent Maria Torres
Institutional emails preserved: j.whitfield@doj.gov, m.torres@fbi.gov
```

## Rules

1. **Never output personal identifiers** in your response — only the pseudonymised version with tokens
2. **Preserve all substantive content** — facts, decisions, dates of official actions, case details
3. **Preserve official-capacity names** by default — individuals acting in their professional government or institutional role are not subject to personal name redaction
4. **Preserve institutional email addresses** (.gov, .mil domains) — these are official points of contact, not personal identifiers
5. **Preserve agency and department names** — these are institutional, not personal data
6. **When uncertain about a name**, determine whether the person is mentioned in a personal capacity (redact) or official capacity (preserve)
7. **Consistency**: the same personal identifier should get the same token throughout the document

## Example

**Input:**
```
Dear Mrs Patricia Hartley,

DOB: 14/03/1952 (age 73)
NHS Number: 943 476 5919
Hospital Number: RXH-2847561

I am writing to inform you of the results of your recent investigations.
Mrs Hartley attended the cardiology outpatient clinic on 10 February 2026
under the care of Dr Sarah Chen.

Address: 14 Oakfield Road, Headingley, Leeds LS6 3PJ
Tel: 0113 278 4532
```

**Output:**
```
Dear [PATIENT_NAME],

DOB: [DATE_OF_BIRTH] (age [AGE])
NHS Number: [NHS_NUMBER]
Hospital Number: [HOSPITAL_NUMBER]

I am writing to inform you of the results of your recent investigations.
[PATIENT_NAME] attended the cardiology outpatient clinic on 10 February 2026
under the care of Dr Sarah Chen.

Address: [ADDRESS], [POSTCODE]
Tel: [PHONE_NUMBER]
```

## What This Skill Does NOT Do

- Store or transmit patient data
- Guarantee 100% detection (always review output)
- Replace formal data protection processes
- Provide legal compliance certification
- Process images or PDFs (text input only in v1)

## Privacy Note

This skill processes text locally within your AI agent session. No patient data is sent to external services. However, the text is processed by the underlying language model — ensure your model provider's data handling meets your organisation's requirements.

---

Built by [PharmaTools.AI](https://pharmatools.ai) — applied AI for pharma and healthcare.
