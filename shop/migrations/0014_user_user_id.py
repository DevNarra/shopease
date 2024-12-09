# Generated by Django 4.2.16 on 2024-12-09 18:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0013_alter_user_options_alter_user_managers_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="user_id",
            field=models.UUIDField(default=uuid.uuid1, editable=False, unique=True),
        ),
    ]