from django import forms
from .models import Problem

class AnswerForm(forms.Form):
    answer = forms.FloatField(label='Ваш ответ', required=True)

    def clean_answer(self):
        answer = self.cleaned_data['answer']
        if answer < 0:
            raise forms.ValidationError("Ответ не может быть отрицательным")
        return answer

class ProblemForm(forms.ModelForm):
    class Meta:
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
            'title': forms.TextInput(attrs={'class': 'w-full p-2 border rounded'}),
            'description': forms.Textarea(attrs={'class': 'w-full p-2 border rounded', 'rows': 5}),
            'topic': forms.Select(attrs={'class': 'w-full p-2 border rounded'}),
            'correct_answer': forms.NumberInput(attrs={'class': 'w-full p-2 border rounded'}),
            'unit': forms.TextInput(attrs={'class': 'w-full p-2 border rounded'}),
        }

    def clean_correct_answer(self):
        correct_answer = self.cleaned_data['correct_answer']
        if correct_answer < 0:
            raise forms.ValidationError("Правильный ответ не может быть отрицательным")
        return correct_answer