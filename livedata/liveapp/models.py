from __future__ import unicode_literals

from django.db import models

# Create your models here.
class livedatas(models.Model):
    PSDETAILS=models.CharField(max_length=1000)

    
    def __str__ (self):
        return self.PSDETAILS
