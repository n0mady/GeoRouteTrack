from django import forms
from .models import FileUpload

class FileForm(forms.ModelForm):
    """Upload files with this form"""
    class Meta:
        model = FileUpload
        exclude = ('md5',)