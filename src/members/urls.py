from django.urls import path
from . import views

urlpatterns = [
    #http://localhost:8000/members/register
    path("register", views.register, name = "register"),

    #http://localhost:8000/members/login
    path("login", views.log_in, name = "login"),

    #http://localhost:8000/members/logout
    path("logout", views.log_out, name = "logout"),

]