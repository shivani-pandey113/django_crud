from django.db import models

class UserInfo(models.Model):
    fname    = models.CharField(max_length=50,null=False,blank=False)
    lname    = models.CharField(max_length= 20,null=True,blank=True) 
    email    = models.EmailField(max_length=254, null=False, blank=False,default="user@gmail.com")
    password = models.CharField(max_length=10,null=False,blank=False)

