# Generated by Django 3.2.23 on 2023-12-13 08:42

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pp4app', '0008_alter_comment_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='review',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comments_review', to='pp4app.review'),
        ),
    ]
