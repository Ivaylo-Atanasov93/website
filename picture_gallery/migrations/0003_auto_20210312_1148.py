# Generated by Django 3.1.7 on 2021-03-12 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picture_gallery', '0002_auto_20210223_1302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='picture',
            name='photo',
        ),
        migrations.AddField(
            model_name='picture',
            name='photo_url',
            field=models.CharField(default=0, max_length=500),
            preserve_default=False,
        ),
    ]
