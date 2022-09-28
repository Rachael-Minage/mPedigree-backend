from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Employee
        fields = ["first_name","middle_name","position","salary","supervisors"]