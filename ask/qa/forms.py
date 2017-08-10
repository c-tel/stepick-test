from django import forms
from models import Question, Answer

class AskForm(forms.Form):
	title = forms.CharField(max_length = 100, label='Type title your question')
	text = forms.TextField(label='Type text your question', widget=forms.Textarea)
	def clean_title(self):
		title = self.cleaned_data['title']
		return title
	def clean_text(self):
		text = self.cleaned_data['text']
		return text
	def save(self):
		question = Question(self.**cleaned_data)
		question.save()
		return question
	def clean(self):
		pass

class AnswerForm(forms.Form)
	text = forms.CharField(widget=forms.Textarea, label='')
	question = forms.IntegerField(widget=forms.HiddenInput)
	def clean_text(self):
		text = self.cleaned_data['text']
		return text
	def save(self):
		answer = Answer(self.**cleaned_data)
		answer.save()
		return answer
	def clean(self):
		pass