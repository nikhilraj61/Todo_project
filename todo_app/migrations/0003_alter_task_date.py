# Generated by Django 4.0 on 2022-11-18 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0002_task_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateTimeField(default=None),
        ),
    ]