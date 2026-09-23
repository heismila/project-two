#!/usr/bin/env python3
"""Main application entry point."""
from config import CONFIG


def main() -> None:
    print(f"Project Two v{CONFIG['api_version']}")
    print("Initial setup complete")


if __name__ == "__main__":
    main()