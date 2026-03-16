from tabnanny import verbose
from django.db import models

# Create your models here.
class teacher(models.Model):
    Name = models.CharField(max_length=25)
    Area = models.CharField(max_length=30)

class Photo(models.Model):
    title = models.CharField(max_length=100, verbose_name='Photo Title')
    image = models.ImageField(upload_to='photos/', verbose_name="Photo File")
    uploaded_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.title