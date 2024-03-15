
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register,login
from . import views



urlpatterns = [
    
    path('', login, name='login'),
   
    path('register/', register, name='register'),
  
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('index/', views.index, name='index',),
]


