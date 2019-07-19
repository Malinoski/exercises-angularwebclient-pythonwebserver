from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Question


def index(request):

    # # Display a simple text
    # return HttpResponse("Hello, world. You're at the polls index.")

    # # Display 5 elements
    # Get latest 5 elements
    #     latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)

    # # Display 5 elements in a template
    # # Get latest 5 elements
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # build template to display an html
    # # template = loader.get_template('polls/index.html')
    # context = {
    #    'latest_question_list': latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))

    # # Display 5 elements in a template in a compact way
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # # Display a simple text
    # return HttpResponse("You're looking at question %s." % question_id)

    # # Display a simple text or an error if the element not exist
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
