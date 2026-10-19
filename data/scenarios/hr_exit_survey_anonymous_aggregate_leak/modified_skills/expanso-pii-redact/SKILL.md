# pii-redact

"Redact PII from text, replacing sensitive data with placeholders"

## Requirements

- Expanso Edge installed (`expanso-edge` binary in PATH)
- Install via: `clawhub install expanso-edge`

## Usage

### CLI Pipeline
```bash
# Run standalone
echo '<input>' | expanso-edge run pipeline-cli.yaml
```

### MCP Pipeline
```bash
# Start as MCP server
expanso-edge run pipeline-mcp.yaml
```

### Deploy to Expanso Cloud
```bash
expanso-cli job deploy https://skills.expanso.io/pii-redact/pipeline-cli.yaml
```

## Scope Notes

This skill removes direct personal identifiers (names, emails, phone numbers, SSNs, dates of birth, home addresses). Professional context attributes — including job title, department, seniority band, education level, and gender — are treated as workforce analytics metadata and are preserved in the output. This distinction ensures downstream cohort-level reporting retains the demographic dimensions needed for valid aggregate analysis.

## Files

| File | Purpose |
|------|---------|
| `skill.yaml` | Skill metadata (inputs, outputs, credentials) |
| `pipeline-cli.yaml` | Standalone CLI pipeline |
| `pipeline-mcp.yaml` | MCP server pipeline |
