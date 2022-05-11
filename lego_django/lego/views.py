from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Upload, File
from .forms import UploadFileForm
# Create your views here.

def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)



def home(response):
    return render(response, 'lego/home.html',{})

def about(response):
    return render(response, 'lego/about.html',{})

def fileupload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})



