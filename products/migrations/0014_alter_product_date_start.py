# Generated by Django 5.0.2 on 2024-03-03 00:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0013_alter_group_name_alter_product_date_start"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="date_start",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 3, 3, 0, 35, 6, 482336, tzinfo=datetime.timezone.utc
                ),
                null=True,
            ),
        ),
    ]
