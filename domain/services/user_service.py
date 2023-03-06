from infrastructure.database import Database
from domain.models.customer import Customer
from domain.exceptions.invalidParameterException import InvalidParameterException
import bcrypt
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

        encrypted_password = self.__encrypt_password(password)
        query = "INSERT INTO humans (username, password) VALUES (%s, %s)"
        values = (username, encrypted_password)
        human_id = self.database.insert_query(query, values)

        query = "INSERT INTO customers (first_name, last_name, address, phone_number, email, id) " \
                "VALUES (%s, %s, %s, %s, %s, %s)"
        values = (first_name, last_name, address, phone_number, email, human_id)
        user_id = self.database.insert_query(query, values)

        return user_id

    def validate_user_password(self, username: str, password: str) -> None:
        query = "SELECT password FROM humans WHERE username = %s"
        values = (username,)
        encrypted_password = self.database.select_one_query(query, values)
        if encrypted_password is None:
            raise InvalidParameterException("username est invalide")

        is_password_valid = bcrypt.checkpw(password.encode('utf-8'), encrypted_password[0].encode('utf-8'))
        if not is_password_valid:
            raise InvalidParameterException("password est invalide")

        return


    def get_user_id(self, username):
        query = "SELECT id FROM humans WHERE username = %s"
        values = (username,)
        user_id = self.database.select_one_query(query, values)
        if user_id is None:
            return None
        return user_id[0]

    def __encrypt_password(self, password):
        salt = bcrypt.gensalt()
        encrypted_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return encrypted_password