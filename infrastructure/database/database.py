import pymysql
from infrastructure.config import Config


class Database:
    def __init__(self):
        self.connection = pymysql.connect(
            host=Config.MYSQL_HOST,
            user=Config.MYSQL_USER,
            password=Config.MYSQL_PASSWORD,
            db=Config.MYSQL_DB,
            port=Config.MYSQL_PORT,
        )
        self.commands_file = Config.DATABASE_COMMANDS_FILE

    @staticmethod
    def init_db():
        connection = pymysql.connect(
            host=Config.MYSQL_HOST,
            user=Config.MYSQL_USER,
            password=Config.MYSQL_PASSWORD,
            port=Config.MYSQL_PORT,
        )
        cursor = connection.cursor()
        file = open(Config.DATABASE_COMMANDS_FILE, "r")
        sql_file = file.read()
        file.close()
        sql_commands = sql_file.split(";")

        for commands in sql_commands:
            try:
                cursor.execute(commands)
            except Exception as e:
                print("Command skipped: ", commands)

        connection.commit()
        connection.close()

    def insert_query(self, query: str, values: tuple) -> int:
        cursor = self.connection.cursor()
        cursor.execute(query, values)
        self.connection.commit()
        return cursor.lastrowid

    def select_one_query(self, query: str, values: tuple) -> tuple:
        cursor = self.connection.cursor()
        cursor.execute(query, values)
        return cursor.fetchone()
