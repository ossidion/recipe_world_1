# Generated by Django 5.1.2 on 2024-11-01 16:11

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_app', '0005_rename_content_recipe_recipe_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
