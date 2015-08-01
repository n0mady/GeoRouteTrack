from django.db import models
from django import forms
from time import time

def content_file_name(instance, filename):
	filename_with_time_stamp=str(time()).replace('.','_') + "_" + filename
	return '/'.join(['.', instance.user.username, filename_with_time_stamp])

def hashed_uploads_dirs(instance, filename):
    """Returns path with md5 hash as directory"""
    return os.path.join(instance.md5, filename)

class FileUpload(models.Model):
    """This holds a single user uploaded file"""
    f = models.FileField(upload_to= '.')
    md5 = models.CharField(max_length=32)

