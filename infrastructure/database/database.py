import pymysql
from infrastructure.config import Config


class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            user=Config.MYSQL_USER,
            password=Config.MYSQL_PASSWORD,
            host=Config.MYSQL_HOST,
            database=Config.MYSQL_DB,
            port=Config.MYSQL_PORT,
        )
        self.commands_file = Config.DATABASE_COMMANDS_FILE

    @staticmethod
    def init_db():
        connection = mysql.connector.connect(
            user=Config.MYSQL_USER,
            password=Config.MYSQL_PASSWORD,
            host=Config.MYSQL_HOST,
            database=Config.MYSQL_DB,
            port=Config.MYSQL_PORT,
        )
        cursor = connection.cursor(dictionary=True)
        file = open(Config.DATABASE_COMMANDS_FILE, "r")

        result_iterator = cursor.execute(file.read(), multi=True)

        for res in result_iterator:
            print(
                "Running query: ", res
            )  # Will print out a short representation of the query
            print(f"Affected {res.rowcount} rows")

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

    def select_all_query(self, query: str) -> list:
        cursor = self.connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
