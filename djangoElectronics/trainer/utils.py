"""Модуль утилит для валидации данных и общей логики в приложении trainer."""

from django.core.exceptions import ValidationError
from .models import UserAnswer


def validate_number_range(value, min_value=-1000, max_value=1000):
    """Проверяет, что число находится в диапазоне."""
    if not min_value <= value <= max_value:
        raise ValidationError(
            f"Значение должно быть в диапазоне от {min_value} до {max_value}"
        )
    return value


def validate_title(value):
    """Проверяет длину названия задачи."""
    if len(value) < 5:
        raise ValidationError("Название задачи должно содержать не менее 5 символов")
    if len(value) > 200:
        raise ValidationError("Название задачи не должно превышать 200 символов")
    return value


def validate_description(value):
    """Проверяет длину описания задачи."""
    if len(value) < 10:
        raise ValidationError("Описание задачи должно содержать не менее 10 символов")
    return value


def validate_unit(value):
    """Проверяет длину единицы измерения."""
    if len(value) < 1:
        raise ValidationError("Единица измерения не может быть пустой")
    if len(value) > 50:
        raise ValidationError("Единица измерения не должна превышать 50 символов")
    return value


def create_user_answer(user, problem, answer):
    """Создает ответ пользователя с проверкой правильности."""
    is_correct = abs(answer - problem.correct_answer) < 0.01
    return UserAnswer.objects.create(
        user=user,
        problem=problem,
        answer=answer,
        is_correct=is_correct
    )
