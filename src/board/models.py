from django.db import models
from django.contrib.auth.models import User


class Board(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.title


class Topic(models.Model):
    title = models.CharField(max_length=100)
    board = models.ForeignKey(Board)

    def __str__(self):
        return self.title


class Message(models.Model):
    post_time = models.DateTimeField('date posted')
    text = models.TextField(max_length=10000)
    topic = models.ForeignKey(Topic)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.text[:20]


