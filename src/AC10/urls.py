"""
URL configuration for games project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    # http://localhost:8000
    path("", views.home, name="home"),

    # http://localhost:8000/home
    path("home", views.home, name="home"),

    # http://localhost:8000/address
    path("address", views.address, name="address"),

    # http://localhost:8000/clothing/...
    path("clothing/", include("clothing.urls")),

    # http://localhost:8000/members/...
    path("members/", include("members.urls")),

    # http://localhost:8000/api/...
    path("api/", include("api.urls")),

    path('admin/', admin.site.urls),
]
