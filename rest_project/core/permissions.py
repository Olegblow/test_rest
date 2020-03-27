from rest_framework import permissions


class IsOwnerOrApiKey(permissions.BasePermission):
    """
    Допуск по owner или по apikey
    """

    def has_object_permission(self, request, view, obj):
        api_key = request.GET.get('api_key')
        api_key_permission = False
        if api_key:
            api_key_permission = obj.api_key == api_key

        return obj.user == request.user or api_key_permission
