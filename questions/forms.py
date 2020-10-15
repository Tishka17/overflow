from django import forms

from .models import Topic


class QuestionForm(forms.Form):
    title = forms.CharField(label='Заголовок', max_length=80)
    text = forms.CharField(label='Текст вопроса', max_length=4096, widget=forms.Textarea())
    topic = forms.ModelChoiceField(queryset=Topic.objects.all(), empty_label="(Выберите тему)")
