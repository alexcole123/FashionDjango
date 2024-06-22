from django.urls import path
from . import views

urlpatterns = [

    #Get http://localhost:8000/api/cloths
    path("cloths", views.get_cloths),
    
    #Get http://localhost:8000/api/cloths/id
    path("cloths/<int:id>", views.get_cloth),

    #POST http://localhost:8000/api/cloths/new
    path("cloths/new", views.add_cloth),

    #PUT http://localhost:8000/api/cloths/edit/id
    path("cloths/edit/<int:id>", views.edit_cloth),

    #DELETE http://localhost:8000/api/cloths/delete/id
    path("cloths/delete/<int:id>", views.delete_cloth),

]