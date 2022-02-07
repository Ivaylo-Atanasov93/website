# Generated by Django 3.1.7 on 2022-02-07 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biography', '0008_auto_20210312_1225'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='biography',
        ),
        migrations.RemoveField(
            model_name='languages',
            name='biography',
        ),
        migrations.RemoveField(
            model_name='passions',
            name='biography',
        ),
        migrations.RemoveField(
            model_name='personalexperience',
            name='biography',
        ),
        migrations.RemoveField(
            model_name='workexperience',
            name='biography',
        ),
        migrations.RemoveField(
            model_name='biography',
            name='address',
        ),
        migrations.RemoveField(
            model_name='biography',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='biography',
            name='email',
        ),
        migrations.RemoveField(
            model_name='biography',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='biography',
            name='name',
        ),
        migrations.RemoveField(
            model_name='biography',
            name='nationality',
        ),
        migrations.RemoveField(
            model_name='biography',
            name='number',
        ),
        migrations.RemoveField(
            model_name='biography',
            name='picture_url',
        ),
        migrations.RemoveField(
            model_name='biography',
            name='specialization',
        ),
        migrations.AddField(
            model_name='biography',
            name='academic_achievements',
            field=models.TextField(default='No Academic Achievements saved', max_length=500),
        ),
        migrations.AddField(
            model_name='biography',
            name='childhood_1',
            field=models.TextField(default='No Childhood 1 saved', max_length=240),
        ),
        migrations.AddField(
            model_name='biography',
            name='childhood_2',
            field=models.TextField(default='No Childhood 2 saved', max_length=290),
        ),
        migrations.AddField(
            model_name='biography',
            name='childhood_3',
            field=models.TextField(default='No Childhood 3 saved', max_length=400),
        ),
        migrations.AddField(
            model_name='biography',
            name='final_thoughts',
            field=models.TextField(default='No Final Thoughts saved', max_length=1340),
        ),
        migrations.AlterField(
            model_name='biography',
            name='summary',
            field=models.TextField(max_length=800),
        ),
        migrations.DeleteModel(
            name='Achievements',
        ),
        migrations.DeleteModel(
            name='Education',
        ),
        migrations.DeleteModel(
            name='Languages',
        ),
        migrations.DeleteModel(
            name='Passions',
        ),
        migrations.DeleteModel(
            name='PersonalExperience',
        ),
        migrations.DeleteModel(
            name='WorkExperience',
        ),
    ]