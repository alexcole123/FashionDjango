from django.forms import EmailInput, ModelForm, PasswordInput, TextInput
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class RegistrationForm(ModelForm):

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password"]
        widgets = {
            "first_name": TextInput(attrs= {"class": "form-control", "minlength": 2, "maxlength": 30}),
            "last_name": TextInput(attrs= {"class": "form-control", "minlength": 2, "maxlength": 30}),
            "email": EmailInput(attrs= {"class": "form-control", "maxlength": 100}),
            "password": PasswordInput(attrs= {"class": "form-control", "minlength": 4, "maxlength": 100}),
        }

    #Override save
    def save(self):
        #Create user without saving in database
        user = super().save(commit = False) 

        #enter email into username
        user.username = self.cleaned_data["email"]

        #Hash password
        user.password = make_password(self.cleaned_data["password"])

        #save user in database 
        user.save()

        #return user
        return user
    
#---------------------------------------
#Login form model:  
class LoginForm(ModelForm):

    class Meta:
        model = User
        fields = ["email", "password"]
        widgets = {
            "email": EmailInput(attrs= {"class": "form-control", "maxlength": 100}),
            "password": PasswordInput(attrs= {"class": "form-control", "minlength": 4, "maxlength": 100}),
        }

