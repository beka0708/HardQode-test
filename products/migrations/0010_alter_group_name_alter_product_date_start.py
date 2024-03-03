# Generated by Django 5.0.2 on 2024-03-02 21:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0009_group_start_datetime_alter_product_date_start"),
    ]

    operations = [
        migrations.AlterField(
            model_name="group",
            name="name",
            field=models.CharField(
                default="default_group the <django.db.models.fields.related.ForeignKey>",
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="date_start",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 3, 2, 21, 15, 16, 428711, tzinfo=datetime.timezone.utc
                ),
                null=True,
            ),
        ),
    ]