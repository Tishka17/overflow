import logging

from django.http import HttpResponse
from django.shortcuts import render

from questions.forms import QuestionForm
from questions.models import Topic

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
