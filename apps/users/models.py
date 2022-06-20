from django.db import models
from django.contrib.auth.models import AbstractUser

ROLE_CHOICES = (
    ('Front-end', 'Front-end'),
    ('Back-end', 'Back-end'),
    ('PM', 'PM'),
    ('Designer', 'Designer')
)


class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    image = models.ImageField()
    role = models.CharField(choices=ROLE_CHOICES, max_length=255)

    def __str__(self):
        return str(self.username)
