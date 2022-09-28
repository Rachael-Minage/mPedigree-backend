from django.contrib import admin
from .models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("first_name","middle_name","position","salary","supervisors")
    search_fields = ("first_name","middle_name")
admin.site.register(Employee,EmployeeAdmin)

