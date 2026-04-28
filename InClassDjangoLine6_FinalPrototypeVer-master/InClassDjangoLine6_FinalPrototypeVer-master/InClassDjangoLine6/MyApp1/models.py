from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class teacher(models.Model):
    Name = models.CharField(max_length=25)
    Area = models.CharField(max_length=30)

class UploadFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=TRUE)
    title = models.CharField(max_length=20)
    file = models.FileField(upload_to='uploads/')