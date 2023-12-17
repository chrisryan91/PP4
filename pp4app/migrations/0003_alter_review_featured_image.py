# Generated by Django 3.2.23 on 2023-12-17 11:17

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pp4app', '0002_alter_review_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
