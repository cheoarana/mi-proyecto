from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hola mi portafolio. En el Index")

def mis_datos(request):
    return render(request,'mi_portafolio/misdatos.html',{})
