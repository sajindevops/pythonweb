from django.conf.urls import url 
from . import views


urlpatterns = [
	url(r'^service1/$',views.service1, name='service1'),
	url(r'^http/$',views.http, name = 'http'),
	url(r'^stop/$',views.stop),
	url(r'^$', views.index),
]

