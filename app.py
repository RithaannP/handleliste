from flask import Flask
import sqlite3
import os

app = Flask(__name__)

DB_FIL = os.path.join(os.path.dirname(__file__), "handleliste.db")

def hent_produkter():
    con = sqlite3.connect(DB_FIL)
    rader = con.execute("SELECT navn, kategori FROM produkt").fetchall()
    con.close()
    return rader
    


@app.route("/")
def forside():
    return "Hei"

@app.route("/handleliste")
def handleliste():
    produkter = hent_produkter()
    html = "<h1>Rithi's Handleliste</h1>"
    
    html += "<h2>Essentials</h2>"
    for navn, kategori in produkter:
        if kategori == "Essentials":
            html += navn + "<br>"
    html += "<h2>Diverse</h2>"
    for navn, kategori in produkter:
        if kategori == "Diverse":
            html += navn + "<br>"
    return html
    

if __name__ == "__main__":
    app.run(debug=True)