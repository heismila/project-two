"""User authentication module."""


class UserAuth:
    def __init__(self) -> None:
        self.users: dict[str, str] = {}

    def register(self, username: str, password: str) -> bool:
        if username in self.users:
            raise ValueError("User already exists")
        self.users[username] = password
        return True

    def login(self, username: str, password: str) -> bool:
        return self.users.get(username) == password