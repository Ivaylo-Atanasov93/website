# Generated by Django 3.1.7 on 2021-02-24 17:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('booking_form', '0003_auto_20210224_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='time',
            field=models.TimeField(default=datetime.datetime(2021, 2, 24, 17, 53, 55, 831093, tzinfo=utc)),
        ),
    ]
