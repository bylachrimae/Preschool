from django.db import models
from members.models import CustomMember,Manager
from datetime import date

class Student(models.Model):
	id = models.AutoField('id',primary_key=True)
	first_name = models.CharField('First Name',max_length=60)
	last_name = models.CharField('Last Name',max_length=60)
	age = models.CharField('Age',max_length=2)
	blood_type = models.CharField('Blood Type',max_length=2)
	allergy = models.TextField('Allergies',max_length=200)
	chronic_illness = models.TextField('Chronic Illnesses',max_length=200)
	student_pic = models.ImageField(verbose_name='Student Picture',default='images/default_pic.jpg',upload_to='images/') 
	parent = models.ForeignKey(CustomMember,blank=True,null=True,on_delete=models.SET_NULL,related_name='parent',verbose_name='parent')

	def __str__(self):
		return self.first_name + " " + self.last_name + " " + self.parent.first_name + " " + self.parent.last_name

class SchoolClass(models.Model):
	CLASS_CHOISE=(
		('A','CLASS-A'),
		('B','CLASS-B'),
		('C','CLASS-C'),
		('D','CLASS-D'),
		('E','CLASS-E'),
		('F','CLASS-F'),
		('G','CLASS-G'),
		('H','CLASS-H'),
		('I','CLASS-I'),
		('J','CLASS-J'),
		)
	id = models.AutoField('id',primary_key=True)

	classroom = models.CharField('Classroom',unique=True,max_length=1,choices=CLASS_CHOISE)
	attending_teacher = models.OneToOneField(CustomMember,on_delete=models.CASCADE,null=True)
	attendingstudent = models.ManyToManyField(Student,related_name='schoolclass')

	def get_attendingstudents(self):
		return ",".join([str(p) for p in self.attendingstudent.all()])

	def __unicode__(self):
		return "{0}.format(self.classroom)"

	def __str__(self):
		teacher = CustomMember.objects.get(id = self.attending_teacher_id)
		return '%s : %s' % (self.classroom,teacher.id)

class Event(models.Model):
	name = models.CharField('Event Name',max_length=120)
	event_date = models.DateTimeField('Event Date')
	venue = models.CharField('Venue',max_length=120)
	manager = models.ForeignKey(CustomMember,blank=True,null=True,on_delete=models.SET_NULL)
	web = models.URLField('Web Address',blank=True)
	descriptions = models.TextField(blank=True)
	attendees = models.ManyToManyField(Student,blank=True)
	approval = models.BooleanField("Approval",default=False)

	def __str__(self):
		return self.name

	@property
	def Days_till(self):
		today = date.today()
		days_till = self.event_date.date() - today
		days_till_stripped = str(days_till).split(',',1) [0]
		return days_till_stripped

