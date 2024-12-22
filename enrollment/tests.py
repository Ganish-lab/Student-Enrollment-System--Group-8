from django.test import TestCase
from django.urls import reverse
from django.core.exceptions import ValidationError
from .models import Student, Instructor, Course, Enrollment
from .forms import StudentForm
from datetime import datetime
from .forms import StudentForm


# Model Tests
class StudentModelTest(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            first_name="Jane",
            last_name="Doe",
            email="janedoe@example.com",
            age=22,
            address="456 Maple St"
        )

    def test_student_string_representation(self):
        self.assertEqual(str(self.student), "Jane Doe")

    def test_student_email_validation(self):
        self.student.email = "invalid-email"
        with self.assertRaises(ValidationError):
            self.student.full_clean()

class CourseModelTest(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            name="Mathematics 101",
            code="MATH101",
            description="Basic Mathematics Course"
        )

    def test_course_string_representation(self):
        self.assertEqual(str(self.course), "Mathematics 101")

class EnrollmentModelTest(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            first_name="John",
            last_name="Smith",
            email="johnsmith@example.com",
            age=24,
            address="789 Oak St"
        )
        self.course = Course.objects.create(
            name="Physics 101",
            code="PHYS101",
            description="Introductory Physics Course"
        )
        self.enrollment = Enrollment.objects.create(
            student=self.student,
            course=self.course,
            enrollment_date=datetime.now()
        )

    def test_enrollment_relationship(self):
        self.assertEqual(self.enrollment.student, self.student)
        self.assertEqual(self.enrollment.course, self.course)

# View Tests
class StudentViewTest(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            first_name='John',
            last_name='Doe',
            email='john.doe@example.com',
            age=20,
            address='123 Main Street'
        )

    def test_student_list_view(self):
        response = self.client.get(reverse('student_list'))
        self.assertEqual(response.status_code, 200)

    def test_student_detail_view(self):
        response = self.client.get(reverse('student_detail', args=[self.student.id]))
        self.assertEqual(response.status_code, 200)


# Form Tests
class StudentFormTest(TestCase):
    def test_student_form_valid(self):
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'johndoe@example.com',
            'age': 25,
            'address': '123 Main St'
        }
        form = StudentForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_student_form_invalid_email(self):
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'invalid-email',
            'age': 25,
            'address': '123 Main St'
        }
        form = StudentForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

# Edge Case Tests
class EdgeCaseTest(TestCase):
    def test_student_missing_required_fields(self):
        student = Student(first_name="OnlyName")
        with self.assertRaises(ValidationError):
            student.full_clean()

    def test_course_large_input(self):
        course = Course(
            name="A" * 256,  # Exceed typical length
            code="CODE",
            description="Test Description"
        )
        with self.assertRaises(ValidationError):
            course.full_clean()
