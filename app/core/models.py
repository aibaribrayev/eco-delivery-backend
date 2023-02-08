from django.conf import settings
from django.db import models  #noqa

# Create your models here.
class Company(models.Model):
    """Company object"""
    name = models.CharField(max_length = 255)
    
    def __str__(self): 
        return self.name
