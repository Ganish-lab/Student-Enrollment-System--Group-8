from rest_framework import serializers
from .models import Student, Course, Enrollment, Instructor, CourseInstructor

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '_all_'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '_all_'

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '_all_'

class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = '_all_'

class CourseInstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseInstructor
        fields = '_all_'