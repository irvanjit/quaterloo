from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=300)

class Answer(models.Model):
	user = models.ForeignKey(User)
	question = models.ForeignKey(Question)
	content = models.CharField(max_length=300)

class Comment(models.Model):
	user = models.ForeignKey(User)
	content = models.CharField(max_length=300)