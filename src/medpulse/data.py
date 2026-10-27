"""Load and validate synthetic JSONL examples."""
import json
from pathlib import Path

REQUIRED_FIELDS = {"instruction", "response"}

def load_jsonl(path):
    path = Path(path)
    records = []
    with path.open("r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, start=1):
            if not line.strip():
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSON on line {line_no}") from exc
            if not REQUIRED_FIELDS.issubset(record):
                raise ValueError(f"Line {line_no} must contain {sorted(REQUIRED_FIELDS)}")
            if not all(isinstance(record[k], str) and record[k].strip() for k in REQUIRED_FIELDS):
                raise ValueError(f"Line {line_no} fields must be non-empty strings")
            records.append(record)
    return records
