# Generated by Django 2.2 on 2021-01-06 09:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210106_0309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created_data',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 6, 15, 6, 59, 229101)),
        ),
    ]
