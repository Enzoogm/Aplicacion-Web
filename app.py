from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<a href="/hola">Hola</a>     <a href="/chau">Chau</a>'

@app.route('/hola')
def saludar():
    return '<h1>Aca no hay nada.</h1>'

@app.route('/chau')
def despedir():
    return '<h1>Aca menos.</h1>'