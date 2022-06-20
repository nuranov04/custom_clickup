from rest_framework import viewsets

from apps.tasks.models import Task
from apps.tasks.serializers import TaskSerializer


class TaskApiViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


