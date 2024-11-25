from rest_framework.permissions import BasePermission


class WarehouseWritePermission(BasePermission):
    message = "No sufficient permissions"

    def has_permission(self, request, view):
        return request.user.profile == "client"


