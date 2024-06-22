from django.urls import path
from . import views

urlpatterns = [

    # http://localhost:8000/clothing/clothes
    path("fashion", views.fashion, name="fashion"),

    # http://localhost:8000/clothing
    path("", views.list, name="clothing"),

    # http://localhost:8000/clothing/details/id
    path("details/<int:id>", views.details, name="details"),

    # http://localhost:8000/clothing/new
    path("new", views.insert, name="insert"),

    # http://localhost:8000/clothing/edit/id
    path("edit/<int:id>", views.edit, name="edit"),

    # http://localhost:8000/clothing/delete/id
    path("delete/<int:id>", views.delete, name="delete"),

    # http://localhost:8000/clothing/info
    path("info", views.info, name="info"),
]