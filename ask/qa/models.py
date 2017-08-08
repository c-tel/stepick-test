from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


class QuestionManager(models.Manager):
	def new(self):
		return self.order_by('-added_at')
	def popular(self):
		return self.order_by('-rating')
class Question(models.Model):                                      
	title = models.CharField(max_length=255, default = ''???)             
	text = models.TextField()                         
	added_at = models.DateTimeField(auto_now_add=True)
	rating = models.IntegerField(default=0);
	author = models.ForeignKey(User, related_name = 'author')
	likes = models.ManyToManyField(User)                 
	objects = QuestionManager()
	def get_url(self):
		return '/question/{}/'.format(self.id)
class Answer(models.Model):                                      
	text = models.TextField() 
	added_at = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User)
	question = models.ForeignKey(Question)