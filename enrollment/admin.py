from django.contrib import admin
from .models import Student, Instructor, Course, Enrollment, Department

# Register the Student model
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'age', 'address')
    search_fields = ('name', 'email')
    list_filter = ('age',)

# Register the Instructor model
@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'expertise')
    search_fields = ('name', 'email')
    list_filter = ('expertise',)

# Register the Course model
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'instructor')
    search_fields = ('name',)
    list_filter = ('instructor',)

# Register the Enrollment model
@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'course', 'enrollment_date')
    search_fields = ('student_name', 'course_name')
    list_filter = ('enrollment_date',)