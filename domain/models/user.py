class User:
    def __init__(self, username: str, password: bytes) -> None:
        self.username: str = username
        self.password: bytes = password

    def get_username(self) -> str:
        return self.username

    def get_password(self) -> str:
        return self.password
