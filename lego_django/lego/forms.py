from django import forms

from .models import Art_project

class Art_project_form(forms.ModelForm):
    class Meta:
        model = Art_project
        fields = ('img',)
    
    def __init__(self, *args, **kwargs):
        super(Art_project_form, self).__init__(*args, **kwargs)
        self.fields['img'].widget.attrs.update({'class': 'form-control'})