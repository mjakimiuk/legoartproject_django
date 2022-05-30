from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .forms import Art_project_form
import imghdr


def home(request):
    if request.method == 'POST':
        form = Art_project_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Art_project_form()
    return render(request, 'lego/upload_image.html', {
        'form': form
    })

def about(response):
    return render(response, 'lego/about.html',{})


def fileupload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        file_storage = FileSystemStorage()
        name = file_storage.save(uploaded_file.name, uploaded_file)
        context['url'] = file_storage.url(name)
        
    return render(request, 'lego/upload.html',context)


def upload_image(request):
    if request.method == 'POST':
        form = Art_project_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Art_project_form()
    return render(request, 'lego/upload_image.html', {
        'form': form
    })



