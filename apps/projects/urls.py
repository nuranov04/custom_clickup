from rest_framework.routers import DefaultRouter

from apps.projects.views import ProjectApiViewSet

router = DefaultRouter()
router.register(
    prefix='projects',
    viewset=ProjectApiViewSet
)

urlpatterns = router.urls