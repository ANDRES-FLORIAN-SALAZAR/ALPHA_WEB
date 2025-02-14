from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistroForm

def inicio_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('inicio')
    else:
        form = AuthenticationForm()
    return render(request, 'inicio_sesion.html', {'form': form})

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('inicio_sesion')
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})

def crear_contraseña(configuracion):
    import random
    import string

    char_length = configuracion.char_length
    min_nums = configuracion.min_nums
    min_minus = configuracion.min_minus
    min_mayus = configuracion.min_mayus
    min_simbolos = configuracion.min_simbolos

    password = []

    def crear_numero():
        return random.choice(string.digits)

    def crear_letra_minuscula():
        return random.choice(string.ascii_lowercase)

    def crear_letra_mayuscula():
        return random.choice(string.ascii_uppercase)

    def crear_simbolo():
        simbolos = "!@#$%^&*()_+[]{}|;:,.<>?"
        return random.choice(simbolos)

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

        while len(password) < char_length:
            funciones = [crear_numero, crear_letra_minuscula, crear_letra_mayuscula, crear_simbolo]
            password.append(random.choice(funciones)())

    random.shuffle(password)
    return ''.join(password)
