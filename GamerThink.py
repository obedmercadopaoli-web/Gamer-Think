from flask import Flask, request, jsonify, redirect, url_for, render_template_string

app = Flask(__name__)

# Ruta raíz -> redirige a /mensaje
@app.route('/', methods=['GET'])
def index():
    return redirect(url_for('mensaje'))

# Ruta GET /info
@app.route('/info', methods=['GET'])
def info():
    data = {
        "nombre_app": "Gamer-Think",
        "descripcion": "Plataforma de recomendación de videojuegos",
        "version": "1.0",
        "autor": "Obed Y Mercado Paoli"
    }
    accept = request.headers.get('Accept', '')
    # Si el navegador solicita HTML, devolver una página amigable; si no, JSON
    if 'text/html' in accept:
        html = '''
        <html>
        <head><meta charset="utf-8"><title>Gamer-Think</title></head>
        <body>
            <h1>{{ nombre_app }}</h1>
            <p><strong>Descripción:</strong> {{ descripcion }}</p>
            <p><strong>Versión:</strong> {{ version }}</p>
            <p><strong>Autor:</strong> {{ autor }}</p>
            <hr>
            <p>Ir a <a href="/mensaje">/mensaje</a> para probar el endpoint de mensajes.</p>
        </body>
        </html>
        '''
        return render_template_string(html, **data)

    return jsonify(data)

# Ruta GET y POST /mensaje
@app.route('/mensaje', methods=['GET', 'POST'])
def mensaje():
    if request.method == 'GET':
        # Mensaje simple para probar en navegador
        return "Envía un POST con JSON {'mensaje': 'TuNombre'} para recibir respuesta"
    
    # Procesar POST
    data = request.get_json()
    if not data or "mensaje" not in data:
        return jsonify({"error": "Debe enviar un mensaje en formato JSON"}), 400
    
    texto = data["mensaje"]
    return jsonify({"respuesta": f"Hola {texto}, bienvenido a Gamer-Think!"})

if __name__ == '__main__':
    # Ejecutar servidor en localhost:5000
    app.run(debug=True)