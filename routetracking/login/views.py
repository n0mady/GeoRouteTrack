from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from .forms import LoginForm,ExcelForm
from readmapdata import ReadMap

from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, FormView
from django.contrib import messages
from .forms import FileForm
from .models import FileUpload

def LoginView(request):
	LoginData={}
	return render(request,'georoutetrack.html',LoginData)


def ExcelView(request):
	form=ExcelForm(request.POST,request.FILES)

	context = {"form":form}

	if not str(request.user)=="AnonymousUser":
		return render(request,'excel-file-input.html',context)
	else:
		return render(request,'georoutetrack.html',{})


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
	

class FileAddView(FormView):

    form_class = FileForm
    #success_url = reverse_lazy('home')
    template_name = "add.html"

    def form_valid(self, form):
        instance=form.save(commit=True)
	print instance['f']
        messages.success(self.request, 'File uploaded!', fail_silently=True)
        return super(FileAddView, self).form_valid(form)