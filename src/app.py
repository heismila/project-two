#!/usr/bin/env python3
"""Main application entry point."""
from auth import UserAuth
from config import CONFIG


def main() -> None:
    print(f"Project Two v{CONFIG['api_version']}")
    print("Authentication enabled")
    auth = UserAuth()
    auth.register("admin", "secret123")


if __name__ == "__main__":
    main()