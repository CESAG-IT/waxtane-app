# Generated by Django 5.0.6 on 2024-07-10 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("topics", "0002_topic_image_topic_is_deleted"),
    ]

    operations = [
        migrations.AlterField(
            model_name="topic",
            name="image",
            field=models.ImageField(default="default.png", upload_to="media/topics/"),
        ),
    ]
