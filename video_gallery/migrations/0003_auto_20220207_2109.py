# Generated by Django 3.1.7 on 2022-02-07 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_gallery', '0002_auto_20210223_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]