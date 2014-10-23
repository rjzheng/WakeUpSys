from django.contrib import admin

from auth.models import Auth

class AuthAdmin(admin.ModelAdmin):
	list_display = ('user', 'alarm_setting', 'traffic_start', 'traffic_end', 'weather')

admin.site.register(Auth, AuthAdmin)