# Generated by Django 5.0.3 on 2024-04-08 20:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_recipe_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='favorited_by',
            field=models.ManyToManyField(blank=True, related_name='favorite_recipes', to=settings.AUTH_USER_MODEL),
        ),
    ]
