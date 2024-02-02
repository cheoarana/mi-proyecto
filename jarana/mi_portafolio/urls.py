from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('misdatos/',views.mis_datos, name='misdatos'),
    path('profile/',views.list_profiles,name='profile')
]