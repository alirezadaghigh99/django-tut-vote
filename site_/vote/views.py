from django.shortcuts import render
from django.shortcuts import HttpResponse, get_list_or_404, get_object_or_404
# Create your views here.
from . models import Question, Choice
def index_vote(request, *args, **kwargs):
    return HttpResponse("hello")


def all_questions(request, *args, **kwargs):

    all_questions = Question.objects.all()
    context = {
        "all_q": all_questions
    }
    return render(request, 'show_all.html', context )

def show_detail(request, question_id):
    if request.method == "GET":
        q = Question.objects.get(id=question_id)
        context = {
            "question":q
        }
        return render(request, 'show_detail.html',context)
    
    else:
        q = Question.objects.get(id=question_id)

        try:
            choice_selected = q.choice_set.get(id = request.POST["choice"])
        except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
            return render(request, 'show_detail.html', {
                'question': q,
                'error_message': "You didn't select a choice.",
            })
        else:
            choice_selected.vote += 1
            choice_selected.save()
        return HttpResponse("submited")