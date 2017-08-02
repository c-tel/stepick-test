from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


class QuestionManager(models.Manager):
	def sortByDate(question):
		return question.added_at
	def new(self):
		return self.all().sort(key = sortByDate)
	def sortByPop(question):
		return question.rating
	def popular(self):
		return self.all().sort(key = sortByPop)
		

class Question(models.Model):                                      
	title = models.CharField(max_length=255)             
	text = models.TextField()                         
	added_at = models.DateTimeField(auto_now_add=True)
	rating = models.IntegerField(default=0);
	author = models.ForeignKey(User, related_name = 'author')
	likes = models.ManyToManyField(User)                 
	objects = QuestionManager()

class Answer(models.Model):                                      
	text = models.TextField() 
	added_at = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User)
	question = models.OneToOneField(Question)                 

	