# Generated by Django 4.1.4 on 2023-01-08 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0004_remove_goal_is_deleted_alter_goal_status_goalcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'К выполнению'), (2, 'В процессе'), (3, 'Выполнено'), (4, 'Архив')], default=1, verbose_name='Статус'),
        ),
    ]
