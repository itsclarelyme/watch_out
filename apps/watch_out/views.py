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

	#to geocode the address
	# post = request.get('address')
	# print post
	# output = "csv"
	# request = requests.get("http://maps.google.com/maps/geo?q=%s&output=%s&key=%s" % (post, output, settings.GOOGLE_API_KEY))
	# print request
	payload = {'lat': '37.89', 'lon': '-122.9', 'radius': '3', 'key': '.', '_': '1479774917477'}
	r = requests.get('https://api.spotcrime.com/crimes.json', params=payload)
	print ('im about to return stuff')

	return JsonResponse(r.json())





def addalertprocess(request):
	if request.POST:
		### if user not logged in, redirect to /login

		###models method to check input

		pass

	return redirect('/')



		