import pymysql
from config import Config

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

    def query_one(self, query: str):
        cursor = self.connection.cursor()
        cursor.execute(query)
        return cursor.fetchone()

    def create_customer(self, user_info: dict) -> int:
        first_name = user_info["first_name"]
        last_name = user_info["last_name"]
        username = user_info["username"]
        password = user_info["password"]
        address = user_info["address"]
        phone_number = user_info["phone_number"]
        email = user_info["email"]

        cursor = self.connection.cursor()
        command = "INSERT INTO humans (username, password) VALUES (%s, %s)"
        cursor.execute(command, (username, password))
        user_id = cursor.lastrowid

        command = "INSERT INTO customers (first_name, last_name, address, phone_number, email, id) " \
                  "VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(command, (first_name, last_name, address, phone_number, email, user_id))
        self.connection.commit()

        user_id = cursor.lastrowid
        return user_id

    def get_user_password(self, username):
        cursor = self.connection.cursor()
        command = "SELECT password FROM humans WHERE username = %s"
        cursor.execute(command, (username,))
        password = cursor.fetchone()
        if password is None:
            return None
        return password[0]

    def get_user_id(self, username):
        cursor = self.connection.cursor()
        command = "SELECT id FROM humans WHERE username = %s"
        cursor.execute(command, (username,))
        user_id = cursor.fetchone()
        if user_id is None:
            return None
        return user_id[0]
