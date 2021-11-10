from django import forms
from django.db.models import fields
from .models import Book, User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "description", "URL", "imgURL",]

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'password')