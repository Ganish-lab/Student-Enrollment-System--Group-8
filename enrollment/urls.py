from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, CourseViewSet, EnrollmentViewSet, InstructorViewSet, CourseInstructorViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'enrollments', EnrollmentViewSet)
router.register(r'instructors', InstructorViewSet)
router.register(r'course-instructors', CourseInstructorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
