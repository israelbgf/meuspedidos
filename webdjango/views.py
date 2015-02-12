from django.shortcuts import render
from parsers import SafeForm
from evaluator.usecases.answer_evaluation_form import AnswerEvaluationFormUseCase, EvaluationForm
import json
from django.http import HttpResponse
from webdjango.email_gateway import DjangoEmailGateway


def index(request):
    return render(request, 'index.html', {})


def recruitment(request):
    form = SafeForm(request.POST.dict())

    evaluation_form = EvaluationForm(form.str('name'), form.str('email'), skills={
        'html': form.int('html'),
        'css': form.int('css'),
        'javascript': form.int('javascript'),
        'python': form.int('python'),
        'django': form.int('django'),
        'android': form.int('android'),
        'ios': form.int('ios'),
        })
    
    response = AnswerEvaluationFormUseCase(DjangoEmailGateway()).execute(evaluation_form)
    return HttpResponse(json.dumps(response), content_type="application/json")
