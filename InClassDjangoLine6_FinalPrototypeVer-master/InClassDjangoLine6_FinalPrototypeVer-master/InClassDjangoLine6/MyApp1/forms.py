from django import forms
from .models import teacher
from .models import UploadFile

class InputForm(forms.ModelForm):
    class Meta:
        model = teacher
        fields = ['Name', 'Area']

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadFile
        fields = ['category','title', 'file']
