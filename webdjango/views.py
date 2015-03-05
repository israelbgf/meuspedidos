import json

from django.shortcuts import render
from django.http import HttpResponse

from parsers import SafeForm
from evaluator.usecases.answer_evaluation_form import AnswerEvaluationFormUseCase, EvaluationForm
from webdjango.factories import create_sync_evaluation_form_usecase
from webdjango.gateways.email import DjangoSyncEmailGateway


def index(request):
    return render(request, 'index.html', {'delivery_mechanism': 'Django'})


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
    
    usecase = create_sync_evaluation_form_usecase()
    response = usecase.execute(evaluation_form)
    return HttpResponse(json.dumps(response), content_type="application/json")
