from django.contrib.admin.options import InlineModelAdmin
from django.db import models


# Create your models here.
class Biography(models.Model):
    summary_title = models.CharField(max_length=255, default='Summary Title')
    summary = models.TextField(max_length=800)
    academic_achievements_title = models.CharField(max_length=255, default='Academic Achievements Title')
    academic_achievements = models.TextField(max_length=500, default='No Academic Achievements saved')
    childhood_title = models.CharField(max_length=255, default='Childhood Title')
    childhood_1 = models.TextField(max_length=240, default='No Childhood 1 saved')
    childhood_2 = models.TextField(max_length=290, default='No Childhood 2 saved')
    childhood_3 = models.TextField(max_length=400, default='No Childhood 3 saved')
    final_thoughts_title = models.CharField(max_length=255, default='Final Thoughts Title')
    final_thoughts = models.TextField(max_length=1340, default='No Final Thoughts saved')

    def __str__(self):
        return 'Biography'


# class Education(models.Model):
#     biography = models.ForeignKey(Biography, on_delete=models.CASCADE)
#     start_date = models.DateField(blank=False)
#     end_date = models.DateField(null=True, blank=True)
#     name_of_institution = models.CharField(max_length=300, blank=False)
#     speciality = models.CharField(max_length=100, blank=False)
#     covered_subjects = models.TextField(max_length=1000)
#
#     def __str__(self):
#         return self.name_of_institution
#
#
# class PersonalExperience(models.Model):
#     biography = models.ForeignKey(Biography, on_delete=models.CASCADE)
#     topic_name = models.CharField(max_length=150)
#     topic_summary = models.TextField(max_length=1000)
#     location = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.topic_name
#
#
# class WorkExperience(models.Model):
#     biography = models.ForeignKey(Biography, on_delete=models.CASCADE)
#     start_date = models.DateField(blank=False)
#     end_date = models.DateField(null=True, blank=True)
#     position = models.CharField(max_length=150, blank=False)
#     position_summary = models.TextField(max_length=1000)
#     responsibilities = models.TextField(max_length=2000)
#
#     def __str__(self):
#         return self.position
#
#
# class Achievements(models.Model):
#     biography = models.ForeignKey(Biography, on_delete=models.CASCADE)
#     accomplishment = models.TextField(max_length=500)
#
#     def __str__(self):
#         return self.accomplishment
#
#
# class Languages(models.Model):
#     biography = models.ForeignKey(Biography, on_delete=models.CASCADE)
#     language = models.CharField(max_length=50)
#     fluency = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.language
#
#
# class Passions(models.Model):
#     biography = models.ForeignKey(Biography, on_delete=models.CASCADE)
#     passion = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.passion
