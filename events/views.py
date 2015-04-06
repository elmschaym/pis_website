from django.shortcuts import render, render_to_response, redirect, RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from pis_website.forms import *
from django.contrib import auth
from pis_website.models import (
		Events
	)
import json
# Create your views here.
def login_page(request):
    form=LogInForm()
    user = request.session.get('user')
    redirect_to = '/dashboard'
    system = 'Dashboard'
    names = {
      
      }
    if user is not None: 
    	return HttpResponseRedirect('/pis_admin/')
    	
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            employee = auth.authenticate(username=form.cleaned_data['userID'], password=form.cleaned_data['password'])
          
            if employee is not None and employee.is_active:
                request.session.set_test_cookie()
                auth.login(request,employee)
                request.session['user'] = {'id':employee.id, 'userID': employee.username, 'firstname':employee.first_name, 'lastname':employee.last_name}
                
               	return HttpResponseRedirect('/pis_admin/')
            else:
                return HttpResponseRedirect('/events/login?valid=ok&has_access=no')
        else:
            return HttpResponseRedirect('/events/login?valid=ok&has_access=no')        
    # if 'next' in request.GET:
    #   redirect_to = request.GET.get('next')
    #   system = names[redirect_to]
      
    return render(
                  request,
                  'login.html',
                  {
                      #'action_url': '',
                      'form': form,
                      'system_name': system,
                      'valid': request.GET.get('valid', 'none'),
                      'has_access': request.GET.get('has_access', 'none'),
                      'login':'active'
                      
                  }
                )


def view_news(request):
  context = RequestContext(request)
  params = json.loads(request.body)
  news_id = params['news_id']
	
  news = Events.objects.get(id=news_id)
  return render_to_response('./events/view_news.html', {'news':news}, context)

