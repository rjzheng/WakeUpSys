from Alarm_App import *

class Alarm():
	def __init__(self, alarm_setting):
		self.initalarm(alarm_setting)
		return
	def initalarm(self,alarm_setting):
		#COVERTING INPUT TO ARRAY
		self.alarm_setting = alarm_setting
		self.settings = self.alarm_setting.split(';')

		#INITILIZING ARRAY LISTS
		self.alarm_list_enable = []
		self.alarm_list_disable =[]
		self.alarm_fixed_list = []

		#TAKING EACH VALUE OF THE ARRAY AND SETTING IT TO ALARM VARIABLES
		for n in range(len(self.settings)):
			self.setting = self.settings[n].split(',')
			self.days_of_week = [int(day) for day in self.setting[4:]]
			self.time = self.setting[3]
			self.sound = self.setting[2]
			self.repeat = self.setting[1]=='True'
			self.enable = self.setting[0] == 'True'

			#APPEND THE ENABLED ALARMS TO A LIST
			if self.enable:
				alarm = Alarm_App(self.days_of_week, self.time, self.sound, self.repeat, self.enable)
				self.alarm_list_enable.append(alarm)

			#APPEND THE DISABLED ALARMS TO A LIST
			elif not self.enable:
				alarm = Alarm_App(self.days_of_week, self.time, self.sound, self.repeat, self.enable)
				self.alarm_list_disable.append(alarm)

	def sortalarm(self):
		if len(self.alarm_list_enable) > 0:
			self.alarm_sleep_time =  [alarm.alarm_days() for alarm in self.alarm_list_enable]
			self.sorted_list = [alarm for sleep_time, alarm in sorted(zip(self.alarm_sleep_time, self.alarm_list_enable))]
			return self.sorted_list[0]
			if self.sorted_list[0].enable == False:
				self.alarm_list_disable.append(self.sorted_list[0])
				self.alarm_list_enable.remove(self.sorted_list[0])
		else:
			return 'no more active alarms'
			

	def runalarm(self, alarm_setting):
		self.initalarm(alarm_setting)
		while True:
			self.next_alarm_to_run = self.sortalarm()
			self.next_alarm_to_run.run()


	def update(self):
		self.alarm_list = self.alarm_list_enable + self.alarm_list_disable
		for n in range(len(self.alarm_list)):
			self.alarm_fixed = self.alarm_list[n].overwrite().replace('[','').strip(']')
			self.alarm_fixed_list.append(alarm_fixed)

		self.alarm_setting = self.alarm_fixed_list

# a = Alarm().runalarm('True,False,Alarm2.mp3,14:18,1, 2, 3, 4;False,False,Alarm1.mp3,10:56,0, 3;True,True,Alarm3.mp3,14:31,0, 1, 3, 6')