from django.db import models

# Create your models here.

class FlashWord(models.Model):
    word = models.CharField(max_length=100)
    translate = models.CharField(max_length=255)
    defenition = models.TextField()
