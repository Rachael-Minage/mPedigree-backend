from django.shortcuts import render 
from api.models import Employee
from employeemanagement.settings import CSRF_COOKIE_SECURE

from .serializers import EmployeeSerializers,UserSerializer,RegisterSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.response import Response
from knox.models import AuthToken
from rest_framework import generics, permissions
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView


import csv, io
from django.shortcuts import render
from django.contrib import messages


@csrf_exempt
def employeeApi(request,id=0):
    if request.method=='GET':
        employees = Employee.objects.all()
        employee_serializer = EmployeeSerializers(employees,many=True)
        return JsonResponse(employee_serializer.data,safe=False)

    elif request.method=='POST':
        employee_data = JSONParser().parse(request)
        employee_serializer = EmployeeSerializers(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to add",safe=False)
    elif request.method=='PUT':
        employee_data=JSONParser().parse(request)
        employee = Employee.objects.get(middle_name = employee_data['middle_name'])
        employee_serializer=EmployeeSerializers(employee,data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to update",safe=False)
    
    elif request.method=='DELETE':
        employee=Employee.objects.get(middle_name='middle_name')
        employee.delete()
        return JsonResponse("Deleted successfully",safe=False)


def csv_upload(request):
    csv_template = "csv_upload.html"

    prompt = {
     'order':'Order of the CSV should be first_name,middle_name,position,salary,supervisor'
    }
    if request.method=='GET':
        return render(request,"api/csv_upload.html",prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request,'This is not a CSV file')

    data_set = csv_file.read().decode('UTF-8')
    io_string=io.StringIO(data_set) 
    next(io_string)

    employee_csv = csv.reader(io_string, delimiter=',', quotechar="|")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(employee_csv)
    for first_name,middle_name,position, salary,supervisors, *__ in employee_csv:
        # print("HELLO WORLD")
        print(first_name)
        created = Employee(
            first_name = first_name,
            middle_name =middle_name,
            position = position,
            salary = salary,
            supervisors = supervisors
        )
        print(created)
        created.save()
    

    context = {}
    return render(request,"api/csv_upload.html") 


# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)
