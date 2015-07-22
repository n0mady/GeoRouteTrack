from django.db import models
from django import forms

class Login(models.Model):
	from socket import gethostname,gethostbyaddr
	from platform import platform
	from getpass import getuser

	Email		=models.EmailField(max_length=50,null=False,blank=False)
	Pwd		=models.CharField(max_length=32,null=False,blank=False)
	TimeStamp	=models.DateTimeField(auto_now_add=True,auto_now=False)
	LastSeen	=models.DateTimeField(auto_now_add=False,auto_now=True)
	User		=str(getuser())
	HostName	=str(gethostname())
	IPAddr		=str(gethostbyaddr(gethostname())[2])	#Get only the IP Address of the Host
	OS		=platform()

	def __str__(self):
		return self.Pwd
