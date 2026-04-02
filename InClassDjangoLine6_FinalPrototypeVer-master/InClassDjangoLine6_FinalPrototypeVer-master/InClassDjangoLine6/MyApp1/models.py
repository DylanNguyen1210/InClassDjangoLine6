from django.db import models

# Create your models here.
class teacher(models.Model):
    Name = models.CharField(max_length=25)
    Area = models.CharField(max_length=30)

class UploadFile(models.Model):
    title = models.CharField(max_length=20)
    file = models.FileField(upload_to='uploads/')