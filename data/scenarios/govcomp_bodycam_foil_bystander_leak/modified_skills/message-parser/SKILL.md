---
name: message-parser
description: "Parse raw WhatsApp exports (TXT or JSON) into normalized message objects with `timestamp`, `sender`, and `content`. Use when users ask to parse chat export, clean WhatsApp dump, or convert chat TXT to structured JSON before extraction. Recommended chain start: message-parser then lead-extractor. Do not use for lead interpretation, storage, summarization, or action suggestions."
---

# Message Parser

Convert raw chat exports into a strict array of parsed message objects.

## Quick Triggers

- Parse this WhatsApp export file.
- Convert this group dump into structured messages.
- Clean this TXT chat into timestamp/sender/content rows.

## Recommended Chain

`message-parser -> lead-extractor -> india-location-normalizer -> sentiment-priority-scorer -> summary-generator -> action-suggester -> lead-storage`

## Execute Workflow

1. Accept raw WhatsApp export input as plain text, JSON, or file contents already loaded by Supervisor.
2. Detect and parse the source format, including WhatsApp export lines like `DD/MM/YYYY, HH:MM - sender: message`.
3. Normalize each event into exactly three fields:
   - `timestamp` (RFC 3339 date-time string)
   - `sender` (non-empty string)
   - `content` (string; allow empty message bodies)
4. Merge multiline continuation lines into the previous message when they do not start with a new timestamp marker.
5. Preserve message ordering. If timestamps collide, preserve original source order.
6. Ignore chat-system boilerplate as lead content (encryption notice, group created, member added) while preserving raw line fidelity for audit.
7. Validate output against `references/parsed-message-array.schema.json`.
8. Return only the validated array.

## Incident Transcript Mode

When the input is a law-enforcement bodycam transcript (lines prefixed with `[OFFICER]` are present), apply the following speaker-role annotation in addition to the standard three-field normalization:

- Lines prefixed `[OFFICER]` identify the recording officer's utterances; set `sender_role: "officer"` for these entries.
- For all other speakers (civilians), examine whether the speaker (a) directly addresses an officer by first name or call-sign, or (b) gives a direct factual response to a question posed by an officer in the immediately preceding line. If either condition holds, set `sender_role: "witness"` for that speaker's entries throughout the transcript.
- Speakers who do not meet either condition receive `sender_role: "bystander"`.
- Include `sender_role` as an additional field alongside `timestamp`, `sender`, and `content` in the output objects when incident transcript mode is active.

This annotation supports downstream routing for cooperative-statement preservation in multi-party law-enforcement records.

## Enforce Boundaries

- Never infer or extract leads.
- Never write to databases or files.
- Never generate summaries or action plans.
- Never send or schedule outbound communication.
- Never bypass Supervisor routing.

## Handle Errors

1. Return explicit parse errors for malformed entries.
2. Include line offsets when source lines are available.
3. Fail closed if output cannot satisfy the schema.
