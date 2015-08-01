from django.db import models
from django import forms
from time import time

def content_file_name(instance, filename):
	filename_with_time_stamp=str(time()).replace('.','_') + "_" + filename
	return '/'.join(['.', instance.user.username, filename_with_time_stamp])

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
		return self.Email

class UploadFiles(models.Model):
	from socket import gethostname,gethostbyaddr
	from platform import platform
	from getpass import getuser
	

	Excell		=models.FileField(upload_to=content_file_name)
	Email		=models.EmailField(max_length=50,null=False,blank=False)
	TimeStamp	=models.DateTimeField(auto_now_add=True,auto_now=False)
	LastSeen	=models.DateTimeField(auto_now_add=False,auto_now=True)
	User		=str(getuser())
	HostName	=str(gethostname())
	IPAddr		=str(gethostbyaddr(gethostname())[2])	#Get only the IP Address of the Host
	OS		=platform()

	def __str__(self):
		return self.Excell
	

def hashed_uploads_dirs(instance, filename):
    """Returns path with md5 hash as directory"""
    return os.path.join(instance.md5, filename)

class FileUpload(models.Model):
    """This holds a single user uploaded file"""
    f = models.FileField(upload_to= '.')
    md5 = models.CharField(max_length=32)

