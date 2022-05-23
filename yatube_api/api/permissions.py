from rest_framework import permissions


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class AuthorIsOwnerOrReadOnly(permissions.BasePermission):
    edit_methods = ('PUT', 'PATCH', 'DELETE')

    def has_permission(self, request, view):
        return (
                request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated
            )

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user and request.method in self.edit_methods
        )
