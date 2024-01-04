from django.urls import path
from .views import *

urlpatterns = [
    path('registration/', registration, name='registration'),
    path('login/', Login, name='login'),
    path('logout/', Logout, name='logout'),
    path('forget-password/', forget_password, name='forget_password'),
    path('reset-password/', reset_password, name='reset_password'),
]