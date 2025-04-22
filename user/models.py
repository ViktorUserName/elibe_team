from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('author', 'Автор'),
        ('reader', 'Читатель'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='author')

    def __str__(self):
        return f'{self.username} -- ({self.role})'
