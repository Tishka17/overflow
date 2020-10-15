from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import prefetch_related_objects

from .models import Topic, Question
import logging

logger = logging.getLogger(__name__)

def index(request):
    return HttpResponse("Hello, world. You're at the questions index.")


def get_topic(request, topic_key):
    topic = Topic.objects.get(key=topic_key)
    latest_questions = topic.question_set.order_by('-created_at')[:5]
    context = {
        'latest_questions': latest_questions,
        'topic': topic
    }
    return render(request, 'questions/topic.html', context)


def get_question(request, question_id):
    question = Question.objects.get(id=question_id)
    answers = question.answer_set.order_by('created_at').all()
    context = {
        'question': question,
        'answers': answers
    }
    return render(request, 'questions/question.html', context)
