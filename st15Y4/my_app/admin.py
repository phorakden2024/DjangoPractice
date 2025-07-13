from django.contrib import admin
from .models import *
# Register your models here.
# User : admin
# pwd :  123
# python manage.py createsuperuser

admin.site.register(Position)
admin.site.register(Staff)
admin.site.register(Teacher)
admin.site.register(Subject)