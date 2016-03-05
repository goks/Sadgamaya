from django.db import models
from django.utils import timezone
from django.utils.timezone import utc
# from django.utils.crypto import get_random_string
from random import choice
from string import ascii_uppercase
from datetime import datetime

def generatetoken():
			return (''.join(choice(ascii_uppercase) for i in range(12)))
	
class User(models.Model):
	"""docstring for User"""
	firstName = models.CharField(max_length=200, unique=False)
	lastName = models.CharField(max_length=200)
	signuptime = models.DateTimeField(auto_now=False, auto_now_add=False)
	#user_id = models.CharField(max_length=200,primary_key=True)
	email = models.EmailField(max_length=254,primary_key=True)
	imageurl = models.URLField(max_length=200,default='https://cdn4.iconfinder.com/data/icons/small-n-flat/24/user-alt-128.png')
	token = models.CharField(max_length=16, editable=False, unique=True, default=generatetoken)
	beacon = models.TimeField(blank=True, null=True)
	chatactive = models.BooleanField(default=False)
	friendslist = models.CharField(max_length=1000, null=True)
	tempfriendtoken = models.CharField(max_length=254,null=True,default='0')
	chattype = models.CharField(max_length=10, null=True)

	# def __str__(self, arg):
	# 	return self.email

	


class Onlinelist(models.Model):
	"""docstring for User"""
	user = models.ForeignKey(User,unique=True)
	lastUpdate = models.DateTimeField(auto_now=True, null=True)
	def __str__(self, arg):
		return self.online		
	def save(self, *args, **kwargs):
# self.lastUpdate =
		super(Onlinelist, self).save(*args, **kwargs)
	def get_time_diff(self):
		timediff =  datetime.utcnow().replace(tzinfo=utc)-self.lastUpdate
		return timediff.total_seconds()