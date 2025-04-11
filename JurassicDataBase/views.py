from django.shortcuts import render

def index(request):
    return render(request, "JurassicDataBase/index.html")

def sobre(request):
    return render(request, "JurassicDataBase/sobre.html")

# Create your views here.
