from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # Only authenticated users are allowed to view the accounts list
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        # Only the account owner can view details of their account
        return obj.user_uuid == str(request.user.user_uuid)
