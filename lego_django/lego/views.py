import os
from pathlib import Path

from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.urls import reverse
from lego_logic.lego_image import (  # part_description,
    PDF,
    Lego_image,
    main_page,
    pages_of_manual,
    save_output,
)

from .forms import ArtProjectForm


def home(request):
    if request.method == "POST":
        form = ArtProjectForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            webpage = reverse("files")
            form_file_name = request.FILES["img"]
            print(form_file_name)
            lego_object = Lego_image(form_file_name)
            pdf = PDF()
            # lego_object.save_output()
            main_page(lego_object, pdf)
            # part_description()
            pages_of_manual(lego_object, pdf)
            save_output(pdf)
            return redirect(webpage)
    else:
        form = ArtProjectForm()
    return render(request, "lego/upload_image.html", {"form": form})


def about(response):
    return render(response, "lego/about.html", {})


def files(request):
    BASE_DIR = Path(__file__).resolve().parent.parent

    PDFLOCATION = os.path.join(BASE_DIR, "media/art/pdf/output.pdf")
    print(PDFLOCATION)
    file_location = PDFLOCATION

    try:
        with open(file_location, "rb") as f:
            file_data = f.read()

        # sending response
        response = HttpResponse(
            file_data,
            headers={
                "Content-Type": "application/pdf",
                "Content-Disposition": 'attachment; filename="output.pdf"',
            },
        )
        os.remove(PDFLOCATION)

    except IOError:
        # handle file not exist case here
        response = HttpResponseNotFound("<h1>File does not exist</h1>")

    return response
