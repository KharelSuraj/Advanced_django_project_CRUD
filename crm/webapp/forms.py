from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Record

from django import forms 

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

# -Create a user

class CreateUserForm(UserCreationForm):
    
    class Meta:

        model = User
        fields = ['username', 'password1', 'password2']

#-User login 

class LoginForm(AuthenticationForm):
    
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
    
#- Creaing a record

class CreateRecordForm(forms.ModelForm):

    class Meta:

        model = Record
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'province', 'country']


#- Upadating a record

class UpdateRecordForm(forms.ModelForm):

    class Meta:

        model = Record
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'province', 'country']
