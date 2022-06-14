from dataclasses import field
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Book

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField
    phone_no = forms.CharField(max_length=20)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    class Meta:
        model = User
        # fields = ['username', 'email', 'phone_no', 'password1', 'password2']
        fields = ['username', 'email', 'phone_no', 'password1', 'password2']

# TODO add a form to insert book to database
class BookUploadForm(ModelForm):
    name = forms.TextInput()
    author = forms.TextInput()
    class Meta:
        model = Book
        fields = ['name', 'author']
