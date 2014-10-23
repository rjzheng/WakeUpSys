from Alarm import *
from Alarm_GUI import *
from Login_GUI import *

class Top():
	def __init__(self):
		self.login = Login_GUI()
		self.username = self.login.get_username()
		self.password = self.login.get_password()

		if self.login.login_sucess == True:
			self.alarm_list = self.login.alarm_response.read()
			self.alarm = Alarm(self.alarm_list)
			while True:
				self.next_to_run = self.alarm.sortalarm()
				self.alarm_gui = Alarm_GUI(self.next_to_run, self.username, self.password)


a = Top()
