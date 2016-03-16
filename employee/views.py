from django.shortcuts import render, render_to_response, redirect, RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from pis_website.forms import *
from django.contrib import auth
from pis_website.models import (
		Events
	)
# Create your views here.
SYSTEM_NAME = 'Philippine Integrated School Foundation Inc.'
def view_board_of_trustess(request):
  return render(request,
    './employee/board_of_trustees.html',
    {
      'system_name' : SYSTEM_NAME + ' - Board of Trustees',
      'aboutus':'active'
    }
  )

def administrative(request):
  return render(request,
    './employee/administrative.html',
    {
      'system_name' : SYSTEM_NAME + ' - Execom',
      'aboutus':'active'
    }
  )

def execom(request):
  return render(request,
    './employee/execom.html',
    {
      'system_name' : SYSTEM_NAME + ' - Execom',
      'aboutus':'active'
    }
  )

def developers(request):
  return render(request,
    './employee/developers.html',
    {
      'system_name' : SYSTEM_NAME + ' - Execom',
    }
  )

