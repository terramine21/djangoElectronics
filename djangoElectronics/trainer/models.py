"""Модуль моделей для приложения trainer."""

from django.db import models
from django.contrib.auth.models import User


class Problem(models.Model):
    """Модель задачи для тренажера по электрическим цепям."""
    TOPIC_CHOICES = [
        ('ohm', 'Закон Ома'),
        ('series', 'Последовательные цепи'),
        ('parallel', 'Параллельные цепи'),
        ('kirchhoff', 'Законы Кирхгофа'),
    ]
    title = models.CharField(max_length=200)
    topic = models.CharField(max_length=20, choices=TOPIC_CHOICES)
    description = models.TextField()
    correct_answer = models.FloatField()
    unit = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        """Возвращает строковое представление задачи."""
        return self.title


class UserAnswer(models.Model):
    """Модель ответа пользователя на задачу."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    answer = models.FloatField()
    is_correct = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        """Возвращает строковое представление ответа пользователя."""
        return f"{self.user.username} - {self.problem.title}"