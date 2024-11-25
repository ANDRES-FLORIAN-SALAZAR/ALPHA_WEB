from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

# Conectar a la base de datos SQLite (o crearla si no existe)
def init_sqlite_db():
    conn = sqlite3.connect('mi_base_de_datos.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        apellido TEXT,
        edad INTEGER,
        genero TEXT,
        email TEXT,
        telefono TEXT
    )
    ''')
    conn.commit()
    conn.close()

init_sqlite_db()

@app.route('/')
def index():
    return render_template_string(open('index.html').read())

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        edad = request.form['edad']
        genero = request.form['genero']
        email = request.form['email']
        telefono = request.form['telefono']

        conn = sqlite3.connect('mi_base_de_datos.db')
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO usuarios (nombre, apellido, edad, genero, email, telefono)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (nombre, apellido, edad, genero, email, telefono))
        conn.commit()
        conn.close()

        return 'Datos guardados exitosamente'

if __name__ == '__main__':
    app.run(debug=True)
