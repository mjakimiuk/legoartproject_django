import os
from pathlib import Path

from django.http import HttpResponse, HttpResponseNotFound, FileResponse

from django.shortcuts import redirect, render
from django.urls import reverse
from lego_logic.lego_image import (  # part_description,
    PDF,
    Lego_image,
    main_page,
    pages_of_manual,
    save_output,
)

from .forms import ArtProjectForm, ArtProjectForm2
from .models import ArtProject

# def home(request):
#     if request.method == "POST":
#         form = ArtProjectForm(request.POST, request.FILES,{'title':request.FILES["img"]})

#         if form.is_valid():
#             form.save()
#             webpage = reverse("files")
#             form_file_name = request.FILES["img"]
#             print(form_file_name)
#             lego_object = Lego_image(form_file_name)
#             pdf = PDF()
#             # lego_object.save_output()
#             main_page(lego_object, pdf)
#             # part_description()
#             pages_of_manual(lego_object, pdf)
#             save_output(pdf)
#             return redirect(webpage)
#     else:
#         form = ArtProjectForm()
#     return render(request, "lego/upload_image.html", {"form": form})


# def about(response):
#     return render(response, "lego/about.html", {})


# def files(request):
#     BASE_DIR = Path(__file__).resolve().parent.parent

#     PDFLOCATION = os.path.join(BASE_DIR, "media/art/pdf/output.pdf")
#     print(PDFLOCATION)
#     file_location = PDFLOCATION

#     try:
#         with open(file_location, "rb") as f:
#             file_data = f.read()

#         # sending response
#         response = HttpResponse(
#             file_data,
#             headers={
#                 "Content-Type": "application/pdf",
#                 "Content-Disposition": 'attachment; filename="output.pdf"',
#             },
#         )
#         os.remove(PDFLOCATION)

#     except IOError:
#         # handle file not exist case here
#         response = HttpResponseNotFound("<h1>File does not exist</h1>")

#     return response


# def home(request):
    
#     if request.method == "POST":
#         form = ArtProjectForm2(request.POST, request.FILES)

#         if form.is_valid():
#             form.save()
#             # webpage = reverse("files")
#             form_file_name = request.FILES["img"]
#             pdf_form_file_name=str(form_file_name).split('.')[0]+'.pdf'
#             BASE_DIR = Path(__file__).resolve().parent.parent

#             PDFLOCATION = os.path.join(BASE_DIR, f"media/art/pdf/{pdf_form_file_name}")
#             print(form_file_name)
#             lego_object = Lego_image(form_file_name)
#             pdf = PDF()
#             # lego_object.save_output()
#             main_page(lego_object, pdf)
#             # part_description()
#             pages_of_manual(lego_object, pdf)
            
#             save_output(pdf,filename=PDFLOCATION)
#             return FileResponse(open(PDFLOCATION, 'rb'),as_attachment=True,filename=pdf_form_file_name)
#     else:
#         form = ArtProjectForm2()
#     return render(request, "lego/upload_image.html", {"form": form})


# def about(response):
#     return render(response, "lego/about.html", {})
from contextlib import contextmanager



def home(request):
    
    if request.method == "POST":
        form = ArtProjectForm2(request.POST, request.FILES)

        if form.is_valid():
            name = 'dummy name'
            img = None
            obj = ArtProject.objects.create(
                                 title = name,
                                 img = img
                                 )
            obj.save()
            entries= ArtProject.objects.all()
            entries.delete()
            print(obj)
        
            
            form_file_name = request.FILES["img"]
            
            pdf_form_file_name=str(form_file_name).split('.')[0]+'.pdf'
            BASE_DIR = Path(__file__).resolve().parent.parent

            PDFLOCATION = os.path.join(BASE_DIR, f"media/art/pdf/{pdf_form_file_name}")
            
            lego_object = Lego_image(form_file_name)
            pdf = PDF()
            # lego_object.save_output()
            main_page(lego_object, pdf)
            # part_description()
            pages_of_manual(lego_object, pdf)
            
            save_output(pdf,filename=PDFLOCATION)
            try:
                with open(PDFLOCATION, "rb") as f:
                    file_data = f.read()

                # sending response
                response = HttpResponse(
                    file_data,
                    headers={
                        "Content-Type": "application/pdf",
                        "Content-Disposition": f'attachment; filename={pdf_form_file_name}',
                    },
                )
                os.remove(PDFLOCATION)

            except IOError:
                # handle file not exist case here
                response = HttpResponseNotFound("<h1>File does not exist</h1>")

            return response





    else:
        form = ArtProjectForm2()
    return render(request, "lego/upload_image.html", {"form": form})


def about(response):
    return render(response, "lego/about.html", {})
