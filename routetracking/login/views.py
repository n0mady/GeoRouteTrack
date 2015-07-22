from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf

# Create your views here.

#def login(request):
#	return render(request,"login.html",{})


def login(request):
	title="I dont know"
	return render(request,'login.html',{"title":title})


"""


def login(request):
	c={}
	c.update(csrf(request))
	return render_to_response('login.html',c)

def authview(request):
	username = request.POST.get('username','')
	password = request.POST.get('password','')
	user	= auth.authenticate(username=Email,password=Pwd)
	
	print "fucking user name" + str(user)
	print Email

	if user is not None:
		auth.login(request,user)
		return HttpResponseRedirect('/accounts/loggedin')
	else:
		return HttpResponseRedirect('/accounts/invalid')

def loggedin(request):
	return render_to_response('loggedin.html',{'full_name',request.user.username})


def loggedout(request):
	return render_to_response('loggedout.html',{'full_name',request.user.username})


def invalidlogin(request):
	return render_to_response('invalid.html',{'full_name',request.user.username})

"""
