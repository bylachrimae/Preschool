from django.contrib import admin
from members.models import CustomMember
from .models import Student,SchoolClass
from django.contrib.auth.models import Group

#admin.site.register(Student)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
	list_display=('first_name','last_name','parent')
	ordering=('first_name',)
	search_fields=('last_name','parent')

@admin.register(SchoolClass)
class SchoolClassAdmin(admin.ModelAdmin):
	list_display=('classroom','attending_teacher','get_attendingstudents')
	ordering=('classroom',)
	search_fields=('classroom',)