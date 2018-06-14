from django.db import models

class Users(models.Model):
	name = models.CharField(max_length=250)
	username = models.CharField(max_length=255,unique=True)
	password = models.CharField(max_length=100)
	email = models.CharField(max_length=1000)
	

		
class todo(models.Model):
	username = models.ForeignKey(Users, to_field='username')
	task = models.CharField(max_length=500)
	deadline = models.CharField(max_length=250)
