from domain.models.customer import Customer
from domain.models.vendor import Vendor
import bcrypt
class UserFactory:

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

    def create_vendor(self, vendor_infos: {}) -> Vendor:
        name = vendor_infos['name']
        description = vendor_infos['description']
        username = vendor_infos['username']
        password = vendor_infos['password']
        address = vendor_infos['address']
        phone_number = vendor_infos['phone_number']
        email = vendor_infos['email']

        encrypted_password = self.__encrypt_password(password)

        vendor = Vendor(username, encrypted_password, name, description, address, phone_number, email)

        return vendor

    def __encrypt_password(self, password):
        salt = bcrypt.gensalt()
        encrypted_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return encrypted_password