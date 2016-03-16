from django.db import models

'''STUDENT MODEL'''
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
    privilege = models.CharField(max_length=100, blank=True, null=True)
    year_level = models.IntegerField(choices=YEAR_LEVEL)
    cell_no = models.CharField(max_length=11)
    Section = models.CharField(max_length=50, blank=True)
    password = models.CharField(max_length=50)

    class Meta():
        db_table = 'student'

    def __unicode__(self):
      return self.studentid

#edit

class StudentGrades(models.Model):
	student = models.ForeignKey(Student)
	subject = models.CharField(max_length=100)
	q1 = models.DecimalField(max_digits = 5, decimal_places=3, default=0)
	q2 = models.DecimalField(max_digits = 5, decimal_places=3, default=0)
	q3 = models.DecimalField(max_digits = 5, decimal_places=3, default=0)
	q4 = models.DecimalField(max_digits = 5, decimal_places=3, default=0)
	final = models.DecimalField(max_digits = 5, decimal_places=3, default=0)
	school_year = models.CharField(max_length=20)


	class Meta():
		db_table = 'student_grades'

	def __unicode__(self):
		return self.student

class StudentBehavior(models.Model):
	student = models.ForeignKey(Student)
	date = models.DateField()
	remarks = models.CharField(max_length=540)
	school_year = models.CharField(max_length=20)


	class Meta():
		db_table = 'student_behavior'

	def __unicode__(self):
		return self.student

class StudentFinancial(models.Model):
	student = models.ForeignKey(Student)
	bill_item = models.CharField(max_length=120)
	amount = models.DecimalField(max_digits=7, decimal_places=2)
	school_year = models.CharField(max_length=20)	

	class Meta():
		db_table = 'student_financial'

	def __unicode__(self):
		return self.student