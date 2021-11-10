from django.contrib import admin
from .models import Book, User
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ["username", "email", "first_name", "last_name", "is_admin", "is_staff"]



admin.site.register(Book)
admin.site.register(User, CustomUserAdmin)