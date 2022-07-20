"""Users URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from users.views import user

router = DefaultRouter()
router.register(r'', user.UserViewSet, basename='users')

users_patterns = [
    path('', user.user_list),
    path('/auth/', include(router.urls)),
    path('/<int:pk>', user.user_one),
]