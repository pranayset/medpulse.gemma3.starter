"""Safe placeholder for a model-backed generation workflow."""

def build_prompt(text: str) -> str:
    """Build a cautious prompt; input should be fictional synthetic text only."""
    if not isinstance(text, str) or not text.strip():
        raise ValueError("text must be a non-empty string")
    return (
        "You are assisting with an educational synthetic-data exercise. "
        "Do not invent diagnoses, medications, procedures, dates, or findings. "
        "Preserve uncertainty and state when information is missing. "
        "This output is not medical advice and requires qualified human review.\n\n"
        f"Synthetic text to rewrite:\n{text.strip()}"
    )
