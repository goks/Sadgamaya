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
# Create your views here.
#======Index Page======#
@ensure_csrf_cookie #cross reference 
def index(request):
	template=loader.get_template('login.html')
	context=RequestContext(request)
	request.session['dashboard']==0
	#request.session.set_test_cookie()
	#request.session['login'] = 0
	return HttpResponse(template.render(context))

@csrf_exempt
def auth(request):
	#userid = request.POST.get('iduser=', 'NULL')
 	token = request.POST.get('idtoken=', 'NULL')
 	# firstname = request.POST.get('idfirstname=', 'NULL')
 	# lastname = request.POST.get('idlastname=', 'NULL')
 	# email = request.POST.get('idemail=', 'NULL')
 	#  imageurl = request.POST.get('idimageurl=','NULL')

 # 	proxy = urllib2.ProxyHandler({'https': 'http://mec:mec@192.168.0.4:3128'})
	# auth = urllib2.HTTPBasicAuthHandler()
	# opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler)
	# urllib2.install_opener(opener)

 	url = 'https://www.googleapis.com/oauth2/v3/tokeninfo?id_token='+token
 	req = urllib2.Request(url)
 	response = urllib2.urlopen(req)
 	response = json.load(response)
 	if response['aud']=='841750429424-1hba7bekjmrm1ngbn3m2hrlfb44fodgu.apps.googleusercontent.com':
 		firstname = response['given_name']
 		lastname = response['family_name']
 		email = response['email']
 	 	imageurl = response['picture']
 	 	userid = response['sub']
 	 	print ">>>>JSON PARSE COMPLETE"
 	else:
 		return HttpResponse("fail")
 	url= 'https://www.googleapis.com/plus/v1/people/'+userid+'/people/connected'	
 	req = urllib2.Request(url)
 	response = urllib2.urlopen(req)
 	print response
    # set the body
    #r = HttpResponse(response.read())
#
    # set the headers
    #for header in response.info().keys():
        # r[header] = response.info()[header]
 
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
		print ">>>Existing user"
	except:
		print ">>>Firstuser"	
		u = User(firstname, lastname, email, imageurl)
		u.save()
	request.session['email'] = email
	request.session['dashboard']=1
	print ">>>passed Oauth"
	#request.session['login'] = 1
	#return HttpResponse("firstname: " + firstname +"\nlastname: " + lastname + "\nemail: " + email +"\nimageurl: " + imageurl)
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
    	template=loader.get_template('dash.html')
    	context=RequestContext(request)
    	u = User.objects.get(email=request.session['email'])
    	userid = u.firstName+" "+u.lastName
    	return render_to_response('dash.html',{'userid':userid})
    return redirect('index')
    		
	