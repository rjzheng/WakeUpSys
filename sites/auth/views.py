import pywapi
import string
import time
import datetime

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm

import urllib, urllib2

from auth.models import *
from django.contrib.auth.models import User
from auth.forms import *

import os.path

import gflags
import httplib2

from apiclient.discovery import build
from oauth2client.file import Storage
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.tools import run


def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			return HttpResponseRedirect("/add/")
	else:
		form = UserCreationForm()
	return render_to_response('register.html', {'form': form,})

def add(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			return HttpResponse('Saved', content_type = 'text/plain')
	else:
		form = RegistrationForm()
	return render_to_response('alarm.html', {'form': form,})


def login_user(request):
	username = password = ''
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username = username, password = password)

		if user is not None:
			if user.is_active:

				login(request, user)

				alarm_setting = Auth.objects.get(user = user).alarm_setting

				return HttpResponse(alarm_setting, content_type = 'text/plain')


def maps(request):
	username = password = ''
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username = username, password = password)

		if user is not None:
			if user.is_active:

				login(request, user)

				traffic_start = Auth.objects.get(user = user).traffic_start
				traffic_end = Auth.objects.get(user = user).traffic_end
				zip_code = Auth.objects.get(user = user).weather

				yahoo_result = pywapi.get_weather_from_yahoo(zip_code)

				temperature = str(float(yahoo_result['condition']['temp']) * 9 / 5 + 32)
				status = string.lower(yahoo_result['condition']['text'])
				city = yahoo_result['location']['city']
				state = yahoo_result['location']['region']

				day = time.strftime("%A")
				
				now = time.strftime("%I:%M %p")



				##########################################

				client_id = '107104525841-unshiaeg7lkur5s26g9gambmn06r9c5g.apps.googleusercontent.com'
				client_secret = '2MlHKycM1zjWa3sDkvDXgiyP'
				user_agent = 'ATW/v1'
				developerKey = 'AIzaSyBVAKDYSs526Hq74_WtCc6XswQjrH5hpyQ'


				here = os.path.dirname(os.path.realpath(__file__))
				storage_file = os.path.join(here, 'calendar.dat')


				FLAGS = gflags.FLAGS

				FLOW = OAuth2WebServerFlow(
					client_id = client_id,
					client_secret = client_secret,
					scope = 'https://www.googleapis.com/auth/calendar',
					user_agent = user_agent
					)

				storage = Storage(storage_file)
				credentials = storage.get()
				if credentials is None or credentials.invalid == True:
					credentials = run(FLOW, storage)

				http = httplib2.Http()
				http = credentials.authorize(http)

				service = build(serviceName = 'calendar', version = 'v3', http = http,\
								developerKey = developerKey)
				

				d = datetime.datetime.now()
				date = '{:%Y-%m-%d}'.format(d)
				timeMax = date + 'T23:59:00-08:00'
				timeMin = date + 'T12:00:00-08:00'
				calendarId = 'rjzhengsg@gmail.com'
				events = service.events().list(
					calendarId = calendarId,
					timeMax = timeMax,
					timeMin = timeMin
					).execute()
				calendar_events = []
				event_start_time = []
				event_end_time = []
				for event in events['items']:
					event_start_time.append(str(event['start'])[27:32])
					event_end_time.append(str(event['end'])[27:32])
					calendar_events.append(event['summary'])


				##################################


	return render_to_response('maps.html', {'start':traffic_start, 'end': traffic_end, 'temperature': temperature,\
		'status': status, 'city': city, 'state': state, 'day': day, 'time': now, 'zip_code': zip_code, \
		'calendar': calendar_events, 'start_time': event_start_time, 'end_time': event_end_time})




