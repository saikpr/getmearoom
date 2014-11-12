from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.template import RequestContext
from portal.models import Category
from django.http import HttpResponse
from django.core.mail import send_mail
from django.core.exceptions import ValidationError
from django.core import serializers
import random
import hashlib
from portal.models import *
import datetime
#import urllib2
#import requests
import json
from django.db.models import Q
from django.forms.models import model_to_dict
from django.shortcuts import render
import string,re
from recaptcha.client import captcha  
#from portal.forms import Registration_Form
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
def ValuesQuerySetToDict(vqs):
    return [item for item in vqs]
def has_special(pw):
	'Password must contain a special character'
	return len(set(string.punctuation).intersection(pw)) > 0
def has_numeric(pw):
	'Password must contain a digit'
	return len(set(string.digits).intersection(pw)) > 0
def main_page(request):
	context = RequestContext(request)   
	try:
		
		context_dict=None
				# Add category to the context so that we can access the id and likes
				
	
	except Category.DoesNotExist:
		pass

	  
	return render_to_response('index.html',context_dict,context)
def logout_page(request):
	logout(request)
	#   
	return HttpResponseRedirect('/')


def signup_page(request):
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		AddEmail=request.POST.get('email')          
		Pass=request.POST.get('pass')
		CPass=request.POST.get('cpass')
		roll=request.POST.get('roll')
		context_dict={} 
		context_dict["roll_no"]=roll
		context_dict["email"]=AddEmail      
		#form=Registration_Form(request.POST)       
		
		# see if the user correctly entered CAPTCHA information
		# and handle it accordingly.
			

		if (AddEmail!="" and Pass!="" and CPass!="" and roll!=""):
			if(Pass==CPass):
				try:
					exist=User.objects.get(username=roll)
					context_dict["error"]="You are already signed up with this roll number"
					c = RequestContext(request,context_dict)            
					return render_to_response('login.html',c )
				except User.DoesNotExist:
					pass
				if not re.match("[\d]*\dEN\d[\d]*", roll):
					context_dict["error"]="Wrong Roll no"
					c = RequestContext(request, context_dict)           
					return render_to_response('login.html',c )
				if len(Pass)<=8 and not has_special(Pass) and not has_numeric(Pass) :
					context_dict["error"]="Password should be minimum 8 characters long,a special character and a number"
					c = RequestContext(request, context_dict)           
					return render_to_response('login.html',c )
				try:
					response = captcha.submit(request.POST.get('recaptcha_challenge_field'),request.POST.get('recaptcha_response_field'),'6LdEWv0SAAAAACGFFj_XcbCnR-S0zsNwJDtjb6GF',request.META['REMOTE_ADDR'],)
								
					if response.is_valid:
						captcha_response = "YOU ARE HUMAN:"
					else:
						context_dict["error"]="Type right captcha"
						c = RequestContext(request,context_dict)            
						return render_to_response('login.html',c )      
	
					q=random.randint(0,1000000)
					string=str(q)+AddEmail
					m=hashlib.md5(string)
					hash_value=m.hexdigest()                    
					try:
						check=Verification.objects.get(roll_no=roll)
						context_dict["error"]="A mail has been sent to you already"                 
						c = RequestContext(request,context_dict)            
						return render_to_response('login.html',c )
					except:
						pass
					try:
						validate_email( AddEmail )
							
					except ValidationError:
						context_dict["error"]="Please Enter A valid Email ID"                   
						c = RequestContext(request,context_dict)            
						return render_to_response('login.html',c )
					message="This is the verification email.Please click on the link below to authenticate yourself into the room allocation portal"+"\n\n\n"+"http://db.sainyam.me/portal/verify/"+hash_value+"/"
					send_mail('Verification Mail',message,'tanay.sharma.cse12@itbhu.ac.in',[AddEmail],fail_silently=False)
					x=Verification(email=AddEmail,password=Pass,roll_no=roll,hash_value=hash_value)
					x.full_clean()                  
					x.save()
								
					return render(request,'portal/email_verify.html',context_dict)
				except ValidationError,e:
					context_dict["error"]=e.message_dict                    
					c = RequestContext(request,context_dict)            
					return render_to_response('login.html',c )
			else:
				context_dict["error"]="Password Doesnot Match"              
				c = RequestContext(request, context_dict)           
				return render_to_response('login.html',c )
		else:
			context_dict["error"]="Field Cannot Be Empty"           
			c = RequestContext(request, context_dict)           
			return render_to_response('login.html',c )
			
	#   if form.is_valid():
		#try:       
			#user=User.objects.create_user(username=AddEmail,password=AddPass)
			#user.save()        
			#userLog=authenticate(username=AddEmail, password=AddPass,email=AddEmail)       
			#login(request,userLog) 
			
				
		#   return HttpResponseRedirect('/portal/')     
		#except:
		#   c = RequestContext(request, {'error': "SignUp unsuccessfull:username may have already taken"})          
		#   return render_to_response('login.html',c )
				
		


def like_category(request):
	context = RequestContext(request)
	cat_id = None
	if request.method == 'GET':
		cat_id = request.GET['category_id']

	likes = 0
	if cat_id:
		category = Category.objects.get(id=int(cat_id))
		if category:
				likes = category.likes + 1
				category.likes =  likes
				category.save()

	return HttpResponse(likes)
		
			
def pass_recovery(request):
	context_dict={}
	roll=None   
	if request.method == 'GET':
				
		roll=request.GET['roll_number']     
						
	try:
		x=Student.objects.get(roll_no=roll)
		email=x.email
		password="#"                
		try:
			q=random.randint(0,1000000)
			string=str(q)+roll
			m=hashlib.md5(string)
			hash_value=m.hexdigest()                    
			try:
				check=Verification.objects.get(roll_no=roll)
				return HttpResponse( "A mail has been sent to you already")
			except:
				pass    
			message="This is the Password Recovery email.Please click on the link below to recover your password"+"\n\n\n"+"http://db.sainyam.me/portal/pass_change/"+hash_value+"/"
			send_mail('Password Recovery Mail',message,'tanay.sharma.cse12@itbhu.ac.in',[email],fail_silently=False)
			x=Verification(roll_no=roll,hash_value=hash_value,email=email,password=password)
			x.full_clean()                  
			x.save()                
			return HttpResponse("Message sent")
		except ValidationError,e:
			context_dict["message"]=e.message_dict                  
			c = RequestContext(request,context_dict)            
			return HttpResponse("Message cannot be sent.A mail has been sent to you already")
	except Student.DoesNotExist:
		context_dict["message"]="This username doesnot exist.Please enter valid username"                   
		c = RequestContext(request,context_dict)            
		return HttpResponse("This username doesnot exist.Please enter valid username")
	
	return HttpResponse("Something bad is happening. Shhh! Keep quite.")



def search_page(request):
	context = RequestContext(request)
	hostel = None
	room=None
	search_result=""
	if request.method == 'GET':
		hostel = request.GET['search_hostel']
		room=request.GET['search_room']
		if room.isdigit()==False:
			return HttpResponse("Please enter a valid number")          
		total_room=Hostel.objects.get(hostel_name=hostel)
		room_sum=total_room.g_floor+total_room.f_floor+total_room.s_floor           
		
		if hostel and room and int(room)>0 and int(room)<=room_sum:
			
			room_same_dict=Student.objects.filter(room_alloted=int(room))   
			room_is_occupied=room_same_dict.count()
			count=0
				
			id=[]
			if room_is_occupied==0:
				search_result="2 Available"             
				return HttpResponse(search_result)
			else:
				for room_no in room_same_dict:
					try:                
						exist_batch=Batch.objects.get(roll_no=room_no.roll_no)
						exist_hostel=HostelAlloted.objects.get(department=exist_batch.department,year=exist_batch.year)
						hostelName=exist_hostel.hostel_name
					except:
						return HttpResponse("error")    
					
					if str(hostelName) == str(hostel):
						search_result+=room_no.roll_no+" "
						#id[count]=room_no.roll_no                          
						count=count+1
							
			
				if count==0:
					search_result="2 Available" 
					#values = json.dumps({"count":"2","search_result":search_result})               
					return HttpResponse(search_result)

				elif count==1:
					search_result+="1 Available"
					#values = json.dumps({"search_result":search_result,"count":"1"})               
					return HttpResponse(search_result)
						
									 
				else:
					#values = json.dumps({"search_result":search_result,"count":"0"})               
					return HttpResponse(search_result)
			
				
		

	return HttpResponse("Room does not exist")

def room_page(request):
	context = RequestContext(request)
	pref1 = None
	pref2=None
	now=datetime.datetime.now()
	room_sum=0	
	student=Student.objects.get(roll_no=request.user)
										
	try:
		exist=Student.objects.get(roll_no=request.user)
		room_number=exist.room_alloted
		try:        
			nodues=Registration.objects.get(roll_no=exist.roll_no)
		except:
			return HttpResponse("No nodues set")        
		if nodues.no_dues==0:
			return HttpResponse("No dues certificate is not clear.Contact the warden of your hostel")       
		elif room_number>0: 
			return HttpResponse("Room is already occupied by you.You are not eligible for this")
			
	except:
		pass        
		
	room_start=now.replace(year=2014,month=11,day=6,hour=10, minute=0, second=0, microsecond=0)
	room_start_15=now.replace(year=2014,month=11,day=6,hour=10, minute=15, second=0, microsecond=0)             
	room_start_30 =now.replace(year=2014,month=11,day=6,hour=10, minute=30, second=0, microsecond=0)            
	room_start_45 =now.replace(year=2014,month=11,day=6,hour=10, minute=45, second=0, microsecond=0)            
	room_start_60 =now.replace(year=2014,month=11,day=6,hour=11, minute=0, second=0, microsecond=0)             
		

	if request.method == 'GET':
		hostel = request.GET['search_hostel']           
		pref1 = request.GET['pref1']
 #      pref2=request.GET['pref2']
		pref1_data=request.GET['pref1_data']        
 #      pref2_data=request.GET['pref2_data']        
		if pref1.isdigit()==False:
			return HttpResponse("Please enter a valid number")  
		total_room=Hostel.objects.get(hostel_name=hostel)
		room_sum+=total_room.g_floor+total_room.f_floor+total_room.s_floor           
		if pref1:
			roll_no_reciever1=""
			count=0 
			#if now<room_start:
			#   return HttpResponse("Allotement is scheduled for 6th November at 10am")
			#elif now<room_start_15:
			if int(pref1)>0 and int(pref1)<room_sum:

				if 'Available' in pref1_data:
					now=datetime.datetime.now() 
					try:
						room_add=Rooms.objects.get(room_no=int(pref1),hostel_name=hostel)
						
						if room_add.roll_no_1=="0EN0":
							#student=Student.objects.get(roll_no=request.user)
							student.room_alloted=int(pref1)
							student.save()
							room_add.roll_no_1=student.roll_no
							
							#room_add.date_time_roll_1=datetime.now()
							room_add.save()
							return HttpResponse("Room "+ pref1+ " is alloted to you")	 
						elif room_add.roll_no_2=="0EN0":
							#student=Student.objects.get(roll_no=request.user)
							student.room_alloted=int(pref1)
							student.save()
							room_add.roll_no_2=student.roll_no
							#room_add.date_time_roll_2=datetime.now()
							room_add.save()
							return HttpResponse("Room "+ pref1+ " is alloted to you")
						else:
							return HttpResponse("Room "+ pref1+ " is already alloted to some other student.Try again")
						  
					except:
						default=Student.objects.get(roll_no="0EN0")
						#now=datetime.now()
						
						try:
							t=Rooms(room_no=int(pref1),hostel_name=total_room,roll_no_1=student.roll_no,roll_no_2=default.roll_no)
							t.full_clean()
							t.save()
							
						except:
							return HttpResponse("Something went wrong")
						
						student.room_alloted=int(pref1)
						student.save()
						return HttpResponse("Room "+ pref1+ " is alloted to you")
				
				else:
					return HttpResponse("Both the rooms are occupied.Try again")

			else:
				return HttpResponse("Enter a valid room no.")           
		
		else:
			return HttpResponse("Field Cannot Be Empty")


	return HttpResponse("Something went wrong.Try again")               

def accept_page(request):
	
	context = RequestContext(request)
	roll = None
	data=None
	if request.method == 'GET':
		roll = request.GET['roll']
		data=request.GET['data_room']
		try:
			if '1 Available' in data:   
				student=Student.objects.get(roll_no=roll)
				student_owner=Student.objects.get(roll_no=request.user) 
				if student.room_alloted==0 :
					student.room_alloted=student_owner.room_alloted
					student.save()
					notification=Notifications.objects.get(roll_no_reciever=request.user,roll_no_sender=roll)
					notification.delete()   
					return HttpResponse("1")

		
				else:
					notification=Notifications.objects.get(roll_no_reciever=request.user,roll_no_sender=roll)
					notification.delete()   
					
					return HttpResponse("He already occupied the room")
			else:
				notification=Notifications.objects.get(roll_no_reciever=request.user,roll_no_sender=roll)
				notification.delete()   

				return HttpResponse("You have already accepted someone's request")
		
		except:
			return HttpResponse("Something went wrong")

def reject_page(request):
	context = RequestContext(request)
	roll = None
	if request.method == 'GET':
		roll = request.GET['roll']
		try:
			
			notification=Notifications.objects.get(roll_no_reciever=request.user,roll_no_sender=roll)
			notification.delete()   
			return HttpResponse('/portal/') 
		except:
			return HttpResponse("Something went wrong.Try again")
def get_room(request):
	student=Student.objects.get(roll_no=request.user)
	room=student.room_alloted
	return HttpResponse(room)   
def available_page(request):
	hostel=""
	if request.method == 'GET':
		try:
			hostel = request.GET['search_hostel']
			x=Rooms.objects.filter(Q(hostel_name=hostel),~Q(roll_no_1="0EN0"),~Q(roll_no_2="0EN0"))
			#print type(x)
			#print x
			data = serializers.serialize('json', list(x), ensure_ascii=True)
			#print data
			#y=ValuesQuerySetToDict(x)
			#print y['room_no']
			#print y['room_no']
			#print y.encode ('UTF-8')
			k=eval(data)
			lm=list()
			#i=0
			for ih in k:
				#print ih['fields']
				lm.append(ih['fields'])
				#print i
				#i+=1
		
			return HttpResponse(json.dumps(lm))
		except:
			#print "wtf"
			return HttpResponse("Something went wrong")

