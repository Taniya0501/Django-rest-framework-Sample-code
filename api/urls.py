from django.urls import path, include
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
   
  path('', views.apiOverview, name = 'Student-API-overview'),
  path('student-list/', views.studentList, name = 'Student-List'),
  path('student-detail/<str:pk>/', views.studentDetail, name = 'Student-Details'),
  path('student-create/', views.studentCreate, name = 'New-Student'),
  path('student-update/<str:pk>/', views.studentUpdate, name = 'Update-Student-Details'),
  path('student-delete/<str:pk>/', views.studentDelete, name = 'Delete-Student-Entry'),
  path('school-list/', views.SchoolList.as_view(), name = 'School-List'),

]
urlpatterns = format_suffix_patterns(urlpatterns)