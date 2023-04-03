from domain.models.user import User


class Seller(User):
    def __init__(
        self,
        username: str,
        password: str,
        name: str,
        description: str,
        address: str,
        phone_number: str,
        email: str,
    ) -> None:
        super().__init__(username, password)
        self.name: str = name
        self.description: str = description
        self.address: str = address
        self.phone_number: str = phone_number
        self.email: str = email

    def get_name(self) -> str:
        return self.name

    def get_description(self) -> str:
        return self.description

    def get_address(self) -> str:
        return self.address

    def get_phone_number(self) -> str:
        return self.phone_number

    def get_email(self) -> str:
        return self.email
