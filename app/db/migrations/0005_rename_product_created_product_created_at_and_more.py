# Generated by Django 4.2.2 on 2023-06-11 10:02

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("db", "0004_remove_product_user"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="product_created",
            new_name="created_at",
        ),
        migrations.RenameField(
            model_name="product",
            old_name="product_updated",
            new_name="updated_at",
        ),
    ]
