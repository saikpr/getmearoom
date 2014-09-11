from django.conf.urls import patterns,url,include
from portal.views import *

urlpatterns = patterns('',

    # Main web portal entrance.
    (r'^$', portal_main_page),

)
