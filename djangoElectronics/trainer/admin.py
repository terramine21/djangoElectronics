"""Модуль админ-панели для моделей приложения trainer."""

from django.contrib import admin
from .models import Problem, UserAnswer


@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    """Класс админ-панели для модели Problem."""
    list_display = ('title', 'topic', 'unit', 'created_at')
    list_filter = ('topic',)
    search_fields = ('title', 'description')


@admin.register(UserAnswer)
class UserAnswerAdmin(admin.ModelAdmin):
    """Класс админ-панели для модели UserAnswer."""
    list_display = ('user', 'problem', 'answer', 'is_correct', 'submitted_at')
    list_filter = ('is_correct', 'submitted_at')
    search_fields = ('user__username', 'problem__title')