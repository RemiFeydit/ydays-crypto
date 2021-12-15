# -- coding: utf-8 --
"""
Created on Wed Oct 27 16:19:24 2021

@author: pol:)
"""
import sqlite3


def transf():
    sqliteConnection = sqlite3.connect('client.db')
    cursor_insert = sqliteConnection.cursor()
    id = []
    solde = []
    inp = "Donnez votre email :  "
    for ind in range(0,2):
        user = "'" + input(inp) + "'"
        sqlite_get_id_query = 'SELECT id FROM Client WHERE email=' + user + ';' 
        id.append(cursor_insert.execute(sqlite_get_id_query).fetchone()[0])
        inp = "Donnez son email :  "

    trans_value = int(input("Donnez la valeur du transfert :  "))

    for i in range(0,2):
        sqlite_get_solde_query = 'SELECT solde FROM Client WHERE id=' + str(id[i]) + ';' 
        solde.append(cursor_insert.execute(sqlite_get_solde_query).fetchone()[0])

    solde[0] -= trans_value
    solde[1] += trans_value

    for i in range(0,2):
        sqlite_upt_value_query = "UPDATE Client SET solde=" + str(solde[i]) + " WHERE id=" + str(id[i]) + ";"
        cursor_insert.execute(sqlite_upt_value_query)

    sqliteConnection.commit()
    cursor_insert.close()
    sqliteConnection.close()

transf()