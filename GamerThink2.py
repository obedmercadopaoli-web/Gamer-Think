from flask import Flask, request, jsonify

app = Flask(__name__)

# Lista en memoria para almacenar usuarios
usuarios = []

# GET /info
# Devuelve información del sistema

@app.route('/info', methods=['GET'])
def info():
    return jsonify({
        "sistema": "Gamer-Think API",
        "descripcion": "API para gestión básica de usuarios",
        "version": "1.0",
        "autor": "Obed Y Mercado Paoli"
    }), 200

# POST /crear_usuario
# Recibe nombre y correo en JSON

@app.route('/crear_usuario', methods=['POST'])
def crear_usuario():
    data = request.get_json()

    # Validar que se envió JSON
    if not data:
        return jsonify({
            "error": "Debe enviar datos en formato JSON"
        }), 400

    nombre = data.get("nombre")
    correo = data.get("correo")

    # Validar campos obligatorios
    if not nombre or not correo:
        return jsonify({
            "error": "Los campos 'nombre' y 'correo' son obligatorios"
        }), 400

    # Crear usuario
    nuevo_usuario = {
        "id": len(usuarios) + 1,
        "nombre": nombre,
        "correo": correo
    }

    usuarios.append(nuevo_usuario)

    return jsonify({
        "mensaje": "Usuario creado correctamente",
        "usuario": nuevo_usuario
    }), 201
    
# GET /usuarios
# Devuelve lista de usuarios

@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    if len(usuarios) == 0:
        return jsonify({
            "mensaje": "No hay usuarios registrados",
            "usuarios": []
        }), 200

    return jsonify({
        "total_usuarios": len(usuarios),
        "usuarios": usuarios
    }), 200


# Ejecutar servidor
if __name__ == '__main__':
    print("Starting GamerThink2 Flask app...")
    app.run(debug=True)
    print("App.run returned, exiting.")