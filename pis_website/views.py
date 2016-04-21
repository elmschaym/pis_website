import json
import datetime
import csv
import codecs
from django.shortcuts import render, render_to_response, redirect, RequestContext
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from pis_website.models import (
		Events
	)
from student.models import (
		Student,
		StudentFinancial,
        StudentGrades
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

def school_year_funtion():
  month_s = datetime.datetime.now().month
  if month_s > 3:
    today_year = datetime.datetime.now().year
  else:
    today_year = datetime.datetime.now().year
    today_year = today_year - 1
  start_year = today_year
  end_year =   today_year + 1
  return str(start_year)+'-'+str(end_year)

def csv_student(request):
    if request.POST and request.FILES:
        csvfile = request.FILES['csv_file']
        dialect = csv.Sniffer().sniff(codecs.EncodedFile(csvfile, "utf-8").read(1024))
        csvfile.open()
        reader = csv.reader(codecs.EncodedFile(csvfile, "utf-8"), delimiter=',', dialect=dialect)
        file_upload = False
        success = False
        for x in reader:
        	
        	if x[0] =='Student':
        		file_upload = True
        	else:
        		if Student.objects.filter(studentid=x[0]).exists():
        				student_update = Student.objects.get(studentid=x[0])
        		if file_upload:
        			
        			if Student.objects.filter(studentid=x[0]).exists():
						student_update.firstname = x[1]
						student_update.middlename = x[2]
						student_update.lastname = x[3]
						student_update.gender = x[4]
						student_update.date_of_birth =x[5]
						student_update.date_admitted = x[6]
						student_update.address = x[7]
						student_update.mother_name = x[8]
						student_update.father_name = x[9]
						student_update.mother_occ =  x[10]
						student_update.father_occ = x[11]
						student_update.last_school_att = x[12]
						student_update.last_school_att_address = x[13]
						student_update.acad_status = x[14]
						student_update.privilege = x[15]
						student_update.year_level = x[16]
						student_update.cell_no = x[17]
						student_update.Section = x[18]
						student_update.password = x[19]
						success = True

			        else:

			        		student_create = Student(

								studentid = x[0],
							    firstname = x[1],
							    middlename = x[2],
							    lastname = x[3],
							    gender = x[4],
							    date_of_birth =x[5],
							    date_admitted = x[6],
							    address = x[7],
							    mother_name = x[8],
							    father_name = x[9],
							    mother_occ =  x[10],
							    father_occ = x[11],
							    last_school_att = x[12],
							    last_school_att_address = x[13],
							    acad_status = x[14],
							    privilege = x[15],
							    year_level = x[16],
							    cell_no = x[17],
							    Section = x[18],
							    password = x[19],
			        		)
				        	student_create.save()
				        	success = True
				student_update.save()
		      
    	if success:
			return render(request,'msge.html', {'success':'success'} )
    else:
    	return render(request,'msge.html', {'success':'no'} )
    return render(request,'msge.html', {'success':'no'} )

def csv_financial(request):
    if request.POST and request.FILES:
        csvfile = request.FILES['csv_file']
        dialect = csv.Sniffer().sniff(codecs.EncodedFile(csvfile, "utf-8").read(1024))
        csvfile.open()
        reader = csv.reader(codecs.EncodedFile(csvfile, "utf-8"), delimiter=',', dialect=dialect)
        #files = csv.reader(codecs.EncodedFile(csvfile, "utf-8"), delimiter=',', dialect=dialect)
        #data = [x[0] for x in files]
        StudentFinancial.objects.filter(school_year=school_year_funtion).delete()
        success = False
        #if data[0]=='Financial':
        file_upload = False
        for x in reader:
            if x[0] =='Financial':
                file_upload = True
            else:
            	
                if file_upload:
                	if Student.objects.filter(studentid= x[0]).exists():
	                    st = StudentFinancial(
	                        student_id = x[0],
	                        bill_item = x[1],
	                        amount = x[2],
	                        school_year = x[3],

	                    )
	                    st.save()
	                    success =  True
        if success:
			return render(request,'msge.html', {'success':'success'} )
    else:
    	return render(request,'msge.html', {'success':'no'} )
    return render(request,'msge.html', {'success':'no'} )

def csv_grades(request):
    if request.POST and request.FILES:
        csvfile = request.FILES['csv_file']
        dialect = csv.Sniffer().sniff(codecs.EncodedFile(csvfile, "utf-8").read(1024))
        csvfile.open()
        reader = csv.reader(codecs.EncodedFile(csvfile, "utf-8"), delimiter=',', dialect=dialect)
        #files = csv.reader(codecs.EncodedFile(csvfile, "utf-8"), delimiter=',', dialect=dialect)
        #data = [x[0] for x in files]
        #StudentFinancial.objects.filter(school_year=school_year_funtion).delete()
        success = False
        #if data[0]=='Financial':
        file_upload = False
        for x in reader:
            
            if x[0] =='Grades':
                file_upload = True
            else:
                if file_upload:
                	if Student.objects.filter(studentid= x[0]).exists():
	                    st = StudentGrades.objects.update_or_create(
	                        student_id = x[0],
	                        subject = x[1],
	                        q1 = x[2],
	                        q2 = x[3],
	                        q3 = x[4],
	                        q4 = x[5],
	                        final = x[6],
	                        school_year = x[7] 

	                    )
	                    success =  True
        if success:
            return render(request,'msge.html', {'success':'success'} )
    else:
        return render(request,'msge.html', {'success':'no'} )
    return render(request,'msge.html', {'success':'no'} )

def real_monitoring(request):
	
	return render_to_response(
		'real_monitor.html',
		{
			'system_name' : SYSTEM_NAME + ' - Real Monitoring',
			'url_monitor':'http://192.168.0.159',
			'rtm':'active',
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
