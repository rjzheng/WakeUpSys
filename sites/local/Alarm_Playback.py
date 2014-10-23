import datetime
import pygame
import time

ALARM_SOUND_DIR = './Alarm Sound/'

class Alarm_Playback():
	
	def __init__(self, sound):

		self.sound = ALARM_SOUND_DIR+sound

	#plays the alarm sound
	def alarm_play(self):

		#loading the alarm sound
		pygame.init()
		pygame.mixer.init()
		pygame.mixer.music.load(self.sound)

		pygame.mixer.music.play(-1)
		
	#stops the alarm sound
	def alarm_stop(self):
		pygame.mixer.music.stop()

	#puts alarm to sleep while it's not time to ring 
	def alarm_sleep(self,sleep_time):
	 	time.sleep(sleep_time)