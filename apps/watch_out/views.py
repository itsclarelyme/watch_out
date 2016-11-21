from django.shortcuts import render, redirect
from . import models

# Create your views here.





def index(request):

	return render(request, 'watch_out/index.html')

def login(request):

	return render(request, 'watch_out/login.html')


def addalert(request):

	return render(request, 'watch_out/addalert.html')

def display(request):

	return render(request, 'watch_out/display.html')







def addalertprocess(request):
	if request.POST:
		### if user not logged in, redirect to /login

		###models method to check input

		pass

	return redirect('/')



		