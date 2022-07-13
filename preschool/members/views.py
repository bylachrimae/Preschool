from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from .forms import SignupForm,MemberAuthenticationForm,MemberUpdateForm
from django.contrib import messages


def signup(request):
	context = {}
	if request.POST:
		form = SignupForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email')
			first_name = form.cleaned_data.get('first_name')
			last_name = form.cleaned_data.get('last_name')
			raw_password = form.cleaned_data.get('password1')
			member = authenticate(email=email,first_name=first_name,last_name=last_name,password=raw_password)
			login(request,member)
			messages.success(request,'You Have Been Registered Successfully')
			return redirect('home')
		else:
			context['signup_form'] = form
	else:
		form = SignupForm()
		context['signup_form'] = form
	return render(request,'authenticate/signup.html',context)

def member_login(request):
	context = {}

	member = request.user

	if member.is_authenticated:
		messages.success(request,'You Have Been Logged In Successfully')
		return redirect('home')

	if request.POST:
		form = MemberAuthenticationForm(request.POST)
		if form.is_valid():
			email = request.POST['email']
			password = request.POST['password']

			member = authenticate(email=email,password=password)

			if member:
				login(request,member)
				messages.success(request,'You Have Been Logged In Successfully')
				return redirect('home')
	else:
		form = MemberAuthenticationForm()

	context['login_form'] = form
	return render(request,'authenticate/member_login.html',context)

def member_logout(request):
	messages.success(request,'You Have Been Logged Out Successfully')
	logout(request)
	return redirect('home')