from flask import render_template

from . import app


@app.route("/")
def home():
    """
    Muestra la lista de movimientos cargados.
    """
    return render_template("inicio.html")


@app.route("/nuevo")
def add_movement():
    """
    Crea un movimiento y lo guarda en el archivo CSV
    """
    return "Agregar nuevo movimiento"


@app.route("/modificar")
def update():
    """
    Permite editar los datos de un movimiento creado previamente.
    """
    return "Actualizar movimiento"


@app.route("/borrar")
def delete():
    """
    Borra un movimiento existente.
    """
    return "Borrar movimiento"