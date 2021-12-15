import sqlite3

sqliteConnection = sqlite3.connect('client.db')
cursor_see = sqliteConnection.cursor()

sqlite_insert_table_query = '''SELECT *
                            FROM Client;'''

cursor_see.execute(sqlite_insert_table_query)
data = cursor_see.fetchall()
for row in data:
    print("id", row[0])
    print("name", row[1])
    print("email", row[2])
    print("solde:", row[3])

sqliteConnection.commit()

cursor_see.close()
sqliteConnection.close()