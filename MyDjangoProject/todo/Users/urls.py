from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'Users'
urlpatterns = [
    url(r'^$', views.index),
 	url(r'^login/$',views.login,name='login'),
 	url(r'^home/$', views.home),
 	url(r'^register/$', views.register, name='register'),
 	url(r'^Aboutus/$', views.about),
 	url(r'^logout/$', views.logout),
 	url(r'^my_dashboard/$', views.my_dashboard),
 	url(r'^add_task/$', views.add_task,name='add_task'),
 	url(r'^edit_task/$', views.edit_tas,name='edit_task'),
 	url(r'^edit_task/(?P<id>[0-9]+)/$', views.edit_task),
 	url(r'^delete_task/$', views.del_task,name='delete_task'),
 	url(r'^delete_task/(?P<id>[0-9]+)/$', views.delete_task),


 	
 	      
]
