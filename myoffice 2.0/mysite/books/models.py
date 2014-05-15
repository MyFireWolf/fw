from django.db import models

# Create your models here.

class Namebook(models.Model):
    name=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    
    def __unicode__(self):
        return '%s , %s' %(self.name,self.country)