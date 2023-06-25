from rest_framework import generics, permissions


class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS


class IsEmployeeAllOtherReadOnly(permissions.BasePermission):

    """
    Allows access only to authenticated users if it is Employee.
    """

    def has_permission(self, request, view):
        return bool(
            request.method in permissions.SAFE_METHODS
            or request.user
            and request.user.is_authenticated
            and request.user.is_employee
        )


class IsEmployeeOnly(permissions.BasePermission):

    """
    Allows access only to authenticated users if it is Employee.
    """

    def has_permission(self, request, view):
        return bool(
            request.user and request.user.is_authenticated and request.user.is_employee
        )
