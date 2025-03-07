from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "Alpha_web/home.html", {})