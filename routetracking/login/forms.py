from django import forms
from .models import Login,UploadFiles,FileUpload

class LoginForm(forms.ModelForm):
	
	class Meta:
		model=Login
		fields=['Email']

	def clean_Email(self):
		_Email=self.cleaned_data['Email']
		#print _Email
		return _Email
	
	def clean_Pwd(self):
		_Pwd=self.cleaned_data['Pwd']
		#print _Pwd
		return _Pwd


class ExcelForm(forms.ModelForm):
	print "asd"	


class FileForm(forms.ModelForm):
    """Upload files with this form"""
    class Meta:
        model = FileUpload
        exclude = ('md5',)

	