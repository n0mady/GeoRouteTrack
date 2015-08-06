from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from readmapdata import ReadMap

from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, FormView
from django.contrib import messages
from .forms import FileForm
from .models import FileUpload
from django.conf import settings

FilePath={}

def LoginView(request):
	LoginData={}
	return render(request,'georoutetrack.html',LoginData)

def MapView(request):
	GeoRouteData={}
	
	FilePath["file_with_path"]=str(settings.MEDIA_ROOT) + "/" + str(FilePath["Excel"])
	
	print FilePath["file_with_path"]
	
	GeoRouteData=ReadMap(FilePath["file_with_path"])

	context={}
	context["GeoRouteData"]=GeoRouteData
	
	if not str(request.user)=="AnonymousUser":
		return render(request,'google-maps-render.html',context)
	else:
		return render(request,'georoutetrack.html',{})


def DebugViewParsedData(request):
	""" This Function is for the Debugging Purpose and it will be visible even during production """
	
	GeoRouteData={}
	GeoRouteData=ReadMap(FilePath["file_with_path"])

	context={}
	context["GeoRouteData"]=GeoRouteData
	
	if not str(request.user)=="AnonymousUser":
		return render(request,'debug-parsed-data.html',context)
	else:
		return render(request,'georoutetrack.html',{})
	

def ExcelView(request):
	if request.POST:
	    form = FileForm(request.POST, request.FILES)
	    if form.is_valid():
		form.save()
		FilePath["Excel"]=request.FILES['f']
		if not str(request.user)=="AnonymousUser":
			return HttpResponseRedirect('/map')
		else:
			return render(request,'georoutetrack.html',{})
	else:
		form=FileForm()
	
	context = {}
	context.update(csrf(request))
	context["form"]=form
		
	if not str(request.user)=="AnonymousUser":
		return render(request,'excel-file-input.html',context)
	else:
		return render(request,'georoutetrack.html',{})
