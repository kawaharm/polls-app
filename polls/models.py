import datetime

from django.db import models
from django.utils import timezone

# Create your models here.


class Question(models.Model):
    # Fields
    question_text = models.CharField(max_length=200)
    # 'date published' for human-readable name (usually for documentation)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    # Fields
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE)  # M:1 relationship
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
