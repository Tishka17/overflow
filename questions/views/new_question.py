import logging

from django.shortcuts import render, redirect
from django.views.generic.base import View

from questions.forms import QuestionForm
from questions.models import Question

logger = logging.getLogger(__name__)


class NewQuestionView(View):
    template_name = "home.html"

    def post(self, request):
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = Question(
                title=form.cleaned_data["title"],
                text=form.cleaned_data["text"],
                topic=form.cleaned_data["topic"],
                author=request.user,
            )
            question.save()
            return redirect("question", question.id)
        context = {
            'question_form': form,
        }
        return render(request, 'questions/new_question.html', context)

    def get(self, request):
        context = {
            'question_form': QuestionForm(),
        }
        return render(request, 'questions/new_question.html', context)
