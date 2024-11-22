from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Ruta principal para mostrar el formulario de registro
@app.route('/')
def registro():
    return render_template('registro.html')

# Ruta para manejar la solicitud POST del formulario
@app.route('/registro', methods=['POST'])
def registro_post():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    edad = request.form['edad']
    genero = request.form['genero']
    email = request.form['email']
    telefono = request.form['telefono']

    # Conectar a la base de datos y guardar la información
    with sqlite3.connect('database.db') as con:
        cur = con.cursor()
        cur.execute("INSERT INTO usuarios (nombre, apellido, edad, genero, email, telefono) VALUES (?, ?, ?, ?, ?, ?)",
                    (nombre, apellido, edad, genero, email, telefono))
        con.commit()
    
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
