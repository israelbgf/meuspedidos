import json

from django.shortcuts import render
from django.http import HttpResponse

from evaluator.usecases.answer_evaluation_form import DataStructure
from webdjango.factories import create_sync_evaluation_form_usecase


def index(request):
    return render(request, 'index.html', {'delivery_mechanism': 'Django'})


def recruitment(request):
    post = request.POST.dict()

    evaluation_form = DataStructure(
        name=post.get('name'), 
        email=post.get('email'),
        html_skill=post.get('html'),
        css_skill=post.get('css'),
        javascript_skill=post.get('javascript'),
        python_skill=post.get('python'),
        django_skill=post.get('django'),
        ios_skill=post.get('ios'),
        android_skill=post.get('android')
    )
    
    usecase = create_sync_evaluation_form_usecase()
    response = usecase.execute(evaluation_form)
    return HttpResponse(json.dumps(response), content_type="application/json")
