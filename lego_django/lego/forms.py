from django import forms

from .models import ArtProject

class ArtProjectForm(forms.ModelForm):
    class Meta:
        model = ArtProject
        fields = ('img',)
    
    def __init__(self, *args, **kwargs):  # bootstrap styling
        super(ArtProjectForm, self).__init__(*args, **kwargs)
        self.fields['img'].widget.attrs.update({'class': 'form-control'})