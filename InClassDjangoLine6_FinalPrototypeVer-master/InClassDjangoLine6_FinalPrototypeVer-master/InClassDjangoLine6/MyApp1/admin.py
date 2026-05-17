from django.contrib import admin
from .models import teacher
from .models import UploadFile, Category
# Register your models here.
admin.site.register(UploadFile)
admin.site.register(Category)
admin.site.register(teacher)