from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Question, Choice

# index view
def index(request):
  latest_question_list = Question.objects.order_by('-pub_date')
  # template = loader.get_template('polls/index.html')
  context = {
    'latest_question_list': latest_question_list,
  }
  return render(request, 'polls/index.html', context)
 
# details view of question with id
def detail(request, question_id):
  #try:
  question = get_object_or_404(Question,pk=question_id)
  context = {
    'question': question
  }
  #except Question.DoesNotExist:
    #raise Http404('Question does not exist')
  return render(request, 'polls/detail.html', context)
 
# results of question with id
def results (request, question_id):
  question = Question.objects.get(id=question_id)
  context = {
    'question': question
  }
  return render(request,'polls/result.html', context)

# vote the question with id
def vote(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  try:
    selected_choice = question.choice_set.get(pk=request.POST['choice'])
  except (KeyError, Choice.DoesNotExist):
    # Redisplay the question voting form
    context = {
    'question': question,
    'error_message': "You didn't select choice.",
    }
    return render(request,'polls/detail.html', context)
  else:
    selected_choice.votes += 1
    selected_choice.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))