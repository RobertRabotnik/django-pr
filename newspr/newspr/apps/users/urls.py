from atexit import register
from .views import *
from django.urls import URLPattern, path

app_name = 'users'

urlpatterns = [
    path('',users),
    path('register/',register,name='register'),
    path('login/',login_user,name='login'),
    path('logout/',logout_user,name='logout'),
    path('account/',account,name='account'),
]