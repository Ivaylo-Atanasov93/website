# Generated by Django 3.1.7 on 2021-03-12 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biography', '0007_biography_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='biography',
            name='picture',
        ),
        migrations.AddField(
            model_name='biography',
            name='picture_url',
            field=models.CharField(default=0, max_length=500),
            preserve_default=False,
        ),
    ]