from fileinput import filename
from django import forms
from django.db import models
from .models import ArtProject


class ArtProjectForm(forms.ModelForm):
    class Meta:
        model = ArtProject
        fields = ("img",)

    def __init__(self, *args, **kwargs):  # bootstrap styling
        super(ArtProjectForm, self).__init__(*args, **kwargs)
        self.fields["img"].widget.attrs.update({"class": "form-control"})


class ArtProjectForm2(forms.Form):
    
    img = forms.ImageField()