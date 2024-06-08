# Generated by Django 4.2.2 on 2024-06-08 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0005_subscription_sent_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='sent_time',
        ),
        migrations.AddField(
            model_name='course',
            name='last_update',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Последнее обновление'),
        ),
    ]
