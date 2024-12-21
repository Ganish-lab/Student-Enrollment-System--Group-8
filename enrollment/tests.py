from rest_framework.test import APITestCase
from rest_framework import status
from .models import Student, Course

class StudentTests(APITestCase):
    def test_create_student(self):
        data = {"first_name": "John", "last_name": "Doe", "email": "john@example.com"}
        response = self.client.post('/api/students/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_get_students(self):
        response = self.client.get('/api/students/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class CourseTests(APITestCase):
    def test_create_course(self):
        data = {"name": "Math 101", "code": "MATH101"}
        response = self.client.post('/api/courses/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
