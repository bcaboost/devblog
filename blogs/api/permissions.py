from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    message = "You cannot change others' posts."

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user