# Generated by Django 3.1.5 on 2021-01-27 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='pick_up_time',
            field=models.TimeField(),
        ),
    ]
