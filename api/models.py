from django.db import models
from django.contrib.postgres.fields import ArrayField
from datetime import date
# Create your models here.

class Student(models.Model):
    student_name = models.CharField(max_length=200)
    student_class =  models.IntegerField()
    student_school = models.CharField(max_length=200)
    student_rank = models.IntegerField()

    def __str__(self):
        return self.student_name

class School(models.Model):
    school_name = models.CharField(max_length=200)
    school_city = models.CharField(max_length=200)
    school_state = models.CharField(max_length=200)
    school_rank = models.IntegerField()
    school_type = models.CharField(max_length=200)
    school_des = models.TextField()

    def __str__(self):
        return self.school_name