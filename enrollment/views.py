from django.shortcuts import render
from rest_framework import viewsets
from .models import Student, Course, Enrollment, Instructor
from .serializers import StudentSerializer, CourseSerializer, EnrollmentSerializer, InstructorSerializer

class StudentViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing student instances.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class CourseViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing course instances.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class EnrollmentViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing enrollment instances.
    """
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
  class InstructorViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing instructor instances.
    """
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer



