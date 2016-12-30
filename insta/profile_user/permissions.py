from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        #  we'll always allow GET, HEAD or OPTIONS requests.
        # so if someone send those requests , he will always get True
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        # so we will check if the user that send the request , is the user that upload the post
        return obj.user.user == request.user

