from django.shortcuts import render
from qa.models import Question, Answer

# content of view.py
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage
# Create your views here.
from django.http import HttpResponse 

def test(request, *args, **kwargs):
    return HttpResponse('OKKK')

def handler404(request):
    return HttpResponse(status=404)

def draw_question(request, q_id):
    try:
        question = Question.objects.get(id = q_id)
    except Question.DoesNotExist:
        raise Http404
    try:
        answers = Answer.objects.filter(question_id=q_id)
    except Answer.DoesNotExist:
        answers = ''
    return render(request, 'question.html', {
        'question' : question,
        'title' : question.title,
        'text' : question.text,
        'answers': answers
        })

def pages_all(request):
    posts = Question.objects.all()
    posts = posts.order_by('-added_at')
    limit = request.GET.get('limit', 10)
    try:
    	page = request.GET.get('page', 1)
    except ValueError:
    	 raise Http404
    paginator = Paginator(posts, limit)
    paginator.baseurl = '/?page='
    try:
    	page = paginator.page(page)  # Page
    except EmptyPage:
    	page = paginator.page(paginator.num_pages)
    return render(request, 'all.html', {
        'posts':  page.object_list,
        'paginator': paginator, 'page': page,
    })

def pages_popular(request):
    posts = Question.objects.all()
    posts = posts.order_by('-rating')
    limit = request.GET.get('limit', 10)
    try:
    	page = request.GET.get('page', 1)
    except ValueError:
    	 raise Http404
    paginator = Paginator(posts, limit)
    paginator.baseurl = '/?page='
    try:
    	page = paginator.page(page)  # Page
    except EmptyPage:
    	page = paginator.page(paginator.num_pages)
    return render(request, 'all.html', {
        'posts':  page.object_list,
        'paginator': paginator, 'page': page,
    })
