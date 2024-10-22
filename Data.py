import mysql.connector
import datetime

connect = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='expenses'
)

cursor = connect.cursor()

cursor.execute('''

    CREATE TABLE IF NOT EXIST expenses(
        id INT,
        amount INT,
        description VARCHAR(1000),
        category VARCHAR(50),
        extra_info VARCHAR(50)
    );
''')

