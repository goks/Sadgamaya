from django.shortcuts import render
from models import User
from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie,csrf_exempt
from django.template import RequestContext, loader
import logging
from django.core.validators import validate_email
from django import forms
# Create your views here.
#======Index Page======#
@ensure_csrf_cookie #cross reference 
def index(request):
    context=RequestContext(request) #
    template=loader.get_template('login.html')
    return HttpResponse(template.render(context))

@csrf_exempt
def auth(request):
	userid = request.POST.get('iduser=', 'NULL')
 	token = request.POST.get('idtoken=', 'NULL')
 	firstname = request.POST.get('idfirstname=', 'NULL')
 	lastname = request.POST.get('idlastname=', 'NULL')
 	email = request.POST.get('idemail=', 'NULL')
 	imageurl = request.POST.get('idimageurl=','NULL')

 	#url = 'https://www.googleapis.com/oauth2/v3/tokeninfo?id_token='+token
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
		return HttpResponse("error")
	try:
		u = User.objects.get(email=email)
	except:
		u = User(firstname, lastname, email, imageurl)
		u.save()
		return HttpResponse("DONE!!!")
	return HttpResponse("firstname: " + firstname +"\nlastname: " + lastname + "\nemail: " + email +"\nimageurl: " + imageurl)
	