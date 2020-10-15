from django.shortcuts import render, redirect
from django.views.generic.base import View

from questions.forms import AnswerForm
from questions.models import Answer, Question


class QuestionView(View):
    def post(self, request, question_id):
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = Answer(
                text=form.cleaned_data["text"],
                question_id=question_id,
                author=request.user,
            )
            answer.save()
            return redirect("question", question_id)
        context = {
            'answer_form': form,
        }
        return render(request, 'questions/question.html', context)

    def get(self, request, question_id):
        question = Question.objects.get(id=question_id)
        answers = question.answer_set.order_by('created_at').all()
        context = {
            'question': question,
            'answers': answers,
            "answer_form": AnswerForm(),
        }
        return render(request, 'questions/question.html', context)
