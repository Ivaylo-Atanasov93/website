# Generated by Django 3.1.7 on 2021-03-01 11:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0006_auto_20210301_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactme',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 3, 1, 11, 58, 8, 67134, tzinfo=utc)),
        ),
    ]
