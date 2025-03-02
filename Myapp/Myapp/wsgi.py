"""
WSGI config for Myapp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""
sys.path.append('/home/andres/Escritorio/PROGRAMACIÓN/APLICACIONES WEB/ALPHA_WEB/Myapp')
import os

from django.core.wsgi import get_wsgi_application
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Myapp.settings')

application = get_wsgi_application()
