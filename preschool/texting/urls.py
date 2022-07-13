from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('send_text',views.send_text,name='send-text'),
    path('inbox',views.inbox,name='inbox'),
    path('sentbox',views.sentbox,name='sentbox'),
    path('text_detail/<text_id>',views.text_detail,name='text-detail'),
    path('delete_text/<text_id>',views.delete_text,name='delete-text'),
]