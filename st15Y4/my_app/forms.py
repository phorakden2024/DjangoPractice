from django.forms import ModelForm
from django import forms
from .models import *

class PositionForm(forms.ModelForm):
          class Meta:
                    model = Position
                    fields = ['name']
          def clean(self):
                    super(PositionForm, self).clean()
                    name = self.cleaned_data.get('name')
                    if Position.objects.filter(name=name).exists():
                              raise forms.ValidationError("Position already exists")
                    return self.cleaned_data
class StaffForm(ModelForm):
          class Meta:
                    model = Staff
                    fields = ['firstname','lastname','gender','dateofbirth','position']
          def clean(self):
                    super(StaffForm, self).clean()
                    firstname = self.cleaned_data.get('firstname')
                    lastname = self.cleaned_data.get('lastname')
                    gender = self.cleaned_data.get('gender')
                    dateofbirth = self.cleaned_data.get('dateofbirth')
                    position = self.cleaned_data.get('position')
                    
                    return self.cleaned_data
class SubjectForm(ModelForm):
          class Meta:
                    model = Subject
                    fields = ['subject_name','create_by']
          def clean(self):
                    super(SubjectForm, self).clean()
                    subject_name = self.cleaned_data.get('subject_name')
                    create_by = self.cleaned_data.get('create_by')
                    
                    return self.cleaned_data
class TeacherForm(ModelForm):
          class Meta:
                    model = Teacher
                    fields = ['firstname','lastname','gender','dateofbirth','salary','subject']
          def clean(self):
                    super(TeacherForm, self).clean()
                    firstname = self.cleaned_data.get('firstname')
                    lastname = self.cleaned_data.get('lastname')
                    gender = self.cleaned_data.get('gender')
                    dateofbirth = self.cleaned_data.get('dateofbirth')
                    salary = self.cleaned_data.get('salary')
                    subject = self.cleaned_data.get('subject')
                    
                    return self.cleaned_data