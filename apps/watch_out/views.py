from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.http import JsonResponse

import requests
import datetime
import bcrypt
from django.contrib import messages

from . import models
from .models import Users, Alerts 

# Create your views here.





def index(request):

	return render(request, 'watch_out/index.html')

def login(request):

	return render(request, 'watch_out/login.html')

def register(request):

	return render(request, 'watch_out/register.html')


def addalert(request):
	print ("inside addalert")
	if "user_id" not in request.session:
		print ("user not logged in")
		return redirect('/login')
	else:
		print ("user logged in")
		return render(request, 'watch_out/addalert.html')

def display(request):

	return render(request, 'watch_out/display.html')


def formprocess(request):
	
	print('im in the formprocess')
	data = request.POST
	radius = data['radius']
	lat = data['lat']
	lng = data['lng']
	
	payload = {'lat': lat, 'lon': lng, 'radius': radius, 'key': '.', '_': '1479774917477'}
	r = requests.get('https://api.spotcrime.com/crimes.json', params=payload)
	print ('im about to return stuff')

	return JsonResponse(r.json())







def addalertprocess(request):
	if request.POST:
		inputs = request.POST
		print inputs
		thisuser = models.Users.objects.get(id = request.session['user_id'])
		alert= models.Alerts.objects.create(address = request.POST.get('location'), date= request.POST.get('date'), crime= request.POST.get('type'), description=request.POST.get('description'), poster=thisuser)
		pass

	return redirect('/')



#LOGIN REGS
def loginprocess(request):
	post = request.POST
	print post

	email=request.POST.get('email')
	print "email", email
	password=request.POST.get('password')
	
	#check if existing user or input error
	existuser = models.Users.objects.loginvalid(request,email, password)
	if existuser == True:
		print "user exist"
		user_id = models.Users.objects.get(email = email).id
		request.session['user_id'] = user_id
		context = {
			'username' : email,
			'status' : "logged in"
		}
		return redirect('/')
	##DISPLAY MSGED TO SHOW ERROR
	for ind in range (0, len(existuser)):
		messages.error(request, existuser[ind])
	return redirect('/registration')

def registerprocess(request):
	#GET USER INPUT
	
	name=request.POST.get('name')
	email = request.POST.get('email')
	password=request.POST.get('password')
	repassword=request.POST.get('re_password')
	newuser = models.Users.objects.registervalid(name, email, password, repassword)
	print newuser
	if not newuser:
		hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
		newuser = models.Users.objects.create(name=name, email=email, hashed_pw=hashed)
		user_id = models.Users.objects.get(email = email).id
		request.session['user_id'] = user_id
		return redirect('/')
	if newuser[0] == "User already exist! Please login instead!":
		print("go to login page")
		return redirect('/login')

	for ind in range (0, len(newuser)):
		messages.error(request, newuser[ind])
	return redirect('/registration')


def loggingout(request):
	request.session.pop('user_id')
	return redirect('/')



		