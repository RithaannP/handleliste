import sqlite3

connect = sqlite3.connect("handleliste.db")

handlliste = connect.execute(""" 
    SELECT *
    FROM handleliste
""").fetchall()


for rad in handlliste:
    print(rad)

connect.close()