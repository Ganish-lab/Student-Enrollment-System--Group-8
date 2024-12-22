from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .models import Student, Course, Enrollment, Instructor
from .serializers import StudentSerializer, CourseSerializer, EnrollmentSerializer, InstructorSerializer
from django.views.generic import ListView, DetailView
from .models import Student

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
class StudentListView(ListView):
    model = Student
    template_name = 'student_list.html'  # Replace with your template name
    context_object_name = 'students'

class StudentDetailView(DetailView):
    model = Student
    template_name = 'student_detail.html'  # Replace with your template name
    context_object_name = 'student'


def student_list(request):
    students = Student.objects.all()
    return render(request, 'enrollment/student_list.html', {'students': students})

def student_detail(request, pk):
    student = Student.objects.get(id=pk)
    return render(request, 'enrollment/student_detail.html', {'student': student})



