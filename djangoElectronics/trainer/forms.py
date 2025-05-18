"""Модуль форм для приложения trainer."""

from django import forms
from .models import Problem


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
        """Проверяет, что ответ находится в диапазоне от -1000 до 1000."""
        answer = self.cleaned_data['answer']
        if not -1000 <= answer <= 1000:
            raise forms.ValidationError(
                "Ответ должен быть в диапазоне от -1000 до 1000"
            )
        return answer


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
        """Проверяет, что правильный ответ в диапазоне от -1000 до 1000."""
        correct_answer = self.cleaned_data['correct_answer']
        if not -1000 <= correct_answer <= 1000:
            raise forms.ValidationError(
                "Правильный ответ должен быть в диапазоне от -1000 до 1000"
            )
        return correct_answer

    def clean_title(self):
        """Проверяет длину названия задачи."""
        title = self.cleaned_data['title']
        if len(title) < 5:
            raise forms.ValidationError(
                "Название задачи должно содержать не менее 5 символов"
            )
        if len(title) > 200:
            raise forms.ValidationError(
                "Название задачи не должно превышать 200 символов"
            )
        return title

    def clean_description(self):
        """Проверяет длину описания задачи."""
        description = self.cleaned_data['description']
        if len(description) < 10:
            raise forms.ValidationError(
                "Описание задачи должно содержать не менее 10 символов"
            )
        return description

    def clean_unit(self):
        """Проверяет длину единицы измерения."""
        unit = self.cleaned_data['unit']
        if len(unit) < 1:
            raise forms.ValidationError("Единица измерения не может быть пустой")
        if len(unit) > 50:
            raise forms.ValidationError(
                "Единица измерения не должна превышать 50 символов"
            )
        return unit