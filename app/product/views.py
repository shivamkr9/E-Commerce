
from rest_framework import viewsets
from product import serializers
from rest_framework.settings import api_settings
from rest_framework import generics, permissions
from db.models import Product, Category


class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS

class IsEmployee(permissions.BasePermission):

    """
    Allows access only to authenticated users if it is Employee.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_employee)

class CatoegoryView(viewsets.ModelViewSet):
    """Manage the authenticated user."""
    serializer_class = serializers.CategorySerializer
    authentication_classes = api_settings.DEFAULT_AUTHENTICATION_CLASSES
    permission_classes = [IsEmployee|ReadOnly]
    queryset = Category.objects.all()


