from django.contrib.admin.options import InlineModelAdmin
from django.db import models


# Create your models here.
class Biography(models.Model):
    name = models.CharField(max_length=200, blank=False)
    picture = models.ImageField(upload_to='images')
    specialization = models.CharField(max_length=200, blank=False)
    address = models.CharField(max_length=300, blank=False)
    number = models.CharField(max_length=15, blank=False)
    email = models.EmailField(blank=False)
    nationality = models.CharField(max_length=30)
    date_of_birth = models.DateField(blank=False)
    gender = models.CharField(max_length=50)
    summary = models.TextField(max_length=3000)

    def __str__(self):
        return 'Biography'


class Education(models.Model):
    biography = models.ForeignKey(Biography, on_delete=models.CASCADE)
    start_date = models.DateField(blank=False)
    end_date = models.DateField(null=True, blank=True)
    name_of_institution = models.CharField(max_length=300, blank=False)
    speciality = models.CharField(max_length=100, blank=False)
    covered_subjects = models.TextField(max_length=1000)

    def __str__(self):
        return self.name_of_institution


class PersonalExperience(models.Model):
    biography = models.ForeignKey(Biography, on_delete=models.CASCADE)
    topic_name = models.CharField(max_length=150)
    topic_summary = models.TextField(max_length=1000)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.topic_name


class WorkExperience(models.Model):
    biography = models.ForeignKey(Biography, on_delete=models.CASCADE)
    start_date = models.DateField(blank=False)
    end_date = models.DateField(null=True, blank=True)
    position = models.CharField(max_length=150, blank=False)
    position_summary = models.TextField(max_length=1000)
    responsibilities = models.TextField(max_length=2000)

    def __str__(self):
        return self.position


class Achievements(models.Model):
    biography = models.ForeignKey(Biography, on_delete=models.CASCADE)
    accomplishment = models.TextField(max_length=500)

    def __str__(self):
        return self.accomplishment


class Languages(models.Model):
    biography = models.ForeignKey(Biography, on_delete=models.CASCADE)
    language = models.CharField(max_length=50)
    fluency = models.CharField(max_length=50)

    def __str__(self):
        return self.language


class Passions(models.Model):
    biography = models.ForeignKey(Biography, on_delete=models.CASCADE)
    passion = models.CharField(max_length=100)

    def __str__(self):
        return self.passion
