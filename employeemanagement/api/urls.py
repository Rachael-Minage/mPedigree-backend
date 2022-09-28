# from django.contrib import admin
# from django.urls import path
from django.urls import include, path
from rest_framework import routers
from api  import views
from .views import employeeApi
from .views import RegisterAPI
from knox import views as knox_views
from .views import LoginAPI

from api.views import csv_upload



urlpatterns = [
path("employee/",employeeApi,name='employeeApi'),
path('csv/',csv_upload,name='csv_upload')  ,
path('register/',RegisterAPI.as_view(), name='register'),
path('login/', LoginAPI.as_view(), name='login'),
path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),



]

