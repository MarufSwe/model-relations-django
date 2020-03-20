from django.contrib import admin

from .models import *


# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'project_manager']


class StudentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'teachers']


admin.site.register(ProjectManager)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Teacher)
admin.site.register(Students, StudentsAdmin)
