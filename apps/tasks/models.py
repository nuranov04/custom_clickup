from django.db import models

from apps.users.models import User
from apps.projects.models import Project

TASK_STATUSES = (
    ('Нужно сделать', 'Нужно сделать'),
    ('В работе', 'В работе'),
    ('Сделано', 'Сделано'),
    ('Готово к тесту', 'Готово к тесту'),
    ('Тестирование', 'Тестирование'),
    ('На доработку', 'На доработку'),
)


class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    create_at = models.DateField(auto_now_add=True)
    date_of_end = models.DateField()
    developer = models.ForeignKey(User, related_name='task', on_delete=models.CASCADE)
    project = models.ForeignKey(Project, related_name='project', on_delete=models.CASCADE)
    status = models.CharField(choices=TASK_STATUSES, max_length=255)

    def __str__(self):
        return self.title
