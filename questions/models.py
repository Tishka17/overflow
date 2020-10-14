from django.conf import settings
from django.db import models


# Create your models here.
class Topic(models.Model):
    title = models.CharField(null=False, max_length=80)
    key = models.CharField(primary_key=True, null=False, max_length=40)
    visible = models.BooleanField(default=True)


class Question(models.Model):
    class Meta:
        db_table = "question"

    title = models.CharField(max_length=80)
    text = models.CharField(max_length=4096)
    topic = models.ForeignKey(Topic, on_delete=models.RESTRICT, db_column="topic")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Answer(models.Model):
    class Meta:
        db_table = "answer"

    text = models.CharField(max_length=4096)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
