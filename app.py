from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<a href="/hola">Hola</a>     <a href="/chau">Chau</a>'

@app.route('/hola')
def saludar():
    return '<h1>Aca no hay nada.</h1>'


@app.route('//<int:n1></int:n2>')
def suma (n1+n2)
    suma= n1+n2
    return f'<h1>{1} mas {2} da {suma}.</h1>'


@app.route('/sumar/<int:n1></int:n2>')
def suma (n1+n2)
    suma= n1+n2
    return f'<h1>{1} mas {2} da {suma}.</h1>'


@app.route('/chau')
def despedir():
    return '<h1>Aca menos.</h1>'
    