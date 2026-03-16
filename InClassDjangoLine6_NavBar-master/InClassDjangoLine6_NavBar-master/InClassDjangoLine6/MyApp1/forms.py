from django import forms
from .models import teacher
from .models import Photo

class InputForm(forms.ModelForm):
    class Meta:
        model = teacher
        fields = ['Name', 'Area']

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['title', 'image']

