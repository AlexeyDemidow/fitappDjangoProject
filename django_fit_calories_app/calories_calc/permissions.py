from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Разрешение для изменения создателем или только просмотр"""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return [i.get('id') for i in obj.customer.values('id')][0] == request.user.id