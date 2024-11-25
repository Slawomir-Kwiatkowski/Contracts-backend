from rest_framework.permissions import BasePermission, SAFE_METHODS


class ContractWritePermission(BasePermission):
    message = "No sufficient permissions"

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.profile == "client"


