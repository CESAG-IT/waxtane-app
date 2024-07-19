# Generated by Django 5.0.6 on 2024-07-19 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0007_alter_account_role"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="account",
            name="role",
        ),
        migrations.AddField(
            model_name="account",
            name="user_type",
            field=models.IntegerField(
                choices=[(1, "Customer"), (2, "Owner")], default=1
            ),
        ),
        migrations.DeleteModel(
            name="Role",
        ),
    ]