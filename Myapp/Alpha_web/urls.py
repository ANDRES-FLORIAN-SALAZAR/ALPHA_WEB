from django.urls import path, include
from Myapp import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('Alpha_web.urls')),
]
