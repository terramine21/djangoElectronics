"""Модуль тестов для приложения trainer."""

from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from .models import Problem, UserAnswer


class ProblemAPITestCase(TestCase):
    """Тесты для API задач."""

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser', password='testpass'
        )
        self.admin = User.objects.create_superuser(
            username='admin', password='adminpass'
        )
        self.problem = Problem.objects.create(
            title="Test Problem",
            topic="ohm",
            description="Test description",
            correct_answer=5.0,
            unit="A"
        )

    def test_get_problems_authenticated(self):
        """Проверяет получение списка задач аутентифицированным пользователем."""
        self.client.login(username='testuser', password='testpass')
        response = self.client.get('/api/problems/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 5)  # 4 начальные + 1 из setUp

    def test_create_problem_admin(self):
        """Проверяет создание задачи суперпользователем."""
        self.client.login(username='admin', password='adminpass')
        data = {
            'title': 'New Problem',
            'topic': 'series',
            'description': 'New description',
            'correct_answer': 10.0,
            'unit': 'Ohm'
        }
        response = self.client.post('/api/problems/', data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Problem.objects.count(), 6)  # 4 начальные + 1 из setUp + 1 новая


class UserAnswerAPITestCase(TestCase):
    """Тесты для API ответов пользователей."""

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser', password='testpass'
        )
        self.problem = Problem.objects.create(
            title="Test Problem",
            topic="ohm",
            description="Test description",
            correct_answer=5.0,
            unit="A"
        )

    def test_create_user_answer(self):
        """Проверяет создание ответа пользователем."""
        self.client.login(username='testuser', password='testpass')
        data = {
            'problem': self.problem.id,
            'answer': 5.0
        }
        response = self.client.post('/api/user-answers/', data)
        self.assertEqual(response.status_code, 201)
        self.assertTrue(UserAnswer.objects.filter(user=self.user).exists())
