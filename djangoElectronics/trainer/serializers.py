"""Модуль сериализаторов для API приложения trainer."""

from rest_framework import serializers
from .models import Problem, UserAnswer
from .utils import validate_number_range, validate_title, validate_description, validate_unit, create_user_answer


class ProblemSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Problem."""
    topic_display = serializers.CharField(source='get_topic_display', read_only=True)

    class Meta:
        model = Problem
        fields = [
            'id', 'title', 'topic', 'topic_display', 'description',
            'correct_answer', 'unit', 'created_at'
        ]
        read_only_fields = ['created_at']

    def validate_correct_answer(self, value):
        """Проверяет валидность правильного ответа."""
        return validate_number_range(value)

    def validate_title(self, value):
        """Проверяет валидность названия."""
        return validate_title(value)

    def validate_description(self, value):
        """Проверяет валидность описания."""
        return validate_description(value)

    def validate_unit(self, value):
        """Проверяет валидность единицы измерения."""
        return validate_unit(value)


class UserAnswerSerializer(serializers.ModelSerializer):
    """Сериализатор для модели UserAnswer."""
    user = serializers.StringRelatedField(read_only=True)
    problem = serializers.PrimaryKeyRelatedField(queryset=Problem.objects.all())

    class Meta:
        model = UserAnswer
        fields = ['id', 'user', 'problem', 'answer', 'is_correct', 'submitted_at']
        read_only_fields = ['user', 'is_correct', 'submitted_at']

    def validate_answer(self, value):
        """Проверяет валидность ответа."""
        return validate_number_range(value)

    def create(self, validated_data):
        """Создает ответ пользователя с проверкой правильности."""
        problem = validated_data['problem']
        answer = validated_data['answer']
        user = self.context['request'].user
        return create_user_answer(user, problem, answer)
