from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from .forms import LoginForm,ExcelForm

from ReadMapData import ReadMap

# Create your views here.

#def login(request):
#	return render(request,"login.html",{})


def login(request):
	LoginData={}
	title="Welcome"
	#if request.user.is_authenticated():
	#	title += " | %s" %(str(request.user).capitalize())

	if request.method=="POST":	
		print request.POST

	form = LoginForm(request.POST or None)

	if form.is_valid():
		instance=form.save(commit=False)
		print instance.Email + " --> Email "
		print instance.Pwd + " --> Pwd "
		print instance.OS

		if instance.Email=="abc@gmail.com":
			instance.Email="NoUserMailaddress@abcd.com"

		instance.save()

	LoginData['title']=title
	LoginData['form']=form
	return render(request,'login.html',LoginData)



def excel(request):
	form=ExcelForm(request.POST or None)
	print form['ExcelFile']
	print form['MapFile']
	if form.is_valid():
		instance1=form.save(commit=False)
		print instance1.MapFile + "Fuck"
		print instance1.ExcelFile
		instance1.save()

	context = {"form":form}
		
	return render(request,'ExcelFile.html',context)


def RenderMap(request):
	GeoRouteData={}
	GeoRouteData=ReadMap("/home/N0maD/My_Works/Django/18_07_2015/Step0/routetracking/templates/MapCoordinates.xls")

	context={}
	context["Fuck"]="Fuck You"
	context["GeoRouteData"]=GeoRouteData
	
	for Sheet in GeoRouteData.keys():
		L0=GeoRouteData[Sheet]
		for Location in L0.keys():
			L1=L0[Location]
			for key1 in L1.keys():
				print "Sheet Number : => " + Sheet
				print "Location : => " + Location
				print key1 + " : => " + L1[key1]

	return render(request,'GoogleMapRenderTest.html',context)


def parseddata(request):
	""" This Function is for the Debugging Purpose and it will be visible even during production """
	
	GeoRouteData={}
	GeoRouteData=ReadMap("/home/N0maD/My_Works/Django/18_07_2015/Step0/routetracking/templates/MapCoordinates.xls")

	context={}
	context["GeoRouteData"]=GeoRouteData
	
	return render(request,'debug_parsed_data.html',context)