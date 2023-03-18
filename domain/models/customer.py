from domain.models.user import User


class Customer(User):
    def __init__(
        self,
        username: str,
        password: str,
        first_name: str,
        last_name: str,
        address: str,
        phone_number: str,
        email: str,
    ) -> None:
        super().__init__(username, password)
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.address: str = address
        self.phone_number: str = phone_number
        self.email: str = email

    def get_first_name(self) -> str:
        return self.first_name

    def get_last_name(self) -> str:
        return self.last_name

    def get_address(self) -> str:
        return self.address

    def get_phone_number(self) -> str:
        return self.phone_number

    def get_email(self) -> str:
        return self.email
