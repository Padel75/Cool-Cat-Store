from domain.models.user import User


class Vendor(User):
    def __init__(self, username, password, name, description, address, phone_number, email):
        super().__init__(username, password)
        self.name = name
        self.description = description
        self.address = address
        self.phone_number = phone_number
        self.email = email

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_address(self):
        return self.address

    def get_phone_number(self):
        return self.phone_number

    def get_email(self):
        return self.email




