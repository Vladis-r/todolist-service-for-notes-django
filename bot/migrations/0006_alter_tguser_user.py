# Generated by Django 4.1.4 on 2023-01-12 02:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bot', '0005_alter_tguser_tg_chat_id_alter_tguser_tg_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tguser',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
