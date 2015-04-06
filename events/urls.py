from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login
from events.views import( 
    login_page,
    view_news,

)
  
urlpatterns = patterns('',
                       url(r'^login?', login_page),
                       url(r'^news$', view_news),
)
