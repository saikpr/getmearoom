from django.conf.urls import patterns, include, url
from django.contrib import admin

from mysite.views import *
urlpatterns = patterns('',
(r'^$',main_page),
#login/logout
(r'^login/$','django.contrib.auth.views.login'),
(r'^logout/$',logout_page),

#web portal
(r'^portal/',include('portal.urls')),
 # Serve static content.
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': 'static'}),
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

   # url(r'^admin/', include(admin.site.urls)),
)
