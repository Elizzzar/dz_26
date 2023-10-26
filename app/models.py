from django.db import models

# Create your models here.

class test_model(models.Model):
    name = models.CharField(max_length=48)