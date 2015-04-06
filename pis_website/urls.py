from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import *
from django.contrib.auth.views import logout
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'pis_website.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^pis_admin/', include(admin.site.urls)),
                       url(r'^$', index),
                       url(r'news/$', news),
                       url(r'events/$', events),
                       url(r'news_view_more/$', news_limit),
                       url(r'news_view_more_event/$', news_limit_events),
                       url(r'^events/', include('events.urls')),
                       url(r'^employee/', include('employee.urls')),
                       url(r'^student/', include('student.urls')),    
                       url(r'^contact/', include('contact.urls')),    

)
urlpatterns += patterns(
    'django.views.static',
    (r'media/(?P<path>.*)',
     'serve',
     {'document_root': settings.MEDIA_ROOT}), )
