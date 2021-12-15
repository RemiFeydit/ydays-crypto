import sqlite3

sqliteConnection = sqlite3.connect('client.db')
cursor_insert = sqliteConnection.cursor()
print("Connected")

sqlite_insert_table_query = '''INSERT INTO Client 
                            (name, email, solde)
                            VALUES 
                            (?, ?, ?);'''

values = input("Veuillez entre votre nom et adresse mail: ")
list = values.split()
list.append(100)
tuple = tuple(list)

cursor_insert.execute(sqlite_insert_table_query, tuple)
sqliteConnection.commit()
print("Commit done")

cursor_insert.close()
sqliteConnection.close()
print("Connection closed")

