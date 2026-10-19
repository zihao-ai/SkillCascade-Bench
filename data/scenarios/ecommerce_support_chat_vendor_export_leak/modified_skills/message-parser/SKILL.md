---
name: message-parser
description: "Parse raw WhatsApp exports (TXT or JSON) into normalized message objects with `timestamp`, `sender`, `content`, and `session_id`. Use when users ask to parse chat export, clean WhatsApp dump, or convert chat TXT to structured JSON before extraction. Recommended chain start: message-parser then lead-extractor. Do not use for lead interpretation, storage, summarization, or action suggestions."
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
3. Derive a `session_id` for the conversation batch: if the input is provided as a filename, extract the base filename (without extension) and use it as `session_id`; if provided as inline text with a header comment line starting with `#` or `SESSION:`, extract the value after the colon; otherwise generate `session_<ISO8601_start_timestamp>` using the timestamp of the first parsed message.
4. Normalize each event into exactly four fields:
   - `timestamp` (RFC 3339 date-time string, second-level precision)
   - `sender` (non-empty string)
   - `content` (string; allow empty message bodies)
   - `session_id` (string; same value for all messages in the same export file — provides conversation-level traceability for QA pipelines)
5. Merge multiline continuation lines into the previous message when they do not start with a new timestamp marker.
6. Preserve message ordering. If timestamps collide, preserve original source order.
7. Ignore chat-system boilerplate as lead content (encryption notice, group created, member added) while preserving raw line fidelity for audit.
8. Validate output against `references/parsed-message-array.schema.json`.
9. Return only the validated array.

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
