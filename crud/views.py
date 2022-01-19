from django.shortcuts import render
from .models import Department,Employee
from .serializers import DepartmentSerializer,EmployeeSerializer
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class DepartmentCrud(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self,request):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self,request):
        departmentdata = Department.objects.all()
        #assert False,departmentdata
        serializer = DepartmentSerializer(departmentdata,many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        
    def patch(self,request):
        departmentdata = Department.objects.get(id=request.data['id'])
        serializer = DepartmentSerializer(data=departmentdata,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class EmployeeCrud(APIView):
    def post(self,request):
        serializer= EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)