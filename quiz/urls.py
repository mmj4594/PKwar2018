from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index/$', views.quiz),
	url(r'^announcement/$', views.announcement),
	url(r'^json/$', views.json),
]
