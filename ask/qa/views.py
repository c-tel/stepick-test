from django.shortcuts import render
from django.core.paginator import Paginator
# Create your views here.
from django.http import HttpResponse 
def main(request):    
    limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except:
		page = 1
    paginator = Paginator(Question.objects.new(), limit)
    questions = paginator.page(page)
    return render(request, 'qa/main.html',{
	'q_list' : questions,
	'paginator' : padinator
	})
		
def popular(request):    
    limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except:
        page = 1
    paginator = Paginator(Question.objects.popular(), limit)
    questions = paginator.page(page)
    return render(request, 'qa/popular.html',{
	'q_list' : questions,
	'paginator' : padinator
	})
def question(request, id):    
	question = get_object_or_404(Question, pk=id)
	answer_list = question.answer_set.order_by('-added_at')
	return render(request, 'qa/question.html',{
		'quest' : question,
		'answer_list' : answer_list
		})