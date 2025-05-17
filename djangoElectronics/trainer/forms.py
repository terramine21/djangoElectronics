from django import forms

class AnswerForm(forms.Form):
    answer = forms.FloatField(label='Ваш ответ', required=True)

    def clean_answer(self):
        answer = self.cleaned_data['answer']
        if answer < 0:
            raise forms.ValidationError("Ответ не может быть отрицательным")
        return answer