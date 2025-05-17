from django.contrib import admin
from .models import Problem, UserAnswer

@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ('title', 'topic', 'unit', 'created_at')  # Поля для отображения в списке
    list_filter = ('topic',)  # Фильтр по теме
    search_fields = ('title', 'description')  # Поиск по названию и описанию

@admin.register(UserAnswer)
class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ('user', 'problem', 'answer', 'is_correct', 'submitted_at')  # Поля для отображения
    list_filter = ('is_correct', 'submitted_at')  # Фильтры
    search_fields = ('user__username', 'problem__title')  # Поиск по пользователю и задаче