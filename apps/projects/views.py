from rest_framework import viewsets

from apps.projects.models import Project
from apps.projects.serializers import ProjectSerializer


class ProjectApiViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
