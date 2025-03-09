from django.urls import path
from Aplicacion import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('Inicio/', views.Inicio, name='Inicio'),
    path('Planes/', views.Planes, name='Planes'),
    path('Inicio_Sesión/', views.Inicio_Sesión, name='Inicio_Sesión'),
    path('Registro/', views.Registro, name='Registro'),
    path('Contraseñas/', views.Contraseñas, name='Contraseñas'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
