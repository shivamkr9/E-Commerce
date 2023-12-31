"""
Django custom user model
"""
import os
import uuid
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, mobile, password=None, **extra_fields):
        """Create, save and return a new user."""
        if not email:
            raise ValueError("User must have an email address.")
        if not mobile:
            raise ValueError("User must have a mobile number.")
        user = self.model(
            email=self.normalize_email(email), mobile=mobile, **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, mobile, password):
        """Create and return a new superuser."""
        user = self.create_user(email, mobile, password)
        user.is_superuser = True
        user.is_employee = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    User model for register the user on the site for different purposes
    """

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    mobile = models.BigIntegerField(blank=False, unique=True)
    is_active = models.BooleanField(default=True)
    is_employee = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["mobile"]

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


# class Address(models.Model):
#     """Address model for user."""

#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=255, blank=False, null=False)
#     mobile = models.BigIntegerField(blank=False, null=False)
#     pincode = models.IntegerField(blank=False, null=False)
#     state = models.CharField(max_length=255, blank=False, null=False)
#     city = models.CharField(max_length=255, blank=False, null=False)
#     address = models.CharField(max_length=255, blank=False, null=False)
#     landmark = models.CharField(max_length=255, blank=False, null=False)

#     def __str__(self):
#         return self.name


class Category(models.Model):
    """Product Type in the system."""

    category = models.CharField(max_length=30, unique=True)
    category_discription = models.TextField(max_length=255, blank=False)

    def __str__(self):
        return self.category


def product_image_upload_path(instance, filename):
    """Return the path for the image."""
    ext = os.path.splitext(filename)[1]
    filename = f"{uuid.uuid4()}{ext}"
    return os.path.join("product", filename)


class Product(models.Model):
    """Product in detail the system."""

    name = models.CharField(max_length=255)
    price = models.IntegerField(blank=False)
    discount_price = models.IntegerField(blank=False)
    quantity_in_stock = models.IntegerField(blank=False, null=False)
    product_image1 = models.ImageField(
        upload_to=product_image_upload_path, blank=True, null=True
    )
    product_image2 = models.ImageField(
        upload_to=product_image_upload_path, blank=True, null=True
    )
    product_image3 = models.ImageField(
        upload_to=product_image_upload_path, blank=True, null=True
    )
    product_image4 = models.ImageField(
        upload_to=product_image_upload_path, blank=True, null=True
    )
    product_image5 = models.ImageField(
        upload_to=product_image_upload_path, blank=True, null=True
    )
    brand = models.CharField(max_length=255, blank=False, null=False)
    product_categoty = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )
    dicription = models.TextField(max_length=255, blank=False)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    """Order model for user."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(blank=False, null=False, default=1)
    name = models.CharField(max_length=255, blank=False, null=False)
    mobile = models.BigIntegerField(blank=False, null=False)
    pincode = models.IntegerField(blank=False, null=False)
    state = models.CharField(max_length=255, blank=False, null=False)
    city = models.CharField(max_length=255, blank=False, null=False)
    address = models.CharField(max_length=255, blank=False, null=False)
    landmark = models.CharField(max_length=255, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.id)

    @property
    def total_price(self):
        return self.product.price * self.quantity

    @property
    def total_discount_price(self):
        return self.product.discount_price * self.quantity

    @property
    def total_saving(self):
        return self.total_price - self.total_discount_price

    @property
    def total_quantity(self):
        return self.quantity


class Transuction(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    razorpay_order_id = models.CharField(max_length=255, blank=False, null=False)
    razorpay_payment_id = models.CharField(max_length=255, blank=False, null=False)
    razorpay_signature = models.CharField(max_length=255, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.razorpay_payment_id)
