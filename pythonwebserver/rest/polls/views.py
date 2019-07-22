from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse
from django.utils import timezone
from rest_framework import viewsets
from .models import Question, Choice
from .serializers import QuestionSerializer


"""
def index(request):

    # # Display a simple text
    # return HttpResponse("Hello, world. You're at the polls index.")

    # # Display 5 elements
    # Get latest 5 elements
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
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
    # # Display a simple text and some var
    # return HttpResponse("You're looking at question %s." % question_id)

    # # Display a simple text or an error if the element not exist
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    # # Display a simple text and some var
    # response = "You're looking at the results of question %s."
    # return HttpResponse(response % question_id)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
"""


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows elements to be viewed or edited.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


def vote(request, question_id):

    # # Simple view, where displays some text and some var
    # return HttpResponse("You're voting on question %s." % question_id)

    # # Update data and redirect to another page. Or will produce an error
    # Check is object exists
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist): # We need a Choice! Otherwise, show an error.
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:

        # Update data (Increment one choice)
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
