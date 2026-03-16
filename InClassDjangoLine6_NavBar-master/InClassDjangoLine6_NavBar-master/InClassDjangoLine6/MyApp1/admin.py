from django.contrib import admin
from .models import teacher
from .models import Photo

# Register your models here.
admin.site.register(teacher)

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at')