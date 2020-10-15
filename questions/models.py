from django.conf import settings
from django.db import models


# Create your models here.
class Topic(models.Model):
    title = models.CharField(null=False, max_length=80)
    key = models.CharField(primary_key=True, null=False, max_length=40)
    visible = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    class Meta:
        db_table = "question"

    title = models.CharField(max_length=80)
    text = models.CharField(max_length=4096)
    topic = models.ForeignKey(Topic, on_delete=models.RESTRICT, db_column="topic")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Question("{self.title[:20]}...", "{self.topic_id}", {self.created_at:%Y-%m-%d %H:%M})'


class Answer(models.Model):
    class Meta:
        db_table = "answer"

    text = models.CharField(max_length=4096)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Answer("{self.text[:20]}...", {self.created_at:%Y-%m-%d %H:%M})'
