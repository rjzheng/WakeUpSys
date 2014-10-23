from django.db import models
from django.contrib.auth.models import User

class Auth(models.Model):
	user = models.OneToOneField(User)
	alarm_setting = models.CharField(max_length = 500)
	traffic_start = models.CharField(max_length = 200)
	traffic_end = models.CharField(max_length = 200)
	weather = models.CharField(max_length = 200)


