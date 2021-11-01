from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.SlugField(max_length=40, required=True)
    last_name = forms.SlugField(max_length=40, required=True)
    email = forms.EmailField(max_length=100, help_text='youremail@example.com')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2', 'email')
