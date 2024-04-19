from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django.forms.widgets import PasswordInput, TextInput

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email','password1','password2')
        labels = {'username':'', 'email':'','password1':'','password2':''}

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
    
class SocialAccountForm(forms.ModelForm):
    class Meta:
        model = SocialAccount
        fields = ('specific_username', 'profile_pic', 'friend_code', 'private_code',
                   'description', 'is_public', 'is_active', 'purpose',
                     'platform')
        labels = {'specific_username':'', 'profile_pic':'', 'friend_code':'',
                  'description':'', 'is_public':'', 'purpose':'', 
                  'platform':''}

