from django.db import models

# Create your models here.
class Quotes(models.Model):
    quotes = models.TextField(max_length=800)
    author = models.CharField(max_length=255)