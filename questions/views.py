import logging

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.base import View

from .forms import QuestionForm
from .models import Topic, Question

logger = logging.getLogger(__name__)


def index(request):
    return HttpResponse("Hello, world. You're at the questions index.")


def get_topic(request, topic_key):
    topic = Topic.objects.get(key=topic_key)
    latest_questions = topic.question_set.order_by('-created_at')[:5]
    context = {
        'latest_questions': latest_questions,
        'topic': topic,
        'question_form': QuestionForm(initial={"topic": topic}),
    }
    return render(request, 'questions/topic.html', context)


def get_question(request, question_id):
    question = Question.objects.get(id=question_id)
    answers = question.answer_set.order_by('created_at').all()
    context = {
        'question': question,
        'answers': answers,
    }
    return render(request, 'questions/question.html', context)


class NewQuestion(View):
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
            return redirect("get_question", question.id)
        context = {
            'question_form': form,
        }
        return render(request, 'questions/new_question.html', context)

    def get(self, request):
        context = {
            'question_form': QuestionForm(),
        }
        return render(request, 'questions/new_question.html', context)
