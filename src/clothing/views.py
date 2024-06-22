from django.http import Http404
from django.shortcuts import render, redirect
from .models import ClothingModel, ClothingForm
from django.contrib.auth.decorators import login_required, permission_required



# Fashion view:
def fashion(request):
    context = { "active": "fashion" }
    return render(request, "fashion.html", context)

#Clothing view:
def list(request):
    clothing = ClothingModel.objects.all()
    context = { "active": "clothing", "clothing": clothing }
    return render(request, "clothing.html", context)

#Details view:
def details(request, id):
    try:
        cloth = ClothingModel.objects.get(pk = id) #pk Primary key
        context = { "clothing": cloth }
        return render(request, "details.html", context)
    except ClothingModel.DoesNotExist:
        raise Http404()

#Insert view
@login_required(login_url= "login")
def insert(request):
    if request.method == "GET":
        context = { "active": "insert", "form": ClothingForm()}
        return render(request, "insert.html", context)
    
    form = ClothingForm(request.POST)
    if not form.is_valid(): # returns true if all is valid or False if there are validations errors
        context = {"form": form}
        return render(request, "insert.html", context)
    form.save() # save in database
    return redirect("clothing")

# Edit View:
@login_required(login_url= "login")
def edit(request, id):
    try:
        if request.method == "GET":
            clothing = ClothingModel.objects.get(pk = id)
            context = { "form": ClothingForm(instance=clothing) }
            return render(request, "edit.html", context)
        
        dummy_clothing = ClothingModel(pk = id)
        form = ClothingForm(request.POST, instance=dummy_clothing)
        if not form.is_valid():
            context = { "form":form }
            return render(request, "edit.html", context)
        form.save() # save in database
        return redirect("clothing")
    except ClothingModel.DoesNotExist:
        raise Http404()

# Delete View:
@permission_required("is_superuser", login_url= "login")
def delete(request, id):
    try:
        dummy_clothing = ClothingModel(pk = id)
        dummy_clothing.delete()
        return redirect("clothing")
    except ClothingModel.DoesNotExist:
        raise Http404()

# Info view:
def info(request):
    context = { "active": "info" }
    return render(request, "info.html", context)
