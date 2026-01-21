from django.contrib.auth import get_user_model
from rest_framework import viewsets
from .models import UserProfile
from .serializers import UserSerializer, UserProfileSerializer
from drf_spectacular.utils import extend_schema, OpenApiExample
from .permissions import IsAuthenticatedOrHasAPIKey

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrHasAPIKey]
    queryset = User.objects.all().order_by("id")
    serializer_class = UserSerializer

    @extend_schema(
        summary="Create a new user",
        description="Create a new user with the provided details.",
        examples=[
            OpenApiExample(
                "Create User Example",
                value={
                    "username": "Pedro Rua",
                    "email": "pedrorua@gmail.com",
                    "first_name": "New",
                    "last_name": "User",
                    "password": "securepassword123",
                },
                request_only=True,
            ),
        ],
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
class UserProfileViewSet(viewsets.ModelViewSet):
    """
    Manage user profiles.
    - list: Get all profiles
    - create: Create a profile
    """
    permission_classes = [IsAuthenticatedOrHasAPIKey]
    queryset = UserProfile.objects.select_related('user').all()
    serializer_class = UserProfileSerializer
    
    