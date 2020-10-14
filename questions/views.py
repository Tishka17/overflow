from django.http import HttpResponse
from django.template import loader

from .models import Topic, Question


def index(request):
    return HttpResponse("Hello, world. You're at the questions index.")


def get_topic(request, topic_key):
    topic = Topic.objects.get(key=topic_key)
    latest_questions = Question.objects.order_by('-created_at')[:5]
    template = loader.get_template('questions/topic.html')
    context = {
        'latest_questions': latest_questions,
        'topic': topic
    }
    return HttpResponse(template.render(context, request))
