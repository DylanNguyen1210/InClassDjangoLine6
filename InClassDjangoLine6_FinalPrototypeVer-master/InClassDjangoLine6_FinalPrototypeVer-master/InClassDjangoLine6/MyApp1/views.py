
from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from .models import teacher
from .forms import InputForm
from .forms import UploadFileForm

# Create your views here.
def index(request):
    teach = teacher.objects.all()
    return render(request, "MyApp1/index.html", {'content' : teach})

def home(request):
    teach = teacher.objects.all()
    return render(request, "MyApp1/home.html")

def input_view(request):
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = InputForm()
    return render(request, "input.html", {"form": form})

def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = UploadFileForm()
    return render(request, "upload.html", {"form": form})
