from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):

        if obj.user == request.user:
            return True
        return False

class IsEmptyOwner(BasePermission):

    def has_object_permission(self, request, view, obj):

        if obj.user is None:
            return True

        return False

class IsPublic(BasePermission):

    def has_object_permission(self, request, view, obj):
        if obj.is_public == True:
            return True
        return False
