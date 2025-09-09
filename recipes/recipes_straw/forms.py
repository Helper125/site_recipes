# import datetime

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CustomUser
# from django.core.exceptions import ValidationError
# from .models import
# import re

class Register(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'photos_profil', 'email', 'password1', 'password2']

    def clean_username(self):
        return self.cleaned_data['username']