class Customer:
    def __init__(self, username, password, first_name, last_name, address, phone_number, email):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.phone_number = phone_number
        self.email = email

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_address(self):
        return self.address

    def get_phone_number(self):
        return self.phone_number

    def get_email(self):
        return self.email