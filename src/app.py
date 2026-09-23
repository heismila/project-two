#!/usr/bin/env python3
"""Main application entry point."""
from data_processor import process_data, validate_data
from config import CONFIG


def main() -> None:
    print(f"Project Two v{CONFIG['api_version']}")
    print("Data processing ready")
    sample = ["hello", "world", "test"]
    if validate_data(sample):
        print(f"Processed: {process_data(sample)}")


if __name__ == "__main__":
    main()