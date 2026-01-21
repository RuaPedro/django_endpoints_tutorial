from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, UserProfileViewSet

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="user")
router.register(r"profiles", UserProfileViewSet, basename="profile")

urlpatterns = [
    path("", include(router.urls))
]