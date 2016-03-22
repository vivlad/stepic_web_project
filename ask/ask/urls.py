from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


"""urlpatterns = [
    url(r'^admin/', admin.site.urls),
]"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^$', 'qa.views.pages_all'),
	url(r'^login/$', 'qa.views.test'),
	url(r'^signup/$', 'qa.views.test'),
	#url(r'^question/\d+/$', 'qa.views.test'),
	url(r'^question/(?P<q_id>\d+)/$','qa.views.draw_question', name = 'draw_question'),
	url(r'^ask/.*$', 'qa.views.test'),
	url(r'^popular/.*$', 'qa.views.pages_popular'),
	url(r'^new/$', 'qa.views.test'),
]
handler404 = 'qa.views.handler404'
