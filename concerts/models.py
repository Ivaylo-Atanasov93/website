from django.db import models


# Create your models here.

class Concert(models.Model):
    def make_location_clean(self, location):
        return location.split('"')

    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=1000, blank=False)
    # raw_location = models.CharField(max_length=500, blank=False)
    location = models.CharField(max_length=500, blank=False)
    date = models.DateField(blank=False)
    time = models.TimeField(blank=False)
