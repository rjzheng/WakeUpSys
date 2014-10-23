from django import forms
from auth.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(forms.ModelForm):
	alarm_setting = forms.CharField(max_length = 500)
	traffic_start = forms.CharField(max_length = 200)
	traffic_end = forms.CharField(max_length = 200)
	weather = forms.CharField(max_length = 200)

	class Meta:
		model = Auth
		fields = ('user','alarm_setting')

	def save(self, commit = True):
		user = super(RegistrationForm, self).save(commit = False)
		user.alarm_setting = self.cleaned_data["alarm_setting"]
		user.traffic_start = self.cleaned_data["traffic_start"]
		user.traffic_end = self.cleaned_data["traffic_end"]
		user.weather = self.cleaned_data["weather"]
		if commit:
			user.save()
		return user

