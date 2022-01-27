from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .serializer import *
from .models import *
# from djangoRestDemo.api import serializer

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Student-List': '/student-list/',
        'Student-Detail': '/student-detail/<str:pk>/',
        'New-Student': '/student-create/',
        'Update-Student': '/student-update/<str:pk>/',
        'Delete-Student': '/student-delete/<str:pk>/',
        # urls of school model
        'School-List': '/school-list/',
        'School-List': '/school-list/',
        'School-List': '/school-list/',
        
        'School-Detail': '/school-detail/<str:pk>/',
        'New-School': '/school-create/',
    }

    return Response(api_urls)

class SchoolList(generics.ListAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['school_rank', 'school_state']

# class SchoolList(APIView):
#     def get(self, request):
#         schools = School.objects.all()
#         serializer = SchoolSerializer(schools, many=True)
#         return Response(serializer.data) 
    # def get(self, request):
    #     schools = School.objects.filter(school_type='English-Medium')
    #     serializer = SchoolSerializer(schools, many=True)
    #     return Response(serializer.data) 
    # def get(self, request):
    #     schools = School.objects.filter(school_state='Chhattisgarh',school_rank=3)
    #     serializer = SchoolSerializer(schools, many=True)
    #     return Response(serializer.data) 
    




@api_view(['GET'])
def studentList(request):
    """
    List all Students.
    """
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data) 

@api_view(['GET'])
def studentDetail(request, pk):
    student = Student.objects.get(id=pk)
    serializer = StudentSerializer(student, many=False)
    return Response(serializer.data) 

@api_view(['POST'])
def studentCreate(request):
    serializer = StudentSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data) 

@api_view(['POST'])
def studentUpdate(request, pk):
    student = Student.objects.get(id=pk)
    serializer = StudentSerializer(instance=student, data=request.data)
    
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data) 

@api_view(['DELETE'])
def studentDelete(request, pk):
    student = Student.objects.get(id=pk)
    student.delete()
    return Response('Item Deleted Successfully!!') 