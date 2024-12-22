from django.contrib import admin
from .models import Student, Instructor, Course, Enrollment

# Register the Student model
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'age', 'address')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('age',)

# Register the Instructor model
@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'field_of_expertise')
    search_fields = ('name', 'email')
    list_filter = ('field_of_expertise',)

# Register the Course model
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code', 'description')  # Removed 'instructor'
    search_fields = ('name', 'code')
   

# Register the Enrollment model
@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'course', 'enrollment_date')
    search_fields = ('student__first_name', 'student__last_name', 'course__name')
    list_filter = ('enrollment_date',)

# Customize the admin interface
admin.site.site_header = "Student Enrollment Admin"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Welcome to the Enrollment Management System"
