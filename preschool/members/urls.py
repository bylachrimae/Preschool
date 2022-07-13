from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('signup',views.signup,name='signup'),
   path('member_login',views.member_login,name='login'),
   path('member_logout',views.member_logout,name='logout'),
]
