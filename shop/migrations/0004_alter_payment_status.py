# Generated by Django 4.2.16 on 2024-12-10 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0003_payment_status_payment_transaction_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payment",
            name="status",
            field=models.CharField(
                choices=[("Pending", "Pending"), ("Success", "Success")], max_length=100
            ),
        ),
    ]
