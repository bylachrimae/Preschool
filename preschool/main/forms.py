from django import forms
from .models import Student,SchoolClass,Event
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class SchoolClassCreate(forms.ModelForm):
	class Meta:
		model = SchoolClass
		fields=('classroom','attending_teacher','attendingstudent')
		labels = {
		'classroom':'Classroom',
		'attending_teacher':'Teacher',
		'attendingstudent':'Students',
		}

		help_texts = {
		'attending_teacher' : _('Choose only 1 Teacher'),
		'attendingstudent': _('Choose maximum 10 Students'),
		}

		widgets={
		'classroom' : forms.Select(attrs={'class':'form-control','placeholder':'Classroom'}),
		'attending_teacher' : forms.Select(attrs={'class':'form-control','placeholder':'Teacher'}),
		'attendingstudent' : forms.SelectMultiple(attrs={'class':'form-control','size':'10','placeholder':'Students'}),
		}
	
class SchoolClassUpdate(forms.ModelForm):
	class Meta:
		model = SchoolClass
		fields = ('attending_teacher','attendingstudent')
		labels = {
		'attending_teacher':'Teacher',
		'attendingstudent':'Students',
		}

		help_texts = {
		'attending_teacher' : _('Choose only 1 Teacher'),
		'attendingstudent': _('Choose maximum 10 Students'),
		}

		widgets={
		'attending_teacher' : forms.Select(attrs={'class':'form-control','placeholder':'Teacher'}),
		'attendingstudent' : forms.SelectMultiple(attrs={'class':'form-control','size':'10','placeholder':'Students'}),
		}
	
class AddStudentAdminForm(forms.ModelForm):
	class Meta:
		model = Student 
		fields = ('first_name','last_name','age','blood_type','allergy','chronic_illness','student_pic','parent')
		labels = {
		'first_name':'First Name',
		'last_name': 'Last Name',
		'age': 'Age',
		'blood_type': 'Blood Type',
		'allergy': 'Allergies',
		'chronic_illness':'Chronic Illnesses',
		'student_pic':'',
		'parent':'Parent',
		}
	
		widgets={
		'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}),
		'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),
		'age':forms.TextInput(attrs={'class':'form-control','placeholder':'Age'}),
		'blood_type':forms.TextInput(attrs={'class':'form-control','placeholder':'Blood Type'}),
		'allergy':forms.Textarea(attrs={'class':'form-control','placeholder':'Allergies'}),
		'chronic_illness':forms.Textarea(attrs={'class':'form-control','placeholder':'Chronic Illnesses'}),
		'parent':forms.Select(attrs={'class':'form-control','placeholder':'Parent'})
		}

class AddStudentForm(forms.ModelForm):
	class Meta:
		model = Student 
		fields = ('first_name','last_name','age','blood_type','allergy','chronic_illness','student_pic')
		labels = {
		'first_name':'First Name',
		'last_name': 'Last Name',
		'age': 'Age',
		'blood_type': 'Blood Type',
		'allergy': 'Allergies',
		'chronic_illness':'Chronic Illnesses',
		'student_pic':'',
		}
	
		widgets={
		'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}),
		'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),
		'age':forms.TextInput(attrs={'class':'form-control','placeholder':'Age'}),
		'blood_type':forms.TextInput(attrs={'class':'form-control','placeholder':'Blood Type'}),
		'allergy':forms.Textarea(attrs={'class':'form-control','placeholder':'Allergies'}),
		'chronic_illness':forms.Textarea(attrs={'class':'form-control','placeholder':'Chronic Illnesses'})
		}

class StudentUpdateAdminForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = ('first_name','last_name','age','blood_type','allergy','chronic_illness','parent','student_pic')
		labels = {
		'first_name':'First Name',
		'last_name': 'Last Name',
		'age': 'Age',
		'blood_type': 'Blood Type',
		'allergy': 'Allergies',
		'chronic_illness':'Chronic Illnesses',
		'parent':'Parent',
		'student_pic':'',
		}
	
		widgets={
		'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}),
		'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),
		'age':forms.TextInput(attrs={'class':'form-control','placeholder':'Age'}),
		'blood_type':forms.TextInput(attrs={'class':'form-control','placeholder':'Blood Type'}),
		'chronic_illness':forms.Textarea(attrs={'class':'form-control','placeholder':'Chronic Illnesses'}),
		'allergy':forms.Textarea(attrs={'class':'form-control','placeholder':'Allergies'}),
		'parent':forms.Select(attrs={'class':'form-control','placeholder':'Parent'})
		}

class StudentUpdateForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = ('first_name','last_name','age','blood_type','allergy','chronic_illness','student_pic')
		labels = {
		'first_name':'First Name',
		'last_name': 'Last Name',
		'age': 'Age',
		'blood_type': 'Blood Type',
		'allergy': 'Allergies',
		'chronic_illness':'Chronic Illnesses',
		'student_pic':'',
		}
	
		widgets={
		'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}),
		'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),
		'age':forms.TextInput(attrs={'class':'form-control','placeholder':'Age'}),
		'blood_type':forms.TextInput(attrs={'class':'form-control','placeholder':'Blood Type'}),
		'allergy':forms.Textarea(attrs={'class':'form-control','placeholder':'Allergies'}),
		'chronic_illness':forms.Textarea(attrs={'class':'form-control','placeholder':'Chronic Illnesses'})
		}

class EventAdminForm(forms.ModelForm):
	class Meta:
		model = Event
		fields = ('name','event_date','venue','manager','web','descriptions','attendees')

		labels={
		'name':'Event Name',
		'event_date':'YYYY-MM-DD HH:MM:SS',
		'venue':'Venue',
		'manager':'Manager',
		'web':'Web',
		'descriptions':'Description',
		'attendees':'Attendees',
		}

		widgets = {
		'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Event Name'}),
		'event_date':forms.TextInput(attrs={'class':'form-control','placeholder':'Event Date'}),
		'venue':forms.TextInput(attrs={'class':'form-control','placeholder':'Venue'}),
		'manager':forms.Select(attrs={'class':'form-control','placeholder':'Manager'}),
		'web':forms.TextInput(attrs={'class':'form-control','placeholder':'Web Address'}),
		'descriptions':forms.Textarea(attrs={'class':'form-control','placeholder':'Description'}),
		'attendees':forms.SelectMultiple(attrs={'class':'form-control','size':'10','placeholder':'Attendees'}),
		}

class EventForm(forms.ModelForm):
	class Meta:
		model = Event
		fields = ('name','event_date','venue','web','descriptions','attendees')

		labels={
		'name':'Event Name',
		'event_date':'YYYY-MM-DD HH:MM:SS',
		'venue':'Venue',
		'web':'Web',
		'descriptions':'Description',
		'attendees':'Attendees',
		}

		widgets = {
		'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Event Name'}),
		'event_date':forms.TextInput(attrs={'class':'form-control','placeholder':'Event Date'}),
		'venue':forms.TextInput(attrs={'class':'form-control','placeholder':'Venue'}),
		'web':forms.TextInput(attrs={'class':'form-control','placeholder':'Web Address'}),
		'descriptions':forms.Textarea(attrs={'class':'form-control','placeholder':'Description'}),
		'attendees':forms.SelectMultiple(attrs={'class':'form-control','size':'10','placeholder':'Attendees'}),
		}

