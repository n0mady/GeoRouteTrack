from django.contrib import admin
from .forms import LoginForm
from .models import Login

# Register your models here.

class LoginAdmin(admin.ModelAdmin):
	list_display=["__str__","Pwd","TimeStamp","LastSeen","User","HostName","IPAddr","OS"]
	form = LoginForm
	#class Meta:
	#	model = Login
	

admin.site.register(Login,LoginAdmin) 
