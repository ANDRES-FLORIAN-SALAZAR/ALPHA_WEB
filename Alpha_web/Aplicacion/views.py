from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')   

def Planes(request):
    return render(request, 'Planes.html')

def Registro(request):
    return render(request, 'Registro.html')

def Inicio_Sesión(request):
    return render(request, 'Inicio_Sesión.html')

def Contraseñas(request):
    return render(request, 'Contraseñas.html')