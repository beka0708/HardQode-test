# Generated by Django 5.0.2 on 2024-03-02 19:48

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0007_alter_accessstudents_product_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="accessstudents",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="access_students",
                to="products.product",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="date_start",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 3, 2, 19, 48, 17, 254971, tzinfo=datetime.timezone.utc
                ),
                null=True,
            ),
        ),
    ]