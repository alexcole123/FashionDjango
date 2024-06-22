from django.shortcuts import render

def home(request): #View function
    #request is an object containing request data
    return render(request, "home.html", { "active" : "home" })

def address(request): #View function
    #request is an object containing request data
    return render(request, "address.html", { "active" : "address" })

