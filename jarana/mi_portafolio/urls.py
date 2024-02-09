from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('mydata/',views.mis_datos, name='mydata'),
    path('profile/',views.list_profiles,name='profile'),
    path('profile/new/',views.new_profile,name='new-profile'),
    path('view/<int:id>/',views.view_profile,name='view-profile')
]