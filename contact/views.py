from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect, HttpResponse
from pis_website.forms import *
from django.contrib import auth
from pis_website.models import *
from django.core.mail import EmailMultiAlternatives

SYSTEM_NAME = 'Philippine Integrated School Foundation Inc.'

def contact_index(request):
    template_name = './contact/contact_page.html'
    data = {'system_name' : SYSTEM_NAME,
            'contactus'   : 'active'}
    return render(request, template_name, data)

def contact_send(request):
	full_name = request.POST.get('name')
	c_number = request.POST.get('c_number')
	email = request.POST.get('email')
	message_form = request.POST.get('message')
	subject, from_email, to_email = 'PISFI Website', 'senderpis@gmail.com', 'hanifnasser30@gmail.com'
	text_content = "From "+email+" ("+full_name+"), \n\nPhone Number: "+c_number+" \n\n\n"+message_form
	#html_content = "From "+email+" ("+full_name+"), "+c_number+""+"<br/><br/><br/>"+message_form % (full_name, email, email)
	message      = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
	#message.attach_alternative(html_content, "text/html")
	message.send()
	template_name = './contact/contact_page.html'
	data = {'system_name' : SYSTEM_NAME,
			'contactus'   : 'active',
			'success': 'yes'}

	return render(request, template_name, data)


