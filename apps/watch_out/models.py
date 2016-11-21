from __future__ import unicode_literals

from django.db import models

# Create your models here.

#class ALertManager(models.Manager):
#####ADD ALERT



class User(models.Model):
	name=models.CharField(max_length=45)
	user_name=models.CharField(max_length=45)	
	email=models.CharField(max_length=45)         #### maybe to contact? is this safe?
	hashed_pw= models.CharField(max_length=150)
	created_at=models.DateTimeField(auto_now_add=True)

