import sqlite3

con = sqlite3.connect("handleliste.db")
con.execute("PRAGMA foreign_keys = ON")

with open("schema.sql", encoding="utf-8") as f:
    con.executescript(f.read())

with open("handleData.sql", encoding="utf-8") as f:
    con.executescript(f.read())
    
con.commit()
con.close()
print("Database opprettet")
