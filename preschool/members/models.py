from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

class MyMemberManager(BaseUserManager):
	def create_user(self,email,first_name,last_name,password=None):
		if not email:
			raise ValueError("Members must have an email")
		if not first_name:
			raise ValueError("Members must have a first name")
		if not last_name:
			raise ValueError("Members must have a last name")
		user = self.model(
			email=self.normalize_email(email),
			first_name = first_name,
			last_name = last_name,
			)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self,email,first_name,last_name,password):
		user = self.create_user(
			email = self.normalize_email(email),
			first_name = first_name,
			last_name = last_name,
			password = password,
			)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user

class CustomMember(AbstractBaseUser):
	email = models.EmailField(verbose_name='Email',max_length=60,unique=True)
	first_name = models.CharField(verbose_name='First Name',max_length=50,null=True,blank=True)
	last_name = models.CharField(verbose_name='Last Name',max_length=50,null=True,blank=True)
	date_joined = models.DateTimeField(verbose_name='Date Joined',auto_now_add=True)
	last_login = models.DateTimeField(verbose_name='Last Login',auto_now=True)
	address = models.CharField(verbose_name='Address',max_length=300,null=True,blank=True,default='Your Address')
	phone = models.CharField(verbose_name='Phone',max_length=40,null=True,blank=True,default='Your Phone Number')
	mobile_phone = models.CharField(verbose_name='Mobile Number',max_length=40,null=True,blank=True,default='Your Mobile Phone Number')
	member_pic = models.ImageField(verbose_name='Profile Picture',default='images/default_pic.jpg',upload_to='images/')
	is_parent = models.BooleanField(default=True)
	is_teacher = models.BooleanField(default=False)
	is_manager = models.BooleanField(default=False)
	is_admin = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)
	is_staff = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['first_name','last_name']

	objects = MyMemberManager()

	def __str__(self):
		return self.email

	def has_perm(self,perm,obj=None):
		return self.is_admin

	def has_module_perms(self,app_label):
		return True

class Manager(models.Model):
	user = models.OneToOneField(CustomMember,on_delete=models.CASCADE)

	def __str__(self):
		return self.user.first_name + ' ' + self.user.last_name + ' ' + self.user.email

