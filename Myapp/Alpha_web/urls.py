from django.urls import path
from Myapp import views

urlpatterns = [
    path('', views.home, name='home'),
]
