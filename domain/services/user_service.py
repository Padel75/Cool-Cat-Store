from infrastructure.database import Database
from domain.models.customer import Customer
class UserService:
    def __init__(self):
        self.database = Database()

    def create_customer(self, customer: Customer) -> int:
        first_name = customer.get_first_name()
        last_name = customer.get_last_name()
        username = customer.get_username()
        password = customer.get_password()
        address = customer.get_address()
        phone_number = customer.get_phone_number()
        email = customer.get_email()

        query = "INSERT INTO humans (username, password) VALUES (%s, %s)"
        values = (username, password)
        human_id = self.database.insert_query(query, values)

        query = "INSERT INTO customers (first_name, last_name, address, phone_number, email, id) " \
                "VALUES (%s, %s, %s, %s, %s, %s)"
        values = (first_name, last_name, address, phone_number, email, human_id)
        user_id = self.database.insert_query(query, values)

        return user_id

    def get_user_password(self, username):
        query = "SELECT password FROM humans WHERE username = %s"
        values = (username,)
        password = self.database.select_one_query(query, values)
        if password is None:
            return None
        return password[0]

    def get_user_id(self, username):
        query = "SELECT id FROM humans WHERE username = %s"
        values = (username,)
        user_id = self.database.select_one_query(query, values)
        if user_id is None:
            return None
        return user_id[0]