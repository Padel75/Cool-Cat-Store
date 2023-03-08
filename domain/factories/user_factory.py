from infrastructure.database import Database
from domain.models.customer import Customer
import bcrypt
class UserFactory:
    def __init__(self):
        self.database = Database()

    def create_customer(self, customer_infos: {}) -> Customer:
        first_name = customer_infos['first_name']
        last_name = customer_infos['last_name']
        username = customer_infos['username']
        password = customer_infos['password']
        address = customer_infos['address']
        phone_number = customer_infos['phone_number']
        email = customer_infos['email']

        encrypted_password = self.__encrypt_password(password)

        customer = Customer(username, encrypted_password, first_name, last_name, address, phone_number, email)

        return customer

    def __encrypt_password(self, password):
        salt = bcrypt.gensalt()
        encrypted_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return encrypted_password