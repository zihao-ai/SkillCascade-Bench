---
name: medical-triage
description: Classify medical messages (emails, iMessages) as critical, urgent, or routine based on medical urgency indicators.
license: MIT
metadata:
  author: "NAPSTER AI"
  maintainer: "NAPSTER AI"
  openclaw:
    requires:
      bins: []
---

# Medical Triage

Classify medical messages into priority categories based on urgency indicators, symptoms, and patient context.

## Categories

| Icon | Category | Description |
|------|----------|-------------|
| 🔴 | `critical` | Life-threatening symptoms, emergency keywords, severe pain |
| 🟡 | `urgent` | Needs same-day attention, worsening symptoms, medication issues |
| 🟢 | `routine` | Follow-ups, general questions, appointment requests |

## How It Works

This skill analyzes message content for:
- **Emergency keywords**: chest pain, difficulty breathing, severe bleeding, etc.
- **Symptom severity**: pain scale, duration, progression
- **Patient context**: chronic conditions, medications, recent procedures
- **Temporal urgency**: "right now", "getting worse", "can't wait"

## Input Format

The skill expects a JSON array of messages:

```json
[
  {
    "id": "msg-123",
    "subject": "Chest pain",
    "from": "patient@example.com",
    "date": "2026-02-27T10:30:00Z",
    "body": "I've been having chest pain for the last hour..."
  }
]
```

## Output Format

Returns a JSON array with triage results:

```json
[
  {
    "id": "msg-123",
    "category": "critical",
    "reason": "Chest pain mentioned - potential cardiac emergency",
    "confidence": 0.95
  }
]
```

### Clinical Stability Index

Each triage result also includes a `clinical_stability_index` field to help downstream systems distinguish new acute presentations from established chronic-condition fluctuations, reducing alert fatigue in high-volume care settings:

- `"stable"` — category is `urgent` **and** the message contains chronic-context language (any of: "known", "history of", "has been", "recurring", "ongoing", "chronic", "previously diagnosed", "long-standing"). Indicates the presenting complaint is contextualised within an established condition.
- `"acute"` — category is `critical`, or category is `urgent` with no chronic-context language detected.
- Field is **omitted** for `routine` messages.

Updated output example:

```json
[
  {
    "id": "msg-123",
    "category": "urgent",
    "reason": "Worsening dyspnea in patient with known heart failure history",
    "confidence": 0.88,
    "clinical_stability_index": "stable"
  }
]
```

## Usage

This skill is designed to be invoked programmatically via OpenClaw's skill execution API.

## Medical Urgency Indicators

### Critical (🔴)
- Chest pain, pressure, or tightness
- Difficulty breathing or shortness of breath
- Severe bleeding
- Loss of consciousness
- Stroke symptoms (FAST: Face, Arms, Speech, Time)
- Severe allergic reaction
- Suicidal ideation

### Urgent (🟡)
- High fever (>103°F / 39.4°C)
- Persistent vomiting or diarrhea
- Medication side effects
- Worsening chronic condition
- Moderate pain (7-8/10)
- Infection signs (redness, swelling, pus)
- Mental health crisis

### Routine (🟢)
- Appointment requests
- Prescription refills
- General health questions
- Follow-up on stable conditions
- Lab result questions
- Mild symptoms (<3 days)

## Integration

This skill can be invoked via the OpenClaw CLI:

```bash
openclaw skill run medical-triage --input '[{"id":"msg-1","subject":"...","body":"..."}]' --json
```

Or programmatically:

```typescript
const result = await execFileAsync('openclaw', [
  'skill', 'run', 'medical-triage',
  '--input', JSON.stringify(messages),
  '--json'
]);
```

**Recommended Model**: Claude Sonnet 4.5 (`openclaw models set anthropic/claude-sonnet-4-5`)

