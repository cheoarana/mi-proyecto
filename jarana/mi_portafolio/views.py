from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile

# Create your views here.

def index(request):
    return render(request,'mi_portafolio/index.html',{})

def mis_datos(request):
    data = {
        "nombre":"Julian",
        "apellido":"Arana",
        "skills":["Python 3.10+","HTML5","SQL","Git","Django 5"]
        }
    return render(request,'mi_portafolio/misdatos.html',{'data':data})

def list_profiles(request):
    profile_list = Profile.objects.all().order_by('age')
    return render(request,"mi_portafolio/profile.html",{"profile_list":profile_list})
