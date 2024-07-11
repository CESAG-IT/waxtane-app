# Generated by Django 5.0.6 on 2024-07-10 19:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tags", "0002_hashtag_test"),
        ("topics", "0004_remove_topic_image_topic_image_topic"),
    ]

    operations = [
        migrations.AddField(
            model_name="topic",
            name="tag_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="tags.hashtag",
            ),
        ),
    ]
