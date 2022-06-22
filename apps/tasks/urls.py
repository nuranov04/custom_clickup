from rest_framework.routers import DefaultRouter

from apps.tasks.views import TaskApiViewSet

router = DefaultRouter()

router.register(
    prefix='tasks',
    viewset=TaskApiViewSet
)

urlpatterns = router.urls
