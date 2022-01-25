from django import forms
from .models import CodeSource

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = CodeSource
        fields = ['name', 'file']
