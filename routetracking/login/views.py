from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from .forms import LoginForm,ExcelForm
from readmapdata import ReadMap

def LoginView(request):
	LoginData={}
	return render(request,'georoutetrack.html',LoginData)


def ExcelView(request):
	form=ExcelForm(request.POST or None)
	print form['ExcelFile']
	print form['MapFile']
	if form.is_valid():
		instance1=form.save(commit=False)
		print instance1.MapFile + "Fuck"
		print instance1.ExcelFile
		instance1.save()

	context = {"form":form}
		
	return render(request,'excel-file-input.html',context)


def MapView(request):
	GeoRouteData={}
	GeoRouteData=ReadMap("/home/N0maD/My_Works/Django/18_07_2015/Step0/routetracking/templates/MapCoordinates.xls")

	context={}
	context["GeoRouteData"]=GeoRouteData

	return render(request,'google-maps-render.html',context)


def DebugViewParsedData(request):
	""" This Function is for the Debugging Purpose and it will be visible even during production """
	
	GeoRouteData={}
	GeoRouteData=ReadMap("/home/N0maD/My_Works/Django/18_07_2015/Step0/routetracking/templates/MapCoordinates.xls")

	context={}
	context["GeoRouteData"]=GeoRouteData
	
	return render(request,'debug-parsed-data.html',context)