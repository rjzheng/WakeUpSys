import threading
from Alarm_Playback import *
import webbrowser
import time
import datetime

class Alarm_App():
	###INITIALIZATION###
	def __init__(self, days_of_week, time, sound, repeat, enable):
		
		self.playback_obj = Alarm_Playback(sound)	#create an instance from the Alarm_playback() class object

		self.sound = sound
		self.days_of_week = days_of_week	#list ['MON','TUE','FRI']
		self.time = time					#string '07:20'
		self.repeat = repeat				#boolean True/False
		self.enable = enable				#boolean True/False
		self.snoozed = False				#default False unless snooze is pressed
		self.dismissd = False				#defaul False unless dismiss is pressed
		self.play_on = False

	def run(self):
		self.play()
		if not self.repeat:
			self.enable = False
		# while True:
		# 	usr_input = raw_input('snooze/stop: ')
		# 	if usr_input == 'snooze':
		# 		self.snooze()

		# 	elif usr_input == 'stop':
		# 		self.dismiss()
		# 		break



	def __str__(self):
		if self.enable:
			return 'This alarm will go off on: ' + self.days_of_week.__str__() \
												 + ' at ' \
												 + self.time \
												 + '.'

		else:
			return 'This alarm is disabled.'

	def play(self):
		# sleep_time = self.alarm_days()
		# print sleep_time
		# self.playback_obj.alarm_sleep(sleep_time)
		self.playback_obj.alarm_play()
		self.play_on = True

	def snooze(self):
		self.snoozed = False
		self.playback_obj.alarm_stop()
		print 'This alarm will go off again in one minute'
		# sleep_time = 300
		# self.playback_obj.alarm_sleep(sleep_time)
		# self.playback_obj.alarm_play()
		self.play_on = False


	def dismiss(self):
		self.playback_obj.alarm_stop()
		# webbrowser.open_new('http://localhost:8000/maps/')
		self.play_on = False


	#finds how long the alarm should sleep
	def alarm_days(self):
			DAY_SEC = 24*60*60
			WEEK_SEC = 7*DAY_SEC

			#finding the total seconds for time
			x = time.strptime(self.time,'%H:%M')
			x_sec = datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds= 0).total_seconds()
	
			#finding the total seconds for today's time
			today = datetime.datetime.now().weekday()
			today_time = datetime.datetime.now().time().__str__()
			y = time.strptime(today_time.split('.')[0], '%H:%M:%S')
			y_sec = datetime.timedelta(hours=y.tm_hour,minutes=y.tm_min,seconds=y.tm_sec).total_seconds()
			today_time_sec = today*DAY_SEC + y_sec

			#finding the time difference in seconds
			sleep_times = [(day*DAY_SEC + x_sec - today_time_sec)%WEEK_SEC for day in self.days_of_week]

			return min(sleep_times)

	def overwrite(self):
		return self.enable.__str__() + ',' + self.repeat.__str__() + ',' + self.sound.__str__() + \
				',' + self.time.__str__() + ',' + self.days_of_week.__str__()