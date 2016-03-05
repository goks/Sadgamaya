# import json
# from django.utils import simplejson
from django.core import serializers
from django.http import JsonResponse
class Friend(object):
 	"""docstring for friend"""
 	def __init__(self, fullname, status, imageurl, email, online):
 		self.fullname = fullname
 		self.status = status
 		self.imageurl = imageurl
 		self.email = email
 		self.online = online

class ShortFriend(object):
	def __init__(self,email,status):
		self.email = email
		self.status = status
	# def jsonReturner(self):
	# 	return serializers.serialize("json", ShortFriend.objects.all())


# class ChatCheckFriend(object):
# 	def __init__(self, response, friendslist):
# 		self.response = response
# 		self.friendslist = friendslist
	