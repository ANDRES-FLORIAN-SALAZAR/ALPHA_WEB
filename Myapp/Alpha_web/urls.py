from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('your_app_name.urls')),  # Replace 'your_app_name' with the name of your app
]