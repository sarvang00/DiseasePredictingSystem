from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registration_page', views.registration_page, name='registration_page'),
    path('register_user', views.register_user, name='register_user'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout')
]