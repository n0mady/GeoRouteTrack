from django import forms
from .models import Login

class LoginForm(forms.ModelForm):
	
	class Meta:
		model=Login
		fields=['Email','Pwd']

	def clean_Email(self):
		return self.cleaned_data['Email']
	
	def clean_Pwd(self):
		return self.cleaned_data['Pwd']
