import json
from pathlib import Path
from medpulse.data import load_jsonl
from medpulse.generate import build_prompt

ROOT = Path(__file__).resolve().parents[1]

def test_synthetic_sample_loads():
    records = load_jsonl(ROOT / "data/sample/synthetic_discharge_examples.jsonl")
    assert records
    assert all("instruction" in r and "response" in r for r in records)

def test_prompt_requires_nonempty_text():
    try:
        build_prompt(" ")
    except ValueError:
        pass
    else:
        raise AssertionError("Expected empty input to fail")

def test_prompt_contains_safety_language():
    prompt = build_prompt("Fictional example only.")
    assert "not medical advice" in prompt
