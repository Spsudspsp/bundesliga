from django.contrib.auth.forms import UserCreationForm
from django import forms

from accounts.models import CustomUser


class UserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["username", "email", "first_name", "last_name"]


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
