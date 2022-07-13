from django.shortcuts import render,redirect
from members.models import CustomMember,Manager
from texting.models import Text
from members.forms import MemberUpdateForm
from django.contrib import messages
from django.http import HttpResponseRedirect,HttpResponse
from .models import SchoolClass,Student,Event
from .forms import SchoolClassCreate,SchoolClassUpdate,AddStudentAdminForm,AddStudentForm,StudentUpdateAdminForm,StudentUpdateForm,EventAdminForm,EventForm
from django.contrib.auth.decorators import login_required



#Home Page
def home(request):
	event_list = Event.objects.all().order_by('event_date')
	return render(request,'main/home.html',{'event_list':event_list})

def classes(request):
	return render(request,'main/classes.html',{})

#Adding Classroom
def add_class(request):
	submitted = False
	form = SchoolClassCreate()
	if request.method == "POST":
		form = SchoolClassCreate(request.POST or None)
		if form.is_valid():
			messages.success(request,'Classroom is Created')
			form.save()
			return HttpResponseRedirect('/add_class?submitted=True')
	else:
		form = SchoolClassCreate()
	if 'submitted' in request.GET:
		submitted = True
	return render(request,'main/add_class.html',{'form':form,'submitted':submitted})	

#Total Classroom View
@login_required
def classrooms(request):
	classroom_list = SchoolClass.objects.all().order_by('classroom')
	return render(request,'main/classrooms.html',{'classroom_list':classroom_list})

#Individual Classroom View
def view_class(request,classroom_id):
	context={}
	classroom = SchoolClass.objects.get(id=classroom_id)
	context['classroom'] = classroom
	return render(request,'main/view_class.html',context)

#Update Classroom
@login_required
def update_class(request,classroom_id):
	context={}
	if request.user.is_manager:
		classroom = SchoolClass.objects.get(id=classroom_id)
		context['classroom'] = classroom
		form = SchoolClassUpdate(request.POST or None,instance = classroom)
		context['form'] = form
		if request.method == "POST":
			if form.is_valid():
				messages.success(request,'The Class is Updated')
				form.save()
				return redirect('view-class',classroom.id)
			else:
				messages.success(request,'You can not add assigned teacher or students to this class.')
		else:
			return render(request,'main/update_class.html',context)
		return render(request,'main/update_class.html',context)
	else:
		messages.success(request,"You are not Authorized to View This Page")
		return redirect('home')

#Delete Classroom
@login_required
def delete_class(request,classroom_id):
	context={}
	classroom = SchoolClass.objects.get(id=classroom_id)
	context['classroom'] = classroom
	if request.user.is_manager:
		classroom.delete()
		messages.success(request,'The Classroom is Deleted Successfully')
		return redirect('home')
	else:
		messages.success(request,"You are not Authorized to Delete")
		return redirect('home')

#Parent Dashboard Page
@login_required
def dashboard(request,user_id):
	context={}
	member = CustomMember.objects.get(pk=user_id)
	unread = Text.objects.filter(receiver=request.user).filter(read=False)
	try:
	 	students = Student.objects.filter(parent_id = user_id)
	 	context={'member':member,'students':students,'unread':unread}
	except Student.DoesNotExist:
		students = None
		context={'member':member,'students':students,'unread':unread}
		
	return render(request,'main/dashboard.html',context)


#Teacher Dashboard Page
@login_required
def teacher_dashboard(request,user_id):
	context={}
	if request.user.is_teacher:
		unread = Text.objects.filter(receiver=request.user).filter(read=False)
		context['unread'] = unread
		try:
			classroom = SchoolClass.objects.get(attending_teacher = request.user)
			context['classroom'] = classroom
			return render(request,'main/teacher_dashboard.html',context)
		except:
			classroom = None
			return render(request,'main/teacher_dashboard.html',context)
	else:
		messages.success(request,'You are not Authorized to View This Page')
		return redirect('home')
	return render(request,'main/teacher_dashboard.html',context)

#Teacher Detail View
@login_required
def teacher_details(request,teacher_id):
	teacher = CustomMember.objects.get(id = teacher_id)
	return render(request,'main/teacher_details.html',{'teacher':teacher})

#Manager Dashboard Page
@login_required
def manager_dashboard(request,user_id):
	context={}

	if request.user.is_manager:
		classrooms = SchoolClass.objects.all()
		unread = Text.objects.filter(receiver=request.user).filter(read=False)
		context = {'classrooms':classrooms,'unread':unread}
		return render(request,'main/manager_dashboard.html',context)
	else:
		messages.success(request,'You Are Not Authorized To Access This Page')
		return redirect('home')
	return render(request,'main/manager_dashboard.html',context)

#Assign Teacher Accounts
@login_required
def teacher_accounts(request):
	account_list = CustomMember.objects.all().order_by('first_name')
	if request.user.is_manager:
		if request.method == "POST":
			teacher_list = request.POST.getlist('boxes')
			account_list.update(is_teacher=False)
			for x in teacher_list:
				CustomMember.objects.filter(pk=int(x)).update(is_teacher=True)
			messages.success(request,'Selected Members are Given Teacher Privaligies.')
			return redirect('home')
		else:
			return render(request,'main/teacher_accounts.html',{'account_list':account_list})
	else:
		messages.success(request,'You are not Authorized to View This Page.')
		return redirect('home')
	return render(request,'main/teacher_accounts.html',{'account_list':account_list})

#Parent Details View
@login_required
def parent_details(request,parent_id):
	if request.user.is_manager or request.user.is_teacher:
		parent = CustomMember.objects.get(id=parent_id)
		return render(request,'main/parent_details.html',{'parent':parent})
	else:
		messages.success(request,'You are not Authorized to View This Page')
		return redirect('home')

#Parent Update
@login_required
def update_member(request):
	context = {}
	if request.POST:
		form = MemberUpdateForm(request.POST or None,request.FILES or None,instance=request.user)
		if form.is_valid():
			form.initial={
			'email': request.POST['email'],
			'first_name' : request.POST['first_name'],
			'last_name' : request.POST['last_name'],
			'address' : request.POST['address'],
			'phone' : request.POST['phone'],
			'mobile_phone' : request.POST['mobile_phone'],
			}
			messages.success(request,'Your Info Has Been Updated!')
			form.save()
			return redirect('home')
	else:
		form= MemberUpdateForm(
			initial={
			'email': request.user.email,
			'first_name': request.user.first_name,
			'last_name': request.user.last_name,
			'address': request.user.address,
			'phone': request.user.phone,
			'mobile_phone': request.user.mobile_phone,
			}
			)
	
	context['update_form'] = form
	return render(request,'main/update.html',context)

#Adding Student/Child
@login_required
def add_student(request,user_id):
	context={}
	member = CustomMember.objects.get(pk=user_id)
	if request.POST:
		if request.user.is_teacher or request.user.is_manager:
			form = AddStudentAdminForm(request.POST or None,request.FILES or None)
			if form.is_valid():
				form.save()
				return redirect('home')
		else:
			form = AddStudentForm(request.POST or None,request.FILES or None)
			if form.is_valid():
				student = form.save(commit=False)
				student.parent = request.user
				student.save()

				messages.success(request,'Child Details are Saved Successfully')
				return redirect('home')
			else:
				context['addStudentForm'] = form
	else:
		if request.user.is_teacher or request.user.is_manager:
			form = AddStudentAdminForm()
			context['addStudentForm'] = form
		else:
			form = AddStudentForm()
			context['addStudentForm'] = form

	return render(request,'main/add_student.html',context)

#Updating Student/Child
@login_required
def update_student(request,student_id):
	student = Student.objects.get(pk=student_id)
	if request.user.is_teacher or request.user.is_manager:
		form = StudentUpdateAdminForm(request.POST or None,request.FILES or None,instance=student)
		if form.is_valid():
			form.save()
			messages.success(request,'Student Details Has Been Updated')
			return redirect('home')
		return render(request,'main/update_student.html',{'student':student,'form':form})
	else:
		form = StudentUpdateForm(request.POST or None,request.FILES or None,instance=student)
		if form.is_valid():
			student = form.save(commit=False)
			student.parent = request.user
			student.save()
			messages.success(request,'Child Details Has Been Updated')
			return redirect('home')
		return render(request,'main/update_student.html',{'student':student,'form':form})
	return render(request,'main/update_student.html',{'student':student,'form':form})

#Student Details View
def student_details(request,student_id):
	context={}
	student = Student.objects.get(id=student_id)
	context['student'] = student
	return render(request,'main/student_details.html',context)


#Delete Student
def delete_student(request,student_id):
	student = Student.objects.get(pk=student_id)
	if request.user == student.parent or request.user.is_teacher:
		student.delete()
		messages.success(request,'Child/Student Info is Deleted')
		return redirect('home')
	else:
		messages.success(request,'You are not Authorized to Delete!')
		return redirect('home')

#Create Event
@login_required
def create_event(request):
	submitted = False
	if request.method == "POST":
		if request.user.is_manager:
			form = EventAdminForm(request.POST)
			if form.is_valid():
				messages.success(request,'School Event is Created!')
				form.save()
				return HttpResponseRedirect('/create_event?subitted=True')
		elif request.user.is_teacher:
			form = EventForm(request.POST)
			if form.is_valid():
				event = form.save(commit=False)
				event.manager = request.user
				event.save()
				messages.success(request,'School Event is Created!')
				return HttpResponseRedirect('/create_event?subitted=True')
		else:
			messages.success(request,'You are not Authorized to View This Page')
			return redirect('home')
	else:
		if 'submitted' in request.GET:
			submitted=True

		if request.user.is_manager:
			form = EventAdminForm()
		elif request.user.is_teacher:
			form = EventForm()
		else:
			messages.success(request,'You are not Authorized to View This Page')
			return redirect('home')
	return render(request,'main/create_event.html',{'form':form,'submitted':submitted})

#All Events Page
@login_required
def all_events(request):
	event_list = Event.objects.all().order_by('event_date')
	return render(request,'main/event_list.html',{'event_list':event_list})

#Manager Event Appoval Page 
@login_required
def event_approval(request):
	event_list = Event.objects.all().order_by('event_date')
	if request.user.is_manager:
		if request.method == "POST":
			appoval_list = request.POST.getlist('boxes')
			event_list.update(approval=False)

			for x in appoval_list:
				Event.objects.filter(pk=int(x)).update(approval=True)

			messages.success(request,'Selected Events are Approved')
			return redirect('event-list')
		else:
			return render(request,'main/event_approval.html',{'event_list':event_list})
	else:
		messages.success(request,'You are not Authorized to View This Page')
		return redirect('home')
	return render(request,'main/event_approval.html')

#Update Event
@login_required
def update_event(request,event_id):
	event = Event.objects.get(pk=event_id)
	if request.user.is_manager:
		form = EventAdminForm(request.POST or None,instance=event)
	elif request.user.is_teacher:
		form = EventForm(request.POST or None,instance = event)
	else:
		messages.success(request,'You are not Authorized to View This Page')
		return redirect('home')

	if form.is_valid():
		form.save()
		messages.success(request,'The Event is Updated')
		return redirect('event-list')

	return render(request,'main/update_event.html',{'event':event,'form':form})

#Delete Event
@login_required
def delete_event(request,event_id):
	event = Event.objects.get(pk=event_id)
	if request.user.is_manager:
		event.delete()
		messages.success(request,'The Event is Deleted Successfully.')
		return redirect('event-list')
	else:
		messages.success(request,'You Are Not Authorized To Take This Action.')
		return redirect('event-list')
		