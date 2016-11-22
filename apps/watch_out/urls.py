from django.conf.urls import url 
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^login$', views.login),
	url(r'^addalert$', views.addalert),
	url(r'^display$', views.display),     #####crime ID????
	url(r'^addalert/process$', views.addalertprocess),
	url(r'^submitform$', views.formprocess),



	url(r'^$', views.index),

]