from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.template import RequestContext
#from portal.forms import Registration_Form
def main_page(request):
	return render_to_response('index.html')
def logout_page(request):
	logout(request)
	return HttpResponseRedirect('/')


def signup_page(request):
	if request.method == 'POST':
        # create a form instance and populate it with data from the request:
		AddEmail=request.POST.get('email')			
		AddPass=request.POST.get('otp')			
		#form=Registration_Form(request.POST)		
		
	#	if form.is_valid():
		try:		
			user=User.objects.create_user(username=AddEmail,password=AddPass)
			user.save()        
			userLog=authenticate(username=AddEmail, password=AddPass,email=AddEmail)		
			login(request,userLog)		
			return HttpResponseRedirect('/portal/')		
		except:
			c = RequestContext(request, {'error': "SignUp unsuccessfull:username may have already taken"})			
			return render_to_response('login.html',c )
				
			# check whether it's valid:
		
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
		

    # if a GET (or any other method) we'll create a blank form
    	
    		


	
