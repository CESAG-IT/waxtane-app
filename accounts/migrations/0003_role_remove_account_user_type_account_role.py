# Generated by Django 5.0.6 on 2024-07-19 18:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "accounts",
            "0002_remove_account_is_customer_remove_account_is_owner_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="Role",
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
                ("name", models.CharField(default="user", max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name="account",
            name="user_type",
        ),
        migrations.AddField(
            model_name="account",
            name="role",
            field=models.ForeignKey(
                default="user",
                on_delete=django.db.models.deletion.CASCADE,
                to="accounts.role",
            ),
        ),
    ]
