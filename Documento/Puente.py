from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# Conexión a MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['registroDB']
registros = db['registros']

@app.route('/')
def index():
    return render_template('registro.html')

@app.route('/registro', methods=['POST'])
def registro():
    nombre = request.form.get('nombre')
    apellido = request.form.get('apellido')
    edad = request.form.get('edad')
    genero = request.form.get('genero')
    email = request.form.get('email')
    telefono = request.form.get('telefono')

    nuevo_registro = {
        'nombre': nombre,
        'apellido': apellido,
        'edad': edad,
        'genero': genero,
        'email': email,
        'telefono': telefono
    }

    registros.insert_one(nuevo_registro)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
