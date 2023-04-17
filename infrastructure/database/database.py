import mysql.connector
from mysql.connector.cursor import MySQLCursor

from infrastructure.config import Config


class Database:
    def __init__(self) -> None:
        self.connection = mysql.connector.connect(
            user=Config.MYSQL_USER,
            password=Config.MYSQL_PASSWORD,
            host=Config.MYSQL_HOST,
            database=Config.MYSQL_DB,
            # port=Config.MYSQL_PORT,
        )
        self.commands_file: str = Config.DATABASE_COMMANDS_FILE

    @staticmethod
    def init_db() -> None:
        connection = mysql.connector.connect(
            user=Config.MYSQL_USER,
            password=Config.MYSQL_PASSWORD,
            host=Config.MYSQL_HOST,
            # port=Config.MYSQL_PORT,
        )
        cursor: MySQLCursor = connection.cursor(dictionary=True)
        file = open(Config.DATABASE_COMMANDS_FILE, "r")

        result_iterator = cursor.execute(file.read(), multi=True)

        for res in result_iterator:
            print(
                "Running query: ", res
            )  # Will print out a short representation of the query
            print(f"Affected {res.rowcount} rows")

        cursor.close()
        connection.commit()
        connection.close()

    def insert_query(self, query: str, values: tuple) -> int:
        cursor: MySQLCursor = self.connection.cursor()

        cursor.execute(query, values)
        self.connection.commit()

        return cursor.lastrowid

    def insert_human_query(self, query: str, values: tuple) -> int:
        cursor: MySQLCursor = self.connection.cursor()

        cursor.execute("SELECT MAX(id) FROM humans")
        id: int = cursor.fetchone()[0]

        values = (id,) + values

        cursor.execute(query, values)
        self.connection.commit()

        return cursor.lastrowid

    def select_one_query(self, query: str, values: tuple = None) -> tuple:
        cursor = self.connection.cursor()
        cursor.execute(query, values)

        return cursor.fetchone()

    def delete_query(self, query: str, values: tuple) -> None:
        cursor = self.connection.cursor()
        cursor.execute(query, values)
        self.connection.commit()

        return

    def update_query(self, query: str, values: tuple) -> None:
        cursor = self.connection.cursor()
        cursor.execute(query, values)
        self.connection.commit()

        return

    def select_all_query(self, query: str) -> list:
        cursor = self.connection.cursor()
        cursor.execute(query)

        return cursor.fetchall()
