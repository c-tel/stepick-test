from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
# Create your views here.
from django.http import HttpResponse 
from models import Question, Answer
def main(request):    
    limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except:
		page = 1
    paginator = Paginator(Question.objects.new(), limit)
    questions = paginator.page(page)
    return render(request, 'main.html',{
	'q_list' : questions,
	'paginator' : paginator
	})
		
def popular(request):    
    limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except:
        page = 1
    paginator = Paginator(Question.objects.popular(), limit)
    questions = paginator.page(page)
    return render(request, 'popular.html',{
	'q_list' : questions,
	'paginator' : paginator
	})
def question(request, id):    
	question = get_object_or_404(Question, pk=id)
	answer_list = question.answer_set.order_by('-added_at')
	return render(request, 'question.html',{
		'quest' : question,
		'answer_list' : answer_list
		})