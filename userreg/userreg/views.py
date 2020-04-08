from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.conf import settings

def index(request):
    context={"sal":"Hello"}
    return render(request,"profiles/profile.html",context)

def logout_view(request):
	logout(request)
	return redirect('../login')

def some(request):
	output="Go to <a href='",settings.LOGIN_URL,"'>Login</a>"
	return HttpResponse(output)
