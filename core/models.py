from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=300)

class Answer(models.Model):
	user = models.ForeignKey(User)
	content = models.CharField(max_length=300)

class Comment(models.Model):
	user = models.ForeignKey(User)
	content = models.CharField(max_length=300)

class Group(models.Model):
	name = models.CharField(max_length=30)
	course = models.CharField(max_length=7)
	section = models.IntegerField()
