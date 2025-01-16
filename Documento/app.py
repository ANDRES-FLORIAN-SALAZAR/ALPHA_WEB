from flask import Flask, request, render_template, send_from_directory
import random

app = Flask(__name__, static_folder='assets')

# Función para crear un número aleatorio
def crear_numero():
    return str(random.randint(0, 9))

# Función para crear una letra minúscula aleatoria
def crear_letra_minuscula():
    letras = "abcdefghijklmnopqrstuvwxyz"
    i = random.randint(0, (len(letras)-1))
    return letras[i]

# Función para crear una letra mayúscula aleatoria
def crear_letra_mayuscula():
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    i = random.randint(0, (len(letras)-1))
    return letras[i]

# Función para crear un símbolo aleatorio
def crear_simbolo():
    simbolos = "!@#$%&/()=?¡¿*`^[]+´´¨¨¨{}Ç,;:.-_"
    i = random.randint(0, (len(simbolos)-1))
    return simbolos[i]

# Función para crear una contraseña con especificaciones
def crear_contraseña(char_length, min_nums, min_minus, min_mayus, min_simbolos):
    
    # Verifica si la suma de los caracteres no exceda el limite establecido
    if min_nums + min_minus + min_mayus + min_simbolos > char_length:
        return "Los valores que ingresaste no son válidos, intenta nuevamente."

    password = []
    # Genera la contraseña según las especificaciones
    while len(password) < char_length:
        if min_nums > 0:
            password.append(crear_numero())
            min_nums -= 1
        if min_minus > 0 and len(password) < char_length:
            password.append(crear_letra_minuscula())
            min_minus -= 1
        if min_mayus > 0 and len(password) < char_length:
            password.append(crear_letra_mayuscula())
            min_mayus -= 1
        if min_simbolos > 0 and len(password) < char_length:
            password.append(crear_simbolo())
            min_simbolos -= 1
            
        # Completa la contraseña con caracteres aleatorios dentro del limite ya especificado
        while len(password) < char_length:
            functions = [crear_numero, crear_letra_minuscula, crear_letra_mayuscula, crear_simbolo]
            password.append(functions[random.randint(0, len(functions)-1)]())
    
    random.shuffle(password)
    return ''.join(password)

@app.route('/')
def index():
    return render_template('Contraseñas.html')

@app.route('/submit_password', methods=['POST'])
def submit_password():
    char_length = int(request.form['char_length'])
    min_nums = int(request.form['min_nums'])
    min_minus = int(request.form['min_minus'])
    min_mayus = int(request.form['min_mayus'])
    min_simbolos = int(request.form['min_simbolos'])
    
    password = crear_contraseña(char_length, min_nums, min_minus, min_mayus, min_simbolos)
    return f"<center><h2>Tu contraseña generada es: {password}</h2></center><br><br><br><br><br>"

if __name__ == '__main__':
    app.run(debug=True)
