from django.db import models
from django.utils.timezone import now
#import datetime
# Create your models here.
from django.urls import reverse


class ContactMe(models.Model):
    name = models.CharField(max_length=50, blank=False)
    surname = models.CharField(max_length=50, blank=False)
    email = models.EmailField(blank=False)
    message = models.TextField(max_length=5000, blank=False)
    date = models.DateField(auto_now=True)

    def get_absolute_url(self):
        return reverse('contact-details', kwargs={'id': self.id})


