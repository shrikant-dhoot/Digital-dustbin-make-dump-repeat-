from django.db import models

# Create your models here.
class dreams(models.Model):
    dream = models.TextField(max_length=2000)
    career = models.CharField( max_length=200,null=True,blank=True)
    effort = models.CharField(max_length=200,null=True,blank=True)
    
    
    
class dustbin_dreams(models.Model):
    dream = models.TextField(max_length=2000)
    career = models.CharField( max_length=200,null=True,blank=True)
    effort = models.CharField(max_length=200,null=True,blank=True)
        