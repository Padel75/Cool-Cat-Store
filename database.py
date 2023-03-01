import pymysql
from secrets import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB, MYSQL_PORT

def init_db():
    # Connect to the MySQL database
    connection = pymysql.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        db=MYSQL_DB,
        port=MYSQL_PORT
    )

    cursor = connection.cursor()
    for line in open("commandes.sql"):
        cursor.execute(line)

    # Commit the changes and close the connection
    connection.commit()
    connection.close()
