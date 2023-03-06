import pymysql
from infrastructure.config import Config
from domain.models.customer import Customer

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

    def init_db(self):
        cursor = self.connection.cursor()
        for line in open(self.commands_file):
            cursor.execute(line)

        self.connection.commit()
        self.connection.close()

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
        human_id = self.__insert_query(query, values)

        query = "INSERT INTO customers (first_name, last_name, address, phone_number, email, id) " \
                "VALUES (%s, %s, %s, %s, %s, %s)"
        values = (first_name, last_name, address, phone_number, email, human_id)
        user_id = self.__insert_query(query, values)

        return user_id

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

    def __insert_query(self, query: str, values: tuple) -> int:
        cursor = self.connection.cursor()
        cursor.execute(query, values)
        self.connection.commit()
        return cursor.lastrowid

    def __select_one_query(self, query: str, values: tuple) -> tuple:
        cursor = self.connection.cursor()
        cursor.execute(query, values)
        return cursor.fetchone()




