from django.db import models

class Persona(models.Model):
    # Información básica (Usuario y Administrador)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    contraseña = models.CharField(max_length=100)  # Considera encriptarla
    edad = models.IntegerField(null=True, blank=True)  # Campo opcional
    genero = models.CharField(
        max_length=50,
        choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')],
        null=True, blank=True
    )

    # Información de empresa
    nombre_empresa = models.CharField(max_length=100, null=True, blank=True)  # Opcional
    nit = models.CharField(max_length=20, unique=True, null=True, blank=True)  # Opcional
    direccion_empresa = models.CharField(max_length=255, null=True, blank=True)  # Opcional

    # Rol del usuario (Administrador, Empresa, Usuario)
    rol = models.CharField(
        max_length=50,
        choices=[('Administrador', 'Administrador'), ('Empresa', 'Empresa'), ('Usuario', 'Usuario')],
        default='Usuario'
    )

def __str__(self):
    return f"{self.nombre} {self.apellido} - {self.rol}"