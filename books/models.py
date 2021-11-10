from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_admin = models.BooleanField(default=False)

    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    URL = models.CharField(max_length=255, blank=True, null=True)
    imgURL = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)