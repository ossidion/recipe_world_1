# Generated by Django 5.1.2 on 2024-10-31 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_app', '0002_recipe_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='image',
        ),
    ]
