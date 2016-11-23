from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.http import JsonResponse

import requests

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


def formprocess(request):
	
	print('im in the formprocess')

	#print "post", request.POST
	address = request.POST['address']
	this= request.POST
	print len(this)
	print address

	position = {'address': address, 'key': 'AIzaSyCm0CIWG6AZ7uLfzCSDNxL7PueiTOTNCF4'}
	loglat = requests.get('https://maps.googleapis.com/maps/api/geocode/json', params=position)
	print "this is loglat results:", 
	addressinfo = loglat.json()

	lati = addressinfo.results[0].geometry.location
	print lati

	radius = request.POST.get('radius')
	print radius
	
	payload = {'lat': '37.89', 'lon': '-121.9', 'radius': '0.2', 'key': '.', '_': '1479774917477'}
	r = requests.get('https://api.spotcrime.com/crimes.json', params=payload)
	print ('im about to return stuff')

	return JsonResponse(r.json())







def addalertprocess(request):
	if request.POST:
		### if user not logged in, redirect to /login

		###models method to check input

		pass

	return redirect('/')



		