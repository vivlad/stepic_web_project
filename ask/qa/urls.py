from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
urlpatterns = [
	url(r'^$', 'qa.views.test'),
	url(r'^login/$', 'qa.views.test'),
	url(r'^signup/$', 'qa.views.test'),
	url(r'^question/\d+$', 'qa.views.test'),
	url(r'^ask/$', 'qa.views.test'),
	url(r'^popular/$', 'qa.views.test'),
	url(r'^new/$', 'qa.views.test'),
]