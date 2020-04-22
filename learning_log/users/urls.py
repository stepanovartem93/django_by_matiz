from django.urls import path
from django.contrib.auth.views import auth_login as login

from . import views

app_name = 'users'

urlpatterns = [
    path(r'login/', login, {'template_name': 'users/login.html'}, name='login'),
]
