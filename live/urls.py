from django.conf.urls import url
from . import views

app_name = 'elections'
urlpatterns = [
    url(r'^$', views.index),
    url(r'^reload_match/$', views.reload_match),
]
