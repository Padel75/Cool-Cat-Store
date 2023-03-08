from pymysql.err import OperationalError
from infrastructure.database.database import Database
from domain.models.customer import Customer
from domain.models.vendor import Vendor
from exceptions.invalidParameterException import InvalidParameterException


class UserDatabase(Database):

    def create_customer(self, customer: Customer) -> int:
        first_name = customer.get_first_name()
        last_name = customer.get_last_name()
        username = customer.get_username()
        password = customer.get_password()
        address = customer.get_address()
        phone_number = customer.get_phone_number()
        email = customer.get_email()

        human_id = self.__add_human(username, password)
        user_id = self.__add_customer(first_name, last_name, address, phone_number, email, human_id)
        self.__add_cart(user_id)
        return user_id

    def create_vendor(self, vendor: Vendor) -> Vendor:
        name = vendor.get_name()
        description = vendor.get_description()
        username = vendor.get_username()
        password = vendor.get_password()
        address = vendor.get_address()
        phone_number = vendor.get_phone_number()
        email = vendor.get_email()

        human_id = self.__add_human(username, password)
        user_id = self.__add_vendor(name, description, address, phone_number, email, human_id)
        return user_id
    def get_user_password(self, username: str) -> str:
        query = "SELECT password FROM humans WHERE username = %s"
        values = (username,)
        password = self.select_one_query(query, values)
        if password is None:
            return None
        return password[0]

    def get_user_id(self, username: str) -> int:
        query = "SELECT id FROM humans WHERE username = %s"
        values = (username,)
        user_id = self.select_one_query(query, values)
        if user_id is None:
            return None
        return user_id[0]

    def get_user(self, type: str, user_id: int) -> tuple:
        query = f"SELECT * FROM {type} WHERE id = %s"
        values = (user_id,)
        user = self.select_one_query(query, values)
        if user is None:
            return None
        return user

    def __add_human(self, username: str, password: str) -> int:
        query = "INSERT INTO humans (username, password) VALUES (%s, %s)"
        values = (username, password)
        return self.insert_query(query, values)

    def __add_customer(self, first_name: str, last_name: str, address: str, phone_number: str, email: str, human_id: int) -> int:
        query = "INSERT INTO customers (first_name, last_name, address, phone_number, email, id) " \
                "VALUES (%s, %s, %s, %s, %s, %s)"
        values = (first_name, last_name, address, phone_number, email, human_id)

        return self.__insert_user(query, values, human_id)

    def __add_vendor(self, name: str, description: str, address: str, phone_number: str, email: str, human_id: int) -> int:
        query = "INSERT INTO vendors (name, description, address, phone_number, email, id) " \
                "VALUES (%s, %s, %s, %s, %s, %s)"
        values = (name, description, address, phone_number, email, human_id)

        return self.__insert_user(query, values, human_id)

    def __insert_user(self, query: str, values: tuple, human_id: int) -> int:
        try:
            user_id = self.insert_query(query, values)
        except OperationalError as err:
            self.__delete_human(human_id)
            if "phone_number_invalid" in str(err):
                raise InvalidParameterException("Numéro de téléphone doit avoir le format 418-123-4567")
            elif "email_invalid" in str(err):
                raise InvalidParameterException("Email est invalide")
            raise InvalidParameterException(err)
        return user_id

    def __delete_human(self, human_id: int):
        cursor = self.connection.cursor()
        query = "DELETE FROM humans WHERE id = %s"
        cursor.execute(query, (human_id,))

        query = "ALTER TABLE humans AUTO_INCREMENT = %s"
        auto_increment_value = human_id - 1 if human_id > 1 else 1
        cursor.execute(query, (auto_increment_value,))
        self.connection.commit()
        return

    def __add_cart(self, customer_id: int) -> None:
        query = "INSERT INTO carts (total_cost) VALUES (%s)"
        values = (0,)
        cart_id = self.insert_query(query, values)

        query = "INSERT INTO customers_own_carts (customer_id, cart_id) VALUES (%s, %s)"
        values = (customer_id, cart_id)
        self.insert_query(query, values)
        return