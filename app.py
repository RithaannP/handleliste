from flask import Flask, redirect
import sqlite3
import os

app = Flask(__name__)

DB_FIL = os.path.join(os.path.dirname(__file__), "handleliste.db")

def hent_produkter():
    con = sqlite3.connect(DB_FIL)
    rader = con.execute("SELECT id, navn, kategori, trengs FROM produkt").fetchall()
    con.close()
    return rader
    

def bytt_trengs(produkt_id):
    con = sqlite3.connect(DB_FIL)
    con.execute("UPDATE produkt SET trengs = 1 - trengs WHERE id = ?", (produkt_id,))
    con.commit()
    con.close()
    
@app.route("/")
def forside():
    return "Hei"

@app.route("/handleliste")
def handleliste():
    produkter = hent_produkter()
    html = "<h1>Rithi's Handleliste</h1>"

    html += "<h2>Essentials</h2>"
    for produkt_id, navn, kategori, trengs in produkter:
        if kategori == "Essentials":
            html += f'<a href="/bytt/{produkt_id}">{navn}</a> {trengs}<br>'

    html += "<h2>Diverse</h2>"
    for produkt_id, navn, kategori, trengs in produkter:
        if kategori == "Diverse":
            html += f'<a href="/bytt/{produkt_id}">{navn}</a> {trengs}<br>'

    return html

@app.route("/bytt/<int:produkt_id>")
def bytt(produkt_id):
    bytt_trengs(produkt_id)
    return redirect("/handleliste")

if __name__ == "__main__":
    app.run(debug=True)