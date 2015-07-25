from django import forms
from .models import Login

class LoginForm(forms.ModelForm):
	
	class Meta:
		model=Login
		fields=['Email','Pwd']

	def clean_Email(self):
		_Email=self.cleaned_data['Email']
		#print _Email
		return _Email
	
	def clean_Pwd(self):
		_Pwd=self.cleaned_data['Pwd']
		#print _Pwd
		return _Pwd


class ExcelForm(forms.Form):
	ExcelFile=forms.CharField(required=False)
	MapFile=forms.FileField() 