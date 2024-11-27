import sqlite3

# Crear conexión a la base de datos
conn = sqlite3.connect('BASEDATOS/database.db')
print("Base de datos abierta con éxito")

# Conectar a la base de datos SQLite (o crearla si no existe)
conn = sqlite3.connect('mi_base_de_datos.db')
cursor = conn.cursor()

# Crear una tabla para almacenar los datos
cursor.execute('''
CREATE TABLE IF NOT EXISTS datos_binarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_archivo TEXT,
    contenido BLOB
)
''')
print("Tabla creada con éxito")
conn.close()#

# Leer el archivo binario
with open('ruta/al/archivo.bin', 'rb') as file:
    contenido_binario = file.read()

# Insertar los datos en la base de datos
cursor.execute('''
INSERT INTO datos_binarios (nombre_archivo, contenido)
VALUES (?, ?)
''', ('archivo.bin', contenido_binario))

# Confirmar los cambios y cerrar la conexión
conn.commit()
conn.close()

