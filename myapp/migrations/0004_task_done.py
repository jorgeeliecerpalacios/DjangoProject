# Generated by Django 4.1.1 on 2022-10-03 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_rename_tittle_task_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='done',
            field=models.BooleanField(default=True),
        ),
    ]
