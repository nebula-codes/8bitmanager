from django.db import models
from django.utils import timezone
import os
# Create your models here.

class Device(models.Model):
    name = models.CharField(max_length=50)
    id = models.IntegerField(unique=True, primary_key=True)

    def __str__(self):
        return self.name



class CodeSource(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=200)
    file = models.FileField(upload_to='documents/', null=True, blank=True)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    hascompiled = models.BooleanField(default=False)


    

    def __str__(self):
        return self.name

    def extension(self):
        name, extension = os.path.splitext(self.file.name)
        return extension
