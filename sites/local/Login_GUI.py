import Tkinter as tk
from Tkinter import *
import ttk
from ttk import *
import time

import urllib, urllib2

from Alarm import *

class Login_GUI():
	opener = urllib2.build_opener()

	def __init__(self):
		self.initLogin()

	def initLogin(self):

		self.root = Tk()
		self.root.resizable(width = False, height = False)
		self.root.title('Login')
		self.root.rowconfigure(0, weight = 1)
		self.root.columnconfigure(0, weight = 1)
		self.root.geometry('270x180')

	#-------------------------------------------------------------------#
    # Variables
    #-------------------------------------------------------------------#

		self.prompt_text = StringVar()
		self.prompt_text.set('Please enter your user information:')
		
		
    #-------------------------------------------------------------------#
    # GUI
    #-------------------------------------------------------------------#

		ttk.Style().configure("TButton", padding = 6, relief="solid")

		self.mainframe_a = ttk.Frame(self.root, padding = '20 20 20 20')
		self.mainframe_a.grid(row = 0,sticky = (N, E, W, S))
		self.mainframe_a.columnconfigure(0, weight = 1)
		self.mainframe_a.rowconfigure(0, weight = 1)

		self.mainframe_b = ttk.Frame(self.root)
		self.mainframe_b.grid(row = 2,sticky = (N, E, W, S))
		self.mainframe_b.columnconfigure(0, weight = 1)
		self.mainframe_b.rowconfigure(0, weight = 1)

		self.prompt = ttk.Label(self.mainframe_a, textvariable = self.prompt_text, padding = '0 0 0 20')
		self.prompt.grid(row = 0)
		self.prompt.grid_propagate(False)

		self.username = ttk.Label(self.mainframe_a, text = 'Username:', padding = '0 0 100 0')
		self.username.grid(row = 1)
		self.username_entry = ttk.Entry(self.mainframe_a)
		self.username_entry.grid(row = 2)
		self.username_entry.bind('<Return>', self.enter)
		self.username_entry.focus_set()

		self.password = ttk.Label(self.mainframe_a, text = 'Password:', padding = '0 0 100 0')
		self.password.grid(row = 3)
		self.password_entry = ttk.Entry(self.mainframe_a, show = '*')
		self.password_entry.grid(row = 4)
		self.password_entry.bind('<Return>', self.enter)

		self.sign_in = ttk.Button(self.mainframe_b, text = 'Sign in', command=self.check )
		self.sign_in.grid(column = 2)

		self.root.mainloop()

	def check(self):
		self.values = {
			'username': self.username_entry.get(),
			'password': self.password_entry.get(),
			}

		self.params = urllib.urlencode(self.values)
		self.alarm_response = self.opener.open("http://localhost:8000/login/",self.params)
		self.prompt_text.set('you are logged in')
		self.root.destroy()

		self.login_sucess = True

		# return

	def get_username(self):
		return self.values['username']

	def get_password(self):
		return self.values['password']

	def enter(self,event):
		self.check()

	def update_clock(self):
		#gets the current time
		now = time.strftime('%H:%M:%S')
		#sets the clock label to the time
		self.clock.configure(text=now)
		#tick the time
		self.root.after(1000, self.update_clock)
	def alarm_setup(self):
		#creates a new frame that holds one alarm
		self.alarm1 = ttk.LabelFrame(self.root, text= 'Alarm 1')
		self.alarm1.grid(column = 0, row = 2, stick = (W, E))
		self.alarm1.columnconfigure(0, weight = 1)
		self.alarm1.rowconfigure(0, weight = 1)

		#adds a progress bar to alarm frame
		self.left_Frame = ttk.Frame(self.alarm1)
		self.left_Frame.grid(column = 0, row = 0)
		self.progress = ttk.Progressbar(self.left_Frame, orient = HORIZONTAL, length = 200, mode = 'determinate')
		self.progress.grid(column = 0, row = 0, sticky = W)
		self.timeLabel = ttk.Label(self.left_Frame, text = '7:00 AM', padding = '10 0 0 0')
		self.timeLabel.grid(column = 1, row = 0, sticky = E)

		#adds days of week checklist to a new frame
		self.dow = ttk.Frame(self.alarm1)
		self.dow.grid(column = 0)
		self.mon = ttk.Checkbutton(self.dow, text = 'MON')
		self.mon.state(['selected', 'readonly'])
		self.mon.grid(column = 0, row = 0)
		self.tue = ttk.Checkbutton(self.dow, text = 'TUE')
		self.tue.grid(column = 1, row = 0)
		self.wed = ttk.Checkbutton(self.dow, text = 'WED')
		self.wed.grid(column = 2, row = 0)
		self.thur = ttk.Checkbutton(self.dow, text = 'THUR')
		self.thur.grid(column = 3, row = 0)
		self.fri = ttk.Checkbutton(self.dow, text = 'FRI')
		self.fri.grid(column = 4, row = 0)
		self.sat = ttk.Checkbutton(self.dow, text = 'SAT')
		self.sat.grid(column = 5, row = 0)
		self.sun = ttk.Checkbutton(self.dow, text = 'SUN')
		self.sun.grid(column = 6, row = 0)

		#adds time label to alarm frame
		self.right_Frame = ttk.Frame(self.alarm1)
		self.right_Frame.grid(column = 1, row = 0)


