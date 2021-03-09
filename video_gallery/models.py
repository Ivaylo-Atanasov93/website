from datetime import date
from django.db import models
from embed_video.fields import EmbedVideoField


class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    video_url = EmbedVideoField(default='https://www.youtube.com/')  # same like models.URLField()
    date = models.DateField(default=date.today)
