# Generated by Django 5.0 on 2024-02-28 10:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task_photo',
            name='tast',
        ),
        migrations.AddField(
            model_name='task_photo',
            name='task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='task_photo', to='task.task'),
        ),
    ]