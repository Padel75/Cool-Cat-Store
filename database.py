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

    def query_one(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        return cursor.fetchone()
