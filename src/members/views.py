from django.shortcuts import redirect, render
from members.models import LoginForm, RegistrationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

#Register new user
def register(request):

    if request.method == "GET":
        context = { "active": "register", "form": RegistrationForm() }
        return render(request, "register.html", context)
    
    form = RegistrationForm(request.POST)
    if not form.is_valid():
        context = {"active": "register", "form": form }
        return render(request, "register.html", context)
    
    user = form.save() #save in database
    login(request, user) #save user in server-side session
    messages.success(request, "Welcome" + " " + user.first_name + "!")
    return redirect("home")

#login view
def log_in(request):

    if request.method == "GET":
        context = { "active": "login", "form": LoginForm() }
        return render(request, "login.html", context)
    
    form = LoginForm(request.POST)
    if not form.is_valid():
        context = { "active": "login", "form": form}
        return render(request, "login.html", context)
    
    #Check if username and password exist in database
    #return user if exist or None if doesn't exist
    user = authenticate(request, 
                 username = form.cleaned_data["email"], 
                 password = form.cleaned_data["password"])
    
    #if user not exist
    if not user:
        messages.error(request, "Incorrect email or password.")
        context = { "active": "login", "form": form}
        return render(request, "login.html", context)
    
    #user exist
    login(request, user) #save user in server-side session
    messages.success(request, "Welcome back" + " " + user.first_name + "!")
    return redirect("home")

#Logout view
def log_out(request):
    logout(request) #remove user from server-side session
    messages.success(request, "Bye Bye")
    return redirect("home")
