# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    # Əlavə sahələr varsa buraya əlavə edə bilərsən, məsələn:
    # phone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.username
