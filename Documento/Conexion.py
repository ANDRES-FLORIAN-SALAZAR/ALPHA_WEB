import sqlite3

# Crear conexión a la base de datos
conn = sqlite3.connect('database.db')
print("Base de datos abierta con éxito")

# Crear tabla
conn.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    edad INTEGER NOT NULL,
    genero TEXT NOT NULL,
    email TEXT NOT NULL,
    telefono TEXT NOT NULL
);
''')
print("Tabla creada con éxito")
conn.close()

