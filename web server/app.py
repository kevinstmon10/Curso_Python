from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

import jwt
import datetime as dt
import bson

# app es la estrucutra base de la api
app = Flask(__name__)
# Variables globales de la API
app.config['MONGO_URI'] = 'mongodb+srv://API:EIYK4pbopY9FQhk8@diamond.yzzxh.mongodb.net/Curso?ssl=true&ssl_cert_reqs=CERT_NONE'
app.config['SECRET_KEY'] = '%HFG·13j$'
# Realizar operaciones en la base de datos
mongo = PyMongo(app)

#  Respuesta Json por defecto


def Res(status, message, code):
    response = jsonify({
        'status': status,
        'message': message
    })
    response.status_code = code
    return response


@app.route('/', methods=['GET'])
def index():

    return "<div>Hola</div>"

# crear ruta para registrarse


@app.route('/register', methods=['POST'])
def register():

    #  Recibir los datos del cliente y verificarlos
    try:
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
    except:
        return Res('error', 'Llene todos los campos', 400)

    # Verificar si el usuario ya existe en la base de datos
    issetUser = mongo.db.users.find_one(
        {"$or": [{"username": username}, {"email": email}]})

    if issetUser == None:
        # encriptar la contraseña
        passwordEncrypted = generate_password_hash(password)
        user = {
            'username': username,
            'email': email,
            'password': passwordEncrypted
        }
        try:
            # Insertar en la base de datos
            mongo.db.users.insert(user)
            return Res('success', 'usuario insertado correctamente', 200)
        except:
            return Res('error', 'error al insertar el usuario', 400)
    else:
        return Res('error', 'el usuario ya existe', 200)


@app.route('/login', methods=['POST'])
def login():
    try:
        username = request.form['username']
        password = request.form['password']
    except:
        print("ingrese todos los datos")

    # Verificar si el usuario existe
    user = mongo.db.users.find_one({'username': username})
    print(user)
    if user != None:
        # verificar la contraseña
        if check_password_hash(user['password'], password):
            # token
            token = {
                'id': str(user['_id']),
                'username': user['username'],
                'email': user['email'],
                'exp':  datetime.utcnow()+dt.timedelta(days=30)  # expiracion
            }

            # crear el token
            tokenFinal = jwt.encode(token, app.config['SECRET_KEY'])

            return jsonify({
                'status': 'success',
                'message': 'login correcto',
                'token': tokenFinal
            })

        else:
            return Res('error', 'usuario o contraseña incorrecto', 200)

    else:
        return Res('error', 'el usuario no existe', 404)

    return "ok"


# inicia el servidor
if __name__ == '__main__':
    app.run(debug=True)
