from rest_framework import permissions


class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Instance must have an attribute named `owner`.
        return obj.owner and (obj.owner == request.user or request.user.is_staff)


class OwnerPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if view.action in ["update", "partial_update", "destroy"]:
            # Instance must have an attribute named `owner`.
            return obj.owner and (obj.owner == request.user or request.user.is_staff)
        return True


class UserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == "list":
            return request.user.is_authenticated and request.user.is_staff
        elif view.action == "create":
            return True
        elif view.action in ["retrieve", "update", "partial_update", "destroy"]:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False
        if view.action == "retrieve":
            return True
        elif view.action in ["update", "partial_update"]:
            return obj == request.user or request.user.is_staff
        elif view.action == "destroy":
            return request.user.is_staff
        else:
            return False
