import sqlite3

connect = sqlite3.connect("handleliste.db")

handlliste = connect.execute(""" 
    SELECT *
    FROM produkt
    WHERE produkt.kategori = 'Essentials'
""").fetchall()


for rad in handlliste:
    print(rad)

connect.close()