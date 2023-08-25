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
        select_query = "SELECT * FROM t122_answer"
        with connection.cursor() as cursor:
            cursor.execute(select_query)
            for row in cursor.fetchall():
                print(row)
                # print(type(row))
except Error as e:
    print(e)