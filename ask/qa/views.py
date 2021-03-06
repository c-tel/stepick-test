from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_protect
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect  
from models import Question, Answer
from forms import AskForm, AnswerForm
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

@csrf_protect
def question(request, id):    
	question = get_object_or_404(Question, pk=id)
	if request.method == 'POST':
		form = AnswerForm(request.POST)
		if form.is_valid():
			answer = form.save()
	answer_list = question.answer_set.order_by('-added_at')
	form = AnswerForm()
	return render(request, 'question.html',{
		'title' : question.title,
		'quest' : question,
		'answer_list' : answer_list,
		'form': form,
		})
@csrf_protect
def ask(request):
	if request.method == "POST":
		form = AskForm(request.POST)
		if form.is_valid():
			question = form.save()
			url = '/question/' + str(question.id)
			return HttpResponseRedirect(url)
	else:
		form = AskForm()
	return render(request, 'ask.html', {
		'form': form,
		})
