from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

db = None

def dict_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}

def abrirConexion():
    global db
    db = sqlite3.connect("instance/datos.sqlite")
    db.row_factory = dict_factory

def cerrarConexion():
    global db
    if db is not None:
        db.close()
        db = None

@app.route("/usuarios/")
def verUsuarios():
    abrirConexion()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    cerrarConexion()
    return render_template("usuarios.html", usuarios=usuarios)

@app.route("/usuario/<int:id>")
def verUsuario(id):
    abrirConexion()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE id = ?", (id,))
    res = cursor.fetchone()
    cerrarConexion()
    if res is None:
        return render_template("error.html", id=id)
    else:
        return render_template("usuario_detalle.html", id=id, usuario=res["usuario"], email=res["email"], telefono=res["telefono"], direccion=res["direccion"])

@app.route("/crear-usuario/<nombre>/<email>/<telefono>/<direccion>")
def crear_usuario(nombre, email, telefono, direccion):
    abrirConexion()
    cursor = db.cursor()
    consulta = "INSERT INTO usuarios (usuario, email, telefono, direccion) VALUES (?, ?, ?, ?)"
    cursor.execute(consulta, (nombre, email, telefono, direccion))
    db.commit()
    cerrarConexion()
    return f"Se creó el usuario {nombre} con mail {email}, su número es {telefono} y su dirección es {direccion}"

@app.route("/borrar-usuario/<int:id>")
def borrarUsuario(id):
    abrirConexion()
    cursor = db.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id,))
    db.commit()
    cerrarConexion()
    return redirect("/usuarios")

@app.route("/registros")
def testDB():
    abrirConexion()
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) AS cant FROM usuarios")
    res = cursor.fetchone()
    registros = res["cant"]
    cerrarConexion()
    return f"Hay {registros} usuarios registrados"
