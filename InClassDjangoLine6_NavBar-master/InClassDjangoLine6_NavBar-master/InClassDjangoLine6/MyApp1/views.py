
from tkinter import PhotoImage
from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from .models import teacher
from .forms import InputForm
from .forms import PhotoForm 
from .models import Photo

# Create your views here.
def index(request):
    teach = teacher.objects.all()
    return render(request, "MyApp1/index.html", {'content' : teach})

def home(request):
    teach = teacher.objects.all()
    return render(request, "MyApp1/home.html", {'content' : teach})


def about(request):
    teach = teacher.objects.all()
    return render(request, "MyApp1/about.html")

def input_view(request):
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = InputForm()
    return render(request, "input.html", {"form": form})

def upload_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('photo_list')
    else:
        form = PhotoForm()
    return render(request, 'main/upload_photo.html', {'form': form})
            
def photo_list(request):
    photos = Photo.objects.all().order_by('-uploaded_at')
    return render(request, 'main/photo_list.html', {'photos': photos})