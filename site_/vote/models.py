from django.db.models.fields.related import OneToOneField
from site_.settings import TIME_ZONE
from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    q_text = models.CharField(max_length=100)
    q_date = models.DateField(default=timezone.now)

    def __str__(self) -> str:
        return self.q_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    c_text = models.CharField(max_length = 100)
    vote = models.IntegerField(default=0)
    def __str__(self) -> str:
        return self.c_text