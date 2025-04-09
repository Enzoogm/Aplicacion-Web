# Aplicacion-Web

Para crear un entorno virtual, desde la carpeta del proyecto usar el comando:

python -m venv .venv
---------------------------------------------------------------------------------------------------------

Para activar el entorno virtual, desde la carpeta del proyecto usar el comando:

source .venv/bin/activate
---------------------------------------------------------------------------------------------------------

Para instalar el flask (en el entorno virtual, después de activarlo) usar el comando: 

pip install flask
---------------------------------------------------------------------------------------------------------

Para verificar si está instalado el flask usar el comando: 

flask --version

Debería figurar la versión 2.3.2 o más nueva.

---------------------------------------------------------------------------------------------------------
Sirve para cuando hay un bug en la pagina tambien sirve para el auto recargado de la pagina

flask run opcions

flask run --debug
flask run -h 0.0.0.0
flask run -p 5010
