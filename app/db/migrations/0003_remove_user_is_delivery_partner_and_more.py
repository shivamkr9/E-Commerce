# Generated by Django 4.2.2 on 2023-06-10 20:31

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("db", "0002_category_product"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="is_delivery_partner",
        ),
        migrations.RemoveField(
            model_name="user",
            name="is_distributer",
        ),
    ]
