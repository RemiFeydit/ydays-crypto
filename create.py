import sqlite3

sqliteConnection = sqlite3.connect('client.db')
sqlite_create_table_query = '''CREATE TABLE Client(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            email TEXT NOT NULL UNIQUE,
                            solde INTEGER);'''

cursor_create = sqliteConnection.cursor()
print("Connected")

cursor_create.execute(sqlite_create_table_query)
sqliteConnection.commit()
print("Table created")

cursor_create.close()

sqliteConnection.close()
print("sqlite connection is closed")
