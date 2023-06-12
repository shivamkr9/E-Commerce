from rest_framework import viewsets, status
from product import serializers
from rest_framework.settings import api_settings
from rest_framework import generics, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from db.models import Product, Category


class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS


class IsEmployee(permissions.BasePermission):

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


class CatoegoryView(viewsets.ModelViewSet):
    """Manage the authenticated user."""

    serializer_class = serializers.CategorySerializer
    authentication_classes = api_settings.DEFAULT_AUTHENTICATION_CLASSES
    permission_classes = [IsEmployee]
    queryset = Category.objects.all()


class ProductView(viewsets.ModelViewSet):
    """Manage the authenticated user."""

    serializer_class = serializers.ProductSerializer
    authentication_classes = api_settings.DEFAULT_AUTHENTICATION_CLASSES
    permission_classes = [IsEmployee]
    queryset = Product.objects.all()

    def _params_to_ints(self, qs):
        """Convert a list of strings to integers."""
        return [int(str_id) for str_id in qs.split(",")]

    # if we want to filter by login user
    # def get_queryset(self):
    #     """Retrieve recipes for authenticated user."""
    #     queryset = self.queryset
    #     return queryset.filter(
    #         user=self.request.user
    #     ).order_by('-id').distinct()

    def get_queryset(self):
        """Retrieve recipes for authenticated user."""
        queryset = self.queryset
        return queryset.filter().order_by("-id").distinct()

    def get_serializer_class(self):
        """Return the serializer class for request."""
        if self.action == "list":
            return serializers.ProductSerializer
        elif self.action == "upload_image":
            return serializers.ProductImageSerializer

        return self.serializer_class

    # add the login user during create of product
    # def perform_create(self, serializer):
    #     """Create a new product."""
    #     serializer.save(user=self.request.user)

    @action(methods=["POST"], detail=True, url_path="upload-image")
    def upload_image(self, request, pk=None):
        """Upload an image to recipe."""
        recipe = self.get_object()
        serializer = self.get_serializer(recipe, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
