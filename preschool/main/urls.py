from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('classes',views.classes,name='classes'),
    path('add_class/',views.add_class,name='add-class'),
    path('view_class/<classroom_id>',views.view_class,name='view-class'),
    path('classrooms/',views.classrooms,name='classrooms'),
    path('update_class/<classroom_id>',views.update_class,name='update-class'),
    path('delete_class/<classroom_id>',views.delete_class,name='delete-class'),
    path('dashboard/<user_id>',views.dashboard,name='dashboard'),
    path('teacher_dashboard/<user_id>',views.teacher_dashboard,name='teacher-dashboard'),
    path('manager_dashboard/<user_id>',views.manager_dashboard,name='manager-dashboard'),
    path('teacher_accounts',views.teacher_accounts,name="teacher-accounts"),
    path('update/',views.update_member,name='update'),
    path('add_student/<user_id>',views.add_student,name="add-student"),
    path('student_details/<student_id>',views.student_details,name="student-details"),
    path('update_student/<student_id>',views.update_student,name="update-student"),
    path('delete_student/<student_id>',views.delete_student,name="delete-student"),
    path('create_event/',views.create_event,name="create-event"),
    path('event_list/',views.all_events,name="event-list"),
    path('update_event/<event_id>',views.update_event,name="update-event"),
    path('delete_event/<event_id>',views.delete_event,name="delete-event"),
    path('event_approval',views.event_approval,name="event-approval"),
    path('parent_details/<parent_id>',views.parent_details,name="parent-details"),
    path('teacher_details/<teacher_id>',views.teacher_details,name="teacher-details"),
]