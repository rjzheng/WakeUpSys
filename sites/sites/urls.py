from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', 'sites.views.home', name='home'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'auth.views.login_user', name = 'login'),
    url(r'^register/$', 'auth.views.register', name = 'register'),
    url(r'^add/$', 'auth.views.add', name = 'add'),
    url(r'^maps/$', 'auth.views.maps', name = 'maps'),

)
