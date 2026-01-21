from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework_api_key.permissions import HasAPIKey

class IsAuthenticatedOrHasAPIKey(BasePermission):
    """
    Custom permission to allow access if the user is authenticated
    or if a valid API key is provided.
    """

    def has_permission(self, request, view):
        return (
            IsAuthenticated().has_permission(request, view)
            or HasAPIKey().has_permission(request,view)
        )