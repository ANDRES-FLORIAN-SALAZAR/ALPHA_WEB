from django import forms
from django.contrib.auth.models import User
from .models import PerfilUsuario

class RegistroForm(forms.ModelForm):
    username = forms.CharField(max_length=30, required=True)
    password = forms.CharField(widget=forms.PasswordInput)
    telefono = forms.CharField(max_length=15, required=False)
    direccion = forms.CharField(max_length=255, required=False)
    char_length = forms.IntegerField(min_value=1, max_value=20, initial=8)
    min_nums = forms.IntegerField(min_value=0, max_value=20, initial=1)
    min_minus = forms.IntegerField(min_value=0, max_value=20, initial=1)
    min_mayus = forms.IntegerField(min_value=0, max_value=20, initial=1)
    min_simbolos = forms.IntegerField(min_value=0, max_value=20, initial=1)

    class Meta:
        model = User
        fields = ['username', 'password', 'telefono', 'direccion', 'char_length', 'min_nums', 'min_minus', 'min_mayus', 'min_simbolos']
