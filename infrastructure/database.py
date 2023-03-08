import pymysql
from pymysql.err import OperationalError
from infrastructure.config import Config
from domain.models.customer import Customer
from domain.models.vendor import Vendor
from domain.models.product import Product
from exceptions.invalidParameterException import InvalidParameterException


class Database:
    def __init__(self):
        self.connection = pymysql.connect(
            host=Config.MYSQL_HOST,
            user=Config.MYSQL_USER,
            password=Config.MYSQL_PASSWORD,
            db=Config.MYSQL_DB,
            port=Config.MYSQL_PORT
        )
        self.commands_file = Config.DATABASE_COMMANDS_FILE

    @staticmethod
    def init_db():
        connection = pymysql.connect(
            host=Config.MYSQL_HOST,
            user=Config.MYSQL_USER,
            password=Config.MYSQL_PASSWORD,
            port=Config.MYSQL_PORT
        )
        cursor = connection.cursor()
        file = open(Config.DATABASE_COMMANDS_FILE, 'r')
        sql_file = file.read()
        file.close()
        sql_commands = sql_file.split(';')

        for commands in sql_commands:
            try:
                cursor.execute(commands)
            except Exception as e:
                print("Command skipped: ", commands)

        connection.commit()
        connection.close()

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

    def create_product(self, product: Product) -> int:
        name = product.get_name()
        description = product.get_description()
        price = product.get_price()
        category_id = product.get_category_id()
        vendor_id = product.get_vendor_id()

        product_id = self.__add_product(name, description, price, category_id, vendor_id)
        return product_id

    def get_user_password(self, username: str) -> str:
        query = "SELECT password FROM humans WHERE username = %s"
        values = (username,)
        password = self.__select_one_query(query, values)
        if password is None:
            return None
        return password[0]

    def get_user_id(self, username: str) -> int:
        query = "SELECT id FROM humans WHERE username = %s"
        values = (username,)
        user_id = self.__select_one_query(query, values)
        if user_id is None:
            return None
        return user_id[0]

    def get_user(self, user_id: int) -> tuple:
        query = "SELECT * FROM humans WHERE id = %s"
        values = (user_id,)
        user = self.__select_one_query(query, values)
        if user is None:
            return None
        return user

    def __add_human(self, username: str, password: str) -> int:
        query = "INSERT INTO humans (username, password) VALUES (%s, %s)"
        values = (username, password)
        return self.__insert_query(query, values)

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
            user_id = self.__insert_query(query, values)
        except OperationalError as err:
            self.__delete_human(human_id)
            if "phone_number_invalid" in str(err):
                raise InvalidParameterException("Numéro de téléphone doit avoir le format 418-123-4567")
            elif "email_invalid" in str(err):
                raise InvalidParameterException("Email est invalide")
            raise InvalidParameterException(err)
        return user_id

    def __add_product(self, name: str, description: str, price: float, category_id: int, vendor_id: int) -> int:
        query = "INSERT INTO products (name, description, price, category_id) " \
                "VALUES (%s, %s, %s, %s)"
        values = (name, description, price, category_id)
        product_id = self.__insert_query(query, values)

        query = "INSERT INTO vendors_adds_products (product_id, vendor_id) " \
                "VALUES (%s, %s)"
        values = (product_id, vendor_id)
        self.__insert_query(query, values)
        return product_id

    def __insert_query(self, query: str, values: tuple) -> int:
        cursor = self.connection.cursor()
        cursor.execute(query, values)
        self.connection.commit()
        return cursor.lastrowid

    def __delete_human(self, human_id: int):
        cursor = self.connection.cursor()
        query = "DELETE FROM humans WHERE id = %s"
        cursor.execute(query, (human_id,))

        query = "ALTER TABLE humans AUTO_INCREMENT = %s"
        auto_increment_value = human_id - 1 if human_id > 1 else 1
        cursor.execute(query, (auto_increment_value,))
        self.connection.commit()
        return

    def __select_one_query(self, query: str, values: tuple) -> tuple:
        cursor = self.connection.cursor()
        cursor.execute(query, values)
        return cursor.fetchone()
