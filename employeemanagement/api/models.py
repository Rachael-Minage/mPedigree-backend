from datetime import datetime
from django.db import models


# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(primary_key=True,max_length=24)
    middle_name = models.CharField(max_length=26,blank=True) 
    # date_of_graduation = models.DateField(null=True)
    # date_of_employment = models.DateField(null=True)
    position = models.CharField(max_length=20,blank=True)
    salary = models.IntegerField(default=True)
    # supervisors = models.ForeignKey(,on_delete =models.CASCADE)
    supervisors = models.CharField(max_length=26,blank=True)
    # filecsv=models.FileField(upload_to='files',default='test.csv')
    # @property
    # def employee_code(first_name,middle_name):





    

