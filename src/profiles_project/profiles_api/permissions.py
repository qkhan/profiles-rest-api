from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile."""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile."""
        #print ("USER ID: " , request.user.id)
        print ("REQUEST: ", request.user.id)
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class PostOwnStatus(permissions.BasePermission):
    """Allow users to update their own status."""

    def has_object_permission(self, request, view, obj):
        print ("REQUEST: ", request.user.id)
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
