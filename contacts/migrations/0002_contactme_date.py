# Generated by Django 3.1.7 on 2021-02-26 10:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactme',
            name='date',
            field=models.DateField(default=datetime.date(2021, 2, 26)),
        ),
    ]
