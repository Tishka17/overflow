from django import forms

from .models import Topic


class QuestionForm(forms.Form):
    title = forms.CharField(label='Заголовок', max_length=80,
                            widget=forms.TextInput(attrs={"class": "form-control"}))
    text = forms.CharField(label='Текст вопроса', max_length=4096,
                           widget=forms.Textarea(attrs={"class": "form-control"}))
    topic = forms.ModelChoiceField(label="Тема",queryset=Topic.objects.all(), empty_label="(Выберите тему)",
                                   widget=forms.Select(attrs={"class": "form-control"}))


class AnswerForm(forms.Form):
    text = forms.CharField(label='Текст ответа', max_length=4096,
                           widget=forms.Textarea(attrs={"class": "form-control"}))
