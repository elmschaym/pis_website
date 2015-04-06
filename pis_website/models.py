from django.db import models
from django.contrib.auth.models import User

YEAR_LEVEL = ((1,'Nursery'),
              (2,'Kinder 1'),
              (3,'Kinder 2'),
              (4,'Grade 1'),
              (5,'Grade 2'),
              (6,'Grade 3'),
              (7,'Grade 4'),
              (8,'Grade 5'),
              (9,'Grade 6'),
              (10,'Grade 7'),
              (11,'Grade 8'),
              (12,'1st Year Junior'),
              (13,'2nd Year Junior'),
              (14,'1st Year Senior'),
              (15,'2nd Year Senior')
             )

GRADING_PERIODS = ((1, '1st Grading'),
                   (2, '2nd Grading'),
                   (3, '3rd Grading'),
                   (4, '4th Grading'),
                   (5, 'Final')
                  )

MONTHS = ((1, 'January'), 
          (2, 'February'), 
          (3, 'March'), 
          (4, 'April'),
          (5, 'May'), 
          (6, 'June'), 
          (7, 'July'),
          (8, 'August'), 
          (9, 'September'), 
          (10, 'October'),
          (11, 'November'), 
          (12, 'December'))



class Position(models.Model):
    POSITION_TYPE = (('E', 'Executive Committee'), ('F', 'Faculty'), ('U', 'Utility'))
    position_type = models.CharField(max_length=1, choices = POSITION_TYPE)
    name = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=9, decimal_places=2)
    
    def __unicode__(self):
        return self.name

    class Meta():
        db_table = 'position'


class Employee(models.Model):
    EMP_TYPES = (('F', 'Faculty'), ('S', 'Staff'), ('C', 'Coordinator'), ('U', 'Utility'))
    user = models.OneToOneField(User)
    employee_type = models.CharField(max_length = 1, choices = EMP_TYPES)
    designation = models.CharField(max_length=45)
    address = models.CharField(max_length=100, blank=True)
    image_path = models.FileField(upload_to='employees_image')
    #additioanl field for payroll
    position = models.ForeignKey(Position)
    basic_salary = models.DecimalField(max_digits = 9, decimal_places = 2)
    date_employed = models.DateField()
    pag_ibig = models.DecimalField(max_digits = 7, decimal_places = 2, default=0)
    phil_health = models.DecimalField(max_digits = 7, decimal_places = 2, default=0)
    honorarium = models.BooleanField(default=False)
    cum_laude = models.BooleanField(default=False)
    let_passer = models.BooleanField(default = False)
    masteral_holder = models.BooleanField(default = False)
    foreign_grad = models.BooleanField(default= False)
    prefect_disc = models.BooleanField(default= False)
    

    class Meta():
        db_table = 'employee'

    def __unicode__(self):
      return self.user.first_name + ' ' + self.user.last_name

#ok    
class StudentPrivilege(models.Model):
    priv_name = models.CharField(max_length=100)
    discount = models.FloatField(max_length=3)
    date_created = models.DateField(auto_now=True, auto_now_add=True)

    class Meta():
        db_table = 'student_privilege'
    def __unicode__(self):
     return self.priv_name

#ok
class Subject(models.Model):
     SUBJECT_TYPES = ((1, 'Major'), (2, 'MAPEH'), (3, 'Makabayan'), (4, 'Minor'))
     CURRICULUM = ((1, 'OLD'), (2, 'K12'), (3, 'OLD AND K12'))
     title = models.CharField(max_length=45)
     units = models.DecimalField(max_digits = 3, decimal_places = 2)
     year_level = models.IntegerField(choices=YEAR_LEVEL)
     subject_type = models.IntegerField(choices = SUBJECT_TYPES)
     lock = models.IntegerField(default=0)
     curriculum = models.IntegerField(choices = CURRICULUM)

     class Meta():
         db_table = 'subject'

     def __unicode__(self):
       return self.title



class SubjectAssignment(models.Model):
    subject = models.ForeignKey(Subject)
    year_level = models.IntegerField(choices = YEAR_LEVEL)
    
    class Meta():
        db_table = 'subject_assignment'

#ok
class Student(models.Model):
    ACAD_STATUS = (
        ('R', 'Regular'),
        ('I', 'Irregular'),
        ('T', 'Transferre'),
        ('G', 'Graduated'),
        ('D', 'Dropped'),
    )
    GENDERS = (('M', 'Male'),('F', 'Female'))
    studentid = models.CharField(max_length=9, primary_key=True)
    firstname = models.CharField(max_length=45)
    middlename = models.CharField(max_length=45)
    lastname = models.CharField(max_length=45)
    gender = models.CharField(max_length=1, choices=GENDERS)
    date_of_birth = models.DateField()
    date_admitted = models.DateField()
    address = models.CharField(max_length=100, blank=True)
    mother_name = models.CharField(max_length=45) 
    father_name = models.CharField(max_length=45)
    mother_occ = models.CharField(max_length=45, blank=True)  # mother occupation
    father_occ = models.CharField(max_length=45, blank=True)  # father occupation
    last_school_att = models.CharField(max_length=100, blank=True)
    last_school_att_address = models.CharField(max_length=100, blank=True)
    acad_status = models.CharField(max_length=45, choices=ACAD_STATUS)
    image_path = models.FileField(upload_to='students')
    privilege = models.ForeignKey(StudentPrivilege, blank=True, null=True)
    year_level = models.IntegerField(choices=YEAR_LEVEL)
    cell_no = models.CharField(max_length=11)
    subjects = models.ManyToManyField(Subject, through='StudentSubjects')

    class Meta():
        db_table = 'student'

    def __unicode__(self):
      return self.studentid

#edit
class StudentGradeInquiry(models.Model):
    studentid  = models.ForeignKey(Student)
    access_key = models.CharField(max_length=15)
    
    class Meta():
        db_table = 'student_grade_inquiry'

    def __unicode__(self):
      return self.studentid

class StudentTempGrade(models.Model):
    student = models.OneToOneField(Student)
    grade = models.DecimalField(max_digits = 5, decimal_places = 3)

    class Meta:
        db_table = 'student_temp_grade'

    def __unicode__(self):
      return self.grade

#ok
class BillItems(models.Model):
    ITEM_TYPES = (
        ('R', "Registration"),
        ('T', "Tuition"),
        ('M', "Miscellaneous"),
        ('K', "Kitab"),
        ('B', "Book"),
        ('A', "Marketable"),
        ('N', "Nonmarketable"),
        ('R', "Rentable"),
        ('O', "Others"),
        ('C',"Custom"),
        ('E',"Remittance"),
    )
 
    item_name = models.CharField(max_length=45)
    item_type = models.CharField(max_length=1, choices=ITEM_TYPES)
    amount  = models.DecimalField(max_digits=7, decimal_places=2)
    # date_created = models.DateField(auto_now=True, auto_now_add=True)
    class Meta():
       db_table = 'bill_items'
   
    def __unicode__(self):
      return self.item_name

class AssignBillItem(models.Model):
    ITEM_TYPES = (('R',"Registration"),('T',"Tuition"),('M',"Miscellaneous"),('K',"Kitab"), ('O',"Others"))
    bill_item_id = models.ForeignKey(BillItems)
    year_level = models.IntegerField(choices=YEAR_LEVEL)
    item_type = models.CharField(max_length=1, choices=ITEM_TYPES)

    class Meta():
        db_table = 'assign_bill_item'

    def __unicode__(self):
      return unicode(self.year_level)
#ok
class BillAccount(models.Model):
    student = models.ForeignKey(Student)
    bill_item_name = models.ForeignKey(BillItems)
    balance = models.DecimalField(max_digits=9, decimal_places=2)
    date_added = models.DateField(auto_now=True, auto_now_add = True)
    date_fully_paid = models.DateField(auto_now=True, auto_now_add = True)
    discount = models.FloatField(max_length=3, default=0)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    school_year = models.CharField(max_length=100)

    class Meta():
        db_table = 'bill_account'

    def __unicode__(self):
      return unicode(self.student)

class Transaction(models.Model):
    amount_due = models.DecimalField(max_digits=9,decimal_places=2)
    date_transacted = models.DateTimeField(auto_now_add=True)
    cashier = models.ForeignKey(Employee)
    student = models.CharField(max_length=45)
    or_number = models.IntegerField()

    class Meta():
        db_table = 'transaction'

    def __unicode__(self):
      return unicode(self.date_transacted)
      
class TransactionBreakdown(models.Model):
    transaction_id = models.ForeignKey(Transaction)
    bill_account_id = models.ForeignKey(BillAccount)

    class Meta():
        db_table = 'transaction_breakdown'


class Packages(models.Model):
    item_name = models.CharField(max_length=50)

    class Meta():
        db_table = 'packages'

    def __unicode__(self):
      return unicode(self.item_name)

class BillPackage(models.Model):
    bill_item = models.ForeignKey(BillItems)
    package_id = models.ForeignKey(Packages)
    date_added = models.DateField(auto_now=True, auto_now_add=True)

    class Meta():
        db_table = 'bill_packages'


    def __unicode__(self):
      return unicode(self.package_id)

class OneOffAccount(models.Model):
 
    payee = models.CharField(max_length=45)
    bill_item_name = models.ForeignKey(BillItems)
    paid = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    
    class Meta():
        db_table = 'one_off_account'

    def __unicode__(self):
      return self.payee
      
class OneOffTransaction(models.Model):
    transaction = models.ForeignKey(Transaction)
    acct = models.ForeignKey(OneOffAccount)    

    class Meta():
        db_table = 'one_off_transaction'

#ok
class Section(models.Model):
    name = models.CharField(max_length=45)
    year_level = models.IntegerField(choices=YEAR_LEVEL)
    room_no = models.IntegerField()
    students = models.ManyToManyField(Student, through='StudentSection')
    capacity = models.IntegerField()
    adviser = models.OneToOneField(Employee)
    max_grade = models.DecimalField(max_digits=4, decimal_places=2)

    class Meta():
        db_table = 'section'

    def __unicode__(self):
      return self.name

#StudentSection
class StudentSection(models.Model):
    student = models.ForeignKey(Student)
    section = models.ForeignKey(Section)
    school_year = models.CharField(max_length=20)

    class Meta():
        db_table = 'student_section'

    def __unicode__(self):
      return unicode(self.student)

#ok
class StudentSubjects(models.Model):
    subject = models.ForeignKey(Subject)
    student = models.ForeignKey(Student)
#    school_year = models.CharField(max_length=20)
    q1 = models.DecimalField(max_digits = 5, decimal_places=3, default=0)
    q2 = models.DecimalField(max_digits = 5, decimal_places=3, default=0)
    q3 = models.DecimalField(max_digits = 5, decimal_places=3, default=0)
    q4 = models.DecimalField(max_digits = 5, decimal_places=3, default=0)
    final = models.DecimalField(max_digits = 5, decimal_places=3, default=0)
#    remarks = models.CharField(max_length=10)

    class Meta():
        db_table = 'student_subjects'


    def __unicode__(self):
      return self.student



class AverageGrade(models.Model):
    student = models.ForeignKey(Student)
    year_level = models.IntegerField()
    average = models.DecimalField(max_digits = 5, decimal_places = 3)
    
    class Meta():
        db_table = 'average_grade'

    def __unicode__(self):
        return self.average


class SubjectTeacher(models.Model):
    subject = models.ForeignKey(Subject)
    teacher = models.ForeignKey(Employee)
    section = models.ForeignKey(Section)
    school_year = models.CharField(max_length = 45)

    class Meta():
        db_table = 'subject_teacher'


class ClassSchedule(models.Model):   
    DAYS = (('M','Monday'), ('T','Tuesday'), ('W','Wednesday'), ('Th','Thursday'), ('F','Friday'), ('Sat','Saturday'), ('Sun','Sunday'))
    subject_teacher = models.OneToOneField(SubjectTeacher)
    time_start = models.TimeField(blank=True)
    time_end = models.TimeField(blank=True)
    day = models.CharField(max_length = 3, choices = DAYS)

    class Meta():
        db_table = 'class_schedule'


#ok
class CharacterRate(models.Model):
   
    character_choices = (('C','Cleanliness'),
                         ('CP','Courtesy and Politeness'),
                         ('HC','Helpfulness and Cooperativeness'),
                         ('I','Industriousness'),
                         ('LI','Leadership and Innitiative'),
                         ('O','Obedience'),
                         ('SC','Self Control'),
                         ('PP','Promptness and Punctuality'),
                         ('S','Sportmanship'),
                         ('TE','Thrift and Economy'),
                         ('MS','Modesty and Simplicity')
                        )

    student = models.ForeignKey(Student)
    rate = models.FloatField(max_length=3)
    character = models.CharField(max_length=2,choices=character_choices)
    year_level = models.IntegerField(choices=YEAR_LEVEL)
    school_year = models.CharField(max_length=25)
    period = models.IntegerField()
    date_rated = models.DateTimeField(auto_now=True, auto_now_add=True)

    class Meta():
        db_table = 'character_rate'


    def __unicode__(self):
      return self.student
#ok
class Attendance(models.Model):
    MONTHS = ((1, 'January'),
              (2, 'February'),
              (3, 'March'),
              (4, 'April'),
              (5, 'May'),
              (6, 'June'),
              (7, 'July'),
              (8, 'August'),
              (9, 'September'),
              (10, 'October'),
              (11, 'November'),
              (12, 'December')
             )
    student = models.ForeignKey(Student)
    year_level = models.IntegerField()
    school_year = models.CharField(max_length=20)
    no_school_days = models.IntegerField()
    no_school_days_tardy = models.IntegerField()
    no_school_days_present = models.IntegerField()
    month = models.IntegerField(choices=MONTHS)

    class Meta():
        db_table = 'attendance'

    def __unicode__(self):
      return self.student

class ExpensesType(models.Model):
    account_type = (
                    ('PE', 'Personnel Expenses'),
                    ('SA', 'School Activities'),
                    ('AE', 'Administrative Exepenses'),
                    ('GA', 'Grants, Allowances and Subsidy'),
                    ('OC', 'Other Costs')
      )
    account_title = models.CharField(max_length = 120)
    account_type = models.CharField(max_length=2,choices=account_type)

    class Meta():
      db_table = 'exepenses_type'

    def __unicode__(self):
      return self.account_title

class Vouchers(models.Model):
    DEPARTMENT = (
                ('IT', 'Information Technology'),
                ('R',  'Registrar'),
                ('F', 'Finance'),
                ('P', 'Personnel'),
                ('O', 'Other/Miscellaneous'),
                ('BT', 'Board of Trustees'),
                ('EC', 'Executive Committee'),
                ('U', 'Utility'),
                ('L', 'Library'),
                ('C', 'Clinic'),
                ('E', 'Elementary'),
                ('HS', 'High School'),
                ('PS', 'Pre-School'),
                ('A', 'Arabic'),


      )
    
    voucher_id = models.CharField(max_length=12, primary_key=True)
    name_of_claimant = models.CharField(max_length = 200)
    purpose_expenditures = models.CharField(max_length = 220)
    amount = models.DecimalField(max_digits=11, decimal_places=2)
    change = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    date_created = models.DateField(auto_now=True, auto_now_add=True)
    department = models.CharField(max_length=2,choices=DEPARTMENT)
    expense_type = models.ForeignKey(ExpensesType)
    spent = models.DecimalField(max_digits=11,decimal_places=2)
    finance = models.ForeignKey(Employee)
    
    class Meta():
      db_table = 'vouchers'

    def __unicode__(self):
      return self.expense_type

class VoucherReceipt(models.Model):

    date = models.DateField()
    invoice_number = models.CharField(max_length = 60)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    transaction_description = models.CharField(max_length = 300)
    quantity = models.IntegerField()
    voucher = models.ForeignKey(Vouchers)

    class Meta():
      db_table = 'voucher_receipt'

    def __unicode__(self):
      return self.expense_type



'''
payroll models
'''

class IncreaseRates(models.Model):
    annual_increase = models.DecimalField(max_digits=9, decimal_places=2)
    forty_min_sub = models.DecimalField(max_digits=9, decimal_places=2)
    hourly_sub = models.DecimalField(max_digits=9, decimal_places=2)
    let_passer = models.DecimalField(max_digits=9, decimal_places=2)
    masters = models.DecimalField(max_digits=7, decimal_places=2)
    honorarium = models.DecimalField(max_digits=7, decimal_places=2)
    perfect_att_rate = models.DecimalField(max_digits=7, decimal_places=2)
    prefect_disc_rate = models.DecimalField(max_digits=7, decimal_places=2)
    foreign_grad = models.DecimalField(max_digits=7, decimal_places=2)
    cum_laude_rate = models.DecimalField(max_digits=7, decimal_places=2)
    overload_unit_rate = models.DecimalField(max_digits = 7, decimal_places = 2)
    subj_coord = models.DecimalField(max_digits = 7, decimal_places = 2)

    def __unicode__(self):
        return self.pk

    class Meta():
        db_table = 'increase_rates'


class Deductions(models.Model):
    pag_ibig = models.DecimalField(max_digits = 9, decimal_places=2)
    phil_health = models.DecimalField(max_digits = 9, decimal_places=2)

    def __unicode__(self):
        return self.pk

    class Meta():
        db_table = 'deductions'


class Overtime(models.Model):
    employee = models.ForeignKey(User)
    n_hours  = models.DecimalField(max_digits=4,decimal_places=2)
    pay_month= models.IntegerField(choices = MONTHS)
    pay_year = models.IntegerField()

    def __unicode__(self):
        return self.n_hours

    class Meta():
        db_table = 'overtime'


class Subteaching(models.Model):
    employee = models.ForeignKey(User)
    n_hours = models.IntegerField()
    n_40mins = models.IntegerField()
    pay_month = models.IntegerField(choices = MONTHS)
    pay_year = models.IntegerField()

    def __unicode__(self):
        return self.pk

    class Meta():
        db_table = 'subteaching'


class Lates(models.Model):
    employee = models.ForeignKey(User)
    n_mins = models.IntegerField()
    pay_month = models.IntegerField(choices = MONTHS)
    pay_year  = models.IntegerField()

    def __unicode__(self):
        return self.n_mins
        
    class Meta:
        db_table = 'lates'


class Absences(models.Model):
    employee   = models.ForeignKey(User)
    n_absences = models.IntegerField()
    pay_month  = models.IntegerField(choices = MONTHS)
    pay_year   = models.IntegerField()

    def __unicode__():
        return self.n_absences

    class Meta:
        db_table = 'absences'


class Donations(models.Model):
    employee = models.ForeignKey(User)
    amount   = models.DecimalField(max_digits = 9, decimal_places = 2)
    pay_month = models.IntegerField(choices = MONTHS)
    pay_year = models.IntegerField()

    def __unicode__(self):
        return self.amount

    class Meta:
        db_table = 'donations'


class CashAdvance(models.Model):
    employee = models.ForeignKey(User)
    date_released = models.DateTimeField(auto_now_add = True)
    amount = models.DecimalField(max_digits = 9, decimal_places = 2)
    pay_month = models.IntegerField(choices = MONTHS)
    pay_year = models.IntegerField()

    def __unicode__(self):
        return self.amount
        
    class Meta:
        db_table = 'cash_advance'


class Fines(models.Model):
    employee = models.ForeignKey(User)
    description = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    pay_month = models.IntegerField(choices = MONTHS)
    pay_year = models.IntegerField()
      
    def __unicode__(self):
        return self.amount

    class Meta:
        db_table = 'fines'

class PerfectAttendance(models.Model):
    employee = models.ForeignKey(User)
    year = models.IntegerField()

    def __unicode__(self):
        return self.year

    class Meta:
        db_table = "perfect_attendance"


class Overload(models.Model):
    employee = models.ForeignKey(User)
    n_units = models.DecimalField(max_digits = 5, decimal_places=2)
    year = models.IntegerField()

    def __unicode__(self):
        return self.n_units

    class Meta:
        db_table = 'overload'


class Coordinator(models.Model):
    employee = models.ForeignKey(User)
    n_coords = models.IntegerField()
    sy_year  = models.IntegerField()

    def __unicode__(self):
        return self.n_coords

    class Meta:
        db_table = 'coordinator'
    
class CustomSalaryIncrease(models.Model):
    employee = models.ForeignKey(User)
    description = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits = 7, decimal_places=2)
    
    def __unicode__(self):
        return self.amount

    class Meta:
        db_table = 'custom_salary_increase'

def user_unicode(self):
    return "%s %s" %(self.last_name, self.first_name)


User.__unicode__ = user_unicode


class ApprovedPayroll(models.Model):
    pay_year = models.IntegerField()
    pay_month = models.IntegerField()
    date_approved = models.DateTimeField(auto_now_add=True)


    def __unicode__(self):
        return "%s-%s" %(self.pay_year, self.pay_month)

    class Meta:
        db_table = 'approved_payroll'


class PayrollHistory(models.Model):
    employee = models.ForeignKey(Employee)
    basic_salary = models.DecimalField(max_digits=9, decimal_places=2)
    sub = models.DecimalField(max_digits=9, decimal_places=2)
    overtime = models.DecimalField(max_digits=9, decimal_places=2)
    cum_let_ma = models.DecimalField(max_digits=9, decimal_places=2)
    overload = models.DecimalField(max_digits=9, decimal_places=2)
    gross_pay = models.DecimalField(max_digits=9, decimal_places=2)
    philhealth = models.DecimalField(max_digits=9, decimal_places=2)
    pag_ibig = models.DecimalField(max_digits=9, decimal_places=2)
    donation = models.DecimalField(max_digits=9, decimal_places=2)
    penalties = models.DecimalField(max_digits=9, decimal_places=2)
    cash_advance = models.DecimalField(max_digits=9, decimal_places=2)
    total_deduction = models.DecimalField(max_digits=9, decimal_places=2)
    net_salary = models.DecimalField(max_digits=9, decimal_places=2)
    pay_year = models.IntegerField()
    pay_month = models.IntegerField()

    def __unicode__(self):
        return self.net_salary

    class Meta:
        db_table = 'payroll_history'

class InventoryItem(models.Model):
    item_id       = models.AutoField(primary_key = True)
    bill_item     = models.ForeignKey(BillItems)
    item_type     = models.CharField(max_length = 50)
    quantity      = models.IntegerField()
    is_disposable = models.BooleanField(default = False)
    
    class Meta():
        db_table = 'inventory_item'

    def __unicode__(self):
      return unicode(self.item_id)

class InventoryLeaseItem(models.Model):
    lease_item_id  = models.AutoField(primary_key = True) 
    inventory_item = models.ForeignKey(InventoryItem)
    date           = models.DateTimeField(auto_now = True, auto_now_add = True)
    student        = models.ForeignKey(Student)
    is_returned    = models.BooleanField(default = False)

    class Meta():
        db_table = 'inventory_lease_item'

        def __unicode__(self):
            return self.lease_item_id
        
class InventoryPurchaseReport(models.Model):
    purchase_report_id = models.AutoField(primary_key = True)
    item               = models.ForeignKey(InventoryItem)
    quantity           = models.IntegerField()
    date_purchased     = models.DateTimeField(auto_now = True, auto_now_add = True)
    price_per_unit     = models.IntegerField()
    total              = models.IntegerField()

    class Meta():
        db_table = 'inventory_purchase_report'
 
    def __unicode__(self):
      return self.purchase_report_id

 
class InventoryLeaseReport(models.Model):
    lease_report_id = models.AutoField(primary_key = True)
    student         = models.ForeignKey(Student)
    item            = models.ForeignKey(InventoryItem)
    date            = models.DateTimeField(auto_now = True, auto_now_add = True)
    remark          = models.CharField(max_length = 100)
    
    class Meta():
        db_table = 'inventory_lease_report'
 
    def __unicode__(self):
      return self.lease_report_id

class InventoryReleaseReport(models.Model):
    release_report_id = models.AutoField(primary_key = True)
    item              = models.ForeignKey(InventoryItem)
    quantity          = models.IntegerField()
    date              = models.DateTimeField(auto_now = True, auto_now_add = True)
    remark            = models.CharField(max_length = 100)
    
    class Meta():
        db_table = 'inventory_release_report'
 
    def __unicode__(self):
      return self.release_report_id

''' WEBSITE MODEL '''

class Events(models.Model):
    news_event = (
                  ('N', 'News'),
                  ('E', 'Events')
                )

    subject = models.CharField(max_length = 850)
    description = models.TextField()
    category = models.CharField(max_length=2,choices=news_event)
    date_created = models.DateField(auto_now=True, auto_now_add = True)
    date_start = models.DateField()
    date_end = models.DateField()

    class Meta():
        db_table = 'events'
 
    def __unicode__(self):
      return self.subject

class EventImages(models.Model):
    event = models.ForeignKey(Events)
    image_path = models.FileField(upload_to='event_image')


    class Meta():
        db_table = 'events_images'
 
    def __unicode__(self):
      return self.event
  
class AttendanceAndBehaviour(models.Model):
    date       = models.DateField()
    time_start = models.TimeField()
    time_end   = models.TimeField()
    remarks    = models.CharField(max_length = 500)
    student    = models.ForeignKey(Student) 
    
    class Meta():
        db_table = 'attendance_and_behaviour'
 
    def __unicode__(self):
        return unicode(self.id)