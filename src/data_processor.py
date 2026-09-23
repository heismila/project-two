"""Data processing utilities."""


def process_data(data: list[str]) -> list[str]:
    """Normalise raw data into a structured format."""
    return [item.strip().upper() for item in data if item]


def validate_data(data: list[str]) -> bool:
    """Return True if every item is a non-empty string."""
    return all(isinstance(item, str) and item for item in data)