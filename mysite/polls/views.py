from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Choice, Question
# from django.template import loader


class IndexView(generic.ListView):          # Вариант 4
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]   # Вариант 3
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)

# def index(request):
#     return HttpResponse("Hello, Alex! You\'re at the polls index.")  # Вариант 1

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]  # Вариант 2
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))


class DetailView(generic.DetailView):                                  # 4 вариант
    model = Question
    template_name = 'polls/detail.html'


# def detail(request, question_id):                                        # 3 вариант
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})

# def detail(request, question_id):                                       # 2 вариант
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'polls/detail.html', {'question': question})
    # return HttpResponse("Вы видите вопрос № %s." % question_id)        # 1 вариант


class ResultsView(generic.DetailView):                                   # 3 вариант
    model = Question
    template_name = 'polls/results.html'

# def results(request, question_id):                                       # 2 вариант
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})

    # response = "Результаты голосования по вопросу № %s."  # 1 вариант
    # return HttpResponse(response % question_id)


def vote(request, question_id):                             # Вариант 2
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "Вы не сделали выбор.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

    # return HttpResponse("<h1>Вы голосуете по вопросу № %s.</h1>" % question_id)  # 1 вариант


def name(request, user_name):                                   # моя вставка
    result = '"Тестовое значение переменной"'
    context = {'user_name': user_name, 'result': result}
    return render(request, 'polls/name.html', context)
    # return HttpResponse("<h1>Ваше обращение %s зарегистрировано</h1>" % user_name)

# Create your views here.
