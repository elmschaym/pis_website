from django.shortcuts import render, render_to_response, redirect, RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from pis_website.forms import *
from django.contrib import auth
from pis_website.models import *

SYSTEM_NAME = 'Philippine Integrated School Foundation Inc.'

def contact_index(request):
    template_name = './contact/contact_page.html'
    data = {'system_name' : SYSTEM_NAME,
            'contactus'   : 'active'}
    return render(request, template_name, data)


