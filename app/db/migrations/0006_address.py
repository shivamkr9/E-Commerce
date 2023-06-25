# Generated by Django 4.2.2 on 2023-06-12 18:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("db", "0005_rename_product_created_product_created_at_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Address",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("mobile", models.BigIntegerField()),
                ("pincode", models.IntegerField()),
                ("state", models.CharField(max_length=255)),
                ("city", models.CharField(max_length=255)),
                ("address", models.CharField(max_length=255)),
                ("landmark", models.CharField(max_length=255)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]