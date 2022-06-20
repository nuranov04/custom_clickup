from django.urls import path

from apps.users.views import UserListCreateAPIView, UserDetailAPIView


urlpatterns = [
    path("users/<int:pk>/", UserDetailAPIView.as_view(), name='user_detail'),
    path("users/", UserListCreateAPIView.as_view(), name='users')
]