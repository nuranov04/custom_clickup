from django.db import models

from apps.users.models import User

STATUS_CHOICES = (
    ('active', 'active'),
    ('inactive', 'inactive'),
    ('pause', 'pause')
)


class Project(models.Model):
    caption = models.CharField(max_length=255)
    start = models.DateField()
    redline = models.DateField()
    deadline = models.DateField()
    developers = models.ManyToManyField(User, related_name='developers')
    status = models.CharField(choices=STATUS_CHOICES, max_length=255)

    def __str__(self):
        return str(self.caption)
