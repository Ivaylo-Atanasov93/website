from django.db import models
from datetime import date

# Create your models here.
from django.urls import reverse


class Picture(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    photo = models.ImageField(upload_to='images')
    date = models.DateField(default=date.today)

    def get_absolute_url(self):
        return reverse('image-detail', args=[str(self.id)])
