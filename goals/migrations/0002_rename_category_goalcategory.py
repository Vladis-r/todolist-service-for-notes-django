# Generated by Django 4.1.4 on 2023-01-07 10:35

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('goals', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='GoalCategory',
        ),
    ]
