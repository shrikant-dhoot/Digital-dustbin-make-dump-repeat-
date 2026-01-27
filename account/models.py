from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class dreams(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    dream = models.TextField(max_length=2000)
    career = models.CharField( max_length=200,null=True,blank=True)
    effort = models.CharField(max_length=200,null=True,blank=True)
    
    
    
class dustbin_dreams(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    dream = models.TextField(max_length=2000)
    career = models.CharField( max_length=200,null=True,blank=True)
    effort = models.CharField(max_length=200,null=True,blank=True)
        