from datetime import datetime, timezone
import os
from django.shortcuts import render , redirect, HttpResponse
from .models import *
from .forms import *
import sweetify # type: ignore

def home(request):
    return render(request,'layout/index.html')
# Staff
def staff_show(request):
    staff = Staff.objects.all().order_by('id')
    postition = Position.objects.all()
    return render(request,'pages/employees/staff/staff_index.html',{'staffs':staff , 'positions':postition})
def staff_createForm(request):
    postition = Position.objects.all()
    return render(request,'pages/employees/staff/staff_create.html',{'positions':postition})
def staff_create(request):
    postition=Position.objects.all()
    if request.method == 'POST':
        validator = StaffForm(request.POST)
        if validator.is_valid():
            staff_from = validator.save(commit=False)
            staff_from.save()
            sweetify.success(request, 'Staff Create Successfully ')
            return redirect(to='staff_show')
        else:
            return render(request, 'pages/employees/staff/staff_create.html',{'form':validator , 'positions':postition})
    else:
        form = StaffForm(None)
        return render(request=request, template_name='pages/employees/staff/staff_create.html',context={'form':StaffForm(),'positions':postition})
def staff_editshow(request,id):
    staff = Staff.objects.get(id=id)
    postition = Position.objects.all()
    return render(request,'pages/employees/staff/staff_edit.html',{'staff':staff , 'positions':postition})
def staff_update(request,id):
    postition = Position.objects.all()
    staff = Staff.objects.get(id=id)
    validator = StaffForm(request.POST,instance=staff)
    if validator.is_valid():
        validator.save()
        sweetify.success(request, 'Staff Update Successfully ')
        return redirect(to='staff_show')
    elif validator.errors:
        sweetify.warning(request, 'Data keep the same')
        return redirect(to='staff_show')
    else:
        return render(request, 'pages/employees/staff/staff_edit.html',{'form':validator,'staff':staff,'positions':postition})
def staff_delete(request,id):
    staff = Staff.objects.get(id=id)
    staff.delete()
    sweetify.success(request, 'Staff Delete Successfully ')
    return redirect(to='staff_show')
# End Staff

# Position
def position_show(request):
    position = Position.objects.all().order_by('id')
    return render(request,'pages/employees/position/position_index.html',{'positions':position})
def position_createForm(request):
    return render(request,'pages/employees/position/position_create.html')
def position_create(request):
    if request.method == 'POST':
        validator = PositionForm(request.POST)
        if validator.is_valid():
            name = validator.save(commit=False)
            name.save()
            sweetify.success(request, 'Position Create Successfully ')
            return render(request,'pages/employees/position/position_create.html')
        else:
            return render(request, 'pages/employees/position/position_create.html',{'form':validator})
    else:
        form = PositionForm(None)
        return render(request=request, template_name='pages/employees/position/position_create.html',context={'form':PositionForm()})
def position_editshow(request,id):
    position = Position.objects.get(id=id)
    return render(request,'pages/employees/position/position_edit.html',{'position':position})
def update(request,id):
    position = Position.objects.get(id=id)
    form = PositionForm(request.POST,instance=position)
    if form.is_valid():
        if Position.objects.filter(name=request.POST['name']).exclude(id=id).exists():
            return(render(request,'pages/employees/position/position_edit.html',{'form':form , 'position':position}))
        form.save()
        sweetify.success(request, 'Position Update Successfully ')
        return redirect('position_show')
    elif form.errors:
        if 'name' in form.errors:
            return(render(request,'pages/employees/position/position_edit.html',{'form':form , 'position':position}))
        sweetify.warning(request, 'Data keep the same')
        return redirect(to='position_show')
    else:
        sweetify.error(request, 'Position Update Failed ')
        return render(request,'pages/employees/position/position_edit.html',{'form':form , 'position':position})
def delete_position(request,id):
    position = Position.objects.get(id=id)
    position.delete()
    sweetify.success(request, 'Position Delete Successfully ')
    return redirect('position_show')
# End Position

# Teacher
def teacher_show(request):
    teacher = Teacher.objects.all().order_by('id') 
    return render(request,'pages/employees/teacher/teacher_index.html',{'teachers':teacher})
def teacher_createForm(request):
    subject = Subject.objects.all()
    staff = Staff.objects.all()
    return render(request,'pages/employees/teacher/teacher_create.html',{'subjects':subject,'staffs':staff})
def teacher_create(request):
    subject = Subject.objects.all()
    staff = Staff.objects.all()
    # teacher = Teacher.objects.all()
    if request.method == 'POST':
        validator = TeacherForm(request.POST)
        if validator.is_valid():
            teacher = validator.save(commit=False)
            teacher.create_by_id = request.POST['create_by']
            teacher.subject_id = request.POST['subject']
            if len(request.FILES) > 0:          
                teacher.photo = request.FILES['photo']
            teacher.save()
            sweetify.success(request, 'Teacher Create Successfully ')
            return redirect(to='teacher_show')
        else:
            return render(request, 'pages/employees/teacher/teacher_create.html',{'form':validator,'subjects':subject,'staffs':staff})
        #this way create Object teacher send to database
        # teacher = Teacher(
        #     firstname=request.POST['firstname'],
        #     lastname=request.POST['lastname'],
        #     gender=request.POST['gender'],
        #     dateofbirth=request.POST['dateofbirth'],
        #     salary=request.POST['salary'],
        #     create_by_id=request.POST['create_by'],
        #     subject_id=request.POST['subject'],
        # )    
        # teacher.save()
    return redirect(to='teacher_show')
def teacher_editshow(request,id):
    teacher = Teacher.objects.get(id=id)
    staff = Staff.objects.all()
    subject = Subject.objects.all()
    return render(request,'pages/employees/teacher/teacher_edit.html',{'teachers':teacher ,'staffs':staff,'subjects':subject})
def teacher_update(request,id):
    teacher = Teacher.objects.get(id=id)
    staff = Staff.objects.all()
    subject = Subject.objects.all()
    form = TeacherForm(request.POST,instance=teacher)
    if request.method == 'POST':
        if form.is_valid():
            teacher = form.save()
            if len(request.FILES) > 0:
                if teacher.photo:
                    teacher.photo.delete()          
                teacher.photo = request.FILES['photo']
            teacher.update_at = datetime.now()
            teacher.update_by = request.user.username
            teacher.save()
            sweetify.success(request, 'Teacher Update Successfully ')
            return redirect(to='teacher_show')        
        elif form.errors:
            if any(field in form.errors for field in ['firstname', 'lastname', 'gender', 'dateofbirth', 'salary', 'create_by', 'subject']):
                return(render(request,'pages/employees/teacher/teacher_edit.html',{'form':form , 'teachers':teacher,'staffs':staff,'subjects':subject}))
            sweetify.warning(request, 'Data keep the same')
            return redirect(to='teacher_show')
        else:
            sweetify.error(request, 'Teacher Update Failed ')
            return render(request,'pages/employees/teacher/teacher_edit.html',{'form':form , 'teachers':teacher,'staffs':staff,'subjects':subject})
    return redirect(to='teacher_show')
def delete_teacher(request,id):
    teacher = Teacher.objects.get(id=id)
    if teacher.photo:
        # Delete File Option1
        teacher.photo.delete()
        
        # Delete File Option2
        # os.remove(teacher.photo.path)
        teacher.delete()
        sweetify.success(request, 'Teacher Delete Successfully ')
    else:
        teacher.delete()
        sweetify.success(request, 'Teacher Delete Successfully ')
    return redirect(to='teacher_show')
def teacher_detail(request,id):
    teacher = Teacher.objects.get(id=id)
    return render(request,'pages/employees/teacher/teacher_detail.html',{'teachers':teacher})
# End Teacher

# Subject
def subject_show(request):
    subject = Subject.objects.all().order_by('id')
    return render(request,'pages/employees/subject/subject_index.html',{'subjects':subject})
def subject_createForm(request):
    staff = Staff.objects.all()
    return render(request,'pages/employees/subject/subject_create.html',{'staffs':staff})
def subject_create(request):
    staff = Staff.objects.all()
    if request.method == 'POST':
        validator = SubjectForm(request.POST)
        if validator.is_valid():
            name = validator.save(commit=False)
            name.save()
            sweetify.success(request, 'Subject Create Successfully ')
            return render(request,'pages/employees/subject/subject_create.html')
        else:
            return render(request, 'pages/employees/subject/subject_create.html',{'form':validator,'staffs':staff})
    else:
        form = SubjectForm(None)
        return render(request=request, template_name='pages/employees/subject/subject_create.html',context={'form':SubjectForm(),'staffs':staff})
def subject_editshow(request,id):
    subject = Subject.objects.get(id=id)
    staff = Staff.objects.all()
    return render(request,'pages/employees/subject/subject_edit.html',{'subject':subject,'staffs':staff})
def update(request,id):
    subject = Subject.objects.get(id=id)
    form = SubjectForm({'subject_name':request.POST['subject_name']},instance=subject)
    if Subject.objects.filter(subject_name=request.POST['subject_name']).exclude(id=id).exists():
        return(render(request,'pages/employees/subject/subject_edit.html',{'form':form , 'subject':subject}))
    else:
        subject.subject_name = request.POST['subject_name']
        subject.update_at = datetime.now()
        subject.update_by = Staff.objects.get(id=request.POST['create_by']).firstname
        subject.save()
        sweetify.success(request, 'Subject Update Successfully ')
        return redirect('subject_show')       
def delete_subject(request,id):
    subject = Subject.objects.get(id=id)
    subject.delete()
    sweetify.success(request, 'Subject Delete Successfully ')
    return redirect('subject_show')
# End Subject
def dashboard(request):
    return render(request,'pages/dashboard.html') 
def blank(request):
    return render(request,'pages/blank.html')

