# Generated by Django 4.1.1 on 2022-09-22 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list_app', '0004_alter_task_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task',
            field=models.CharField(default='Новая задача', max_length=300, verbose_name='Задача'),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(max_length=3000, verbose_name='Описание'),
        ),
    ]
