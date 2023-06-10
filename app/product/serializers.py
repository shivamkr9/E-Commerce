
from rest_framework import serializers
from db.models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    """Serializer for the user object."""

    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ["id"]

class ProductSerializer(serializers.ModelSerializer):
    """Serializer for the user object."""

    class Meta:
        model = Product
        exclude = ["created_at", "updated_at"]
        read_only_fields = ["id"]