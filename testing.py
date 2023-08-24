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
        select_query = "SELECT quest_num FROM t121_quest ORDER BY quest_num DESC LIMIT 1"
        with connection.cursor() as cursor:
            cursor.execute(select_query)
            for row in cursor.fetchall():
                print(row[0])
                print(type(row))
except Error as e:
    print(e)