from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="127.0.0.1",
        user="root",
        password="123q",
        database='exam',
    ) as connection:
        print(connection)
        select_query = "SELECT * from T122_answer"
        with connection.cursor() as cursor:
            cursor.execute(select_query)
            for row in cursor.fetchall():
                print(row)
except Error as e:
    print(e)