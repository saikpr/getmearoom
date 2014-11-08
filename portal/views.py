from django.shortcuts import render_to_response
from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
from django.contrib.auth.decorators import login_required
from portal.models import *
from django.template import RequestContext
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from portal.forms import *
import string,re
@login_required
def portal_main_page(request):
    """
    If users are authenticated, direct them to the main page. Otherwise, take
        them to the login page.
    """
    name=[]
    context = RequestContext(request)
    try:
        batch=Batch.objects.get(roll_no=Student.objects.get(roll_no=request.user))
        department=batch.department
        year=batch.year
        t=HostelAlloted.objects.get(department=department,year=year)
        hostel_name=Hostel.objects.get(hostel_name=t.hostel_name)   
        context_dict={}
        context_dict['hostel_name'] = hostel_name
        context_dict['hostel_link']=hostel_name.image_path
        user=Student.objects.get(roll_no=request.user)      
        context_dict['user']=user
        try:        
            notifications=Notifications.objects.all().filter(roll_no_reciever=request.user)
            context_dict['notifications']=notifications
            for sender in notifications:
                name.append(Student.objects.get(roll_no=sender.roll_no_sender))
            context_dict['name']=name
        except Notifications.DoesNotExist:
            context_dict['notifications']="No notifications"        
            
    except Hostel.DoesNotExist:
        pass

        return render(request,'portal/index.html',context_dict)


@login_required
def staff_page(request):
    user1=Student.objects.get(roll_no=request.user)
    user=user1.first_name
    return render_to_response('portal/staff.html',{'user':user})
@login_required
def wardenProfile_page(request):
    user1=Student.objects.get(roll_no=request.user)
    user=user1.first_name   
    return render_to_response('portal/wardenProfile.html',{'user':user})
@login_required
def staffProfile_page(request):
    user1=Student.objects.get(roll_no=request.user)
    user=user1.first_name   
    return render_to_response('portal/staffProfile.html',{'user':user})


@login_required
def complaint_page(request):
    user1=Student.objects.get(roll_no=request.user)
    user=user1.first_name   
    complaints=Complaints.objects.all().order_by('-date_time').select_related()
    error=""
    name=[]
    roll=""
    
    if request.method == 'POST':
        if request.POST.get('complaint')!="":
            message=request.POST.get('complaint')           
            x=Complaints(roll_no=user1,message=message)
            try:    
                
                x.save()
                complaints=Complaints.objects.all().order_by('-date_time')
            except ValidationError,e:
                return render(request,'portal/complaint.html',{'user':user,'error_complaint':e.message_dict,'complaints':complaints,'name':name})
            
            return render(request,'portal/complaint.html',{'user':user,'complaints':complaints,'name':name})
        else:
            error="Field cannot be empty"
    return render(request,'portal/complaint.html',{'user':user,'complaints':complaints,'name':name,'error_complaint':error})

@login_required
def suggestion_page(request):
    user1=Student.objects.get(roll_no=request.user)
    user=user1.first_name   
    suggestion=Suggestions.objects.all().order_by('-date_time').select_related()
    error=""
    name=[]
    roll=""
    
    if request.method == 'POST':
        if request.POST.get('suggestion')!="":
            message=request.POST.get('suggestion')          
            x=Suggestions(roll_no=user1,message=message)
            try:    
                
                x.save()
                suggestion=Suggestions.objects.all().order_by('-date_time')
            except ValidationError,e:
                return render(request,'portal/suggestion.html',{'user':user,'error_suggestion':e.message_dict,'suggestion':suggestion,'name':name})
            
            return render(request,'portal/suggestion.html',{'user':user,'suggestion':suggestion,'name':name})
        else:
            error="Field cannot be empty"
    return render(request,'portal/suggestion.html',{'user':user,'suggestion':suggestion,'name':name,'error_suggestion':error})
    

    
    
        
def verify_page(request,hash):
    
    try:
        hash_temp=Verification.objects.get(hash_value=hash)
        username=hash_temp.roll_no
        email=hash_temp.email
        password=hash_temp.password
    except:
        return render(request,'portal/failed_verify.html')
    if request.method == 'POST':
        
            form = StudentForm(request.POST)
        # check whether it's valid:
            if form.is_valid():
                    # process the data in form.cleaned_data as required
                    # ...
                    # redirect to a new URL:
                firstname=form.cleaned_data["firstName"]
                lastname=form.cleaned_data["lastName"]
                gender=form.cleaned_data["gender"]
                fathername=form.cleaned_data["fatherName"]
                mothername=form.cleaned_data["motherName"]                  
                address=form.cleaned_data["address"]
                department=form.cleaned_data["department"]
                course=form.cleaned_data["course"]
                mobile=form.cleaned_data["mobile"]
                year=form.cleaned_data["year"]
                x=Student(roll_no=username,first_name=firstname,last_name=lastname,gender=gender,email=email,father_name=fathername,mother_name=mothername,address=address,contact_no=mobile)
                if not re.match("^[a-zA-Z\s]*$", firstname):                
                    return render(request, 'portal/form.html',{'form': form,'error':"Firstname should contain only characters and whitespace",'hash':hash})
                if not re.match("^[a-zA-Z\s]*$", lastname):             
                    return render(request, 'portal/form.html',{'form': form,'error':"Lastname should contain only characters and whitespace",'hash':hash})
                if not re.match("^[a-zA-Z\s]*$", mothername):               
                    return render(request, 'portal/form.html',{'form': form,'error':"Mothername should contain only characters and whitespace",'hash':hash})
                if not re.match("^[a-zA-Z\s]*$", fathername):               
                    return render(request, 'portal/form.html',{'form': form,'error':"Fathername should contain only characters and whitespace",'hash':hash})
                if len(mobile)!=10 or not mobile.isdigit():
                    return render(request, 'portal/form.html',{'form': form,'error':"Invalid mobile number",'hash':hash})
                
                try:
                    x.full_clean()
                    x.save()
                    y=Batch(roll_no=Student.objects.get(roll_no=username),year=year,department=department)          
                    try:
                        y.full_clean()
                        y.save()
                        try:                
                            user=User.objects.create_user(username=username,password=password,email=email)
                            user.save()        
                            userLog=authenticate(username=username, password=password,email=email)
                            login(request,userLog)
                            return HttpResponseRedirect('/portal/preference/'+hash)
                        
                        except:
                            return render(request,'portal/success.html')
                
                    
                    except ValidationError,e:
                            
                        return render(request, 'portal/form.html',{'form': form,'error':e.message_dict,'hash':hash})
                except ValidationError,e:
                    #return render(request,'portal/success.html')       
                    return render(request, 'portal/form.html',{'form': form,'error':e.message_dict,'hash':hash})
            
            
                

    # if a GET (or any other method) we'll create a blank form
            
            
    else:
        form = StudentForm()
    return render(request, 'portal/form.html', {'form': form,'hash':hash})
        



def preference_page(request,hash):
    hostel=""   
    link=""
    try:
        y=Verification.objects.get(hash_value=hash)
        
        batch=Batch.objects.get(roll_no=Student.objects.get(roll_no=request.user))
        department=batch.department
        year=batch.year
        t=HostelAlloted.objects.get(department=department,year=year)
        hostel=Hostel.objects.get(hostel_name=t.hostel_name)            
        a=Hostel.objects.get(hostel_name=hostel)
        link=a.image_path
    
    except:
        return render(request,'portal/success.html')
    
    if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = PreferenceForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                pref1=form.cleaned_data['pref1']
                pref2=form.cleaned_data['pref2']
            
            
                                
                x=Preference(pref1=pref1,pref2=pref2,roll_no=Student.objects.get(roll_no=request.user),hostel_name=hostel)
                x.full_clean()
                x.save()
                z=Verification.objects.get(hash_value=hash)
                z.delete()
                return HttpResponseRedirect('/portal/')
                        
            
            #   return render(request, 'portal/preference.html', {'form': form,'hash':hash,'error':"error"})

                

    else:
        form = PreferenceForm()
            
            
    return render(request, 'portal/preference.html', {'form': form,'hash':hash,'hostel':hostel,'link':link})

def pass_change(request,hash):
    try:
        hash_temp=Verification.objects.get(hash_value=hash)
        username=hash_temp.roll_no
        email=hash_temp.email
        password=hash_temp.password
    except:
    
        return render(request,'portal/failed_verify.html')
    if request.method == 'POST':
        form = PassRecoveryForm(request.POST)
        if form.is_valid():
            Pass=form.cleaned_data["password"]
            PassC=form.cleaned_data["passwordC"]
            if Pass==PassC:
                try:
                    x=User.objects.get(username=username)
                    x.set_password(Pass)
                    x.save()
                    hash_temp.delete()
                    return render(request, 'portal/pass_success.html')
                except:
                    return render(request, 'portal/pass_recovery.html', {'form': form,'hash':hash,'error':"Error in connection"})

            else:
                return render(request, 'portal/pass_recovery.html', {'form': form,'hash':hash,'error':"Password Doesnot match"})
    else:
        form = PassRecoveryForm()
    return render(request, 'portal/pass_recovery.html', {'form': form,'hash':hash})




                    
        
        
    
    
