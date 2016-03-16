from django.shortcuts import render_to_response, RequestContext
from django.http import  HttpResponseRedirect, HttpResponse
from .forms import Login_Form
from student.models import *
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
    
    if StudentSection.objects.filter(student = student_id, school_year='2015-2016').exists():
        section = StudentSection.objects.get(student = student_id, school_year='2015-2016')
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
    

def school_year_funtion():
    month_s = datetime.datetime.now().month
    if month_s > 3:
        today_year =  datetime.datetime.now().year
    else:
        today_year =  datetime.datetime.now().year
        today_year = today_year - 1
    start_year = today_year
    end_year =   today_year + 1
    return str(start_year)+'-'+str(end_year)
   
def getStudentBehaviour(student_id,school_year):
    return StudentBehavior.objects.filter(student = student_id, school_year=school_year)
    
def getStudentGrades(student_id,school_year):
    return StudentGrades.objects.filter(student = student_id, school_year=school_year)

def getStudentFinancial(student_id,school_year):
    print student_id,school_year
    return StudentFinancial.objects.filter(student = student_id, school_year=school_year)

def index_view(request):
    school_year = school_year_funtion()
    if request.session.get('msg'):
        del request.session['msg']
    user_in_session = request.session.get('user_in_session')
    if user_in_session:
        student        = Student.objects.get(studentid = user_in_session['username'])
        student_bills  = getStudentFinancial(student.studentid, school_year)
        student_grades = getStudentGrades(student.studentid, school_year)
        student_behavior = getStudentBehaviour(student.studentid, school_year)
        
        return render_to_response(
            'student/base.html',
            {
                'system_name'    : student.firstname+ ' ' +student.middlename+ ' ' +student.lastname+ ' - ' +SYSTEM_NAME,
                 'student'        : student,
                 'student_bills'  : student_bills,
                 'student_grades' : student_grades,
                 'student_behavior': student_behavior,
                 'student_hov' : 'active',
                 'total': sum([x.amount for x in student_bills]),
                 'bills':True
            },
            RequestContext(request)
        )

    if request.method == 'POST':
        login_form = Login_Form(request.POST)
        
        if login_form.is_valid():
            username = str(login_form.cleaned_data['username']) 
            password = login_form.cleaned_data['password']
            
                    
            if Student.objects.filter(studentid=username).exists():
                student = Student.objects.get(studentid=username)
                
                if login_form.cleaned_data['password'] == student.password:
                    request.session['current_user'] = str(student.studentid)
                    request.session['user_in_session'] = {
                        'username' : username,
                        'password' : password,
                    }
                    
                    student_bills  = getStudentFinancial(student.studentid, school_year)
                    student_grades = getStudentGrades(student.studentid, school_year)
                    student_behavior = getStudentBehaviour(student.studentid, school_year)
            
                    return render_to_response(
                        'student/base.html',
                        {
                         'system_name'    : student.firstname+ ' ' +student.middlename+ ' ' +student.lastname+ ' - ' +SYSTEM_NAME,
                         'student'        : student,
                         'student_bills'  : student_bills,
                         'student_grades' : student_grades,
                         'student_behavior': student_behavior,
                         'student_hov' : 'active',
                         'total': sum([x.amount for x in student_bills]),
                         'bills':True

                        },
                        RequestContext(request)
                    )
                else:
                    request.session['msg'] = 'Sorry something went wrong, you have entered an invalid password.'
            else:
                request.session['msg'] = 'Sorry something went wrong, you have entered an invalid username.'
    
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