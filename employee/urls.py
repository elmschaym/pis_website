from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login
from employee.views import( 
    view_board_of_trustess,
    administrative,
    execom,
    developers
)
  
urlpatterns = patterns('',
                       url(r'^boardoftrustees$', view_board_of_trustess),
                       url(r'^administrative$', administrative),
                       url(r'^execom$', execom),
                       url(r'^developers$', developers),

)
