from django.contrib import admin
from portal.models import *
from django.contrib.admin import AdminSite
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    # ...
    list_display = ('roll_no', 'first_name','last_name')
class RegistrationAdmin(admin.ModelAdmin):
    # ...
    list_display = ('roll_no', 'year','semester','no_dues','fee_id')
class WardenAdmin(admin.ModelAdmin):
    # ...
    list_display = ('warden_id', 'warden_name','contact_no')
class BatchAdmin(admin.ModelAdmin):
    # ...
    list_display = ('roll_no', 'year','department')
class HostelAllotedAdmin(admin.ModelAdmin):
    # ...
    list_display = ('year', 'department','hostel_name')
class NotificationsAdmin(admin.ModelAdmin):
    # ...
    list_display = ('roll_no_sender', 'roll_no_reciever','status')
class PrefAdmin(admin.ModelAdmin):
    # ...
    list_display = ('roll_no', 'pref1','pref2','hostel_name')
class MyAdminSite(AdminSite):
    site_header = 'New Administration'
admin_site = MyAdminSite(name='myadmin')

admin.site.register(Registration,RegistrationAdmin)
admin.site.register(Hostel)
admin.site.register(HostelAlloted,HostelAllotedAdmin)
admin.site.register(Department)
admin.site.register(Warden,WardenAdmin)
admin.site.register(Batch,BatchAdmin)
admin.site.register(Notifications,NotificationsAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(Preference,PrefAdmin)
admin.site.register(Verification)
