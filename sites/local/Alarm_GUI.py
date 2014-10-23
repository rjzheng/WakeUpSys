import Tkinter
import ttk
from Tkinter import *
from ttk import *

import webbrowser
import urllib, urllib2

import time
from Alarm import *
from Write_html import *
    
class Alarm_GUI():
    opener = urllib2.build_opener()
    def __init__(self, next_to_run_alarm, username, password):
        self.username = username
        self.password = password
        self.alarm = next_to_run_alarm
        self.time = self.alarm.time
        self.days_of_week = self.alarm.days_of_week.__str__()
        self.initAlarm()


    def initAlarm(self):
        #creates the Tk window

        self.root = Tk()
        self.root.resizable(width = False, height = False)
        self.root.title('Alarm')
        #sets up the frame inside the root window
        self.mainframe = ttk.Frame(self.root, padding = '3 3 3 3')
        self.mainframe.grid(column = 0, row = 0, sticky = (N, W, E, S))
        self.mainframe.columnconfigure(0, weight = 1)
        self.mainframe.rowconfigure(0, weight = 1)

        self.clock = ttk.Label(self.mainframe, text='', padding = '130 0 0 0')
        self.clock.grid(row = 0, sticky = (W,E))

        self.alarm_setup()
        self.update_clock()
        
        self.snooze_dismiss()

        # self.alarmfunc(int(1000*self.alarm.alarm_days()))
        self.alarmfunc(1000)
        # self.progress.stop()

        self.root.mainloop()

    def alarm_run(self):
        self.alarm.run()


    def alarmfunc(self, sleep_time):
        # sleep_time = int(1000*self.alarm.alarm_days())
        # sleep_time = 1000
        self.progress.start(sleep_time)
        self.progress.step(1000)
        self.root.after(sleep_time,self.alarm_run)
        self.root2.after(sleep_time, self.root2.deiconify)

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
        self.time_var = StringVar()
        self.time_var.set(self.time)
        self.timeLabel = ttk.Label(self.left_Frame, textvariable = self.time_var, padding = '10 0 0 0')
        self.timeLabel.grid(column = 1, row = 0, sticky = E)
        
        #adds days of week checklist to a new frame
        self.dow = ttk.Frame(self.alarm1)
        self.dow.grid(column = 0)
        self.mon = ttk.Checkbutton(self.dow, text = 'MON')
        if '0' in self.days_of_week:
            self.mon.state(['selected', 'readonly', 'disabled'])
        else:
            self.mon.state(['readonly', 'disabled'])
        self.mon.grid(column = 0, row = 0)

        self.tue = ttk.Checkbutton(self.dow, text = 'TUE')
        if '1' in self.days_of_week:
            self.tue.state(['selected', 'readonly', 'disabled'])
        else:
            self.tue.state(['readonly', 'disabled'])
        self.tue.grid(column = 1, row = 0)

        self.wed = ttk.Checkbutton(self.dow, text = 'WED')
        if '2' in self.days_of_week:
            self.wed.state(['selected', 'readonly', 'disabled'])
        else:
            self.wed.state(['readonly', 'disabled'])
        self.wed.grid(column = 2, row = 0)

        self.thur = ttk.Checkbutton(self.dow, text = 'THUR')
        if '3' in self.days_of_week:
            self.thur.state(['selected', 'readonly', 'disabled'])
        else:
            self.thur.state(['readonly', 'disabled'])
        self.thur.grid(column = 3, row = 0)

        self.fri = ttk.Checkbutton(self.dow, text = 'FRI')
        if '4' in self.days_of_week:
            self.fri.state(['selected', 'readonly', 'disabled'])
        else:
            self.fri.state(['readonly', 'disabled'])
        self.fri.grid(column = 4, row = 0)

        self.sat = ttk.Checkbutton(self.dow, text = 'SAT')
        if '5' in self.days_of_week:
            self.sat.state(['selected', 'readonly', 'disabled'])
        else:
            self.sat.state(['readonly', 'disabled'])
        self.sat.grid(column = 5, row = 0)

        self.sun = ttk.Checkbutton(self.dow, text = 'SUN')
        if '6' in self.days_of_week:
            self.sun.state(['selected', 'readonly', 'disabled'])
        else:
            self.sun.state(['readonly', 'disabled'])
        self.sun.grid(column = 6, row = 0)

        #adds time label to alarm frame
        self.right_Frame = ttk.Frame(self.alarm1)
        self.right_Frame.grid(column = 1, row = 0)

    def snooze_dismiss(self):
        self.root2 = Tk()
        self.root2.resizable(width = False, height = False)
        self.root2.title('Snooze/Dismiss')

        self.mainframe2 = ttk.Frame(self.root2, padding = '3 3 3 3')
        self.mainframe2.grid(row = 1, sticky = (N, W, E, S))
        self.mainframe2.columnconfigure(0, weight = 1)
        self.mainframe2.rowconfigure(0, weight = 1)

        self.snooze = ttk.Button(self.mainframe2, text = 'Snooze', command = self.snooze_button)
        self.snooze.grid(column = 0, row = 1)

        self.dismiss = ttk.Button(self.mainframe2, text = 'Dismiss',command = self.dismiss_button)
        self.dismiss.grid(column = 1, row = 1)

        self.root2.withdraw()

    def snooze_button(self):
        if self.alarm.play_on == True:
            self.alarm.snooze()
            self.root2.withdraw()
            self.alarmfunc(5000)
        else:
            return
            
    def dismiss_button(self):
        if self.alarm.play_on == True:
            self.alarm.dismiss()
            self.write = Write_html(self.username, self.password)
            self.root2.withdraw()
        else:
            return
