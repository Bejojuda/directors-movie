from django.db import models
from django.contrib.auth.models import AbstractUser

class Director(AbstractUser):
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    category = (('action', 'Action'), ('romance', 'Romance'))

    genre = models.CharField(max_length=40, choices=category, default='action')
    
    #date_joined = models.DateTimeField()

    def __str__(self):
        return self.username
