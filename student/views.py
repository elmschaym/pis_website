from django.shortcuts import render_to_response, RequestContext
from django.http import  HttpResponseRedirect, HttpResponse
from .forms import Login_Form
from pis_website.models import *
from django.db import connection
import datetime

SYSTEM_NAME = 'Philippine Integrated School Foundation Inc.'

def myuser_login_required(f):
        def wrap(request, *args, **kwargs):
                #this check the session if userid key exist, if not it will redirect to login page
                print request.session.keys()
                if 'current_user' not in request.session.keys():
                        return HttpResponseRedirect("/student")
                return f(request, *args, **kwargs)
        wrap.__doc__=f.__doc__
        wrap.__name__=f.__name__

        return wrap

def getStudentBills(student_id):
    student = Student.objects.get(studentid = student_id)
    
    if StudentSection.objects.filter(student = student_id).exists():
        section = StudentSection.objects.get(student = student_id)
    else:
        section = False
        
    assign_item         = AssignBillItem.objects.get(year_level=student.year_level,item_type='T')
    monthly_tuition_sum = 0.00
    cursor              = connection.cursor()
  
    cursor.execute("SELECT count(*) from bill_account where \
        extract(year from date_added) = %s and bill_item_name_id = %s and \
        student_id = %s and balance <> %s", 
        [datetime.datetime.now().year,assign_item.bill_item_id_id,student_id,0]
    )
    
    monthly_tuition_count = cursor.fetchone()[0]
    student_privilege     = StudentPrivilege.objects.all()
    
    bills = BillAccount.objects.filter(student = student_id).exclude(balance=0)
    total = sum([float(x.balance) for x in bills])
    dis   = 0.0
    
    
    if monthly_tuition_count > 4:
        if monthly_tuition_count < 10:
            dis = float(5)
        else:
            dis = float(10)
            
    total_due = sum([float(x.balance) for x in bills if x.bill_item_name == assign_item.bill_item_id])
    due       = "{:,.2f}".format(total - ((dis/100) * total_due))
    total     = "{:,.2f}".format(total)
    
    return {
        'bills'      : bills,
        'total'      : total,
        'due'        : due,
        'privileges' : student_privilege,
        'section'    : section,
    }
    
def getStudentGrades(student_id):
    student  = Student.objects.get(studentid = student_id)
    subjects = Subject.objects.filter(year_level = student.year_level)
    divisor  = 0
    
    q1_average     = []
    q2_average     = []
    q3_average     = []
    q4_average     = []
    final_average  = []
    mq1_average    = []
    mq2_average    = []
    mq3_average    = []
    mq4_average    = []
    mfinal_average = []
    dict           = {}
                
    for subject in subjects:
        if StudentSubjects.objects.filter(student = student, subject = subject).exists():
            grade = StudentSubjects.objects.get(student = student, subject = subject) 
        else:
            grade = False
            
        if subject.subject_type == 2:
            if grade:
                q1_average.append(float(grade.q1) / 4)
                q2_average.append(float(grade.q2) / 4)
                q3_average.append(float(grade.q3) / 4)
                q4_average.append(float(grade.q4) / 4)
                final_average.append(round(float(grade.final) / 4))
        elif subject.subject_type == 3:
            if subject.title != 'Araling Panlipunan':
                if grade:
                    mq1_average.append(float(grade.q1) * 0.4)
                    mq2_average.append(float(grade.q2) * 0.4)
                    mq3_average.append(float(grade.q3) * 0.4)
                    mq4_average.append(float(grade.q4) * 0.4)
                    mfinal_average.append(round(float(grade.final) * 0.4))
            else:
                if grade:
                    mq1_average.append(float(grade.q1))
                    mq2_average.append(float(grade.q2))
                    mq3_average.append(float(grade.q3))
                    mq4_average.append(float(grade.q4))
                    mfinal_average.append(round(float(grade.final)))
        else:
            if grade:
                q1_average.append(float(grade.q1))
                q2_average.append(float(grade.q2))
                q3_average.append(float(grade.q3))
                q4_average.append(float(grade.q4))
                final_average.append(round(float(grade.final)))
        
        if grade:    
            dict[subject] = {
                'q1'    : grade.q1,
                'q2'    : grade.q2,
                'q3'    : grade.q3,
                'q4'    : grade.q4,
                'final' : round(grade.final),
            }
        else:
            dict[subject] = {
                'q1'    : 'No grade yet',
                'q2'    : 'No grade yet',
                'q3'    : 'No grade yet',
                'q4'    : 'No grade yet',
                'final' : 'No grade yet',
            }
    
    if student.year_level > 0 and student.year_level < 4: divisor = 4
    elif student.year_level > 3 and student.year_level < 7: divisor = 10
    elif (student.year_level > 6 and student.year_level < 10) or student.year_level == 13: divisor = 8
    elif student.year_level > 9 and student.year_level < 13: divisor = 11
    
    return {
        'grades'        : dict,
        'q1_average'    : sum(q1_average) / len(q1_average) if len(q1_average) < 4  else (sum(q1_average) + (sum(mq1_average) / 2.2)) / divisor,
        'q2_average'    : sum(q2_average) / len(q2_average) if len(q2_average) < 4  else (sum(q2_average) + (sum(mq2_average) / 2.2)) / divisor,
        'q3_average'    : sum(q3_average) / len(q3_average) if len(q3_average) < 4  else (sum(q3_average) + (sum(mq3_average) / 2.2)) / divisor,
        'q4_average'    : sum(q4_average) / len(q4_average) if len(q4_average) < 4  else (sum(q4_average) + (sum(mq4_average) / 2.2)) / divisor,
        'final_average' : sum(final_average) / len(final_average) if len(final_average) < 4  else (sum(final_average) + (sum(mfinal_average) / 2.2)) / divisor,
    }
    
def getStudentAttendanceAndBehaviour(student_id):
    return AttendanceAndBehaviour.objects.filter(student = Student.objects.get(studentid = student_id)).order_by('-date')

def index_view(request):
    if request.session.get('msg'):
        del request.session['msg']
    user_in_session = request.session.get('user_in_session')
    if user_in_session:
        student        = Student.objects.get(studentid = user_in_session['username'])
        student_bills  = getStudentBills(student.studentid)
        student_grades = getStudentGrades(student.studentid)
        student_a_and_b = getStudentAttendanceAndBehaviour(student.studentid)
        
        return render_to_response(
            'student/base.html',
            {
             'system_name'    : student.firstname+ ' ' +student.middlename+ ' ' +student.lastname+ ' - ' +SYSTEM_NAME,
             'student'        : student,
             'bills'          : student_bills['bills'],
             'total'          : student_bills['total'],
             'due'            : student_bills['due'],
             'privileges'     : student_bills['privileges'],
             'section'        : student_bills['section'],
             'grades'         : student_grades['grades'].items(),
             'q1_average'     : student_grades['q1_average'],
             'q2_average'     : student_grades['q2_average'],
             'q3_average'     : student_grades['q3_average'],
             'q4_average'     : student_grades['q4_average'],
             'final_average'  : student_grades['final_average'],
             'att_and_behaviour' : student_a_and_b, 
             'student_hov' : 'active'
            },
            RequestContext(request)
        )

    if request.method == 'POST':
        login_form = Login_Form(request.POST)
        
        if login_form.is_valid():
            username = str(login_form.cleaned_data['username']) 
            password = login_form.cleaned_data['password']
            
            if not StudentGradeInquiry.objects.filter(studentid = username).exists():
                if Student.objects.filter(studentid=username).exists():
                    if login_form.cleaned_data['password'] == 'pisstudent12345':
                        student  = Student.objects.get(studentid = username)
                        request.session['current_user'] = str(student.studentid)
                        request.session['user_in_session'] = {
                            'username' : username,
                            'password' : password,
                        }
                        
                        account = StudentGradeInquiry(
                                studentid  = student, 
                                access_key = password,
                                )
                         
                        account.save()
                        
                        student_bills  = getStudentBills(student.studentid)
                        student_grades = getStudentGrades(student.studentid)
                        student_a_and_b = getStudentAttendanceAndBehaviour(student.studentid)
                
                        return render_to_response(
                            'student/base.html',
                            {
                             'system_name'    : student.firstname+ ' ' +student.middlename+ ' ' +student.lastname+ ' - ' +SYSTEM_NAME,
                             'student'        : student,
                             'bills'          : student_bills['bills'],
                             'total'          : student_bills['total'],
                             'due'            : student_bills['due'],
                             'privileges'     : student_bills['privileges'],
                             'section'        : student_bills['section'],
                             'grades'         : student_grades['grades'].items(),
                             'q1_average'     : student_grades['q1_average'],
                             'q2_average'     : student_grades['q2_average'],
                             'q3_average'     : student_grades['q3_average'],
                             'q4_average'     : student_grades['q4_average'],
                             'final_average'  : student_grades['final_average'],
                             'att_and_behaviour' : student_a_and_b, 
                             'student_hov' : 'active'

                            },
                            RequestContext(request)
                        )
                    else:
                        request.session['msg'] = 'Sorry something went wrong, you have entered an invalid password.'
                else:
                    request.session['msg'] = 'Sorry something went wrong, you have entered an invalid username.'
            
            elif StudentGradeInquiry.objects.filter(studentid = Student.objects.get(studentid=username), access_key=password).exists():
                student  = Student.objects.get(studentid = username)
                
                request.session['current_user'] = str(student.studentid)
                request.session['user_in_session'] = {
                    'username' : username,
                    'password' : password,
                }
                
                student_bills   = getStudentBills(student.studentid)
                student_grades  = getStudentGrades(student.studentid)
                student_a_and_b = getStudentAttendanceAndBehaviour(student.studentid)
                
                return render_to_response(
                    'student/base.html',
                    {
                     'system_name'    : student.firstname+ ' ' +student.middlename+ ' ' +student.lastname+ ' - ' +SYSTEM_NAME,
                     'student'        : student,
                     'bills'          : student_bills['bills'],
                     'total'          : student_bills['total'],
                     'due'            : student_bills['due'],
                     'privileges'     : student_bills['privileges'],
                     'section'        : student_bills['section'],
                     'grades'         : student_grades['grades'].items(),
                     'q1_average'     : student_grades['q1_average'],
                     'q2_average'     : student_grades['q2_average'],
                     'q3_average'     : student_grades['q3_average'],
                     'q4_average'     : student_grades['q4_average'],
                     'final_average'  : student_grades['final_average'],
                     'att_and_behaviour' : student_a_and_b, 
                     'student_hov' : 'active'
                    },
                    RequestContext(request)
                )
            else:
                request.session['msg'] = 'Sorry something went wrong, you have entered an invalid password.'
        else:
            request.session['msg'] = 'Sorry something went wrong, please type again your username and password correctly.'
            
    return HttpResponseRedirect('/student/login/')
    
def login_view(request):
    login_form = Login_Form()
    msg = request.session.get('msg')
    
    return render_to_response(
        'student/login.html',
        {
         'system_name' : 'Student Login - ' +SYSTEM_NAME,
         'login_form'  : login_form,
         'msg'         : msg,
         'student_hov' : 'active'
        },
        RequestContext(request)
    )
    
def logout_view(request):
    if request.session.get('current_user') is not None:
        del request.session['current_user']    
        del request.session['user_in_session']
        
    return HttpResponseRedirect('/student/')