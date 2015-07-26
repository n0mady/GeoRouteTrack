"""routetracking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    	url(r'^$','login.views.login',name='Login'),
	url(r'^excel/$','login.views.excel',name='Contact'),
	url(r'^map/$','login.views.RenderMap',name='Map Render'),
	url(r'^debug/parseddata/$','login.views.parseddata',name='For Debugging - Parsed Data'),
	#Please comment this line during deployment
	url(r'^admin/', include(admin.site.urls)),
    	url(r'^georoutetrackapp/', include(admin.site.urls)),

    	#URLs for User Authentication
    	#url(r'^accounts/login/$','login.views.login',name='Login'),
	#url(r'^accounts/auth$','login.views.authview',name='Authentication'),
	#url(r'^accounts/loggedin/$','login.views.loggedin',name='LoggedIn'),
	#url(r'^accounts/logout/$','login.views.loggedout',name='LogOut'),
	#url(r'^accounts/invalid/$','login.views.invalidlogin',name='InvalidLogin'),
] 


if settings.DEBUG:
	urlpatterns + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)