from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow owners of object to edit it
    """

    def has_object_permission(self, request, vew, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user


class IsOwner(permissions.BasePermission):
    """
    Custom permission to allow owners of object to edit it
    """

    def has_object_permission(self, request, vew, obj):
        return obj.owner == request.user
