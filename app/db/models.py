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
        user.is_delivery_partner = True
        user.is_employee = True
        user.is_distributer = True
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
    is_delivery_partner = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    is_distributer = models.BooleanField(default=False)
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
