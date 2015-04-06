import json
import datetime
from django.shortcuts import render, render_to_response, redirect, RequestContext
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from pis_website.models import (
		Events
	)
SYSTEM_NAME = 'Philippine Integrated School Foundation Inc.'

def index(request):
	#news = Events.objects.filter(category='N').order_by('date_start')
	events = Events.objects.filter(category='E').order_by('date_start')
	request.session['limit'] = 5
	request.session['limit_events'] = 5
	return render_to_response(
		'index.html',
		{
			'system_name' : SYSTEM_NAME + ' - Home',
			'home':'active',
			##'news' : news,
			'events' : events
		},
		RequestContext(request)
	)

def news(request):
	context = RequestContext(request)
	a_hide = False
	#params = json.loads(request.body)
	news = Events.objects.filter(category='N').order_by('date_start')[:5]
	if news and news.count() > 4:
		a_hide = True
	news_result = []
	for x in news:
		news_result.append({
				'id':x.id,
				'subject':x.subject,
				'description': x.description,
				'category':x.category,
				'date_created': str(x.date_created),
				'date_start': str(x.date_start),
				'date_end': str(x.date_end)
			})

	data={'result':news_result, 'a_hide': a_hide}
	json_response = json.dumps(data)
	return HttpResponse(json_response, content_type = 'application/json')

def events(request):
	context = RequestContext(request)
	a_hide = False
	#params = json.loads(request.body)
	events = Events.objects.filter(category='E').order_by('date_start')[:5]
	if events and events.count() >4:
		a_hide=True
	events_result = []
	for x in events:
		date_s = x.date_start.strftime('%B') #date(int(x.date_start.partition[0]),int(x.date_start.partition[1]),1).strftime('%B')
		# print date_s[:3]
		events_result.append({
				'id':x.id,
				'subject':x.subject,
				'description': x.description,
				'category':x.category,
				'date_created': str(x.date_created),
				'date_start': str(x.date_start),
				'date_end': str(x.date_end),
				'month': str(date_s[:3])
				
			})

	data={'result':events_result,'a_hide': a_hide}
	json_response = json.dumps(data)
	return HttpResponse(json_response, content_type = 'application/json')


def news_limit(request):
	print 'pasok sa news_limit'
	a_hide = False
	context = RequestContext(request)
	#params = json.loads(request.body)
	news = Events.objects.filter(category='N').order_by('date_start')[0:request.session['limit']+5]
	
	request.session['limit'] = request.session['limit']+5
	print request.session['limit'], 'request'
	print news.count(), 'count'
	if news.count() >= request.session['limit']:
		print request.session['limit'], 'if'
		a_hide = True

	print a_hide
	
	news_result = []
	for x in news:
		# month = x.date_start.partition('-')[0]
		# print str(month)[:3]
		news_result.append( {
				'id':x.id,
				'subject':x.subject,
				'description': x.description,
				'category':x.category,
				'date_created': str(x.date_created),
				'date_start': str(x.date_start),
				'date_end': str(x.date_end)
			})
	print len(news_result)
	data={'result':news_result,'a_hide': a_hide}
	json_response = json.dumps(data)
	return HttpResponse(json_response, content_type = 'application/json')

def news_limit_events(request):
	print 'pasok sa news_limit'
	a_hide = False
	context = RequestContext(request)
	#params = json.loads(request.body)
	events = Events.objects.filter(category='E').order_by('date_start')[0:request.session['limit_events']+5]
	
	request.session['limit_events'] = request.session['limit_events']+5
	print request.session['limit_events'], 'request'
	print events.count(), 'count'
	if events.count() >= request.session['limit_events']:
		print request.session['limit_events'], 'if'
		a_hide = True

	print a_hide
	
	events_result = []
	for x in events:
		date_s = x.date_start.strftime('%B')
		# month = x.date_start.partition('-')[0]
		# print str(month)[:3]
		events_result.append( {
				'id':x.id,
				'subject':x.subject,
				'description': x.description,
				'category':x.category,
				'date_created': str(x.date_created),
				'date_start': str(x.date_start),
				'date_end': str(x.date_end),
				'month': str(date_s[:3])
			})
	print len(events_result)
	data={'result':events_result,'a_hide': a_hide}
	json_response = json.dumps(data)
	return HttpResponse(json_response, content_type = 'application/json')
