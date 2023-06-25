from rest_framework import serializers
from db.models import Product, Category, Order


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for the user object."""

    class Meta:
        model = Category
        fields = "__all__"
        read_only_fields = ["id"]


class ProductSerializer(serializers.ModelSerializer):
    """Serializer for the user object."""

    class Meta:
        model = Product
        exclude = ["created_at", "updated_at"]
        read_only_fields = ["id"]

    def to_representation(self, instance):
        self.fields["product_categoty"] = CategorySerializer(read_only=True)
        return super(ProductSerializer, self).to_representation(instance)

    def validate(self, attrs):
        if attrs["price"] < 0 or attrs["price"] == 0:
            raise serializers.ValidationError("Price must be greater than 0")
        if attrs["discount_price"] < 0 or attrs["discount_price"] > attrs["price"]:
            raise serializers.ValidationError(
                "Discount price must be greater than 0 and less than price"
            )
        if attrs["quantity_in_stock"] < 0:
            raise serializers.ValidationError("Quantity must be greater than 0")
        return super().validate(attrs)


class ProductImageSerializer(serializers.ModelSerializer):
    """Serializer for uploading images to Product."""

    class Meta:
        model = Product
        fields = [
            "id",
            "product_image1",
            "product_image2",
            "product_image3",
            "product_image4",
            "product_image5",
        ]
        read_only_fields = ["id"]
        extra_kwargs = {
            "product_image1": {"required": "True"},
            "product_image2": {"required": "True"},
            "product_image3": {"required": "True"},
            "product_image4": {"required": "True"},
            "product_image5": {"required": "True"},
        }


class OrderCreateSerializer(serializers.ModelSerializer):
    """Serializer for the user object."""

    class Meta:
        model = Order
        exclude = ["created_at","user"]
        read_only_fields = ["id"]

    # def validate(self, attrs):
    #     if attrs["quantity"] < 0 or attrs["quantity"] == 0:
    #         raise serializers.ValidationError("Quantity must be greater than 0")
    #     return super().validate(attrs)

    def to_representation(self, instance):
        self.fields["product"] = ProductSerializer(read_only=True)
        return super(OrderCreateSerializer, self).to_representation(instance)