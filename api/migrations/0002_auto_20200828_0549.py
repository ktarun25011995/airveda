# Generated by Django 3.1 on 2020-08-28 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='humidityreading',
            name='reading',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='temperaturereading',
            name='reading',
            field=models.JSONField(default=dict),
        ),
    ]
