from datetime import datetime
from django.db import models
from django.urls import reverse


class Booking(models.Model):

    name = models.CharField(max_length=255, blank=False)
    number = models.CharField(max_length=11, blank=False)
    email = models.EmailField(blank=False)
    date = models.DateField(blank=False)
    time = models.TimeField(blank=False)
    message = models.TextField(max_length=500)
    is_free = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('booking-details', kwargs={'id': self.id})
