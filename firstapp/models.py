from django.db import models

# Create your models here.
class userData(models.Model):
    userID=models.AutoField(primary_key=True)
    userName=models.CharField(max_length=200,default="")
    userPassword=models.CharField(max_length=200,default="")
    userEmail=models.CharField(max_length=200,default="")
    userImage=models.CharField(max_length=200,default="")
    isActive=models.BooleanField(default=True)


