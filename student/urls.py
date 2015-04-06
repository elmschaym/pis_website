from django.conf.urls import patterns, include, url
from .views import  *

urlpatterns = patterns('',
    url(r'^$', index_view),
    url(r'^login/$', login_view),
    url(r'^logout/$', logout_view)
)