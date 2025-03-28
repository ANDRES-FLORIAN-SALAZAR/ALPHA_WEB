# Generated by Django 5.1.6 on 2025-03-20 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telefono', models.CharField(max_length=15)),
                ('contraseña', models.CharField(max_length=100)),
                ('edad', models.IntegerField(blank=True, null=True)),
                ('genero', models.CharField(blank=True, choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')], max_length=50, null=True)),
                ('nombre_empresa', models.CharField(blank=True, max_length=100, null=True)),
                ('nit', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('direccion_empresa', models.CharField(blank=True, max_length=255, null=True)),
                ('rol', models.CharField(choices=[('Administrador', 'Administrador'), ('Empresa', 'Empresa'), ('Usuario', 'Usuario')], default='Usuario', max_length=50)),
            ],
        ),
    ]
