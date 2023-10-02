from flask import render_template, request, redirect, url_for

from . import app
from .models import ListaMovimientos


@app.route("/")
def home():
    """
    Muestra la lista de movimientos cargados.
    """
    lista = ListaMovimientos()
    lista.leer_desde_archivo()

    return render_template("inicio.html", movs=lista.movimientos)


@app.route("/nuevo")
def add_movement():
    """
    Crea un movimiento y lo guarda en el archivo CSV
    """
    return render_template("nuevo.html")


@app.route("/guardar", methods=["POST"])
def guardar():
    lista = ListaMovimientos()
    fecha = request.form.get("date")
    concepto = request.form.get("subject")
    tipo = request.form.get("mov_type")
    cantidad = request.form.get("Quantity")
    lista.guardar_archivo(fecha, concepto, tipo, cantidad)

    return redirect(url_for("add_movement"))


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
