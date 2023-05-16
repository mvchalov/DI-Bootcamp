from rest_framework import permissions

class IsYossi(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.username == 'yossi':
            return False
        return True



