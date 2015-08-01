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

def LoginView(request):
	LoginData={}
	return render(request,'georoutetrack.html',LoginData)

def MapView(request):
	GeoRouteData={}
	GeoRouteData=ReadMap("/home/N0maD/My_Works/Django/18_07_2015/Step0/routetracking/templates/MapCoordinates.xls")

	context={}
	context["GeoRouteData"]=GeoRouteData
	
	if not str(request.user)=="AnonymousUser":
		return render(request,'google-maps-render.html',context)
	else:
		return render(request,'georoutetrack.html',{})


def DebugViewParsedData(request):
	""" This Function is for the Debugging Purpose and it will be visible even during production """
	
	GeoRouteData={}
	GeoRouteData=ReadMap("/home/N0maD/My_Works/Django/18_07_2015/Step0/routetracking/templates/MapCoordinates.xls")

	context={}
	context["GeoRouteData"]=GeoRouteData
	
	if not str(request.user)=="AnonymousUser":
		return render(request,'debug-parsed-data.html',context)
	else:
		return render(request,'georoutetrack.html',{})
	

class ExcelView(FormView):
	form_class = FileForm
	template_name = "excel-file-input.html"
	#def get_form(self, form_class):
	#	contact = FileUpload.objects.get('files')
	#	print contact
	#	return form_class(instance=contact, **self.get_form_kwargs())	
	
	def form_valid(self, form):
		self.object=form.save(commit=True)
		return super(ExcelView, self).form_valid(form)
	
		#print self.get_form_kwargs()
		#Data=self.get_form_kwargs()
		#
		

	#print FileUpload.f + "Fuck you mother fucker"
	#
	#for key in Data:
	#    print key
	#    print key['files']
		  
	    #print self.get_form_kwargs.
	    #print(self.request.GET['f'])
	    
	    #print instance['f']
	    #messages.success(self.request, 'File uploaded!', fail_silently=True)
	    #return super(ExcelView, self).form_valid(form)
	    
	    
def ExcelViewTest(request):
	if request.POST:
	    #print request.POST
	    form = FileForm(request.POST, request.FILES)
	    print request.FILES['f']
	    if form.is_valid():
		form.save()
		print request.POST
		return HttpResponseRedirect('/map')
	else:
		form=FileForm()
	
	context = {}
	context.update(csrf(request))
	context["form"]=form
	
	return render_to_response('excel-file-input.html',context)
