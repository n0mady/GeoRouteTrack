from django.contrib import admin
from .forms import LoginForm,ExcelForm
from .models import Login

# Register your models here.

class LoginAdmin(admin.ModelAdmin):
	list_display=["__str__","Pwd","TimeStamp","LastSeen","User","HostName","IPAddr","OS"]
	form = ExcelForm

	#class Meta:
	#	model = Login

admin.site.register(Login,LoginAdmin) 
