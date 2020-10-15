from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('topics/<str:topic_key>', views.get_topic, name='get_topic'),
    path('q/<str:question_id>', views.get_question, name='get_question'),
]
