from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.home,name='home'),
    
    # Staff
    path("staff/",views.staff_show,name='staff_show'),
    path("staff/createForm/",views.staff_createForm,name='staff_createForm'),
    path("staff/create/",views.staff_create,name='staff_create'),
    path("staff/edit/<id>",views.staff_editshow,name='edit'),
    path("staff/update/<id>",views.staff_update,name='staff_update'),
    path("staff/delete/<id>",views.staff_delete,name='delete'),   
    # Position
    path("position/",views.position_show,name='position_show'),
    path("position_createForm/",views.position_createForm,name='position_createForm'),
    path("position_create/",views.position_create,name='position_create'),
    path("position/edit_position/<id>/",views.position_editshow,name='edit_position'),
    path("position/update/<id>",views.update,name='update'),
    path("position/delete_position/<id>/",views.delete_position,name='delete_position'),
     # Teacher
    path("teacher/",views.teacher_show,name='teacher_show'),
    path("teacher_createForm/",views.teacher_createForm,name='teacher_createForm'),
    path("teacher_create/",views.teacher_create,name='teacher_create'),
    path("teacher/edit_teacher/<id>/",views.teacher_editshow,name='edit_teacher'),
    path("teacher/teacher_update/<id>/",views.teacher_update,name='teacher_update'),
    path("teacher/delete_teacher/<id>/",views.delete_teacher,name='delete_teacher'),
    path("teahcer/teacher_detail/<id>/",views.teacher_detail,name='teacher_detail'),
     # Subject
    path("subject/",views.subject_show,name='subject_show'),
    path("subject_createForm/",views.subject_createForm,name='subject_createForm'),
    path("subject_create/",views.subject_create,name='subject_create'),
    path("subject/edit_subject/<id>/",views.subject_editshow,name='edit_subject'),
    path("subject/update/<id>/",views.update,name='update'),
    path("subject/delete_subject/<id>/",views.delete_subject,name='delete_subject'),
    
    path("dashboard/",views.dashboard,name='dashboard'),
    path("blank/",views.blank,name='blank'),
]
