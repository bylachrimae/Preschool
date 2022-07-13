from django.contrib import admin
from .models import CustomMember,Manager
from django.contrib.auth.admin import UserAdmin



@admin.register(CustomMember)
class CustomMemberAdmin(admin.ModelAdmin):
	list_display=('email','first_name','last_name','is_manager','is_teacher','is_parent')
	ordering=('first_name',)
	search_fields=('last_name',)


admin.site.register(Manager)