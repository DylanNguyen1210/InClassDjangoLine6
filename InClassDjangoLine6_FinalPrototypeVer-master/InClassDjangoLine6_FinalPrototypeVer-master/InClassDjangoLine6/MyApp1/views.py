
from pickle import FALSE
from urllib.request import Request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from .models import teacher
from .forms import InputForm
from .forms import UploadFileForm
from django.contrib.auth.decorators import login_required
from .models import UploadFile

# Create your views here.
def index(request):
    teach = teacher.objects.all()
    return render(request, "MyApp1/index.html", {'content' : teach})

@login_required
def home(request):
    return render(request, "MyApp1/home.html")

@login_required
def input_view(request):
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = InputForm()
    return render(request, "input.html", {"form": form})

@login_required
def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.user = request.user
            document.save()

            all_images = UploadFile.objects.filter(user=request.user)

            return render(request, "upload_success.html", {'document': document, 'files': all_images})
    else:
        form = UploadFileForm()
    return render(request, "upload.html", {'form': form})
