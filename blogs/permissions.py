from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdmin(BasePermission):
    """
    Allows full access to admin users.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role == "admin"


class IsEditor(BasePermission):
    """
    Allows access to editors for their own posts.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role == "editor"


class IsUser(BasePermission):
    """
    Allows read-only access to authenticated viewers.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role == "user"


    def has_object_permission(self, request, view, obj):
        # Viewers can only read posts
        return request.method in SAFE_METHODS
