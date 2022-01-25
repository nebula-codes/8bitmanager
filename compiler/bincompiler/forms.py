from django import forms
from .models import CodeSource

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = CodeSource
        
        fields = ['name', 'file']
        
    def __init__(self, *args, **kwargs):
        super(UploadFileForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['name'].widget.attrs.update({'placeholder': 'File Name'})
        self.fields['file'].widget.attrs.update({'id': 'filepicker'})
        
