from django.shortcuts import render_to_response

# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required
def portal_main_page(request):
    """
    If users are authenticated, direct them to the main page. Otherwise, take
    them to the login page.
    """
    return render_to_response('portal/index.html',{'user':request.user})
def staff_page(request):
	return render_to_response('portal/staff.html',{'user':request.user})
def complaint_page(request):
	return render_to_response('portal/complaint.html',{'user':request.user})
def suggestion_page(request):
	return render_to_response('portal/status.html',{'user':request.user})
