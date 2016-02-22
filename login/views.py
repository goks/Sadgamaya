from django.shortcuts import render, render_to_response
from models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import ensure_csrf_cookie,csrf_exempt
from django.template import RequestContext, loader
import logging
from django.core.validators import validate_email
from django import forms
from django.shortcuts import redirect
from django.views.decorators.cache import never_cache
import urllib2 
import json
import datetime
import time
# Create your views here.

#======Index Page======#
@ensure_csrf_cookie #cross reference 
def index(request):
	template=loader.get_template('login.html')
	context=RequestContext(request)
	request.session['dashboard'] =	0
	request.session['chatbox'] = 0
	request.session['receiver'] = 0
	#request.session.set_test_cookie()
	#request.session['login'] = 0
	return HttpResponse(template.render(context))

@csrf_exempt
def auth(request):
	#userid = request.POST.get('iduser=', 'NULL')
	print ("hello")
	token = request.POST.get('idtoken=', 'NULL')

	# proxy = urllib2.ProxyHandler({'https': 'http://mec:mec@192.168.0.4:3128'})
	# auth = urllib2.HTTPBasicAuthHandler()
	# opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler)
	# urllib2.install_opener(opener)

	if(token=='NULL'):
		return HttpResponse("fail")

	url = 'https://www.googleapis.com/oauth2/v3/tokeninfo?id_token='+token
 	req = urllib2.Request(url)
 	response = urllib2.urlopen(req)
 	response = json.load(response)
 	print response

 	
 	if response['aud']=='841750429424-1hba7bekjmrm1ngbn3m2hrlfb44fodgu.apps.googleusercontent.com':
 		firstname = response['given_name']
 		lastname = response['family_name']
 		email = response['email']
 		try:
 	 		imageurl = response['picture']
 	 	except:
 	 		imageurl = 'https://cdn4.iconfinder.com/data/icons/small-n-flat/24/user-alt-128.png'
 	 	userid = response['sub']
 	 	print ">>>>JSON PARSE COMPLETE"
 	else:
 		return HttpResponse("fail")
 	
    #url = 'https://www.googleapis.com/oauth2/v3/tokeninfo?id_token='+token+'/'
 	#serialized_data = urllib2.urlopen(url).read()
 	#data = json.loads(serialized_data)
 	#r = requests.post('https://www.googleapis.com/oauth2/v3/tokeninfo?id_token=', token=token)
 	#idinfo = client.verify_id_token(token, userid)
    	#except AppIdentityError:
    	#	logger.error("Invalid Clientid")
    	# Invalid token
	#userid = idinfo['email']
	try:
		validate_email(email)
	except forms.ValidationError:
		return HttpResponse('0')
	try:
		u = User.objects.get(email=email)
		u.chatactive = False
		print ">>>Existing user"
	except:
		print ">>>Firstuser"	
		#print "image >>>"+imageurl
		now = datetime.datetime.now()
		u = User(firstname, lastname, now, email, imageurl)
	try:
		u.save()
	except:
		return HttpResponse("0")
	request.session['email'] = email
	request.session['dashboard']=1
	print ">>>passed Oauth"
	context=RequestContext(request)
	return HttpResponse("1")

@csrf_exempt
@never_cache
def dash(request):
	#if (request.session.test_cookie_worked()):
	#	print ">>>> TEST COOKIE WORKED!"
    #	request.session.delete_test_cookie()
    if ('dashboard' in request.session and request.session['dashboard']==1):
    	request.session['dashboard']=0
    	request.session['chatbox']=0
    	template=loader.get_template('dash.html')
    	context=RequestContext(request)
    	u = User.objects.get(email=request.session['email'])
    	u.chatactive = False
    	userid = u.firstName+" "+u.lastName
    	print u.token
    	return render_to_response('dash.html',{'userid':userid},context)
    return redirect('index')
 
@csrf_exempt    		
def tokenpass(request):
	email = request.session['email']
 	friendsEmail = request.POST.get('friendsEmail=', 'NULL')
 	chatType = request.POST.get('type=', 'NULL')
	print ">>>friendsEmail: " + friendsEmail
 	# print ">>>Token: " + token
 	print ">>>clientemail: " + email
	try:
		u = User.objects.get(email=email)
		# u.token = token;
		u.beacon = datetime.datetime.now()
		# u.save()
		print ">>Token of Caller: " + u.token
		print ">>Caller is: " + u.firstName
	except:
		print ">>fail"
		return HttpResponse('0')
	temp = u.friendslist	
	try:
		f = User.objects.get(email = friendsEmail)
	except:
		print ">>> Friend Not FOUND"
		return HttpResponse('2')
	# temp = u.friendslist
	# print ">>>>>"+temp
	if temp:
		print ">>>>>"+temp
		tempstring = temp.split()
		for word in tempstring:
			print ">>>>>>" + word
			if(word==friendsEmail):
				print ">>>>>>>Friend already in Database"
				break
		else:		
			print ">>>>>>>>Friend first time"		
			u.friendslist = temp + ' ' + friendsEmail	
	else:
		u.friendslist = friendsEmail
		print ">>>Friend added to db"
	if(f.chatactive):
		print ">>>Friend already in another chat"
		return HttpResponse('3')
	u.chatactive = True
	f.chatactive = True
	f.tempfriendtoken = u.token
	u.tempfriendtoken = f.token
	u.chattype = chatType;
	f.chattype = chatType;
	print f.tempfriendtoken + "  " + f.firstName
	print "Chattype is " + chatType
	u.save()
	f.save()
	request.session['chatbox']=1
	print ">>Invoked Client's Chat Initialized"
	request.session['receiver']=0 
	return HttpResponse('1')

@csrf_exempt
@never_cache
def chatcheck(request):
	#if (request.session.test_cookie_worked()):
	#	print ">>>> TEST COOKIE WORKED!"
    #	request.session.delete_test_cookie()
   	# token = request.POST.get('token=', 'NULL')
   	email = request.session['email']
   	try:
   		u = User.objects.get(email=email)
   		# u.token = token;
   		u.beacon = datetime.datetime.now()
   		u.save()
 		print ">>>receiver is: "+ u.firstName
   		print ">>Token in Database"
   	except:
   		print ">>Error adding token to db"
   		return HttpResponse("3")
   	#	while True :
   	receiver = request.session['receiver'] 
   	if (u.chatactive):
   			print ">>"+u.firstName+" CHAT ACTIVE"
   			request.session['receiver'] = 1
   			request.session['chatbox']=1
   			if(u.chattype == "chat"):
   					return HttpResponse('1')
   			elif(u.chattype == "video"):
   					return HttpResponse('2')
   	else :
   			print ">>"+u.firstName+"RECEIVER WAITING FOR CHAT"
   			return HttpResponse('0')
   	return HttpResponse("Error")

@csrf_exempt
@never_cache
def chatbox(request):
	#if (request.session.test_cookie_worked()):
	#	print ">>>> TEST COOKIE WORKED!"
    #	request.session.delete_test_cookie()
    email = request.session['email']
    if ('chatbox' in request.session and request.session['chatbox']==1):
    	request.session['chatbox']=0
    	request.session['dashboard'] = 0
    	template=loader.get_template('chat.html')
    	context=RequestContext(request)
    	u = User.objects.get(email = email)
    	temp = u.friendslist
    	receiver = request.session['receiver']
    	print "receiver is" + str(receiver)
    	if receiver==1:
    		request.session['receiver'] = 3
    		try:
    			f = User.objects.get(token = u.tempfriendtoken)
    			friendsemail = f.email
    			print ">>>Receivers friend is " + f.firstName
    		except:
    			print ">>> Friend Not FOUND"
    		if temp:
    			# print ">>>>>"+temp
    			tempstring = temp.split()
    			for word in tempstring:
    				# print ">>>>>>" + word
    				if(word==friendsemail):
    					print ">>>>>>>Friend already in Database"
    					break
    			else:
    				print ">>>>>>>>Friendslist not empty;Friend first time"
    				u.friendslist = temp + ' ' + friendsemail
    		else:
    			u.friendslist = friendsemail
    			print ">>>Friend added to db"
    		u.save()	
    	elif receiver==0:
    		request.session['receiver'] = 3
    		try:	
    			f = User.objects.get(token = u.tempfriendtoken)
    		except:
    			print ">>>Failed obtaining activators friend's token"	
    		print ">>>Caller: " + u.firstName + "receiver is: " + f.firstName
    		# userid = u.firstName+" "+u.lastName
    	else:
    		print ">>>RECEIVER session variable 3 error"	
    	print ">>"+u.firstName+"token: " + u.token + " receiverstoken: " + f.token	
    	return render_to_response('chat.html',{'receiver':receiver, 'friendtoken':f.token, 'mytoken':u.token})
    	# else:
    	# 	return render_to_response('chat.html',{'receiver':receiver,'friendtoken':'none', 'mytoken':u.token}) 		
    return redirect('index')

@csrf_exempt
@never_cache
def vidbox(request):
	email = request.session['email']
	if ('chatbox' in request.session and request.session['chatbox']==1):
		request.session['chatbox']=0
		request.session['dashboard'] = 0
		template=loader.get_template('vid.html')
		context=RequestContext(request)
		u = User.objects.get(email = email)
		temp = u.friendslist
		receiver = request.session['receiver']
		print "receiver is" + str(receiver)
		if receiver==1:
			request.session['receiver'] = 3
			try:
				f = User.objects.get(token = u.tempfriendtoken)
				friendsemail = f.email
				print ">>>Receivers friend is " + f.firstName
			except:
				print ">>> Friend Not FOUND"
			if temp:
				# print ">>>>>"+temp
				tempstring = temp.split()
				for word in tempstring:
					# print ">>>>>>" + word
					if(word==friendsemail):
						print ">>>>>>>Friend already in Database"
						break
				else:
					print ">>>>>>>>Friendslist not empty;Friend first time"
					u.friendslist = temp + ' ' + friendsemail
			else:
				u.friendslist = friendsemail
				print ">>>Friend added to db"
			u.save()
		elif receiver==0:
			request.session['receiver'] = 3
			try:
				f = User.objects.get(token = u.tempfriendtoken)
			except:
				print ">>>Failed obtaining activators friend's token"
			print ">>>Caller: " + u.firstName + "receiver is: " + f.firstName
			# userid = u.firstName+" "+u.lastName
		else:
			print ">>>RECEIVER session variable 3 error"
		print ">>"+u.firstName+"token: " + u.token + " receiverstoken: " + f.token
		return render_to_response('vid.html',{'receiver':receiver, 'friendtoken':f.token, 'mytoken':u.token})
	return redirect('index')