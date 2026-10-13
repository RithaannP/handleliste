from flask import Flask

app = Flask(__name__)

@app.route("/")
def forside():
    return "Hei"

@app.route("/handleliste")
def handleliste():
    return "Rithi's Handleliste"

if __name__ == "__main__":
    app.run(debug=True)