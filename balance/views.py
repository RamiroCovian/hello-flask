from . import app


@app.route("/")
def home():
    """
    Muestra la lista de movimientos cargados.
    """
    return "Lista de movimientos"


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
