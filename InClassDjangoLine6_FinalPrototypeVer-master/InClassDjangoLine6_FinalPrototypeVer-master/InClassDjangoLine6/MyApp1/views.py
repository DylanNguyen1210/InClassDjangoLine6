
from tkinter import Canvas
from urllib import response
from urllib.request import Request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import teacher
from .forms import InputForm
from .forms import UploadFileForm
from django.contrib.auth.decorators import login_required
from .models import UploadFile



#PDF
from pypdf import PdfWriter, PdfReader
from reportlab.pdfgen import canvas
from reportlab.platypus import Table
from django.http import FileResponse
from django.contrib.staticfiles.storage import staticfiles_storage
from io import BytesIO

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

def report(request):
    pdf_file = staticfiles_storage.path("DS.pdf")

    try:
        merger = PdfWriter()
        input1 = PdfReader(generate_pdf())
        input2 = PdfReader(pdf_file, "rb")

        merger.append(input1)
        merger.append(input2)

        buffer = BytesIO()
        merger.write(buffer)
        buffer.seek(0)

        response = FileResponse(buffer, as_attachment=True, filename="Attachment.pdf")

    except FileNotFoundError:
        response = FileResponse(generate_pdf(), as_attachment=True, filename="noAttachment.pdf")

    return response

def generate_pdf():
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    lines = [('Name:', 'Teaching Area:')]
    teachers = teacher.objects.all()

    for teach in teachers:
        lines.append((teach.Name, teach.Area))

    table = Table(lines)
    table.wrapOn(p, 300, 300)
    table.drawOn(p, 10, 650)

    p.showPage()
    p.save()

    buffer.seek(0)
    return buffer