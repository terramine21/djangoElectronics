"""Модуль форм для приложения trainer."""

from django import forms
from .models import Problem
from .utils import validate_number_range, validate_title, validate_description, validate_unit


class AnswerForm(forms.Form):
    """Форма для ввода ответа пользователя на задачу."""
    answer = forms.FloatField(
        label='Ваш ответ',
        required=True,
        widget=forms.NumberInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded'}
        )
    )

    def clean_answer(self):
        """Проверяет валидность ответа."""
        answer = self.cleaned_data['answer']
        return validate_number_range(answer)


class ProblemForm(forms.ModelForm):
    """Форма для создания и редактирования задачи."""

    class Meta:
        """Мета-данные формы ProblemForm."""
        model = Problem
        fields = ['title', 'topic', 'description', 'correct_answer', 'unit']
        labels = {
            'title': 'Название задачи',
            'topic': 'Тема',
            'description': 'Описание',
            'correct_answer': 'Правильный ответ',
            'unit': 'Единица измерения',
        }
        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'w-full p-2 border border-gray-300 rounded'}
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'w-full p-2 border border-gray-300 rounded',
                    'rows': 5
                }
            ),
            'topic': forms.Select(
                attrs={'class': 'w-full p-2 border border-gray-300 rounded'}
            ),
            'correct_answer': forms.NumberInput(
                attrs={'class': 'w-full p-2 border border-gray-300 rounded'}
            ),
            'unit': forms.TextInput(
                attrs={'class': 'w-full p-2 border border-gray-300 rounded'}
            ),
        }

    def clean_correct_answer(self):
        """Проверяет валидность правильного ответа."""
        correct_answer = self.cleaned_data['correct_answer']
        return validate_number_range(correct_answer)

    def clean_title(self):
        """Проверяет валидность названия."""
        title = self.cleaned_data['title']
        return validate_title(title)

    def clean_description(self):
        """Проверяет валидность описания."""
        description = self.cleaned_data['description']
        return validate_description(description)

    def clean_unit(self):
        """Проверяет валидность единицы измерения."""
        unit = self.cleaned_data['unit']
        return validate_unit(unit)
