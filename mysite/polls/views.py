from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Question
from django.http import Http404
""" fonction pour rendre un template avec HttpResponse """
"""def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))"""

""" fonction pour rendre un template avec render """
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question n'exist pas")
    return render(request, 'polls/detail.html', {'question': question.__repr__() })