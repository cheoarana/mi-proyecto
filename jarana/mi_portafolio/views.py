from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Profile
from .forms import ProfileForm


# Create your views here.

def index(request):
    return render(request,'mi_portafolio/index.html',{})

def mis_datos(request):
    data = Profile.objects.get(id=3)
    return render(request,'mi_portafolio/mydata.html',{'data':data})

def list_profiles(request):
    profile_list = Profile.objects.all().order_by('id')
    return render(request,"mi_portafolio/profile.html",{"profile_list":profile_list})

def new_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profiles_temp = Profile.objects.filter(first_name=profile.first_name,last_name=profile.last_name,address=profile.address)
            print(profiles_temp)
            if len(profiles_temp) >0:
                return redirect('index')
            else:
                profile.save()
                return redirect('profile')
    else:
        form = ProfileForm()
        return render(request,"mi_portafolio/profile-form.html",{'form':form})

def view_profile(request,id):
    profile = Profile.objects.get(id=id)
    return render(request,'mi_portafolio/view-profile.html',{'data':profile})
