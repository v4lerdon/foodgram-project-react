from rest_framework.permissions import BasePermission, IsAuthenticated


class IsOwnerProfile(IsAuthenticated):
    """Проверка владельца профиля."""
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsAdmin(BasePermission):
    """Проверка на админа."""
    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            request.user.is_staff
        )
