from flask import Flask

# instanciamos Flask
app = Flask(__name__)


@app.route("/")
def hola():
    return "Hola soy Flask. Como te llamas?"


@app.route("/adios")
def adios():
    return "Te dejo que tengo hambre"


@app.route("/new")
def nueva():
    return "Esta es una ruta nueva. Cuidado con los bandidos."
