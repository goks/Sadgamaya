from django.db import models
from django.utils import timezone

class User(models.Model):
	"""docstring for User"""
	firstName = models.CharField(max_length=200)
	lastName = models.CharField(max_length=200)
	#user_id = models.CharField(max_length=200,primary_key=True)
	email = models.EmailField(max_length=254,primary_key=True)
	imageurl = models.URLField(max_length=200,default='https://cdn4.iconfinder.com/data/icons/small-n-flat/24/user-alt-128.png')

	def __str__(self, arg):
		return self.email


class Portfolio(models.Model):
	"""docstring for User"""
	user_id = models.CharField(max_length=200,primary_key=True)

	def __str__(self, arg):
		return self.user_id		
		