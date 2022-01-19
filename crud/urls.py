from django.contrib import admin
from django.urls import path

from crud.models import Employee
from .views import DepartmentCrud, EmployeeCrud

urlpatterns = [
    path('createDepartment/',DepartmentCrud.as_view(),name="create"),
    path('readDepartment/',DepartmentCrud.as_view(),name="read"),
    path('updateDepartment/',DepartmentCrud.as_view(),name="read"),
    path('createEmployee/',EmployeeCrud.as_view(),name="create")
]
