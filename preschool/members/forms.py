from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import CustomMember

class SignupForm(UserCreationForm):
	email = forms.EmailField(max_length=60,help_text='Required.Add a valid email adress')
	fist_name = forms.CharField(max_length=50,help_text='Required.Enter your first name')
	last_name = forms.CharField(max_length=50,help_text='Required.Enter your last name')

	class Meta:
		model = CustomMember
		fields = ('email','first_name','last_name','password1','password2')
		labels = {
		'email': 'Email',
		'first_name':'First Name',
		'last_name': 'Last Name'
		}

	def __init__(self,*args,**kwargs):
		super(SignupForm,self).__init__(*args,**kwargs)
		self.fields['email'].widget.attrs['class'] = 'form-control'
		self.fields['first_name'].widget.attrs['class'] = 'form-control'
		self.fields['last_name'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['class'] = 'form-control'


class MemberAuthenticationForm(forms.ModelForm):
	password = forms.CharField(label='Password',widget=forms.PasswordInput)

	class Meta:
		model = CustomMember
		fields = ('email','password')

	def clean(self):
		email = self.cleaned_data['email']
		password = self.cleaned_data['password']

		if not authenticate(email=email,password=password):
			raise forms.ValidationError('Invalid Login')
	def __init__(self,*args,**kwargs):
		super(MemberAuthenticationForm,self).__init__(*args,**kwargs)
		self.fields['email'].widget.attrs['class'] = 'form-control'
		self.fields['password'].widget.attrs['class'] = 'form-control'


class MemberUpdateForm(forms.ModelForm):
	class Meta:
		model = CustomMember
		fields = ('email','first_name','last_name','address','member_pic','phone','mobile_phone')
		labels = {
		'email': 'Email',
		'first_name':'First Name',
		'last_name': 'Last Name',
		'address': 'Address',
		'member_pic': 'Picture',
		'phone': 'Phone Number',
		'mobile_phone': 'Mobile Phone Number',
		}

	def __init__(self,*args,**kwargs):
		super(MemberUpdateForm,self).__init__(*args,**kwargs)
		self.fields['email'].widget.attrs['class'] = 'form-control'
		self.fields['first_name'].widget.attrs['class'] = 'form-control'
		self.fields['last_name'].widget.attrs['class'] = 'form-control'
		self.fields['address'].widget.attrs['class'] = 'form-control'
		self.fields['phone'].widget.attrs['class'] = 'form-control'
		self.fields['mobile_phone'].widget.attrs['class'] = 'form-control'
		self.fields['member_pic'].widget.attrs['class'] = 'form-control'

	def clean_email(self):
		if self.is_valid():
			email = self.cleaned_data['email']
		try:
			member = CustomMember.objects.exclude(pk=self.instance.pk).get(email=email)
		except CustomMember.DoesNotExist:
			return email
		raise form.ValidationError('Email "%s" is already in use' %member)





